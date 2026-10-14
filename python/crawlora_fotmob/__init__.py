"""Typed FotMob client for the Crawlora hosted API."""

from .platform import FotMobClient, AsyncFotMobClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FotMobClient
AsyncClient = AsyncFotMobClient
__version__ = '0.1.10'
DISPLAY_NAME = 'FotMob'
PLATFORM = 'fotmob'
CONTRACT_REVISION = 'sha256:8769e4cf3f8b6494435a97ef434fd699014967491242a3a3bbe235c93a9c67a0'

__all__ = [
    "FotMobClient", "AsyncFotMobClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
