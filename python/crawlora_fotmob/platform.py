"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class FotMobClient(CrawloraClient):
    """Synchronous FotMob API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-fotmob-python/0.1.3')
        super().__init__(*args, **kwargs)

    def audio_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-audio-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def fifa_ranking_periods(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-fifa-ranking-periods', params, response_type=response_type, timeout=timeout, headers=headers)

    def fifa_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-fifa-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    def latest_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-latest-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def league(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-league', params, response_type=response_type, timeout=timeout, headers=headers)

    def leagues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-leagues', params, response_type=response_type, timeout=timeout, headers=headers)

    def lineup_builder_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-lineup-builder-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def lineup_builder_team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-lineup-builder-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_media(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-match-media', params, response_type=response_type, timeout=timeout, headers=headers)

    def matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-news-article', params, response_type=response_type, timeout=timeout, headers=headers)

    def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_match_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-player-match-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-player-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def stats_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-stats-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def table(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-table', params, response_type=response_type, timeout=timeout, headers=headers)

    def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_fixtures(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-team-fixtures', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-team-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    def trending_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-trending-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def trending_searches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-trending-searches', params, response_type=response_type, timeout=timeout, headers=headers)

    def tv_guide(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-tv-guide', params, response_type=response_type, timeout=timeout, headers=headers)

    def tv_guide_channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-tv-guide-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    def tv_guide_countries(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fotmob-tv-guide-countries', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncFotMobClient(AsyncCrawloraClient):
    """Asynchronous FotMob API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-fotmob-python/0.1.3')
        super().__init__(*args, **kwargs)

    async def audio_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-audio-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def fifa_ranking_periods(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-fifa-ranking-periods', params, response_type=response_type, timeout=timeout, headers=headers)

    async def fifa_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-fifa-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def latest_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-latest-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def league(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-league', params, response_type=response_type, timeout=timeout, headers=headers)

    async def leagues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-leagues', params, response_type=response_type, timeout=timeout, headers=headers)

    async def lineup_builder_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-lineup-builder-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def lineup_builder_team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-lineup-builder-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_media(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-match-media', params, response_type=response_type, timeout=timeout, headers=headers)

    async def matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-news-article', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_match_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-player-match-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-player-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stats_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-stats-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def table(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-table', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_fixtures(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-team-fixtures', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-team-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trending_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-trending-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trending_searches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-trending-searches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tv_guide(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-tv-guide', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tv_guide_channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-tv-guide-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tv_guide_countries(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fotmob-tv-guide-countries', params, response_type=response_type, timeout=timeout, headers=headers)
