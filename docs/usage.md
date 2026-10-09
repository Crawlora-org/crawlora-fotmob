# FotMob client usage

The `@crawlora-org/fotmob` and `crawlora-fotmob` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape FotMob locally; Crawlora is independent from and not endorsed by FotMob or its owners.

The package tracks the public API contract revision `sha256:d40e5ee2b400b1b40b5ca6998063cde26b6bb3e7f84da679b5047d26380f3fa1` bundled with release `0.1.6`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 31 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `fotmob` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `audioMatches` / `audio_matches` | `GET /fotmob/audio-matches` | — | FotMob matches with audio commentary |
| `fifaRankingPeriods` / `fifa_ranking_periods` | `GET /fotmob/fifa-ranking-periods` | `gender` (query, required; values: `men`, `women`) | FotMob FIFA ranking period directory |
| `fifaRankings` / `fifa_rankings` | `GET /fotmob/fifa-rankings` | `gender` (query, required; values: `men`, `women`), `period_id` (query, required) | FotMob FIFA national-team rankings |
| `latestNews` / `latest_news` | `GET /fotmob/latest-news` | `start_index` (query, optional) | FotMob latest football news |
| `league` / `league` | `GET /fotmob/league` | `league_id` (query, required), `season` (query, optional), `shotmap` (query, optional) | FotMob league details and sections |
| `leagues` / `leagues` | `GET /fotmob/leagues` | — | FotMob competition directory |
| `lineupBuilderPlayers` / `lineup_builder_players` | `GET /fotmob/lineup-builder-players` | `player_ids` (query, required) | FotMob lineup builder player metadata |
| `lineupBuilderTeam` / `lineup_builder_team` | `GET /fotmob/lineup-builder-team` | `team_id` (query, required) | FotMob lineup builder team data |
| `match` / `match` | `GET /fotmob/match` | `id` (query, required) | FotMob match details |
| `matches` / `matches` | `GET /fotmob/matches` | `date` (query, required), `timezone` (query, optional) | FotMob matches for a date |
| `matchMedia` / `match_media` | `GET /fotmob/match-media` | `id` (query, required) | FotMob match videos and media metadata |
| `news` / `news` | `GET /fotmob/news` | `league_id` (query, required), `start_index` (query, optional) | FotMob league news |
| `newsArticle` / `news_article` | `GET /fotmob/news-article` | `id` (query, required) | FotMob full top-news article |
| `player` / `player` | `GET /fotmob/player` | `id` (query, required), `include_market_values` (query, optional) | FotMob player profile |
| `playerMatches` / `player_matches` | `GET /fotmob/player-matches` | `player_id` (query, required), `league_id` (query, optional), `team_id` (query, optional), `before` (query, optional) | FotMob player match history |
| `playerMatchStats` / `player_match_stats` | `GET /fotmob/player-match-stats` | `player_id` (query, required), `match_id` (query, required) | FotMob player match stats |
| `playerStats` / `player_stats` | `GET /fotmob/player-stats` | `player_id` (query, required), `season_id` (query, required) | FotMob player season statistics |
| `search` / `search` | `GET /fotmob/search` | `term` (query, required) | Search FotMob entities |
| `seasons` / `seasons` | `GET /fotmob/seasons` | `league_id` (query, required) | FotMob league season discovery |
| `stats` / `stats` | `GET /fotmob/stats` | `league_id` (query, required), `season_id` (query, optional), `type` (query, required; values: `players`, `teams`), `stat` (query, required), `team_id` (query, optional), `position` (query, optional; values: `all`, `striker`, `winger`, `attackingMidfielder`, `midfielder`, `fullback`, `centerBack`) | FotMob league player or team statistics |
| `statsCategories` / `stats_categories` | `GET /fotmob/stats-categories` | `league_id` (query, required), `season_id` (query, optional), `type` (query, required; values: `players`, `teams`) | FotMob league stat categories and seasons |
| `table` / `table` | `GET /fotmob/table` | `league_id` (query, required) | FotMob league table |
| `team` / `team` | `GET /fotmob/team` | `id` (query, required) | FotMob team details |
| `teamFixtures` / `team_fixtures` | `GET /fotmob/team-fixtures` | `team_id` (query, required), `cursor` (query, required) | FotMob paginated team fixtures |
| `teamNews` / `team_news` | `GET /fotmob/team-news` | `team_id` (query, required), `start_index` (query, optional) | FotMob team news |
| `transfers` / `transfers` | `GET /fotmob/transfers` | `mode` (query, optional; values: `all`, `rumours`, `popular`), `page` (query, optional), `last` (query, optional; values: `6months`, `1year`, `2years`, `3years`), `direction` (query, optional; values: `all`, `in`, `out`), `min_fee` (query, optional), `max_fee` (query, optional), `league_ids` (query, optional), `team_ids` (query, optional), `order_by` (query, optional; values: `lastModified`, `fee`, `date`, `name`, `fromClubName`, `toClubName`), `exclude_extensions` (query, optional), `likely_only` (query, optional) | FotMob transfer center |
| `trendingNews` / `trending_news` | `GET /fotmob/trending-news` | — | FotMob trending football news |
| `trendingSearches` / `trending_searches` | `GET /fotmob/trending-searches` | — | FotMob trending search suggestions |
| `tvGuide` / `tv_guide` | `GET /fotmob/tv-guide` | `country` (query, required; values: `us`, `se`, `gb`, `de`, `no`, `es`, `mx`, `ar`, `bo`, `cl`, `co`, `cr`, `ec`, `gt`, `hn`, `ni`, `pa`, `py`, `pe`, `uy`, `ve`, `da`, `ca`, `au`, `at`, `be`, `bg`, `hr`, `cy`, `cz`, `ee`, `fi`, `fr`, `gr`, `hu`, `is`, `ie`, `il`, `it`, `nl`, `pl`, `pt`, `ro`, `ru`, `ch`, `tr`, `za`, `br`, `in`, `me`, `id`, `th`, `mm`, `al`, `az`, `bl`, `ba`, `ks`, `la`, `li`, `mk`, `rs`, `sk`, `ua`, `essv`, `nz`, `bd`, `cn`, `gh`, `hk`, `jp`, `kr`, `ma`, `mt`, `my`, `ng`, `ph`, `pk`, `sg`, `si`, `tz`), `timezone` (query, optional) | FotMob football TV guide |
| `tvGuideChannels` / `tv_guide_channels` | `GET /fotmob/tv-guide-channels` | `country` (query, required; values: `us`, `se`, `gb`, `de`, `no`, `es`, `mx`, `ar`, `bo`, `cl`, `co`, `cr`, `ec`, `gt`, `hn`, `ni`, `pa`, `py`, `pe`, `uy`, `ve`, `da`, `ca`, `au`, `at`, `be`, `bg`, `hr`, `cy`, `cz`, `ee`, `fi`, `fr`, `gr`, `hu`, `is`, `ie`, `il`, `it`, `nl`, `pl`, `pt`, `ro`, `ru`, `ch`, `tr`, `za`, `br`, `in`, `me`, `id`, `th`, `mm`, `al`, `az`, `bl`, `ba`, `ks`, `la`, `li`, `mk`, `rs`, `sk`, `ua`, `essv`, `nz`, `bd`, `cn`, `gh`, `hk`, `jp`, `kr`, `ma`, `mt`, `my`, `ng`, `ph`, `pk`, `sg`, `si`, `tz`) | FotMob TV guide channels |
| `tvGuideCountries` / `tv_guide_countries` | `GET /fotmob/tv-guide-countries` | — | FotMob TV guide country directory |

## Client forms

- JavaScript: import `FotMobClient` (also exported as `Client`) from `@crawlora-org/fotmob`; use `new FotMobClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `FotMobClient` (also exported as `Client`) from `crawlora_fotmob`; use `with FotMobClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncFotMobClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
