# FotMob API endpoint reference and client usage

This reference lists all 31 public FotMob API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/fotmob`, `crawlora-fotmob`, and `crawlora-fotmob` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape FotMob locally; Crawlora is independent from and not endorsed by FotMob or its owners.

The package tracks the public API contract revision `sha256:8769e4cf3f8b6494435a97ef434fd699014967491242a3a3bbe235c93a9c67a0` bundled with release `0.1.10`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `fotmob`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `audioMatches` | `audio_matches` | `fotmob.audio_matches` | `GET /fotmob/audio-matches` | — | FotMob matches with audio commentary |
| `fifaRankingPeriods` | `fifa_ranking_periods` | `fotmob.fifa_ranking_periods` | `GET /fotmob/fifa-ranking-periods` | `gender` (query, required; values: `men`, `women`) | FotMob FIFA ranking period directory |
| `fifaRankings` | `fifa_rankings` | `fotmob.fifa_rankings` | `GET /fotmob/fifa-rankings` | `gender` (query, required; values: `men`, `women`), `period_id` (query, required) | FotMob FIFA national-team rankings |
| `latestNews` | `latest_news` | `fotmob.latest_news` | `GET /fotmob/latest-news` | `start_index` (query, optional) | FotMob latest football news |
| `league` | `league` | `fotmob.league` | `GET /fotmob/league` | `league_id` (query, required), `season` (query, optional), `shotmap` (query, optional) | FotMob league details and sections |
| `leagues` | `leagues` | `fotmob.leagues` | `GET /fotmob/leagues` | — | FotMob competition directory |
| `lineupBuilderPlayers` | `lineup_builder_players` | `fotmob.lineup_builder_players` | `GET /fotmob/lineup-builder-players` | `player_ids` (query, required) | FotMob lineup builder player metadata |
| `lineupBuilderTeam` | `lineup_builder_team` | `fotmob.lineup_builder_team` | `GET /fotmob/lineup-builder-team` | `team_id` (query, required) | FotMob lineup builder team data |
| `match` | `match` | `fotmob.match_` | `GET /fotmob/match` | `id` (query, required) | FotMob match details |
| `matches` | `matches` | `fotmob.matches` | `GET /fotmob/matches` | `date` (query, required), `timezone` (query, optional) | FotMob matches for a date |
| `matchMedia` | `match_media` | `fotmob.match_media` | `GET /fotmob/match-media` | `id` (query, required) | FotMob match videos and media metadata |
| `news` | `news` | `fotmob.news` | `GET /fotmob/news` | `league_id` (query, required), `start_index` (query, optional) | FotMob league news |
| `newsArticle` | `news_article` | `fotmob.news_article` | `GET /fotmob/news-article` | `id` (query, required) | FotMob full top-news article |
| `player` | `player` | `fotmob.player` | `GET /fotmob/player` | `id` (query, required), `include_market_values` (query, optional) | FotMob player profile |
| `playerMatches` | `player_matches` | `fotmob.player_matches` | `GET /fotmob/player-matches` | `player_id` (query, required), `league_id` (query, optional), `team_id` (query, optional), `before` (query, optional) | FotMob player match history |
| `playerMatchStats` | `player_match_stats` | `fotmob.player_match_stats` | `GET /fotmob/player-match-stats` | `player_id` (query, required), `match_id` (query, required) | FotMob player match stats |
| `playerStats` | `player_stats` | `fotmob.player_stats` | `GET /fotmob/player-stats` | `player_id` (query, required), `season_id` (query, required) | FotMob player season statistics |
| `search` | `search` | `fotmob.search` | `GET /fotmob/search` | `term` (query, required) | Search FotMob entities |
| `seasons` | `seasons` | `fotmob.seasons` | `GET /fotmob/seasons` | `league_id` (query, required) | FotMob league season discovery |
| `stats` | `stats` | `fotmob.stats` | `GET /fotmob/stats` | `league_id` (query, required), `season_id` (query, optional), `type` (query, required; values: `players`, `teams`), `stat` (query, required), `team_id` (query, optional), `position` (query, optional; values: `all`, `striker`, `winger`, `attackingMidfielder`, `midfielder`, `fullback`, `centerBack`) | FotMob league player or team statistics |
| `statsCategories` | `stats_categories` | `fotmob.stats_categories` | `GET /fotmob/stats-categories` | `league_id` (query, required), `season_id` (query, optional), `type` (query, required; values: `players`, `teams`) | FotMob league stat categories and seasons |
| `table` | `table` | `fotmob.table` | `GET /fotmob/table` | `league_id` (query, required) | FotMob league table |
| `team` | `team` | `fotmob.team` | `GET /fotmob/team` | `id` (query, required) | FotMob team details |
| `teamFixtures` | `team_fixtures` | `fotmob.team_fixtures` | `GET /fotmob/team-fixtures` | `team_id` (query, required), `cursor` (query, required) | FotMob paginated team fixtures |
| `teamNews` | `team_news` | `fotmob.team_news` | `GET /fotmob/team-news` | `team_id` (query, required), `start_index` (query, optional) | FotMob team news |
| `transfers` | `transfers` | `fotmob.transfers` | `GET /fotmob/transfers` | `mode` (query, optional; values: `all`, `rumours`, `popular`), `page` (query, optional), `last` (query, optional; values: `6months`, `1year`, `2years`, `3years`), `direction` (query, optional; values: `all`, `in`, `out`), `min_fee` (query, optional), `max_fee` (query, optional), `league_ids` (query, optional), `team_ids` (query, optional), `order_by` (query, optional; values: `lastModified`, `fee`, `date`, `name`, `fromClubName`, `toClubName`), `exclude_extensions` (query, optional), `likely_only` (query, optional) | FotMob transfer center |
| `trendingNews` | `trending_news` | `fotmob.trending_news` | `GET /fotmob/trending-news` | — | FotMob trending football news |
| `trendingSearches` | `trending_searches` | `fotmob.trending_searches` | `GET /fotmob/trending-searches` | — | FotMob trending search suggestions |
| `tvGuide` | `tv_guide` | `fotmob.tv_guide` | `GET /fotmob/tv-guide` | `country` (query, required; values: `us`, `se`, `gb`, `de`, `no`, `es`, `mx`, `ar`, `bo`, `cl`, `co`, `cr`, `ec`, `gt`, `hn`, `ni`, `pa`, `py`, `pe`, `uy`, `ve`, `da`, `ca`, `au`, `at`, `be`, `bg`, `hr`, `cy`, `cz`, `ee`, `fi`, `fr`, `gr`, `hu`, `is`, `ie`, `il`, `it`, `nl`, `pl`, `pt`, `ro`, `ru`, `ch`, `tr`, `za`, `br`, `in`, `me`, `id`, `th`, `mm`, `al`, `az`, `bl`, `ba`, `ks`, `la`, `li`, `mk`, `rs`, `sk`, `ua`, `essv`, `nz`, `bd`, `cn`, `gh`, `hk`, `jp`, `kr`, `ma`, `mt`, `my`, `ng`, `ph`, `pk`, `sg`, `si`, `tz`), `timezone` (query, optional) | FotMob football TV guide |
| `tvGuideChannels` | `tv_guide_channels` | `fotmob.tv_guide_channels` | `GET /fotmob/tv-guide-channels` | `country` (query, required; values: `us`, `se`, `gb`, `de`, `no`, `es`, `mx`, `ar`, `bo`, `cl`, `co`, `cr`, `ec`, `gt`, `hn`, `ni`, `pa`, `py`, `pe`, `uy`, `ve`, `da`, `ca`, `au`, `at`, `be`, `bg`, `hr`, `cy`, `cz`, `ee`, `fi`, `fr`, `gr`, `hu`, `is`, `ie`, `il`, `it`, `nl`, `pl`, `pt`, `ro`, `ru`, `ch`, `tr`, `za`, `br`, `in`, `me`, `id`, `th`, `mm`, `al`, `az`, `bl`, `ba`, `ks`, `la`, `li`, `mk`, `rs`, `sk`, `ua`, `essv`, `nz`, `bd`, `cn`, `gh`, `hk`, `jp`, `kr`, `ma`, `mt`, `my`, `ng`, `ph`, `pk`, `sg`, `si`, `tz`) | FotMob TV guide channels |
| `tvGuideCountries` | `tv_guide_countries` | `fotmob.tv_guide_countries` | `GET /fotmob/tv-guide-countries` | — | FotMob TV guide country directory |

## Client forms

- JavaScript: import `FotMobClient` (also exported as `Client`) from `@crawlora-org/fotmob`; use `new FotMobClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `FotMobClient` (also exported as `Client`) from `crawlora_fotmob`; use `with FotMobClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncFotMobClient`, used with `async with` and `await`.
- Rust: add `crawlora-fotmob` with Cargo; import `Client` and the generated operation parameter struct, then call `client.fotmob.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-fotmob/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
