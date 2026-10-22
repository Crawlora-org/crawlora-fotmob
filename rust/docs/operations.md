# Crawlora FotMob Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `31`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fotmob | `fotmob.audio_matches` | `fotmob-audio-matches` | `GET /fotmob/audio-matches` | none | `ApiKeyAuth` | `FotmobAudioMatchesResponse` |  |
| fotmob | `fotmob.fifa_ranking_periods` | `fotmob-fifa-ranking-periods` | `GET /fotmob/fifa-ranking-periods` | `gender` (query String enum{men, women} required) | `ApiKeyAuth` | `FotmobFifaRankingPeriodsResponse` |  |
| fotmob | `fotmob.fifa_rankings` | `fotmob-fifa-rankings` | `GET /fotmob/fifa-rankings` | `gender` (query String enum{men, women} required)<br>`period_id` (query String required) | `ApiKeyAuth` | `FotmobFifaRankingsResponse` |  |
| fotmob | `fotmob.latest_news` | `fotmob-latest-news` | `GET /fotmob/latest-news` | `start_index` (query i64) | `ApiKeyAuth` | `FotmobLatestNewsResponse` |  |
| fotmob | `fotmob.league` | `fotmob-league` | `GET /fotmob/league` | `league_id` (query i64 required)<br>`season` (query String)<br>`shotmap` (query bool) | `ApiKeyAuth` | `FotmobLeagueResponse` |  |
| fotmob | `fotmob.leagues` | `fotmob-leagues` | `GET /fotmob/leagues` | none | `ApiKeyAuth` | `FotmobLeaguesResponse` |  |
| fotmob | `fotmob.lineup_builder_players` | `fotmob-lineup-builder-players` | `GET /fotmob/lineup-builder-players` | `player_ids` (query String required) | `ApiKeyAuth` | `FotmobLineupBuilderPlayersResponse` |  |
| fotmob | `fotmob.lineup_builder_team` | `fotmob-lineup-builder-team` | `GET /fotmob/lineup-builder-team` | `team_id` (query String required) | `ApiKeyAuth` | `FotmobLineupBuilderTeamResponse` |  |
| fotmob | `fotmob.match_` | `fotmob-match` | `GET /fotmob/match` | `id` (query String required) | `ApiKeyAuth` | `FotmobMatchResponse` |  |
| fotmob | `fotmob.match_media` | `fotmob-match-media` | `GET /fotmob/match-media` | `id` (query String required) | `ApiKeyAuth` | `FotmobMatchMediaResponse` |  |
| fotmob | `fotmob.matches` | `fotmob-matches` | `GET /fotmob/matches` | `date` (query String required)<br>`timezone` (query String) | `ApiKeyAuth` | `FotmobMatchesResponse` |  |
| fotmob | `fotmob.news` | `fotmob-news` | `GET /fotmob/news` | `league_id` (query String required)<br>`start_index` (query i64) | `ApiKeyAuth` | `FotmobNewsResponse` |  |
| fotmob | `fotmob.news_article` | `fotmob-news-article` | `GET /fotmob/news-article` | `id` (query String required) | `ApiKeyAuth` | `FotmobNewsArticleResponse` |  |
| fotmob | `fotmob.player` | `fotmob-player` | `GET /fotmob/player` | `id` (query String required)<br>`include_market_values` (query bool) | `ApiKeyAuth` | `FotmobPlayerResponse` |  |
| fotmob | `fotmob.player_match_stats` | `fotmob-player-match-stats` | `GET /fotmob/player-match-stats` | `player_id` (query String required)<br>`match_id` (query String required) | `ApiKeyAuth` | `FotmobPlayerMatchStatsResponse` |  |
| fotmob | `fotmob.player_matches` | `fotmob-player-matches` | `GET /fotmob/player-matches` | `player_id` (query String required)<br>`league_id` (query String)<br>`team_id` (query String)<br>`before` (query String) | `ApiKeyAuth` | `FotmobPlayerMatchesResponse` |  |
| fotmob | `fotmob.player_stats` | `fotmob-player-stats` | `GET /fotmob/player-stats` | `player_id` (query String required)<br>`season_id` (query String required) | `ApiKeyAuth` | `FotmobPlayerStatsResponse` |  |
| fotmob | `fotmob.search` | `fotmob-search` | `GET /fotmob/search` | `term` (query String required) | `ApiKeyAuth` | `FotmobSearchResponse` |  |
| fotmob | `fotmob.seasons` | `fotmob-seasons` | `GET /fotmob/seasons` | `league_id` (query i64 required) | `ApiKeyAuth` | `FotmobSeasonsResponse` |  |
| fotmob | `fotmob.stats` | `fotmob-stats` | `GET /fotmob/stats` | `league_id` (query String required)<br>`season_id` (query String)<br>`type` (query String enum{players, teams} required)<br>`stat` (query String required)<br>`team_id` (query String)<br>`position` (query String enum{all, striker, winger, attackingMidfielder, midfielder, fullback, centerBack}) | `ApiKeyAuth` | `FotmobStatsResponse` |  |
| fotmob | `fotmob.stats_categories` | `fotmob-stats-categories` | `GET /fotmob/stats-categories` | `league_id` (query String required)<br>`season_id` (query String)<br>`type` (query String enum{players, teams} required) | `ApiKeyAuth` | `FotmobStatsCategoriesResponse` |  |
| fotmob | `fotmob.table` | `fotmob-table` | `GET /fotmob/table` | `league_id` (query String required) | `ApiKeyAuth` | `FotmobTableResponse` |  |
| fotmob | `fotmob.team` | `fotmob-team` | `GET /fotmob/team` | `id` (query String required) | `ApiKeyAuth` | `FotmobTeamResponse` |  |
| fotmob | `fotmob.team_fixtures` | `fotmob-team-fixtures` | `GET /fotmob/team-fixtures` | `team_id` (query String required)<br>`cursor` (query String required) | `ApiKeyAuth` | `FotmobTeamFixturesResponse` |  |
| fotmob | `fotmob.team_news` | `fotmob-team-news` | `GET /fotmob/team-news` | `team_id` (query i64 required)<br>`start_index` (query i64) | `ApiKeyAuth` | `FotmobTeamNewsResponse` |  |
| fotmob | `fotmob.transfers` | `fotmob-transfers` | `GET /fotmob/transfers` | `mode` (query String enum{all, rumours, popular})<br>`page` (query i64)<br>`last` (query String enum{6months, 1year, 2years, 3years})<br>`direction` (query String enum{all, in, out})<br>`min_fee` (query i64)<br>`max_fee` (query i64)<br>`league_ids` (query String)<br>`team_ids` (query String)<br>`order_by` (query String enum{lastModified, fee, date, name, fromClubName, toClubName})<br>`exclude_extensions` (query bool)<br>`likely_only` (query bool) | `ApiKeyAuth` | `FotmobTransfersResponse` |  |
| fotmob | `fotmob.trending_news` | `fotmob-trending-news` | `GET /fotmob/trending-news` | none | `ApiKeyAuth` | `FotmobTrendingNewsResponse` |  |
| fotmob | `fotmob.trending_searches` | `fotmob-trending-searches` | `GET /fotmob/trending-searches` | none | `ApiKeyAuth` | `FotmobTrendingSearchesResponse` |  |
| fotmob | `fotmob.tv_guide` | `fotmob-tv-guide` | `GET /fotmob/tv-guide` | `country` (query String enum{us, se, gb, de, no, es, mx, ar, bo, cl, co, cr, ec, gt, hn, ni, pa, py, pe, uy, ve, da, ca, au, at, be, bg, hr, cy, cz, ee, fi, fr, gr, hu, is, ie, il, it, nl, pl, pt, ro, ru, ch, tr, za, br, in, me, id, th, mm, al, az, bl, ba, ks, la, li, mk, rs, sk, ua, essv, nz, bd, cn, gh, hk, jp, kr, ma, mt, my, ng, ph, pk, sg, si, tz} required)<br>`timezone` (query String) | `ApiKeyAuth` | `FotmobTvGuideResponse` |  |
| fotmob | `fotmob.tv_guide_channels` | `fotmob-tv-guide-channels` | `GET /fotmob/tv-guide-channels` | `country` (query String enum{us, se, gb, de, no, es, mx, ar, bo, cl, co, cr, ec, gt, hn, ni, pa, py, pe, uy, ve, da, ca, au, at, be, bg, hr, cy, cz, ee, fi, fr, gr, hu, is, ie, il, it, nl, pl, pt, ro, ru, ch, tr, za, br, in, me, id, th, mm, al, az, bl, ba, ks, la, li, mk, rs, sk, ua, essv, nz, bd, cn, gh, hk, jp, kr, ma, mt, my, ng, ph, pk, sg, si, tz} required) | `ApiKeyAuth` | `FotmobTvGuideChannelsResponse` |  |
| fotmob | `fotmob.tv_guide_countries` | `fotmob-tv-guide-countries` | `GET /fotmob/tv-guide-countries` | none | `ApiKeyAuth` | `FotmobTvGuideCountriesResponse` |  |
