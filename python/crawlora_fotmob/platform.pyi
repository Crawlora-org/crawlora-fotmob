from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelFotmobResponseDoc = TypedDict('ModelFotmobResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFotmobSourceDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFotmobSourceDataDoc = TypedDict('ModelFotmobSourceDataDoc', {
    'data': NotRequired[dict[str, Any]],
    'source_url': NotRequired[str],
}, total=False)

ModelFotmobNewsListResponseDoc = TypedDict('ModelFotmobNewsListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFotmobSourceNewsListDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFotmobSourceNewsListDoc = TypedDict('ModelFotmobSourceNewsListDoc', {
    'data': NotRequired[list[ModelFotmobNewsItemDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFotmobNewsItemDoc = TypedDict('ModelFotmobNewsItemDoc', {
    'gmtTime': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'language': NotRequired[str],
    'lead': NotRequired[str],
    'page': NotRequired[ModelFotmobNewsItemPageDoc],
    'sourceIconUrl': NotRequired[str],
    'sourceStr': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFotmobNewsItemPageDoc = TypedDict('ModelFotmobNewsItemPageDoc', {
    'url': NotRequired[str],
}, total=False)

ModelFotmobFifaRankingsResponseDoc = TypedDict('ModelFotmobFifaRankingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFotmobFifaRankingRowsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFotmobFifaRankingRowsDataDoc = TypedDict('ModelFotmobFifaRankingRowsDataDoc', {
    'data': NotRequired[list[ModelFotmobFifaRankingRowDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFotmobFifaRankingRowDoc = TypedDict('ModelFotmobFifaRankingRowDoc', {
    'gainedRank': NotRequired[bool],
    'id': NotRequired[int],
    'lostRank': NotRequired[bool],
    'name': NotRequired[str],
    'pointsDiff': NotRequired[int],
    'previousPoints': NotRequired[int],
    'rank': NotRequired[int],
    'totalPoints': NotRequired[int],
}, total=False)

ModelFotmobFifaRankingPeriodsResponseDoc = TypedDict('ModelFotmobFifaRankingPeriodsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFotmobFifaRankingPeriodData],
    'msg': NotRequired[str],
}, total=False)

ModelFotmobFifaRankingPeriodData = TypedDict('ModelFotmobFifaRankingPeriodData', {
    'data': NotRequired[list[ModelFotmobFifaRankingPeriodItemDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFotmobFifaRankingPeriodItemDoc = TypedDict('ModelFotmobFifaRankingPeriodItemDoc', {
    'periodId': NotRequired[str],
    'periodName': NotRequired[str],
}, total=False)

FotmobAudioMatchesResponse = ModelFotmobResponseDoc
FotmobAudioMatchesParams = TypedDict('FotmobAudioMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobFifaRankingPeriodsResponse = ModelFotmobFifaRankingPeriodsResponseDoc
FotmobFifaRankingPeriodsParams = TypedDict('FotmobFifaRankingPeriodsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'gender': Required[Literal['men', 'women']],
}, total=False)

FotmobFifaRankingsResponse = ModelFotmobFifaRankingsResponseDoc
FotmobFifaRankingsParams = TypedDict('FotmobFifaRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'gender': Required[Literal['men', 'women']],
    'period_id': Required[str],
}, total=False)

FotmobLatestNewsResponse = ModelFotmobNewsListResponseDoc
FotmobLatestNewsParams = TypedDict('FotmobLatestNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'start_index': NotRequired[int],
}, total=False)

FotmobLeagueResponse = ModelFotmobResponseDoc
FotmobLeagueParams = TypedDict('FotmobLeagueParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
    'season': NotRequired[str],
    'shotmap': NotRequired[bool],
}, total=False)

FotmobLeaguesResponse = ModelFotmobResponseDoc
FotmobLeaguesParams = TypedDict('FotmobLeaguesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobLineupBuilderPlayersResponse = ModelFotmobResponseDoc
FotmobLineupBuilderPlayersParams = TypedDict('FotmobLineupBuilderPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_ids': Required[str],
}, total=False)

FotmobLineupBuilderTeamResponse = ModelFotmobResponseDoc
FotmobLineupBuilderTeamParams = TypedDict('FotmobLineupBuilderTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
}, total=False)

FotmobMatchResponse = ModelFotmobResponseDoc
FotmobMatchParams = TypedDict('FotmobMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobMatchMediaResponse = ModelFotmobResponseDoc
FotmobMatchMediaParams = TypedDict('FotmobMatchMediaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobMatchesResponse = ModelFotmobResponseDoc
FotmobMatchesParams = TypedDict('FotmobMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'date': Required[str],
    'timezone': NotRequired[str],
}, total=False)

FotmobNewsResponse = ModelFotmobResponseDoc
FotmobNewsParams = TypedDict('FotmobNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
    'start_index': NotRequired[int],
}, total=False)

FotmobNewsArticleResponse = ModelFotmobResponseDoc
FotmobNewsArticleParams = TypedDict('FotmobNewsArticleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobPlayerResponse = ModelFotmobResponseDoc
FotmobPlayerParams = TypedDict('FotmobPlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'include_market_values': NotRequired[bool],
}, total=False)

FotmobPlayerMatchStatsResponse = ModelFotmobResponseDoc
FotmobPlayerMatchStatsParams = TypedDict('FotmobPlayerMatchStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'match_id': Required[str],
}, total=False)

FotmobPlayerMatchesResponse = ModelFotmobResponseDoc
FotmobPlayerMatchesParams = TypedDict('FotmobPlayerMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'league_id': NotRequired[str],
    'team_id': NotRequired[str],
    'before': NotRequired[str],
}, total=False)

FotmobPlayerStatsResponse = ModelFotmobResponseDoc
FotmobPlayerStatsParams = TypedDict('FotmobPlayerStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'season_id': Required[str],
}, total=False)

FotmobSearchResponse = ModelFotmobResponseDoc
FotmobSearchParams = TypedDict('FotmobSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
}, total=False)

FotmobSeasonsResponse = ModelFotmobResponseDoc
FotmobSeasonsParams = TypedDict('FotmobSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
}, total=False)

FotmobStatsResponse = ModelFotmobResponseDoc
FotmobStatsParams = TypedDict('FotmobStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
    'stat': Required[str],
    'team_id': NotRequired[str],
    'position': NotRequired[Literal['all', 'striker', 'winger', 'attackingMidfielder', 'midfielder', 'fullback', 'centerBack']],
}, total=False)

FotmobStatsCategoriesResponse = ModelFotmobResponseDoc
FotmobStatsCategoriesParams = TypedDict('FotmobStatsCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
}, total=False)

FotmobTableResponse = ModelFotmobResponseDoc
FotmobTableParams = TypedDict('FotmobTableParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
}, total=False)

FotmobTeamResponse = ModelFotmobResponseDoc
FotmobTeamParams = TypedDict('FotmobTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobTeamFixturesResponse = ModelFotmobResponseDoc
FotmobTeamFixturesParams = TypedDict('FotmobTeamFixturesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
    'cursor': Required[str],
}, total=False)

FotmobTeamNewsResponse = ModelFotmobResponseDoc
FotmobTeamNewsParams = TypedDict('FotmobTeamNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'start_index': NotRequired[int],
}, total=False)

FotmobTransfersResponse = ModelFotmobResponseDoc
FotmobTransfersParams = TypedDict('FotmobTransfersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mode': NotRequired[Literal['all', 'rumours', 'popular']],
    'page': NotRequired[int],
    'last': NotRequired[Literal['6months', '1year', '2years', '3years']],
    'direction': NotRequired[Literal['all', 'in', 'out']],
    'min_fee': NotRequired[int],
    'max_fee': NotRequired[int],
    'league_ids': NotRequired[str],
    'team_ids': NotRequired[str],
    'order_by': NotRequired[Literal['lastModified', 'fee', 'date', 'name', 'fromClubName', 'toClubName']],
    'exclude_extensions': NotRequired[bool],
    'likely_only': NotRequired[bool],
}, total=False)

FotmobTrendingNewsResponse = ModelFotmobNewsListResponseDoc
FotmobTrendingNewsParams = TypedDict('FotmobTrendingNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobTrendingSearchesResponse = ModelFotmobResponseDoc
FotmobTrendingSearchesParams = TypedDict('FotmobTrendingSearchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobTvGuideResponse = ModelFotmobResponseDoc
FotmobTvGuideParams = TypedDict('FotmobTvGuideParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
    'timezone': NotRequired[str],
}, total=False)

FotmobTvGuideChannelsResponse = ModelFotmobResponseDoc
FotmobTvGuideChannelsParams = TypedDict('FotmobTvGuideChannelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
}, total=False)

FotmobTvGuideCountriesResponse = ModelFotmobResponseDoc
FotmobTvGuideCountriesParams = TypedDict('FotmobTvGuideCountriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

class FotmobGroup:
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesParams]) -> FotmobAudioMatchesResponse: ...
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsParams]) -> FotmobFifaRankingPeriodsResponse: ...
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsParams]) -> FotmobFifaRankingsResponse: ...
    def latest_news(self, **params: Unpack[FotmobLatestNewsParams]) -> FotmobLatestNewsResponse: ...
    def league(self, **params: Unpack[FotmobLeagueParams]) -> FotmobLeagueResponse: ...
    def leagues(self, **params: Unpack[FotmobLeaguesParams]) -> FotmobLeaguesResponse: ...
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersParams]) -> FotmobLineupBuilderPlayersResponse: ...
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamParams]) -> FotmobLineupBuilderTeamResponse: ...
    def match(self, **params: Unpack[FotmobMatchParams]) -> FotmobMatchResponse: ...
    def match_media(self, **params: Unpack[FotmobMatchMediaParams]) -> FotmobMatchMediaResponse: ...
    def matches(self, **params: Unpack[FotmobMatchesParams]) -> FotmobMatchesResponse: ...
    def news(self, **params: Unpack[FotmobNewsParams]) -> FotmobNewsResponse: ...
    def news_article(self, **params: Unpack[FotmobNewsArticleParams]) -> FotmobNewsArticleResponse: ...
    def player(self, **params: Unpack[FotmobPlayerParams]) -> FotmobPlayerResponse: ...
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsParams]) -> FotmobPlayerMatchStatsResponse: ...
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesParams]) -> FotmobPlayerMatchesResponse: ...
    def player_stats(self, **params: Unpack[FotmobPlayerStatsParams]) -> FotmobPlayerStatsResponse: ...
    def search(self, **params: Unpack[FotmobSearchParams]) -> FotmobSearchResponse: ...
    def seasons(self, **params: Unpack[FotmobSeasonsParams]) -> FotmobSeasonsResponse: ...
    def stats(self, **params: Unpack[FotmobStatsParams]) -> FotmobStatsResponse: ...
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesParams]) -> FotmobStatsCategoriesResponse: ...
    def table(self, **params: Unpack[FotmobTableParams]) -> FotmobTableResponse: ...
    def team(self, **params: Unpack[FotmobTeamParams]) -> FotmobTeamResponse: ...
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesParams]) -> FotmobTeamFixturesResponse: ...
    def team_news(self, **params: Unpack[FotmobTeamNewsParams]) -> FotmobTeamNewsResponse: ...
    def transfers(self, **params: Unpack[FotmobTransfersParams]) -> FotmobTransfersResponse: ...
    def trending_news(self, **params: Unpack[FotmobTrendingNewsParams]) -> FotmobTrendingNewsResponse: ...
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesParams]) -> FotmobTrendingSearchesResponse: ...
    def tv_guide(self, **params: Unpack[FotmobTvGuideParams]) -> FotmobTvGuideResponse: ...
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsParams]) -> FotmobTvGuideChannelsResponse: ...
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesParams]) -> FotmobTvGuideCountriesResponse: ...

OperationId = Literal[
    'fotmob-audio-matches',
    'fotmob-fifa-ranking-periods',
    'fotmob-fifa-rankings',
    'fotmob-latest-news',
    'fotmob-league',
    'fotmob-leagues',
    'fotmob-lineup-builder-players',
    'fotmob-lineup-builder-team',
    'fotmob-match',
    'fotmob-match-media',
    'fotmob-matches',
    'fotmob-news',
    'fotmob-news-article',
    'fotmob-player',
    'fotmob-player-match-stats',
    'fotmob-player-matches',
    'fotmob-player-stats',
    'fotmob-search',
    'fotmob-seasons',
    'fotmob-stats',
    'fotmob-stats-categories',
    'fotmob-table',
    'fotmob-team',
    'fotmob-team-fixtures',
    'fotmob-team-news',
    'fotmob-transfers',
    'fotmob-trending-news',
    'fotmob-trending-searches',
    'fotmob-tv-guide',
    'fotmob-tv-guide-channels',
    'fotmob-tv-guide-countries',
]

class CrawloraClient:
    fotmob: FotmobGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-audio-matches'],
        params: FotmobAudioMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobAudioMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-fifa-ranking-periods'],
        params: FotmobFifaRankingPeriodsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobFifaRankingPeriodsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-fifa-rankings'],
        params: FotmobFifaRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobFifaRankingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-latest-news'],
        params: FotmobLatestNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLatestNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-league'],
        params: FotmobLeagueParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLeagueResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-leagues'],
        params: FotmobLeaguesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLeaguesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-lineup-builder-players'],
        params: FotmobLineupBuilderPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLineupBuilderPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-lineup-builder-team'],
        params: FotmobLineupBuilderTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLineupBuilderTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-match'],
        params: FotmobMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-match-media'],
        params: FotmobMatchMediaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobMatchMediaResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-matches'],
        params: FotmobMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-news'],
        params: FotmobNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-news-article'],
        params: FotmobNewsArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobNewsArticleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-player'],
        params: FotmobPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobPlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-player-match-stats'],
        params: FotmobPlayerMatchStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobPlayerMatchStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-player-matches'],
        params: FotmobPlayerMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobPlayerMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-player-stats'],
        params: FotmobPlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobPlayerStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-search'],
        params: FotmobSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-seasons'],
        params: FotmobSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobSeasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-stats'],
        params: FotmobStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-stats-categories'],
        params: FotmobStatsCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobStatsCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-table'],
        params: FotmobTableParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTableResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-team'],
        params: FotmobTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-team-fixtures'],
        params: FotmobTeamFixturesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTeamFixturesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-team-news'],
        params: FotmobTeamNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTeamNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-transfers'],
        params: FotmobTransfersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTransfersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-trending-news'],
        params: FotmobTrendingNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTrendingNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-trending-searches'],
        params: FotmobTrendingSearchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTrendingSearchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-tv-guide'],
        params: FotmobTvGuideParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTvGuideResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-tv-guide-channels'],
        params: FotmobTvGuideChannelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTvGuideChannelsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fotmob-tv-guide-countries'],
        params: FotmobTvGuideCountriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTvGuideCountriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-audio-matches'],
        params: FotmobAudioMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobAudioMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-fifa-ranking-periods'],
        params: FotmobFifaRankingPeriodsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobFifaRankingPeriodsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-fifa-rankings'],
        params: FotmobFifaRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobFifaRankingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-latest-news'],
        params: FotmobLatestNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLatestNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-league'],
        params: FotmobLeagueParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLeagueResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-leagues'],
        params: FotmobLeaguesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLeaguesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-lineup-builder-players'],
        params: FotmobLineupBuilderPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLineupBuilderPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-lineup-builder-team'],
        params: FotmobLineupBuilderTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobLineupBuilderTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-match'],
        params: FotmobMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-match-media'],
        params: FotmobMatchMediaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobMatchMediaResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-matches'],
        params: FotmobMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-news'],
        params: FotmobNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-news-article'],
        params: FotmobNewsArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobNewsArticleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-player'],
        params: FotmobPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobPlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-player-match-stats'],
        params: FotmobPlayerMatchStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobPlayerMatchStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-player-matches'],
        params: FotmobPlayerMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobPlayerMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-player-stats'],
        params: FotmobPlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobPlayerStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-search'],
        params: FotmobSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-seasons'],
        params: FotmobSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobSeasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-stats'],
        params: FotmobStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-stats-categories'],
        params: FotmobStatsCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobStatsCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-table'],
        params: FotmobTableParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTableResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-team'],
        params: FotmobTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-team-fixtures'],
        params: FotmobTeamFixturesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTeamFixturesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-team-news'],
        params: FotmobTeamNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTeamNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-transfers'],
        params: FotmobTransfersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTransfersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-trending-news'],
        params: FotmobTrendingNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTrendingNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-trending-searches'],
        params: FotmobTrendingSearchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTrendingSearchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-tv-guide'],
        params: FotmobTvGuideParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTvGuideResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-tv-guide-channels'],
        params: FotmobTvGuideChannelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTvGuideChannelsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fotmob-tv-guide-countries'],
        params: FotmobTvGuideCountriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FotmobTvGuideCountriesResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class FotMobClient(CrawloraClient):
    def __enter__(self) -> FotMobClient: ...
    fotmob: FotmobGroup
    @overload
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesTextResponseParams]) -> str: ...
    @overload
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesParams]) -> FotmobAudioMatchesResponse: ...
    @overload
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsTextResponseParams]) -> str: ...
    @overload
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsParams]) -> FotmobFifaRankingPeriodsResponse: ...
    @overload
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsTextResponseParams]) -> str: ...
    @overload
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsParams]) -> FotmobFifaRankingsResponse: ...
    @overload
    def latest_news(self, **params: Unpack[FotmobLatestNewsStreamParams]) -> BinaryIO: ...
    @overload
    def latest_news(self, **params: Unpack[FotmobLatestNewsTextResponseParams]) -> str: ...
    @overload
    def latest_news(self, **params: Unpack[FotmobLatestNewsParams]) -> FotmobLatestNewsResponse: ...
    @overload
    def league(self, **params: Unpack[FotmobLeagueStreamParams]) -> BinaryIO: ...
    @overload
    def league(self, **params: Unpack[FotmobLeagueTextResponseParams]) -> str: ...
    @overload
    def league(self, **params: Unpack[FotmobLeagueParams]) -> FotmobLeagueResponse: ...
    @overload
    def leagues(self, **params: Unpack[FotmobLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    def leagues(self, **params: Unpack[FotmobLeaguesTextResponseParams]) -> str: ...
    @overload
    def leagues(self, **params: Unpack[FotmobLeaguesParams]) -> FotmobLeaguesResponse: ...
    @overload
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersTextResponseParams]) -> str: ...
    @overload
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersParams]) -> FotmobLineupBuilderPlayersResponse: ...
    @overload
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamStreamParams]) -> BinaryIO: ...
    @overload
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamTextResponseParams]) -> str: ...
    @overload
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamParams]) -> FotmobLineupBuilderTeamResponse: ...
    @overload
    def match(self, **params: Unpack[FotmobMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[FotmobMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[FotmobMatchParams]) -> FotmobMatchResponse: ...
    @overload
    def match_media(self, **params: Unpack[FotmobMatchMediaStreamParams]) -> BinaryIO: ...
    @overload
    def match_media(self, **params: Unpack[FotmobMatchMediaTextResponseParams]) -> str: ...
    @overload
    def match_media(self, **params: Unpack[FotmobMatchMediaParams]) -> FotmobMatchMediaResponse: ...
    @overload
    def matches(self, **params: Unpack[FotmobMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matches(self, **params: Unpack[FotmobMatchesTextResponseParams]) -> str: ...
    @overload
    def matches(self, **params: Unpack[FotmobMatchesParams]) -> FotmobMatchesResponse: ...
    @overload
    def news(self, **params: Unpack[FotmobNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[FotmobNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[FotmobNewsParams]) -> FotmobNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[FotmobNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[FotmobNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[FotmobNewsArticleParams]) -> FotmobNewsArticleResponse: ...
    @overload
    def player(self, **params: Unpack[FotmobPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[FotmobPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[FotmobPlayerParams]) -> FotmobPlayerResponse: ...
    @overload
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsTextResponseParams]) -> str: ...
    @overload
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsParams]) -> FotmobPlayerMatchStatsResponse: ...
    @overload
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesParams]) -> FotmobPlayerMatchesResponse: ...
    @overload
    def player_stats(self, **params: Unpack[FotmobPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_stats(self, **params: Unpack[FotmobPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def player_stats(self, **params: Unpack[FotmobPlayerStatsParams]) -> FotmobPlayerStatsResponse: ...
    @overload
    def search(self, **params: Unpack[FotmobSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[FotmobSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[FotmobSearchParams]) -> FotmobSearchResponse: ...
    @overload
    def seasons(self, **params: Unpack[FotmobSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def seasons(self, **params: Unpack[FotmobSeasonsTextResponseParams]) -> str: ...
    @overload
    def seasons(self, **params: Unpack[FotmobSeasonsParams]) -> FotmobSeasonsResponse: ...
    @overload
    def stats(self, **params: Unpack[FotmobStatsStreamParams]) -> BinaryIO: ...
    @overload
    def stats(self, **params: Unpack[FotmobStatsTextResponseParams]) -> str: ...
    @overload
    def stats(self, **params: Unpack[FotmobStatsParams]) -> FotmobStatsResponse: ...
    @overload
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesTextResponseParams]) -> str: ...
    @overload
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesParams]) -> FotmobStatsCategoriesResponse: ...
    @overload
    def table(self, **params: Unpack[FotmobTableStreamParams]) -> BinaryIO: ...
    @overload
    def table(self, **params: Unpack[FotmobTableTextResponseParams]) -> str: ...
    @overload
    def table(self, **params: Unpack[FotmobTableParams]) -> FotmobTableResponse: ...
    @overload
    def team(self, **params: Unpack[FotmobTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[FotmobTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[FotmobTeamParams]) -> FotmobTeamResponse: ...
    @overload
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesTextResponseParams]) -> str: ...
    @overload
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesParams]) -> FotmobTeamFixturesResponse: ...
    @overload
    def team_news(self, **params: Unpack[FotmobTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    def team_news(self, **params: Unpack[FotmobTeamNewsTextResponseParams]) -> str: ...
    @overload
    def team_news(self, **params: Unpack[FotmobTeamNewsParams]) -> FotmobTeamNewsResponse: ...
    @overload
    def transfers(self, **params: Unpack[FotmobTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def transfers(self, **params: Unpack[FotmobTransfersTextResponseParams]) -> str: ...
    @overload
    def transfers(self, **params: Unpack[FotmobTransfersParams]) -> FotmobTransfersResponse: ...
    @overload
    def trending_news(self, **params: Unpack[FotmobTrendingNewsStreamParams]) -> BinaryIO: ...
    @overload
    def trending_news(self, **params: Unpack[FotmobTrendingNewsTextResponseParams]) -> str: ...
    @overload
    def trending_news(self, **params: Unpack[FotmobTrendingNewsParams]) -> FotmobTrendingNewsResponse: ...
    @overload
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesStreamParams]) -> BinaryIO: ...
    @overload
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesTextResponseParams]) -> str: ...
    @overload
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesParams]) -> FotmobTrendingSearchesResponse: ...
    @overload
    def tv_guide(self, **params: Unpack[FotmobTvGuideStreamParams]) -> BinaryIO: ...
    @overload
    def tv_guide(self, **params: Unpack[FotmobTvGuideTextResponseParams]) -> str: ...
    @overload
    def tv_guide(self, **params: Unpack[FotmobTvGuideParams]) -> FotmobTvGuideResponse: ...
    @overload
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsTextResponseParams]) -> str: ...
    @overload
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsParams]) -> FotmobTvGuideChannelsResponse: ...
    @overload
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesStreamParams]) -> BinaryIO: ...
    @overload
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesTextResponseParams]) -> str: ...
    @overload
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesParams]) -> FotmobTvGuideCountriesResponse: ...

class AsyncFotMobClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncFotMobClient: ...
    fotmob: _AsyncFotmobGroup
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesTextResponseParams]) -> str: ...
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesParams]) -> FotmobAudioMatchesResponse: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsTextResponseParams]) -> str: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsParams]) -> FotmobFifaRankingPeriodsResponse: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsTextResponseParams]) -> str: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsParams]) -> FotmobFifaRankingsResponse: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsTextResponseParams]) -> str: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsParams]) -> FotmobLatestNewsResponse: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueStreamParams]) -> BinaryIO: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueTextResponseParams]) -> str: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueParams]) -> FotmobLeagueResponse: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesParams]) -> FotmobLeaguesResponse: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersTextResponseParams]) -> str: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersParams]) -> FotmobLineupBuilderPlayersResponse: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamTextResponseParams]) -> str: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamParams]) -> FotmobLineupBuilderTeamResponse: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchParams]) -> FotmobMatchResponse: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaStreamParams]) -> BinaryIO: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaTextResponseParams]) -> str: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaParams]) -> FotmobMatchMediaResponse: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesParams]) -> FotmobMatchesResponse: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsParams]) -> FotmobNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleParams]) -> FotmobNewsArticleResponse: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerParams]) -> FotmobPlayerResponse: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsTextResponseParams]) -> str: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsParams]) -> FotmobPlayerMatchStatsResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesParams]) -> FotmobPlayerMatchesResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsParams]) -> FotmobPlayerStatsResponse: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchParams]) -> FotmobSearchResponse: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsTextResponseParams]) -> str: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsParams]) -> FotmobSeasonsResponse: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsTextResponseParams]) -> str: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsParams]) -> FotmobStatsResponse: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesParams]) -> FotmobStatsCategoriesResponse: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableStreamParams]) -> BinaryIO: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableTextResponseParams]) -> str: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableParams]) -> FotmobTableResponse: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamParams]) -> FotmobTeamResponse: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesTextResponseParams]) -> str: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesParams]) -> FotmobTeamFixturesResponse: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsTextResponseParams]) -> str: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsParams]) -> FotmobTeamNewsResponse: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersTextResponseParams]) -> str: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersParams]) -> FotmobTransfersResponse: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsTextResponseParams]) -> str: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsParams]) -> FotmobTrendingNewsResponse: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesTextResponseParams]) -> str: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesParams]) -> FotmobTrendingSearchesResponse: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideTextResponseParams]) -> str: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideParams]) -> FotmobTvGuideResponse: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsTextResponseParams]) -> str: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsParams]) -> FotmobTvGuideChannelsResponse: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesTextResponseParams]) -> str: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesParams]) -> FotmobTvGuideCountriesResponse: ...

class _AsyncFotmobGroup:
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesTextResponseParams]) -> str: ...
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesParams]) -> FotmobAudioMatchesResponse: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsTextResponseParams]) -> str: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsParams]) -> FotmobFifaRankingPeriodsResponse: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsTextResponseParams]) -> str: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsParams]) -> FotmobFifaRankingsResponse: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsTextResponseParams]) -> str: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsParams]) -> FotmobLatestNewsResponse: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueStreamParams]) -> BinaryIO: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueTextResponseParams]) -> str: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueParams]) -> FotmobLeagueResponse: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesParams]) -> FotmobLeaguesResponse: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersTextResponseParams]) -> str: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersParams]) -> FotmobLineupBuilderPlayersResponse: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamTextResponseParams]) -> str: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamParams]) -> FotmobLineupBuilderTeamResponse: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchParams]) -> FotmobMatchResponse: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaStreamParams]) -> BinaryIO: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaTextResponseParams]) -> str: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaParams]) -> FotmobMatchMediaResponse: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesParams]) -> FotmobMatchesResponse: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsParams]) -> FotmobNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleParams]) -> FotmobNewsArticleResponse: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerParams]) -> FotmobPlayerResponse: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsTextResponseParams]) -> str: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsParams]) -> FotmobPlayerMatchStatsResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesParams]) -> FotmobPlayerMatchesResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsParams]) -> FotmobPlayerStatsResponse: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchParams]) -> FotmobSearchResponse: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsTextResponseParams]) -> str: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsParams]) -> FotmobSeasonsResponse: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsTextResponseParams]) -> str: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsParams]) -> FotmobStatsResponse: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesParams]) -> FotmobStatsCategoriesResponse: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableStreamParams]) -> BinaryIO: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableTextResponseParams]) -> str: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableParams]) -> FotmobTableResponse: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamParams]) -> FotmobTeamResponse: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesTextResponseParams]) -> str: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesParams]) -> FotmobTeamFixturesResponse: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsTextResponseParams]) -> str: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsParams]) -> FotmobTeamNewsResponse: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersTextResponseParams]) -> str: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersParams]) -> FotmobTransfersResponse: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsTextResponseParams]) -> str: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsParams]) -> FotmobTrendingNewsResponse: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesTextResponseParams]) -> str: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesParams]) -> FotmobTrendingSearchesResponse: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideTextResponseParams]) -> str: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideParams]) -> FotmobTvGuideResponse: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsTextResponseParams]) -> str: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsParams]) -> FotmobTvGuideChannelsResponse: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesTextResponseParams]) -> str: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesParams]) -> FotmobTvGuideCountriesResponse: ...

FotmobAudioMatchesTextResponseParams = TypedDict('FotmobAudioMatchesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobAudioMatchesStreamParams = TypedDict('FotmobAudioMatchesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobFifaRankingPeriodsTextResponseParams = TypedDict('FotmobFifaRankingPeriodsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'gender': Required[Literal['men', 'women']],
}, total=False)

FotmobFifaRankingPeriodsStreamParams = TypedDict('FotmobFifaRankingPeriodsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'gender': Required[Literal['men', 'women']],
}, total=False)

FotmobFifaRankingsTextResponseParams = TypedDict('FotmobFifaRankingsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'gender': Required[Literal['men', 'women']],
    'period_id': Required[str],
}, total=False)

FotmobFifaRankingsStreamParams = TypedDict('FotmobFifaRankingsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'gender': Required[Literal['men', 'women']],
    'period_id': Required[str],
}, total=False)

FotmobLatestNewsTextResponseParams = TypedDict('FotmobLatestNewsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'start_index': NotRequired[int],
}, total=False)

FotmobLatestNewsStreamParams = TypedDict('FotmobLatestNewsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'start_index': NotRequired[int],
}, total=False)

FotmobLeagueTextResponseParams = TypedDict('FotmobLeagueTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
    'season': NotRequired[str],
    'shotmap': NotRequired[bool],
}, total=False)

FotmobLeagueStreamParams = TypedDict('FotmobLeagueStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
    'season': NotRequired[str],
    'shotmap': NotRequired[bool],
}, total=False)

FotmobLeaguesTextResponseParams = TypedDict('FotmobLeaguesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobLeaguesStreamParams = TypedDict('FotmobLeaguesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobLineupBuilderPlayersTextResponseParams = TypedDict('FotmobLineupBuilderPlayersTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_ids': Required[str],
}, total=False)

FotmobLineupBuilderPlayersStreamParams = TypedDict('FotmobLineupBuilderPlayersStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_ids': Required[str],
}, total=False)

FotmobLineupBuilderTeamTextResponseParams = TypedDict('FotmobLineupBuilderTeamTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
}, total=False)

FotmobLineupBuilderTeamStreamParams = TypedDict('FotmobLineupBuilderTeamStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
}, total=False)

FotmobMatchTextResponseParams = TypedDict('FotmobMatchTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobMatchStreamParams = TypedDict('FotmobMatchStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobMatchMediaTextResponseParams = TypedDict('FotmobMatchMediaTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobMatchMediaStreamParams = TypedDict('FotmobMatchMediaStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobMatchesTextResponseParams = TypedDict('FotmobMatchesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'date': Required[str],
    'timezone': NotRequired[str],
}, total=False)

FotmobMatchesStreamParams = TypedDict('FotmobMatchesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'date': Required[str],
    'timezone': NotRequired[str],
}, total=False)

FotmobNewsTextResponseParams = TypedDict('FotmobNewsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
    'start_index': NotRequired[int],
}, total=False)

FotmobNewsStreamParams = TypedDict('FotmobNewsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
    'start_index': NotRequired[int],
}, total=False)

FotmobNewsArticleTextResponseParams = TypedDict('FotmobNewsArticleTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobNewsArticleStreamParams = TypedDict('FotmobNewsArticleStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobPlayerTextResponseParams = TypedDict('FotmobPlayerTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'include_market_values': NotRequired[bool],
}, total=False)

FotmobPlayerStreamParams = TypedDict('FotmobPlayerStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'include_market_values': NotRequired[bool],
}, total=False)

FotmobPlayerMatchStatsTextResponseParams = TypedDict('FotmobPlayerMatchStatsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'match_id': Required[str],
}, total=False)

FotmobPlayerMatchStatsStreamParams = TypedDict('FotmobPlayerMatchStatsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'match_id': Required[str],
}, total=False)

FotmobPlayerMatchesTextResponseParams = TypedDict('FotmobPlayerMatchesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'league_id': NotRequired[str],
    'team_id': NotRequired[str],
    'before': NotRequired[str],
}, total=False)

FotmobPlayerMatchesStreamParams = TypedDict('FotmobPlayerMatchesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'league_id': NotRequired[str],
    'team_id': NotRequired[str],
    'before': NotRequired[str],
}, total=False)

FotmobPlayerStatsTextResponseParams = TypedDict('FotmobPlayerStatsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'season_id': Required[str],
}, total=False)

FotmobPlayerStatsStreamParams = TypedDict('FotmobPlayerStatsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'player_id': Required[str],
    'season_id': Required[str],
}, total=False)

FotmobSearchTextResponseParams = TypedDict('FotmobSearchTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
}, total=False)

FotmobSearchStreamParams = TypedDict('FotmobSearchStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
}, total=False)

FotmobSeasonsTextResponseParams = TypedDict('FotmobSeasonsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
}, total=False)

FotmobSeasonsStreamParams = TypedDict('FotmobSeasonsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
}, total=False)

FotmobStatsTextResponseParams = TypedDict('FotmobStatsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
    'stat': Required[str],
    'team_id': NotRequired[str],
    'position': NotRequired[Literal['all', 'striker', 'winger', 'attackingMidfielder', 'midfielder', 'fullback', 'centerBack']],
}, total=False)

FotmobStatsStreamParams = TypedDict('FotmobStatsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
    'stat': Required[str],
    'team_id': NotRequired[str],
    'position': NotRequired[Literal['all', 'striker', 'winger', 'attackingMidfielder', 'midfielder', 'fullback', 'centerBack']],
}, total=False)

FotmobStatsCategoriesTextResponseParams = TypedDict('FotmobStatsCategoriesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
}, total=False)

FotmobStatsCategoriesStreamParams = TypedDict('FotmobStatsCategoriesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
}, total=False)

FotmobTableTextResponseParams = TypedDict('FotmobTableTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
}, total=False)

FotmobTableStreamParams = TypedDict('FotmobTableStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[str],
}, total=False)

FotmobTeamTextResponseParams = TypedDict('FotmobTeamTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobTeamStreamParams = TypedDict('FotmobTeamStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FotmobTeamFixturesTextResponseParams = TypedDict('FotmobTeamFixturesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
    'cursor': Required[str],
}, total=False)

FotmobTeamFixturesStreamParams = TypedDict('FotmobTeamFixturesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
    'cursor': Required[str],
}, total=False)

FotmobTeamNewsTextResponseParams = TypedDict('FotmobTeamNewsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'start_index': NotRequired[int],
}, total=False)

FotmobTeamNewsStreamParams = TypedDict('FotmobTeamNewsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
    'start_index': NotRequired[int],
}, total=False)

FotmobTransfersTextResponseParams = TypedDict('FotmobTransfersTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mode': NotRequired[Literal['all', 'rumours', 'popular']],
    'page': NotRequired[int],
    'last': NotRequired[Literal['6months', '1year', '2years', '3years']],
    'direction': NotRequired[Literal['all', 'in', 'out']],
    'min_fee': NotRequired[int],
    'max_fee': NotRequired[int],
    'league_ids': NotRequired[str],
    'team_ids': NotRequired[str],
    'order_by': NotRequired[Literal['lastModified', 'fee', 'date', 'name', 'fromClubName', 'toClubName']],
    'exclude_extensions': NotRequired[bool],
    'likely_only': NotRequired[bool],
}, total=False)

FotmobTransfersStreamParams = TypedDict('FotmobTransfersStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mode': NotRequired[Literal['all', 'rumours', 'popular']],
    'page': NotRequired[int],
    'last': NotRequired[Literal['6months', '1year', '2years', '3years']],
    'direction': NotRequired[Literal['all', 'in', 'out']],
    'min_fee': NotRequired[int],
    'max_fee': NotRequired[int],
    'league_ids': NotRequired[str],
    'team_ids': NotRequired[str],
    'order_by': NotRequired[Literal['lastModified', 'fee', 'date', 'name', 'fromClubName', 'toClubName']],
    'exclude_extensions': NotRequired[bool],
    'likely_only': NotRequired[bool],
}, total=False)

FotmobTrendingNewsTextResponseParams = TypedDict('FotmobTrendingNewsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobTrendingNewsStreamParams = TypedDict('FotmobTrendingNewsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobTrendingSearchesTextResponseParams = TypedDict('FotmobTrendingSearchesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobTrendingSearchesStreamParams = TypedDict('FotmobTrendingSearchesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobTvGuideTextResponseParams = TypedDict('FotmobTvGuideTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
    'timezone': NotRequired[str],
}, total=False)

FotmobTvGuideStreamParams = TypedDict('FotmobTvGuideStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
    'timezone': NotRequired[str],
}, total=False)

FotmobTvGuideChannelsTextResponseParams = TypedDict('FotmobTvGuideChannelsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
}, total=False)

FotmobTvGuideChannelsStreamParams = TypedDict('FotmobTvGuideChannelsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
}, total=False)

FotmobTvGuideCountriesTextResponseParams = TypedDict('FotmobTvGuideCountriesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FotmobTvGuideCountriesStreamParams = TypedDict('FotmobTvGuideCountriesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)
