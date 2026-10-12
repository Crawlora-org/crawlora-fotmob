# Crawlora FotMob API client for PHP (`crawlora/fotmob`)

This PHP package calls Crawlora's hosted FotMob API at `https://api.crawlora.net/api/v1`. It exposes 31 endpoints covering leagues, matches, fixtures, teams, players, search, standings, news, and rankings. It does not call or scrape FotMob directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/fotmob
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Fotmob\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("fotmob-search", ['term' => 'Premier League']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 31 API operations.

## Supported FotMob API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-fotmob/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-fotmob). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-fotmob/blob/main/docs/usage.md).
