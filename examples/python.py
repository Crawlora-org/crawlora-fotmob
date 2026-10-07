import os

from crawlora_fotmob import FotMobClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FotMobClient(api_key=api_key) as client:
    leagues = client.leagues()
    print('leagues', leagues)
    search = client.search(term='Premier League')
    print('search', search)
