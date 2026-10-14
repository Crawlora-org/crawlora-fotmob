# Crawlora FotMob API client for Java

The official Java client for Crawlora's hosted FotMob API. It exposes 31 endpoints covering leagues, matches, fixtures, teams, players, search, standings, news, and rankings. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-fotmob</artifactId>
  <version>0.1.10</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-java-console) to get an API key.

```java
import net.crawlora.fotmob.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.fifaRankingPeriods(Map.ofEntries(Map.entry("gender", "men")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported FotMob API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-fotmob/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-fotmob)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-java-api-docs)
