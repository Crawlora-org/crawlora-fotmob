import os
import tempfile
import unittest
from pathlib import Path

from mypy import api

import crawlora_fotmob as client_package


TYPECHECK_SOURCE = '''
from typing_extensions import assert_type
from crawlora_fotmob import AsyncClient, AsyncFotMobClient, Client, FotMobClient
from crawlora_fotmob.platform import FotmobTvGuideResponse

def check_sync() -> None:
    named: FotMobClient = Client(api_key="key")
    with Client(api_key="key") as client:
        assert_type(client.tv_guide(country='us', timezone='test value'), FotmobTvGuideResponse)
        assert_type(client.tv_guide(_response_type='text', country='us', timezone='test value'), str)
        assert_type(client.tv_guide(_response_type='stream', country='us', timezone='test value').read(), bytes)
        assert_type(client.request('fotmob-tv-guide', {'country': 'us', 'timezone': 'test value'}), FotmobTvGuideResponse)
        assert_type(client.fotmob.tv_guide(country='us', timezone='test value'), FotmobTvGuideResponse)
        assert_type(client.fotmob.tv_guide(_response_type='text', country='us', timezone='test value'), str)
        assert_type(client.fotmob.tv_guide(_response_type='stream', country='us', timezone='test value').read(), bytes)



async def check_async() -> None:
    named: AsyncFotMobClient = AsyncClient(api_key="key")
    async with AsyncClient(api_key="key") as client:
        assert_type(await client.tv_guide(country='us', timezone='test value'), FotmobTvGuideResponse)
        assert_type(await client.tv_guide(_response_type='text', country='us', timezone='test value'), str)
        assert_type((await client.tv_guide(_response_type='stream', country='us', timezone='test value')).read(), bytes)
        assert_type(await client.fotmob.tv_guide(country='us', timezone='test value'), FotmobTvGuideResponse)
        assert_type(await client.fotmob.tv_guide(_response_type='text', country='us', timezone='test value'), str)
        assert_type((await client.fotmob.tv_guide(_response_type='stream', country='us', timezone='test value')).read(), bytes)


'''

NEGATIVE_SOURCE = '''
from crawlora_fotmob import Client
Client().tv_guide(country='us', timezone=123)
Client().tv_guide()
'''


class PublicTypingTests(unittest.TestCase):
    def setUp(self):
        self.package_root = Path(client_package.__file__).resolve().parent
        self.old_mypy_path = os.environ.get("MYPYPATH")
        parent = str(self.package_root.parent)
        os.environ["MYPYPATH"] = parent if self.old_mypy_path is None else parent + os.pathsep + self.old_mypy_path

    def tearDown(self):
        if self.old_mypy_path is None:
            os.environ.pop("MYPYPATH", None)
        else:
            os.environ["MYPYPATH"] = self.old_mypy_path

    def test_installed_platform_stub_is_well_formed(self):
        stdout, stderr, status = api.run([
            "--strict", "--python-version=3.10", "--no-incremental", "--follow-imports=silent",
            str(self.package_root / "platform.pyi"),
        ])
        self.assertEqual(status, 0, stdout + stderr)

    def test_installed_client_signatures_accept_valid_calls_and_reject_invalid_calls(self):
        with tempfile.TemporaryDirectory(prefix="crawlora-python-mypy-") as temp:
            source_path = Path(temp) / "typecheck.py"
            source_path.write_text(TYPECHECK_SOURCE, encoding="utf-8")
            stdout, stderr, status = api.run([
                "--strict", "--python-version=3.10", "--no-incremental", "--follow-imports=silent", str(source_path),
            ])
        self.assertEqual(status, 0, stdout + stderr)

        with tempfile.TemporaryDirectory(prefix="crawlora-python-mypy-negative-") as temp:
            source_path = Path(temp) / "invalid.py"
            source_path.write_text(NEGATIVE_SOURCE, encoding="utf-8")
            stdout, stderr, status = api.run([
                "--strict", "--python-version=3.10", "--no-incremental", "--follow-imports=silent", str(source_path),
            ])
        self.assertNotEqual(status, 0, stdout + stderr)
        self.assertIn("timezone", stdout + stderr)


if __name__ == "__main__":
    unittest.main()
