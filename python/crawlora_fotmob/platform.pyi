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
    @overload
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesTextResponseParams]) -> str: ...
    @overload
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesDefaultParams]) -> FotmobAudioMatchesResponse: ...
    @overload
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsTextResponseParams]) -> str: ...
    @overload
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsDefaultParams]) -> FotmobFifaRankingPeriodsResponse: ...
    @overload
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsTextResponseParams]) -> str: ...
    @overload
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsDefaultParams]) -> FotmobFifaRankingsResponse: ...
    @overload
    def latest_news(self, **params: Unpack[FotmobLatestNewsStreamParams]) -> BinaryIO: ...
    @overload
    def latest_news(self, **params: Unpack[FotmobLatestNewsTextResponseParams]) -> str: ...
    @overload
    def latest_news(self, **params: Unpack[FotmobLatestNewsDefaultParams]) -> FotmobLatestNewsResponse: ...
    @overload
    def league(self, **params: Unpack[FotmobLeagueStreamParams]) -> BinaryIO: ...
    @overload
    def league(self, **params: Unpack[FotmobLeagueTextResponseParams]) -> str: ...
    @overload
    def league(self, **params: Unpack[FotmobLeagueDefaultParams]) -> FotmobLeagueResponse: ...
    @overload
    def leagues(self, **params: Unpack[FotmobLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    def leagues(self, **params: Unpack[FotmobLeaguesTextResponseParams]) -> str: ...
    @overload
    def leagues(self, **params: Unpack[FotmobLeaguesDefaultParams]) -> FotmobLeaguesResponse: ...
    @overload
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersTextResponseParams]) -> str: ...
    @overload
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersDefaultParams]) -> FotmobLineupBuilderPlayersResponse: ...
    @overload
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamStreamParams]) -> BinaryIO: ...
    @overload
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamTextResponseParams]) -> str: ...
    @overload
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamDefaultParams]) -> FotmobLineupBuilderTeamResponse: ...
    @overload
    def match(self, **params: Unpack[FotmobMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[FotmobMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[FotmobMatchDefaultParams]) -> FotmobMatchResponse: ...
    @overload
    def match_media(self, **params: Unpack[FotmobMatchMediaStreamParams]) -> BinaryIO: ...
    @overload
    def match_media(self, **params: Unpack[FotmobMatchMediaTextResponseParams]) -> str: ...
    @overload
    def match_media(self, **params: Unpack[FotmobMatchMediaDefaultParams]) -> FotmobMatchMediaResponse: ...
    @overload
    def matches(self, **params: Unpack[FotmobMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matches(self, **params: Unpack[FotmobMatchesTextResponseParams]) -> str: ...
    @overload
    def matches(self, **params: Unpack[FotmobMatchesDefaultParams]) -> FotmobMatchesResponse: ...
    @overload
    def news(self, **params: Unpack[FotmobNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[FotmobNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[FotmobNewsDefaultParams]) -> FotmobNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[FotmobNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[FotmobNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[FotmobNewsArticleDefaultParams]) -> FotmobNewsArticleResponse: ...
    @overload
    def player(self, **params: Unpack[FotmobPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[FotmobPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[FotmobPlayerDefaultParams]) -> FotmobPlayerResponse: ...
    @overload
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsTextResponseParams]) -> str: ...
    @overload
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsDefaultParams]) -> FotmobPlayerMatchStatsResponse: ...
    @overload
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesDefaultParams]) -> FotmobPlayerMatchesResponse: ...
    @overload
    def player_stats(self, **params: Unpack[FotmobPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_stats(self, **params: Unpack[FotmobPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def player_stats(self, **params: Unpack[FotmobPlayerStatsDefaultParams]) -> FotmobPlayerStatsResponse: ...
    @overload
    def search(self, **params: Unpack[FotmobSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[FotmobSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[FotmobSearchDefaultParams]) -> FotmobSearchResponse: ...
    @overload
    def seasons(self, **params: Unpack[FotmobSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def seasons(self, **params: Unpack[FotmobSeasonsTextResponseParams]) -> str: ...
    @overload
    def seasons(self, **params: Unpack[FotmobSeasonsDefaultParams]) -> FotmobSeasonsResponse: ...
    @overload
    def stats(self, **params: Unpack[FotmobStatsStreamParams]) -> BinaryIO: ...
    @overload
    def stats(self, **params: Unpack[FotmobStatsTextResponseParams]) -> str: ...
    @overload
    def stats(self, **params: Unpack[FotmobStatsDefaultParams]) -> FotmobStatsResponse: ...
    @overload
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesTextResponseParams]) -> str: ...
    @overload
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesDefaultParams]) -> FotmobStatsCategoriesResponse: ...
    @overload
    def table(self, **params: Unpack[FotmobTableStreamParams]) -> BinaryIO: ...
    @overload
    def table(self, **params: Unpack[FotmobTableTextResponseParams]) -> str: ...
    @overload
    def table(self, **params: Unpack[FotmobTableDefaultParams]) -> FotmobTableResponse: ...
    @overload
    def team(self, **params: Unpack[FotmobTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[FotmobTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[FotmobTeamDefaultParams]) -> FotmobTeamResponse: ...
    @overload
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesTextResponseParams]) -> str: ...
    @overload
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesDefaultParams]) -> FotmobTeamFixturesResponse: ...
    @overload
    def team_news(self, **params: Unpack[FotmobTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    def team_news(self, **params: Unpack[FotmobTeamNewsTextResponseParams]) -> str: ...
    @overload
    def team_news(self, **params: Unpack[FotmobTeamNewsDefaultParams]) -> FotmobTeamNewsResponse: ...
    @overload
    def transfers(self, **params: Unpack[FotmobTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def transfers(self, **params: Unpack[FotmobTransfersTextResponseParams]) -> str: ...
    @overload
    def transfers(self, **params: Unpack[FotmobTransfersDefaultParams]) -> FotmobTransfersResponse: ...
    @overload
    def trending_news(self, **params: Unpack[FotmobTrendingNewsStreamParams]) -> BinaryIO: ...
    @overload
    def trending_news(self, **params: Unpack[FotmobTrendingNewsTextResponseParams]) -> str: ...
    @overload
    def trending_news(self, **params: Unpack[FotmobTrendingNewsDefaultParams]) -> FotmobTrendingNewsResponse: ...
    @overload
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesStreamParams]) -> BinaryIO: ...
    @overload
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesTextResponseParams]) -> str: ...
    @overload
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesDefaultParams]) -> FotmobTrendingSearchesResponse: ...
    @overload
    def tv_guide(self, **params: Unpack[FotmobTvGuideStreamParams]) -> BinaryIO: ...
    @overload
    def tv_guide(self, **params: Unpack[FotmobTvGuideTextResponseParams]) -> str: ...
    @overload
    def tv_guide(self, **params: Unpack[FotmobTvGuideDefaultParams]) -> FotmobTvGuideResponse: ...
    @overload
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsTextResponseParams]) -> str: ...
    @overload
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsDefaultParams]) -> FotmobTvGuideChannelsResponse: ...
    @overload
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesStreamParams]) -> BinaryIO: ...
    @overload
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesTextResponseParams]) -> str: ...
    @overload
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesDefaultParams]) -> FotmobTvGuideCountriesResponse: ...

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
    @overload
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesTextResponseParams]) -> str: ...
    @overload
    def audio_matches(self, **params: Unpack[FotmobAudioMatchesDefaultParams]) -> FotmobAudioMatchesResponse: ...
    @overload
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsTextResponseParams]) -> str: ...
    @overload
    def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsDefaultParams]) -> FotmobFifaRankingPeriodsResponse: ...
    @overload
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsTextResponseParams]) -> str: ...
    @overload
    def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsDefaultParams]) -> FotmobFifaRankingsResponse: ...
    @overload
    def latest_news(self, **params: Unpack[FotmobLatestNewsStreamParams]) -> BinaryIO: ...
    @overload
    def latest_news(self, **params: Unpack[FotmobLatestNewsTextResponseParams]) -> str: ...
    @overload
    def latest_news(self, **params: Unpack[FotmobLatestNewsDefaultParams]) -> FotmobLatestNewsResponse: ...
    @overload
    def league(self, **params: Unpack[FotmobLeagueStreamParams]) -> BinaryIO: ...
    @overload
    def league(self, **params: Unpack[FotmobLeagueTextResponseParams]) -> str: ...
    @overload
    def league(self, **params: Unpack[FotmobLeagueDefaultParams]) -> FotmobLeagueResponse: ...
    @overload
    def leagues(self, **params: Unpack[FotmobLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    def leagues(self, **params: Unpack[FotmobLeaguesTextResponseParams]) -> str: ...
    @overload
    def leagues(self, **params: Unpack[FotmobLeaguesDefaultParams]) -> FotmobLeaguesResponse: ...
    @overload
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersTextResponseParams]) -> str: ...
    @overload
    def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersDefaultParams]) -> FotmobLineupBuilderPlayersResponse: ...
    @overload
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamStreamParams]) -> BinaryIO: ...
    @overload
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamTextResponseParams]) -> str: ...
    @overload
    def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamDefaultParams]) -> FotmobLineupBuilderTeamResponse: ...
    @overload
    def match(self, **params: Unpack[FotmobMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[FotmobMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[FotmobMatchDefaultParams]) -> FotmobMatchResponse: ...
    @overload
    def match_media(self, **params: Unpack[FotmobMatchMediaStreamParams]) -> BinaryIO: ...
    @overload
    def match_media(self, **params: Unpack[FotmobMatchMediaTextResponseParams]) -> str: ...
    @overload
    def match_media(self, **params: Unpack[FotmobMatchMediaDefaultParams]) -> FotmobMatchMediaResponse: ...
    @overload
    def matches(self, **params: Unpack[FotmobMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matches(self, **params: Unpack[FotmobMatchesTextResponseParams]) -> str: ...
    @overload
    def matches(self, **params: Unpack[FotmobMatchesDefaultParams]) -> FotmobMatchesResponse: ...
    @overload
    def news(self, **params: Unpack[FotmobNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[FotmobNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[FotmobNewsDefaultParams]) -> FotmobNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[FotmobNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[FotmobNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[FotmobNewsArticleDefaultParams]) -> FotmobNewsArticleResponse: ...
    @overload
    def player(self, **params: Unpack[FotmobPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[FotmobPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[FotmobPlayerDefaultParams]) -> FotmobPlayerResponse: ...
    @overload
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsTextResponseParams]) -> str: ...
    @overload
    def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsDefaultParams]) -> FotmobPlayerMatchStatsResponse: ...
    @overload
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    def player_matches(self, **params: Unpack[FotmobPlayerMatchesDefaultParams]) -> FotmobPlayerMatchesResponse: ...
    @overload
    def player_stats(self, **params: Unpack[FotmobPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_stats(self, **params: Unpack[FotmobPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def player_stats(self, **params: Unpack[FotmobPlayerStatsDefaultParams]) -> FotmobPlayerStatsResponse: ...
    @overload
    def search(self, **params: Unpack[FotmobSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[FotmobSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[FotmobSearchDefaultParams]) -> FotmobSearchResponse: ...
    @overload
    def seasons(self, **params: Unpack[FotmobSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def seasons(self, **params: Unpack[FotmobSeasonsTextResponseParams]) -> str: ...
    @overload
    def seasons(self, **params: Unpack[FotmobSeasonsDefaultParams]) -> FotmobSeasonsResponse: ...
    @overload
    def stats(self, **params: Unpack[FotmobStatsStreamParams]) -> BinaryIO: ...
    @overload
    def stats(self, **params: Unpack[FotmobStatsTextResponseParams]) -> str: ...
    @overload
    def stats(self, **params: Unpack[FotmobStatsDefaultParams]) -> FotmobStatsResponse: ...
    @overload
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesTextResponseParams]) -> str: ...
    @overload
    def stats_categories(self, **params: Unpack[FotmobStatsCategoriesDefaultParams]) -> FotmobStatsCategoriesResponse: ...
    @overload
    def table(self, **params: Unpack[FotmobTableStreamParams]) -> BinaryIO: ...
    @overload
    def table(self, **params: Unpack[FotmobTableTextResponseParams]) -> str: ...
    @overload
    def table(self, **params: Unpack[FotmobTableDefaultParams]) -> FotmobTableResponse: ...
    @overload
    def team(self, **params: Unpack[FotmobTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[FotmobTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[FotmobTeamDefaultParams]) -> FotmobTeamResponse: ...
    @overload
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesTextResponseParams]) -> str: ...
    @overload
    def team_fixtures(self, **params: Unpack[FotmobTeamFixturesDefaultParams]) -> FotmobTeamFixturesResponse: ...
    @overload
    def team_news(self, **params: Unpack[FotmobTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    def team_news(self, **params: Unpack[FotmobTeamNewsTextResponseParams]) -> str: ...
    @overload
    def team_news(self, **params: Unpack[FotmobTeamNewsDefaultParams]) -> FotmobTeamNewsResponse: ...
    @overload
    def transfers(self, **params: Unpack[FotmobTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def transfers(self, **params: Unpack[FotmobTransfersTextResponseParams]) -> str: ...
    @overload
    def transfers(self, **params: Unpack[FotmobTransfersDefaultParams]) -> FotmobTransfersResponse: ...
    @overload
    def trending_news(self, **params: Unpack[FotmobTrendingNewsStreamParams]) -> BinaryIO: ...
    @overload
    def trending_news(self, **params: Unpack[FotmobTrendingNewsTextResponseParams]) -> str: ...
    @overload
    def trending_news(self, **params: Unpack[FotmobTrendingNewsDefaultParams]) -> FotmobTrendingNewsResponse: ...
    @overload
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesStreamParams]) -> BinaryIO: ...
    @overload
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesTextResponseParams]) -> str: ...
    @overload
    def trending_searches(self, **params: Unpack[FotmobTrendingSearchesDefaultParams]) -> FotmobTrendingSearchesResponse: ...
    @overload
    def tv_guide(self, **params: Unpack[FotmobTvGuideStreamParams]) -> BinaryIO: ...
    @overload
    def tv_guide(self, **params: Unpack[FotmobTvGuideTextResponseParams]) -> str: ...
    @overload
    def tv_guide(self, **params: Unpack[FotmobTvGuideDefaultParams]) -> FotmobTvGuideResponse: ...
    @overload
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsTextResponseParams]) -> str: ...
    @overload
    def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsDefaultParams]) -> FotmobTvGuideChannelsResponse: ...
    @overload
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesStreamParams]) -> BinaryIO: ...
    @overload
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesTextResponseParams]) -> str: ...
    @overload
    def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesDefaultParams]) -> FotmobTvGuideCountriesResponse: ...

class AsyncFotMobClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncFotMobClient: ...
    fotmob: _AsyncFotmobGroup
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesTextResponseParams]) -> str: ...
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesDefaultParams]) -> FotmobAudioMatchesResponse: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsTextResponseParams]) -> str: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsDefaultParams]) -> FotmobFifaRankingPeriodsResponse: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsTextResponseParams]) -> str: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsDefaultParams]) -> FotmobFifaRankingsResponse: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsTextResponseParams]) -> str: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsDefaultParams]) -> FotmobLatestNewsResponse: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueStreamParams]) -> BinaryIO: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueTextResponseParams]) -> str: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueDefaultParams]) -> FotmobLeagueResponse: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesDefaultParams]) -> FotmobLeaguesResponse: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersTextResponseParams]) -> str: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersDefaultParams]) -> FotmobLineupBuilderPlayersResponse: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamTextResponseParams]) -> str: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamDefaultParams]) -> FotmobLineupBuilderTeamResponse: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchDefaultParams]) -> FotmobMatchResponse: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaStreamParams]) -> BinaryIO: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaTextResponseParams]) -> str: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaDefaultParams]) -> FotmobMatchMediaResponse: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesDefaultParams]) -> FotmobMatchesResponse: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsDefaultParams]) -> FotmobNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleDefaultParams]) -> FotmobNewsArticleResponse: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerDefaultParams]) -> FotmobPlayerResponse: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsTextResponseParams]) -> str: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsDefaultParams]) -> FotmobPlayerMatchStatsResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesDefaultParams]) -> FotmobPlayerMatchesResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsDefaultParams]) -> FotmobPlayerStatsResponse: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchDefaultParams]) -> FotmobSearchResponse: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsTextResponseParams]) -> str: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsDefaultParams]) -> FotmobSeasonsResponse: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsTextResponseParams]) -> str: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsDefaultParams]) -> FotmobStatsResponse: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesDefaultParams]) -> FotmobStatsCategoriesResponse: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableStreamParams]) -> BinaryIO: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableTextResponseParams]) -> str: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableDefaultParams]) -> FotmobTableResponse: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamDefaultParams]) -> FotmobTeamResponse: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesTextResponseParams]) -> str: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesDefaultParams]) -> FotmobTeamFixturesResponse: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsTextResponseParams]) -> str: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsDefaultParams]) -> FotmobTeamNewsResponse: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersTextResponseParams]) -> str: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersDefaultParams]) -> FotmobTransfersResponse: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsTextResponseParams]) -> str: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsDefaultParams]) -> FotmobTrendingNewsResponse: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesTextResponseParams]) -> str: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesDefaultParams]) -> FotmobTrendingSearchesResponse: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideTextResponseParams]) -> str: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideDefaultParams]) -> FotmobTvGuideResponse: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsTextResponseParams]) -> str: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsDefaultParams]) -> FotmobTvGuideChannelsResponse: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesTextResponseParams]) -> str: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesDefaultParams]) -> FotmobTvGuideCountriesResponse: ...

class _AsyncFotmobGroup:
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesTextResponseParams]) -> str: ...
    @overload
    async def audio_matches(self, **params: Unpack[FotmobAudioMatchesDefaultParams]) -> FotmobAudioMatchesResponse: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsTextResponseParams]) -> str: ...
    @overload
    async def fifa_ranking_periods(self, **params: Unpack[FotmobFifaRankingPeriodsDefaultParams]) -> FotmobFifaRankingPeriodsResponse: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsTextResponseParams]) -> str: ...
    @overload
    async def fifa_rankings(self, **params: Unpack[FotmobFifaRankingsDefaultParams]) -> FotmobFifaRankingsResponse: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsTextResponseParams]) -> str: ...
    @overload
    async def latest_news(self, **params: Unpack[FotmobLatestNewsDefaultParams]) -> FotmobLatestNewsResponse: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueStreamParams]) -> BinaryIO: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueTextResponseParams]) -> str: ...
    @overload
    async def league(self, **params: Unpack[FotmobLeagueDefaultParams]) -> FotmobLeagueResponse: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[FotmobLeaguesDefaultParams]) -> FotmobLeaguesResponse: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersTextResponseParams]) -> str: ...
    @overload
    async def lineup_builder_players(self, **params: Unpack[FotmobLineupBuilderPlayersDefaultParams]) -> FotmobLineupBuilderPlayersResponse: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamTextResponseParams]) -> str: ...
    @overload
    async def lineup_builder_team(self, **params: Unpack[FotmobLineupBuilderTeamDefaultParams]) -> FotmobLineupBuilderTeamResponse: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[FotmobMatchDefaultParams]) -> FotmobMatchResponse: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaStreamParams]) -> BinaryIO: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaTextResponseParams]) -> str: ...
    @overload
    async def match_media(self, **params: Unpack[FotmobMatchMediaDefaultParams]) -> FotmobMatchMediaResponse: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[FotmobMatchesDefaultParams]) -> FotmobMatchesResponse: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FotmobNewsDefaultParams]) -> FotmobNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FotmobNewsArticleDefaultParams]) -> FotmobNewsArticleResponse: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FotmobPlayerDefaultParams]) -> FotmobPlayerResponse: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsTextResponseParams]) -> str: ...
    @overload
    async def player_match_stats(self, **params: Unpack[FotmobPlayerMatchStatsDefaultParams]) -> FotmobPlayerMatchStatsResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[FotmobPlayerMatchesDefaultParams]) -> FotmobPlayerMatchesResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[FotmobPlayerStatsDefaultParams]) -> FotmobPlayerStatsResponse: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[FotmobSearchDefaultParams]) -> FotmobSearchResponse: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsTextResponseParams]) -> str: ...
    @overload
    async def seasons(self, **params: Unpack[FotmobSeasonsDefaultParams]) -> FotmobSeasonsResponse: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsTextResponseParams]) -> str: ...
    @overload
    async def stats(self, **params: Unpack[FotmobStatsDefaultParams]) -> FotmobStatsResponse: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def stats_categories(self, **params: Unpack[FotmobStatsCategoriesDefaultParams]) -> FotmobStatsCategoriesResponse: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableStreamParams]) -> BinaryIO: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableTextResponseParams]) -> str: ...
    @overload
    async def table(self, **params: Unpack[FotmobTableDefaultParams]) -> FotmobTableResponse: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FotmobTeamDefaultParams]) -> FotmobTeamResponse: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesTextResponseParams]) -> str: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FotmobTeamFixturesDefaultParams]) -> FotmobTeamFixturesResponse: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsTextResponseParams]) -> str: ...
    @overload
    async def team_news(self, **params: Unpack[FotmobTeamNewsDefaultParams]) -> FotmobTeamNewsResponse: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersTextResponseParams]) -> str: ...
    @overload
    async def transfers(self, **params: Unpack[FotmobTransfersDefaultParams]) -> FotmobTransfersResponse: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsTextResponseParams]) -> str: ...
    @overload
    async def trending_news(self, **params: Unpack[FotmobTrendingNewsDefaultParams]) -> FotmobTrendingNewsResponse: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesTextResponseParams]) -> str: ...
    @overload
    async def trending_searches(self, **params: Unpack[FotmobTrendingSearchesDefaultParams]) -> FotmobTrendingSearchesResponse: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideTextResponseParams]) -> str: ...
    @overload
    async def tv_guide(self, **params: Unpack[FotmobTvGuideDefaultParams]) -> FotmobTvGuideResponse: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsTextResponseParams]) -> str: ...
    @overload
    async def tv_guide_channels(self, **params: Unpack[FotmobTvGuideChannelsDefaultParams]) -> FotmobTvGuideChannelsResponse: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesStreamParams]) -> BinaryIO: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesTextResponseParams]) -> str: ...
    @overload
    async def tv_guide_countries(self, **params: Unpack[FotmobTvGuideCountriesDefaultParams]) -> FotmobTvGuideCountriesResponse: ...

FotmobAudioMatchesDefaultParams = TypedDict('FotmobAudioMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FotmobAudioMatchesTextResponseParams = TypedDict('FotmobAudioMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FotmobAudioMatchesStreamParams = TypedDict('FotmobAudioMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FotmobFifaRankingPeriodsDefaultParams = TypedDict('FotmobFifaRankingPeriodsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'gender': Required[Literal['men', 'women']],
}, total=False)

FotmobFifaRankingPeriodsTextResponseParams = TypedDict('FotmobFifaRankingPeriodsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'gender': Required[Literal['men', 'women']],
}, total=False)

FotmobFifaRankingPeriodsStreamParams = TypedDict('FotmobFifaRankingPeriodsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'gender': Required[Literal['men', 'women']],
}, total=False)

FotmobFifaRankingsDefaultParams = TypedDict('FotmobFifaRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'gender': Required[Literal['men', 'women']],
    'period_id': Required[str],
}, total=False)

FotmobFifaRankingsTextResponseParams = TypedDict('FotmobFifaRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'gender': Required[Literal['men', 'women']],
    'period_id': Required[str],
}, total=False)

FotmobFifaRankingsStreamParams = TypedDict('FotmobFifaRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'gender': Required[Literal['men', 'women']],
    'period_id': Required[str],
}, total=False)

FotmobLatestNewsDefaultParams = TypedDict('FotmobLatestNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'start_index': NotRequired[int],
}, total=False)

FotmobLatestNewsTextResponseParams = TypedDict('FotmobLatestNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'start_index': NotRequired[int],
}, total=False)

FotmobLatestNewsStreamParams = TypedDict('FotmobLatestNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'start_index': NotRequired[int],
}, total=False)

FotmobLeagueDefaultParams = TypedDict('FotmobLeagueDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[int],
    'season': NotRequired[str],
    'shotmap': NotRequired[bool],
}, total=False)

FotmobLeagueTextResponseParams = TypedDict('FotmobLeagueTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[int],
    'season': NotRequired[str],
    'shotmap': NotRequired[bool],
}, total=False)

FotmobLeagueStreamParams = TypedDict('FotmobLeagueStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[int],
    'season': NotRequired[str],
    'shotmap': NotRequired[bool],
}, total=False)

FotmobLeaguesDefaultParams = TypedDict('FotmobLeaguesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FotmobLeaguesTextResponseParams = TypedDict('FotmobLeaguesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FotmobLeaguesStreamParams = TypedDict('FotmobLeaguesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FotmobLineupBuilderPlayersDefaultParams = TypedDict('FotmobLineupBuilderPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_ids': Required[str],
}, total=False)

FotmobLineupBuilderPlayersTextResponseParams = TypedDict('FotmobLineupBuilderPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_ids': Required[str],
}, total=False)

FotmobLineupBuilderPlayersStreamParams = TypedDict('FotmobLineupBuilderPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_ids': Required[str],
}, total=False)

FotmobLineupBuilderTeamDefaultParams = TypedDict('FotmobLineupBuilderTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[str],
}, total=False)

FotmobLineupBuilderTeamTextResponseParams = TypedDict('FotmobLineupBuilderTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[str],
}, total=False)

FotmobLineupBuilderTeamStreamParams = TypedDict('FotmobLineupBuilderTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[str],
}, total=False)

FotmobMatchDefaultParams = TypedDict('FotmobMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FotmobMatchTextResponseParams = TypedDict('FotmobMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FotmobMatchStreamParams = TypedDict('FotmobMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FotmobMatchMediaDefaultParams = TypedDict('FotmobMatchMediaDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FotmobMatchMediaTextResponseParams = TypedDict('FotmobMatchMediaTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FotmobMatchMediaStreamParams = TypedDict('FotmobMatchMediaStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FotmobMatchesDefaultParams = TypedDict('FotmobMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'date': Required[str],
    'timezone': NotRequired[str],
}, total=False)

FotmobMatchesTextResponseParams = TypedDict('FotmobMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'date': Required[str],
    'timezone': NotRequired[str],
}, total=False)

FotmobMatchesStreamParams = TypedDict('FotmobMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'date': Required[str],
    'timezone': NotRequired[str],
}, total=False)

FotmobNewsDefaultParams = TypedDict('FotmobNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[str],
    'start_index': NotRequired[int],
}, total=False)

FotmobNewsTextResponseParams = TypedDict('FotmobNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[str],
    'start_index': NotRequired[int],
}, total=False)

FotmobNewsStreamParams = TypedDict('FotmobNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[str],
    'start_index': NotRequired[int],
}, total=False)

FotmobNewsArticleDefaultParams = TypedDict('FotmobNewsArticleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FotmobNewsArticleTextResponseParams = TypedDict('FotmobNewsArticleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FotmobNewsArticleStreamParams = TypedDict('FotmobNewsArticleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FotmobPlayerDefaultParams = TypedDict('FotmobPlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'include_market_values': NotRequired[bool],
}, total=False)

FotmobPlayerTextResponseParams = TypedDict('FotmobPlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'include_market_values': NotRequired[bool],
}, total=False)

FotmobPlayerStreamParams = TypedDict('FotmobPlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'include_market_values': NotRequired[bool],
}, total=False)

FotmobPlayerMatchStatsDefaultParams = TypedDict('FotmobPlayerMatchStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[str],
    'match_id': Required[str],
}, total=False)

FotmobPlayerMatchStatsTextResponseParams = TypedDict('FotmobPlayerMatchStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[str],
    'match_id': Required[str],
}, total=False)

FotmobPlayerMatchStatsStreamParams = TypedDict('FotmobPlayerMatchStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[str],
    'match_id': Required[str],
}, total=False)

FotmobPlayerMatchesDefaultParams = TypedDict('FotmobPlayerMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[str],
    'league_id': NotRequired[str],
    'team_id': NotRequired[str],
    'before': NotRequired[str],
}, total=False)

FotmobPlayerMatchesTextResponseParams = TypedDict('FotmobPlayerMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[str],
    'league_id': NotRequired[str],
    'team_id': NotRequired[str],
    'before': NotRequired[str],
}, total=False)

FotmobPlayerMatchesStreamParams = TypedDict('FotmobPlayerMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[str],
    'league_id': NotRequired[str],
    'team_id': NotRequired[str],
    'before': NotRequired[str],
}, total=False)

FotmobPlayerStatsDefaultParams = TypedDict('FotmobPlayerStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'player_id': Required[str],
    'season_id': Required[str],
}, total=False)

FotmobPlayerStatsTextResponseParams = TypedDict('FotmobPlayerStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'player_id': Required[str],
    'season_id': Required[str],
}, total=False)

FotmobPlayerStatsStreamParams = TypedDict('FotmobPlayerStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'player_id': Required[str],
    'season_id': Required[str],
}, total=False)

FotmobSearchDefaultParams = TypedDict('FotmobSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'term': Required[str],
}, total=False)

FotmobSearchTextResponseParams = TypedDict('FotmobSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'term': Required[str],
}, total=False)

FotmobSearchStreamParams = TypedDict('FotmobSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'term': Required[str],
}, total=False)

FotmobSeasonsDefaultParams = TypedDict('FotmobSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[int],
}, total=False)

FotmobSeasonsTextResponseParams = TypedDict('FotmobSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[int],
}, total=False)

FotmobSeasonsStreamParams = TypedDict('FotmobSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[int],
}, total=False)

FotmobStatsDefaultParams = TypedDict('FotmobStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
    'stat': Required[str],
    'team_id': NotRequired[str],
    'position': NotRequired[Literal['all', 'striker', 'winger', 'attackingMidfielder', 'midfielder', 'fullback', 'centerBack']],
}, total=False)

FotmobStatsTextResponseParams = TypedDict('FotmobStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
    'stat': Required[str],
    'team_id': NotRequired[str],
    'position': NotRequired[Literal['all', 'striker', 'winger', 'attackingMidfielder', 'midfielder', 'fullback', 'centerBack']],
}, total=False)

FotmobStatsStreamParams = TypedDict('FotmobStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
    'stat': Required[str],
    'team_id': NotRequired[str],
    'position': NotRequired[Literal['all', 'striker', 'winger', 'attackingMidfielder', 'midfielder', 'fullback', 'centerBack']],
}, total=False)

FotmobStatsCategoriesDefaultParams = TypedDict('FotmobStatsCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
}, total=False)

FotmobStatsCategoriesTextResponseParams = TypedDict('FotmobStatsCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
}, total=False)

FotmobStatsCategoriesStreamParams = TypedDict('FotmobStatsCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[str],
    'season_id': NotRequired[str],
    'type': Required[Literal['players', 'teams']],
}, total=False)

FotmobTableDefaultParams = TypedDict('FotmobTableDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[str],
}, total=False)

FotmobTableTextResponseParams = TypedDict('FotmobTableTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[str],
}, total=False)

FotmobTableStreamParams = TypedDict('FotmobTableStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[str],
}, total=False)

FotmobTeamDefaultParams = TypedDict('FotmobTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FotmobTeamTextResponseParams = TypedDict('FotmobTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FotmobTeamStreamParams = TypedDict('FotmobTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FotmobTeamFixturesDefaultParams = TypedDict('FotmobTeamFixturesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[str],
    'cursor': Required[str],
}, total=False)

FotmobTeamFixturesTextResponseParams = TypedDict('FotmobTeamFixturesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[str],
    'cursor': Required[str],
}, total=False)

FotmobTeamFixturesStreamParams = TypedDict('FotmobTeamFixturesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[str],
    'cursor': Required[str],
}, total=False)

FotmobTeamNewsDefaultParams = TypedDict('FotmobTeamNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
    'start_index': NotRequired[int],
}, total=False)

FotmobTeamNewsTextResponseParams = TypedDict('FotmobTeamNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
    'start_index': NotRequired[int],
}, total=False)

FotmobTeamNewsStreamParams = TypedDict('FotmobTeamNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
    'start_index': NotRequired[int],
}, total=False)

FotmobTransfersDefaultParams = TypedDict('FotmobTransfersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
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

FotmobTransfersTextResponseParams = TypedDict('FotmobTransfersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
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
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
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

FotmobTrendingNewsDefaultParams = TypedDict('FotmobTrendingNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FotmobTrendingNewsTextResponseParams = TypedDict('FotmobTrendingNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FotmobTrendingNewsStreamParams = TypedDict('FotmobTrendingNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FotmobTrendingSearchesDefaultParams = TypedDict('FotmobTrendingSearchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FotmobTrendingSearchesTextResponseParams = TypedDict('FotmobTrendingSearchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FotmobTrendingSearchesStreamParams = TypedDict('FotmobTrendingSearchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FotmobTvGuideDefaultParams = TypedDict('FotmobTvGuideDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
    'timezone': NotRequired[str],
}, total=False)

FotmobTvGuideTextResponseParams = TypedDict('FotmobTvGuideTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
    'timezone': NotRequired[str],
}, total=False)

FotmobTvGuideStreamParams = TypedDict('FotmobTvGuideStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
    'timezone': NotRequired[str],
}, total=False)

FotmobTvGuideChannelsDefaultParams = TypedDict('FotmobTvGuideChannelsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
}, total=False)

FotmobTvGuideChannelsTextResponseParams = TypedDict('FotmobTvGuideChannelsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
}, total=False)

FotmobTvGuideChannelsStreamParams = TypedDict('FotmobTvGuideChannelsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[Literal['us', 'se', 'gb', 'de', 'no', 'es', 'mx', 'ar', 'bo', 'cl', 'co', 'cr', 'ec', 'gt', 'hn', 'ni', 'pa', 'py', 'pe', 'uy', 've', 'da', 'ca', 'au', 'at', 'be', 'bg', 'hr', 'cy', 'cz', 'ee', 'fi', 'fr', 'gr', 'hu', 'is', 'ie', 'il', 'it', 'nl', 'pl', 'pt', 'ro', 'ru', 'ch', 'tr', 'za', 'br', 'in', 'me', 'id', 'th', 'mm', 'al', 'az', 'bl', 'ba', 'ks', 'la', 'li', 'mk', 'rs', 'sk', 'ua', 'essv', 'nz', 'bd', 'cn', 'gh', 'hk', 'jp', 'kr', 'ma', 'mt', 'my', 'ng', 'ph', 'pk', 'sg', 'si', 'tz']],
}, total=False)

FotmobTvGuideCountriesDefaultParams = TypedDict('FotmobTvGuideCountriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FotmobTvGuideCountriesTextResponseParams = TypedDict('FotmobTvGuideCountriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FotmobTvGuideCountriesStreamParams = TypedDict('FotmobTvGuideCountriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)
