# FotMob clients for Crawlora

Official Crawlora client packages for the hosted FotMob API. Access 31 API endpoints covering leagues, matches, fixtures, teams, players, search, standings, news, and rankings from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape FotMob locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by FotMob or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/fotmob`](javascript/README.md)
- Python: [`crawlora-fotmob`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-fotmob`](go.mod)
- Ruby: [`crawlora-fotmob`](ruby/README.md)
- Java: [`net.crawlora:crawlora-fotmob:0.1.10`](java/README.md)
- PHP: [`crawlora/fotmob`](php/README.md)
- Rust: [`crawlora-fotmob`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 31 selected public FotMob API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
