package net.crawlora.fotmob;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the FotMob endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 31;
    public static final List<String> OPERATION_IDS = List.of(
            "fotmob-audio-matches",
            "fotmob-fifa-ranking-periods",
            "fotmob-fifa-rankings",
            "fotmob-latest-news",
            "fotmob-league",
            "fotmob-leagues",
            "fotmob-lineup-builder-players",
            "fotmob-lineup-builder-team",
            "fotmob-match",
            "fotmob-match-media",
            "fotmob-matches",
            "fotmob-news",
            "fotmob-news-article",
            "fotmob-player",
            "fotmob-player-match-stats",
            "fotmob-player-matches",
            "fotmob-player-stats",
            "fotmob-search",
            "fotmob-seasons",
            "fotmob-stats",
            "fotmob-stats-categories",
            "fotmob-table",
            "fotmob-team",
            "fotmob-team-fixtures",
            "fotmob-team-news",
            "fotmob-transfers",
            "fotmob-trending-news",
            "fotmob-trending-searches",
            "fotmob-tv-guide",
            "fotmob-tv-guide-channels",
            "fotmob-tv-guide-countries"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("fotmob-audio-matches", new Operation("fotmob-audio-matches", "GET", "/fotmob/audio-matches", Map.of(), List.of("application/json")));
        operations.put("fotmob-fifa-ranking-periods", new Operation("fotmob-fifa-ranking-periods", "GET", "/fotmob/fifa-ranking-periods", Map.ofEntries(Map.entry("gender", new Param("gender", "query", true, "string", List.of("men", "women"), "csv"))), List.of("application/json")));
        operations.put("fotmob-fifa-rankings", new Operation("fotmob-fifa-rankings", "GET", "/fotmob/fifa-rankings", Map.ofEntries(Map.entry("gender", new Param("gender", "query", true, "string", List.of("men", "women"), "csv")), Map.entry("period_id", new Param("period_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-latest-news", new Operation("fotmob-latest-news", "GET", "/fotmob/latest-news", Map.ofEntries(Map.entry("start_index", new Param("start_index", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-league", new Operation("fotmob-league", "GET", "/fotmob/league", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "integer", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv")), Map.entry("shotmap", new Param("shotmap", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-leagues", new Operation("fotmob-leagues", "GET", "/fotmob/leagues", Map.of(), List.of("application/json")));
        operations.put("fotmob-lineup-builder-players", new Operation("fotmob-lineup-builder-players", "GET", "/fotmob/lineup-builder-players", Map.ofEntries(Map.entry("player_ids", new Param("player_ids", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-lineup-builder-team", new Operation("fotmob-lineup-builder-team", "GET", "/fotmob/lineup-builder-team", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-match", new Operation("fotmob-match", "GET", "/fotmob/match", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-match-media", new Operation("fotmob-match-media", "GET", "/fotmob/match-media", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-matches", new Operation("fotmob-matches", "GET", "/fotmob/matches", Map.ofEntries(Map.entry("date", new Param("date", "query", true, "string", List.of(), "csv")), Map.entry("timezone", new Param("timezone", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-news", new Operation("fotmob-news", "GET", "/fotmob/news", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "string", List.of(), "csv")), Map.entry("start_index", new Param("start_index", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-news-article", new Operation("fotmob-news-article", "GET", "/fotmob/news-article", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-player", new Operation("fotmob-player", "GET", "/fotmob/player", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("include_market_values", new Param("include_market_values", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-player-match-stats", new Operation("fotmob-player-match-stats", "GET", "/fotmob/player-match-stats", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "string", List.of(), "csv")), Map.entry("match_id", new Param("match_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-player-matches", new Operation("fotmob-player-matches", "GET", "/fotmob/player-matches", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "string", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", false, "string", List.of(), "csv")), Map.entry("before", new Param("before", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-player-stats", new Operation("fotmob-player-stats", "GET", "/fotmob/player-stats", Map.ofEntries(Map.entry("player_id", new Param("player_id", "query", true, "string", List.of(), "csv")), Map.entry("season_id", new Param("season_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-search", new Operation("fotmob-search", "GET", "/fotmob/search", Map.ofEntries(Map.entry("term", new Param("term", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-seasons", new Operation("fotmob-seasons", "GET", "/fotmob/seasons", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-stats", new Operation("fotmob-stats", "GET", "/fotmob/stats", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "string", List.of(), "csv")), Map.entry("season_id", new Param("season_id", "query", false, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", true, "string", List.of("players", "teams"), "csv")), Map.entry("stat", new Param("stat", "query", true, "string", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", false, "string", List.of(), "csv")), Map.entry("position", new Param("position", "query", false, "string", List.of("all", "striker", "winger", "attackingMidfielder", "midfielder", "fullback", "centerBack"), "csv"))), List.of("application/json")));
        operations.put("fotmob-stats-categories", new Operation("fotmob-stats-categories", "GET", "/fotmob/stats-categories", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "string", List.of(), "csv")), Map.entry("season_id", new Param("season_id", "query", false, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", true, "string", List.of("players", "teams"), "csv"))), List.of("application/json")));
        operations.put("fotmob-table", new Operation("fotmob-table", "GET", "/fotmob/table", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-team", new Operation("fotmob-team", "GET", "/fotmob/team", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-team-fixtures", new Operation("fotmob-team-fixtures", "GET", "/fotmob/team-fixtures", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-team-news", new Operation("fotmob-team-news", "GET", "/fotmob/team-news", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv")), Map.entry("start_index", new Param("start_index", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-transfers", new Operation("fotmob-transfers", "GET", "/fotmob/transfers", Map.ofEntries(Map.entry("mode", new Param("mode", "query", false, "string", List.of("all", "rumours", "popular"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("last", new Param("last", "query", false, "string", List.of("6months", "1year", "2years", "3years"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("all", "in", "out"), "csv")), Map.entry("min_fee", new Param("min_fee", "query", false, "integer", List.of(), "csv")), Map.entry("max_fee", new Param("max_fee", "query", false, "integer", List.of(), "csv")), Map.entry("league_ids", new Param("league_ids", "query", false, "string", List.of(), "csv")), Map.entry("team_ids", new Param("team_ids", "query", false, "string", List.of(), "csv")), Map.entry("order_by", new Param("order_by", "query", false, "string", List.of("lastModified", "fee", "date", "name", "fromClubName", "toClubName"), "csv")), Map.entry("exclude_extensions", new Param("exclude_extensions", "query", false, "boolean", List.of(), "csv")), Map.entry("likely_only", new Param("likely_only", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-trending-news", new Operation("fotmob-trending-news", "GET", "/fotmob/trending-news", Map.of(), List.of("application/json")));
        operations.put("fotmob-trending-searches", new Operation("fotmob-trending-searches", "GET", "/fotmob/trending-searches", Map.of(), List.of("application/json")));
        operations.put("fotmob-tv-guide", new Operation("fotmob-tv-guide", "GET", "/fotmob/tv-guide", Map.ofEntries(Map.entry("country", new Param("country", "query", true, "string", List.of("us", "se", "gb", "de", "no", "es", "mx", "ar", "bo", "cl", "co", "cr", "ec", "gt", "hn", "ni", "pa", "py", "pe", "uy", "ve", "da", "ca", "au", "at", "be", "bg", "hr", "cy", "cz", "ee", "fi", "fr", "gr", "hu", "is", "ie", "il", "it", "nl", "pl", "pt", "ro", "ru", "ch", "tr", "za", "br", "in", "me", "id", "th", "mm", "al", "az", "bl", "ba", "ks", "la", "li", "mk", "rs", "sk", "ua", "essv", "nz", "bd", "cn", "gh", "hk", "jp", "kr", "ma", "mt", "my", "ng", "ph", "pk", "sg", "si", "tz"), "csv")), Map.entry("timezone", new Param("timezone", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("fotmob-tv-guide-channels", new Operation("fotmob-tv-guide-channels", "GET", "/fotmob/tv-guide-channels", Map.ofEntries(Map.entry("country", new Param("country", "query", true, "string", List.of("us", "se", "gb", "de", "no", "es", "mx", "ar", "bo", "cl", "co", "cr", "ec", "gt", "hn", "ni", "pa", "py", "pe", "uy", "ve", "da", "ca", "au", "at", "be", "bg", "hr", "cy", "cz", "ee", "fi", "fr", "gr", "hu", "is", "ie", "il", "it", "nl", "pl", "pt", "ro", "ru", "ch", "tr", "za", "br", "in", "me", "id", "th", "mm", "al", "az", "bl", "ba", "ks", "la", "li", "mk", "rs", "sk", "ua", "essv", "nz", "bd", "cn", "gh", "hk", "jp", "kr", "ma", "mt", "my", "ng", "ph", "pk", "sg", "si", "tz"), "csv"))), List.of("application/json")));
        operations.put("fotmob-tv-guide-countries", new Operation("fotmob-tv-guide-countries", "GET", "/fotmob/tv-guide-countries", Map.of(), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown FotMob operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest request = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation))
                .GET().build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object audioMatches(Map<String, ?> params) { return request("fotmob-audio-matches", params); }
    public Object fifaRankingPeriods(Map<String, ?> params) { return request("fotmob-fifa-ranking-periods", params); }
    public Object fifaRankings(Map<String, ?> params) { return request("fotmob-fifa-rankings", params); }
    public Object latestNews(Map<String, ?> params) { return request("fotmob-latest-news", params); }
    public Object league(Map<String, ?> params) { return request("fotmob-league", params); }
    public Object leagues(Map<String, ?> params) { return request("fotmob-leagues", params); }
    public Object lineupBuilderPlayers(Map<String, ?> params) { return request("fotmob-lineup-builder-players", params); }
    public Object lineupBuilderTeam(Map<String, ?> params) { return request("fotmob-lineup-builder-team", params); }
    public Object match(Map<String, ?> params) { return request("fotmob-match", params); }
    public Object matchMedia(Map<String, ?> params) { return request("fotmob-match-media", params); }
    public Object matches(Map<String, ?> params) { return request("fotmob-matches", params); }
    public Object news(Map<String, ?> params) { return request("fotmob-news", params); }
    public Object newsArticle(Map<String, ?> params) { return request("fotmob-news-article", params); }
    public Object player(Map<String, ?> params) { return request("fotmob-player", params); }
    public Object playerMatchStats(Map<String, ?> params) { return request("fotmob-player-match-stats", params); }
    public Object playerMatches(Map<String, ?> params) { return request("fotmob-player-matches", params); }
    public Object playerStats(Map<String, ?> params) { return request("fotmob-player-stats", params); }
    public Object search(Map<String, ?> params) { return request("fotmob-search", params); }
    public Object seasons(Map<String, ?> params) { return request("fotmob-seasons", params); }
    public Object stats(Map<String, ?> params) { return request("fotmob-stats", params); }
    public Object statsCategories(Map<String, ?> params) { return request("fotmob-stats-categories", params); }
    public Object table(Map<String, ?> params) { return request("fotmob-table", params); }
    public Object team(Map<String, ?> params) { return request("fotmob-team", params); }
    public Object teamFixtures(Map<String, ?> params) { return request("fotmob-team-fixtures", params); }
    public Object teamNews(Map<String, ?> params) { return request("fotmob-team-news", params); }
    public Object transfers(Map<String, ?> params) { return request("fotmob-transfers", params); }
    public Object trendingNews(Map<String, ?> params) { return request("fotmob-trending-news", params); }
    public Object trendingSearches(Map<String, ?> params) { return request("fotmob-trending-searches", params); }
    public Object tvGuide(Map<String, ?> params) { return request("fotmob-tv-guide", params); }
    public Object tvGuideChannels(Map<String, ?> params) { return request("fotmob-tv-guide-channels", params); }
    public Object tvGuideCountries(Map<String, ?> params) { return request("fotmob-tv-guide-countries", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
