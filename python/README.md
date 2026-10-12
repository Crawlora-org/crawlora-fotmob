# crawlora-fotmob — FotMob API client for Python

Python client for Crawlora's hosted FotMob API. It exposes 31 API endpoints covering leagues, matches, fixtures, teams, players, search, standings, news, and rankings. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-python-homepage); the package does not run a browser or scrape
FotMob locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
FotMob or its owners.

## Install

```sh
python -m pip install crawlora-fotmob
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_fotmob import FotMobClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FotMobClient(api_key=api_key) as client:
    result_1 = client.leagues()
    print(result_1)
    result_2 = client.search(term='Premier League')
    print(result_2)
```

The package also exports `Client` as an alias for `FotMobClient`. Operation
methods are available directly in snake_case and through the `fotmob`
group. The async package client is `AsyncFotMobClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-fotmob/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-fotmob/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_fotmob import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.leagues()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-fotmob/blob/main/examples/python.py) for a complete usage example.

## Supported FotMob API endpoints

This package exposes every route below through direct snake_case methods and the `fotmob` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-fotmob/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/fotmob/audio-matches` | `fotmob-audio-matches` | FotMob matches with audio commentary |
| `GET` | `/fotmob/fifa-ranking-periods` | `fotmob-fifa-ranking-periods` | FotMob FIFA ranking period directory |
| `GET` | `/fotmob/fifa-rankings` | `fotmob-fifa-rankings` | FotMob FIFA national-team rankings |
| `GET` | `/fotmob/latest-news` | `fotmob-latest-news` | FotMob latest football news |
| `GET` | `/fotmob/league` | `fotmob-league` | FotMob league details and sections |
| `GET` | `/fotmob/leagues` | `fotmob-leagues` | FotMob competition directory |
| `GET` | `/fotmob/lineup-builder-players` | `fotmob-lineup-builder-players` | FotMob lineup builder player metadata |
| `GET` | `/fotmob/lineup-builder-team` | `fotmob-lineup-builder-team` | FotMob lineup builder team data |
| `GET` | `/fotmob/match` | `fotmob-match` | FotMob match details |
| `GET` | `/fotmob/match-media` | `fotmob-match-media` | FotMob match videos and media metadata |
| `GET` | `/fotmob/matches` | `fotmob-matches` | FotMob matches for a date |
| `GET` | `/fotmob/news` | `fotmob-news` | FotMob league news |
| `GET` | `/fotmob/news-article` | `fotmob-news-article` | FotMob full top-news article |
| `GET` | `/fotmob/player` | `fotmob-player` | FotMob player profile |
| `GET` | `/fotmob/player-match-stats` | `fotmob-player-match-stats` | FotMob player match stats |
| `GET` | `/fotmob/player-matches` | `fotmob-player-matches` | FotMob player match history |
| `GET` | `/fotmob/player-stats` | `fotmob-player-stats` | FotMob player season statistics |
| `GET` | `/fotmob/search` | `fotmob-search` | Search FotMob entities |
| `GET` | `/fotmob/seasons` | `fotmob-seasons` | FotMob league season discovery |
| `GET` | `/fotmob/stats` | `fotmob-stats` | FotMob league player or team statistics |
| `GET` | `/fotmob/stats-categories` | `fotmob-stats-categories` | FotMob league stat categories and seasons |
| `GET` | `/fotmob/table` | `fotmob-table` | FotMob league table |
| `GET` | `/fotmob/team` | `fotmob-team` | FotMob team details |
| `GET` | `/fotmob/team-fixtures` | `fotmob-team-fixtures` | FotMob paginated team fixtures |
| `GET` | `/fotmob/team-news` | `fotmob-team-news` | FotMob team news |
| `GET` | `/fotmob/transfers` | `fotmob-transfers` | FotMob transfer center |
| `GET` | `/fotmob/trending-news` | `fotmob-trending-news` | FotMob trending football news |
| `GET` | `/fotmob/trending-searches` | `fotmob-trending-searches` | FotMob trending search suggestions |
| `GET` | `/fotmob/tv-guide` | `fotmob-tv-guide` | FotMob football TV guide |
| `GET` | `/fotmob/tv-guide-channels` | `fotmob-tv-guide-channels` | FotMob TV guide channels |
| `GET` | `/fotmob/tv-guide-countries` | `fotmob-tv-guide-countries` | FotMob TV guide country directory |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
