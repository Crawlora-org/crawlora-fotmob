require "json"
require "net/http"
require "uri"

module Crawlora
  module Fotmob
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"fotmob-audio-matches": {"id": "fotmob-audio-matches", "method": "GET", "params": [], "path": "/fotmob/audio-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "fotmob-fifa-ranking-periods": {"id": "fotmob-fifa-ranking-periods", "method": "GET", "params": [{"description": "Ranking gender", "enum": ["men", "women"], "in": "query", "name": "gender", "required": true, "type": "string", "x-example": "men"}], "path": "/fotmob/fifa-ranking-periods", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["men", "women"], "in": "query", "name": "gender", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-fifa-rankings": {"id": "fotmob-fifa-rankings", "method": "GET", "params": [{"description": "Ranking gender", "enum": ["men", "women"], "in": "query", "name": "gender", "required": true, "type": "string", "x-example": "men"}, {"description": "Period id returned for this gender by /fotmob/fifa-ranking-periods", "in": "query", "name": "period_id", "required": true, "type": "string", "x-example": "20260720"}], "path": "/fotmob/fifa-rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["men", "women"], "in": "query", "name": "gender", "required": true, "type": "string"}, {"in": "query", "name": "period_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-latest-news": {"id": "fotmob-latest-news", "method": "GET", "params": [{"description": "Zero-based news offset; defaults to 0", "in": "query", "maximum": 10000, "minimum": 0, "name": "start_index", "type": "integer"}], "path": "/fotmob/latest-news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "start_index", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fotmob-league": {"id": "fotmob-league", "method": "GET", "params": [{"description": "Numeric FotMob league id from /fotmob/leagues", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 47}, {"description": "Optional season value from /fotmob/seasons for this league", "in": "query", "name": "season", "type": "string", "x-example": "2025/2026"}, {"default": false, "description": "Include the optional overview shot map; increases response size", "in": "query", "name": "shotmap", "type": "boolean"}], "path": "/fotmob/league", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}, {"in": "query", "name": "season", "type": "string"}, {"in": "query", "name": "shotmap", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "fotmob-leagues": {"id": "fotmob-leagues", "method": "GET", "params": [], "path": "/fotmob/leagues", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "fotmob-lineup-builder-players": {"id": "fotmob-lineup-builder-players", "method": "GET", "params": [{"description": "Comma-separated list of 1 to 11 numeric FotMob player ids", "in": "query", "name": "player_ids", "required": true, "type": "string", "x-example": "961995,562727"}], "path": "/fotmob/lineup-builder-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-lineup-builder-team": {"id": "fotmob-lineup-builder-team", "method": "GET", "params": [{"description": "Numeric FotMob team id discoverable through /fotmob/search", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "9825"}], "path": "/fotmob/lineup-builder-team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-match": {"id": "fotmob-match", "method": "GET", "params": [{"description": "Numeric FotMob match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "5181825"}], "path": "/fotmob/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-match-media": {"id": "fotmob-match-media", "method": "GET", "params": [{"description": "Numeric FotMob match id, discoverable from /fotmob/matches or /fotmob/search", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "5795457"}], "path": "/fotmob/match-media", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-matches": {"id": "fotmob-matches", "method": "GET", "params": [{"description": "Date in YYYYMMDD format", "in": "query", "name": "date", "required": true, "type": "string", "x-example": "20260925"}, {"description": "IANA timezone; defaults to UTC", "in": "query", "name": "timezone", "type": "string", "x-example": "Asia/Shanghai"}], "path": "/fotmob/matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "date", "required": true, "type": "string"}, {"in": "query", "name": "timezone", "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-news": {"id": "fotmob-news", "method": "GET", "params": [{"description": "Numeric FotMob league id", "in": "query", "name": "league_id", "required": true, "type": "string", "x-example": "47"}, {"description": "Zero-based news offset; defaults to 0", "in": "query", "maximum": 10000, "minimum": 0, "name": "start_index", "type": "integer"}], "path": "/fotmob/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "string"}, {"in": "query", "name": "start_index", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fotmob-news-article": {"id": "fotmob-news-article", "method": "GET", "params": [{"description": "Complete FotMob top-news article id and slug from the public article URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "29776-fotmob-totw-premier-league-matchday-5s-best-xi"}], "path": "/fotmob/news-article", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-player": {"id": "fotmob-player", "method": "GET", "params": [{"description": "Numeric FotMob player id from fotmob/search", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "961995"}, {"default": true, "description": "Include market-value history; defaults to true", "in": "query", "name": "include_market_values", "type": "boolean"}], "path": "/fotmob/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "include_market_values", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "fotmob-player-match-stats": {"id": "fotmob-player-match-stats", "method": "GET", "params": [{"description": "Numeric FotMob player id", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "961995"}, {"description": "Numeric FotMob match id", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "5795457"}], "path": "/fotmob/player-match-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "string"}, {"in": "query", "name": "match_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-player-matches": {"id": "fotmob-player-matches", "method": "GET", "params": [{"description": "Numeric FotMob player id from fotmob/search", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "961995"}, {"default": "all", "description": "all, or a numeric league id from fotmob/player matchFilters", "in": "query", "name": "league_id", "type": "string", "x-example": "47"}, {"default": "all", "description": "all, or a numeric team id paired with league_id in fotmob/player matchFilters", "in": "query", "name": "team_id", "type": "string", "x-example": "9825"}, {"description": "Numeric before timestamp from the upstream previous URL; omit for the newest page", "in": "query", "name": "before", "type": "string", "x-example": "1767902400"}], "path": "/fotmob/player-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "string"}, {"in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "team_id", "type": "string"}, {"in": "query", "name": "before", "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-player-stats": {"id": "fotmob-player-stats", "method": "GET", "params": [{"description": "Numeric FotMob player id from fotmob/search", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "961995"}, {"description": "Player-specific entryId from fotmob/player statSeasons", "in": "query", "name": "season_id", "required": true, "type": "string", "x-example": "0-1"}], "path": "/fotmob/player-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "player_id", "required": true, "type": "string"}, {"in": "query", "name": "season_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-search": {"id": "fotmob-search", "method": "GET", "params": [{"description": "Search phrase, 1 to 50 characters", "in": "query", "maxLength": 50, "minLength": 1, "name": "term", "required": true, "type": "string", "x-example": "Arsenal"}], "path": "/fotmob/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "term", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-seasons": {"id": "fotmob-seasons", "method": "GET", "params": [{"description": "Numeric FotMob league id from /fotmob/leagues", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 47}], "path": "/fotmob/seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "fotmob-stats": {"id": "fotmob-stats", "method": "GET", "params": [{"description": "Numeric FotMob league id", "in": "query", "name": "league_id", "required": true, "type": "string", "x-example": "47"}, {"description": "Numeric season id from /fotmob/stats-categories; defaults to the newest season", "in": "query", "name": "season_id", "type": "string", "x-example": "36781"}, {"description": "Stats subject", "enum": ["players", "teams"], "in": "query", "name": "type", "required": true, "type": "string", "x-example": "players"}, {"description": "Stat id returned by /fotmob/stats-categories for this league, season, and type", "in": "query", "name": "stat", "required": true, "type": "string", "x-example": "goals"}, {"description": "Optional numeric team id to filter player stats", "in": "query", "name": "team_id", "type": "string", "x-example": "8456"}, {"description": "Optional client-side player position filter", "enum": ["all", "striker", "winger", "attackingMidfielder", "midfielder", "fullback", "centerBack"], "in": "query", "name": "position", "type": "string", "x-example": "striker"}], "path": "/fotmob/stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "string"}, {"in": "query", "name": "season_id", "type": "string"}, {"enum": ["players", "teams"], "in": "query", "name": "type", "required": true, "type": "string"}, {"in": "query", "name": "stat", "required": true, "type": "string"}, {"in": "query", "name": "team_id", "type": "string"}, {"enum": ["all", "striker", "winger", "attackingMidfielder", "midfielder", "fullback", "centerBack"], "in": "query", "name": "position", "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-stats-categories": {"id": "fotmob-stats-categories", "method": "GET", "params": [{"description": "Numeric FotMob league id", "in": "query", "name": "league_id", "required": true, "type": "string", "x-example": "47"}, {"description": "Numeric season id; omit to discover seasons", "in": "query", "name": "season_id", "type": "string", "x-example": "36781"}, {"description": "Stats subject", "enum": ["players", "teams"], "in": "query", "name": "type", "required": true, "type": "string", "x-example": "players"}], "path": "/fotmob/stats-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "string"}, {"in": "query", "name": "season_id", "type": "string"}, {"enum": ["players", "teams"], "in": "query", "name": "type", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-table": {"id": "fotmob-table", "method": "GET", "params": [{"description": "Numeric FotMob league id", "in": "query", "name": "league_id", "required": true, "type": "string", "x-example": "47"}], "path": "/fotmob/table", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-team": {"id": "fotmob-team", "method": "GET", "params": [{"description": "Numeric FotMob team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9825"}], "path": "/fotmob/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-team-fixtures": {"id": "fotmob-team-fixtures", "method": "GET", "params": [{"description": "Numeric FotMob team id", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "9825"}, {"description": "Opaque cursor copied from fixtures.previousFixturesUrl in /fotmob/team or previous in the preceding response", "in": "query", "name": "cursor", "required": true, "type": "string", "x-example": "https://pub.fotmob.com/prod/db/api/team/9825/fixture-by-date?beforeTimestamp=1785607200"}], "path": "/fotmob/team-fixtures", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-team-news": {"id": "fotmob-team-news", "method": "GET", "params": [{"description": "Numeric FotMob team id", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 8456}, {"description": "Zero-based news offset from 0 through 10000", "in": "query", "maximum": 10000, "minimum": 0, "name": "start_index", "type": "integer", "x-example": 0}], "path": "/fotmob/team-news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}, {"in": "query", "name": "start_index", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fotmob-transfers": {"id": "fotmob-transfers", "method": "GET", "params": [{"default": "all", "description": "Feed mode", "enum": ["all", "rumours", "popular"], "in": "query", "name": "mode", "type": "string"}, {"default": 1, "description": "One-based result page; 50 rows per page", "in": "query", "maximum": 200, "minimum": 1, "name": "page", "type": "integer"}, {"default": "6months", "description": "Time window", "enum": ["6months", "1year", "2years", "3years"], "in": "query", "name": "last", "type": "string"}, {"default": "all", "description": "Transfer direction; applied when league_ids or team_ids is supplied", "enum": ["all", "in", "out"], "in": "query", "name": "direction", "type": "string"}, {"description": "Minimum transfer fee in EUR", "in": "query", "minimum": 0, "name": "min_fee", "type": "integer"}, {"description": "Maximum transfer fee in EUR", "in": "query", "minimum": 0, "name": "max_fee", "type": "integer"}, {"description": "Comma-separated numeric FotMob league ids, up to 50; discover with /fotmob/leagues", "in": "query", "name": "league_ids", "type": "string", "x-example": "47"}, {"description": "Comma-separated numeric FotMob team ids, up to 50; discover with /fotmob/search", "in": "query", "name": "team_ids", "type": "string", "x-example": "8456"}, {"default": "lastModified", "description": "Sort column", "enum": ["lastModified", "fee", "date", "name", "fromClubName", "toClubName"], "in": "query", "name": "order_by", "type": "string"}, {"default": false, "description": "Exclude contract-extension records", "in": "query", "name": "exclude_extensions", "type": "boolean"}, {"default": false, "description": "Return only likely rumours; mode must be rumours", "in": "query", "name": "likely_only", "type": "boolean"}], "path": "/fotmob/transfers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "rumours", "popular"], "in": "query", "name": "mode", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["6months", "1year", "2years", "3years"], "in": "query", "name": "last", "type": "string"}, {"enum": ["all", "in", "out"], "in": "query", "name": "direction", "type": "string"}, {"in": "query", "name": "min_fee", "type": "integer"}, {"in": "query", "name": "max_fee", "type": "integer"}, {"in": "query", "name": "league_ids", "type": "string"}, {"in": "query", "name": "team_ids", "type": "string"}, {"enum": ["lastModified", "fee", "date", "name", "fromClubName", "toClubName"], "in": "query", "name": "order_by", "type": "string"}, {"in": "query", "name": "exclude_extensions", "type": "boolean"}, {"in": "query", "name": "likely_only", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "fotmob-trending-news": {"id": "fotmob-trending-news", "method": "GET", "params": [], "path": "/fotmob/trending-news", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "fotmob-trending-searches": {"id": "fotmob-trending-searches", "method": "GET", "params": [], "path": "/fotmob/trending-searches", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "fotmob-tv-guide": {"id": "fotmob-tv-guide", "method": "GET", "params": [{"description": "Market code from /fotmob/tv-guide-countries", "enum": ["us", "se", "gb", "de", "no", "es", "mx", "ar", "bo", "cl", "co", "cr", "ec", "gt", "hn", "ni", "pa", "py", "pe", "uy", "ve", "da", "ca", "au", "at", "be", "bg", "hr", "cy", "cz", "ee", "fi", "fr", "gr", "hu", "is", "ie", "il", "it", "nl", "pl", "pt", "ro", "ru", "ch", "tr", "za", "br", "in", "me", "id", "th", "mm", "al", "az", "bl", "ba", "ks", "la", "li", "mk", "rs", "sk", "ua", "essv", "nz", "bd", "cn", "gh", "hk", "jp", "kr", "ma", "mt", "my", "ng", "ph", "pk", "sg", "si", "tz"], "in": "query", "name": "country", "required": true, "type": "string", "x-example": "us"}, {"description": "IANA timezone for local times", "in": "query", "name": "timezone", "type": "string", "x-example": "America/New_York"}], "path": "/fotmob/tv-guide", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["us", "se", "gb", "de", "no", "es", "mx", "ar", "bo", "cl", "co", "cr", "ec", "gt", "hn", "ni", "pa", "py", "pe", "uy", "ve", "da", "ca", "au", "at", "be", "bg", "hr", "cy", "cz", "ee", "fi", "fr", "gr", "hu", "is", "ie", "il", "it", "nl", "pl", "pt", "ro", "ru", "ch", "tr", "za", "br", "in", "me", "id", "th", "mm", "al", "az", "bl", "ba", "ks", "la", "li", "mk", "rs", "sk", "ua", "essv", "nz", "bd", "cn", "gh", "hk", "jp", "kr", "ma", "mt", "my", "ng", "ph", "pk", "sg", "si", "tz"], "in": "query", "name": "country", "required": true, "type": "string"}, {"in": "query", "name": "timezone", "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-tv-guide-channels": {"id": "fotmob-tv-guide-channels", "method": "GET", "params": [{"description": "Market code from /fotmob/tv-guide-countries", "enum": ["us", "se", "gb", "de", "no", "es", "mx", "ar", "bo", "cl", "co", "cr", "ec", "gt", "hn", "ni", "pa", "py", "pe", "uy", "ve", "da", "ca", "au", "at", "be", "bg", "hr", "cy", "cz", "ee", "fi", "fr", "gr", "hu", "is", "ie", "il", "it", "nl", "pl", "pt", "ro", "ru", "ch", "tr", "za", "br", "in", "me", "id", "th", "mm", "al", "az", "bl", "ba", "ks", "la", "li", "mk", "rs", "sk", "ua", "essv", "nz", "bd", "cn", "gh", "hk", "jp", "kr", "ma", "mt", "my", "ng", "ph", "pk", "sg", "si", "tz"], "in": "query", "name": "country", "required": true, "type": "string", "x-example": "us"}], "path": "/fotmob/tv-guide-channels", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["us", "se", "gb", "de", "no", "es", "mx", "ar", "bo", "cl", "co", "cr", "ec", "gt", "hn", "ni", "pa", "py", "pe", "uy", "ve", "da", "ca", "au", "at", "be", "bg", "hr", "cy", "cz", "ee", "fi", "fr", "gr", "hu", "is", "ie", "il", "it", "nl", "pl", "pt", "ro", "ru", "ch", "tr", "za", "br", "in", "me", "id", "th", "mm", "al", "az", "bl", "ba", "ks", "la", "li", "mk", "rs", "sk", "ua", "essv", "nz", "bd", "cn", "gh", "hk", "jp", "kr", "ma", "mt", "my", "ng", "ph", "pk", "sg", "si", "tz"], "in": "query", "name": "country", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fotmob-tv-guide-countries": {"id": "fotmob-tv-guide-countries", "method": "GET", "params": [], "path": "/fotmob/tv-guide-countries", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["fotmob-audio-matches", "fotmob-fifa-ranking-periods", "fotmob-fifa-rankings", "fotmob-latest-news", "fotmob-league", "fotmob-leagues", "fotmob-lineup-builder-players", "fotmob-lineup-builder-team", "fotmob-match", "fotmob-match-media", "fotmob-matches", "fotmob-news", "fotmob-news-article", "fotmob-player", "fotmob-player-match-stats", "fotmob-player-matches", "fotmob-player-stats", "fotmob-search", "fotmob-seasons", "fotmob-stats", "fotmob-stats-categories", "fotmob-table", "fotmob-team", "fotmob-team-fixtures", "fotmob-team-news", "fotmob-transfers", "fotmob-trending-news", "fotmob-trending-searches", "fotmob-tv-guide", "fotmob-tv-guide-channels", "fotmob-tv-guide-countries"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-fotmob-ruby/0.1.7", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = Net::HTTP::Get.new(uri)
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = @transport.call(url, request.to_hash, @timeout)
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('audio_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-audio-matches', params, response_type: response_type)
      end
      define_method('fifa_ranking_periods') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-fifa-ranking-periods', params, response_type: response_type)
      end
      define_method('fifa_rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-fifa-rankings', params, response_type: response_type)
      end
      define_method('latest_news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-latest-news', params, response_type: response_type)
      end
      define_method('league') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-league', params, response_type: response_type)
      end
      define_method('leagues') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-leagues', params, response_type: response_type)
      end
      define_method('lineup_builder_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-lineup-builder-players', params, response_type: response_type)
      end
      define_method('lineup_builder_team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-lineup-builder-team', params, response_type: response_type)
      end
      define_method('match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-match', params, response_type: response_type)
      end
      define_method('match_media') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-match-media', params, response_type: response_type)
      end
      define_method('matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-matches', params, response_type: response_type)
      end
      define_method('news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-news', params, response_type: response_type)
      end
      define_method('news_article') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-news-article', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-player', params, response_type: response_type)
      end
      define_method('player_match_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-player-match-stats', params, response_type: response_type)
      end
      define_method('player_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-player-matches', params, response_type: response_type)
      end
      define_method('player_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-player-stats', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-search', params, response_type: response_type)
      end
      define_method('seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-seasons', params, response_type: response_type)
      end
      define_method('stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-stats', params, response_type: response_type)
      end
      define_method('stats_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-stats-categories', params, response_type: response_type)
      end
      define_method('table') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-table', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-team', params, response_type: response_type)
      end
      define_method('team_fixtures') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-team-fixtures', params, response_type: response_type)
      end
      define_method('team_news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-team-news', params, response_type: response_type)
      end
      define_method('transfers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-transfers', params, response_type: response_type)
      end
      define_method('trending_news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-trending-news', params, response_type: response_type)
      end
      define_method('trending_searches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-trending-searches', params, response_type: response_type)
      end
      define_method('tv_guide') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-tv-guide', params, response_type: response_type)
      end
      define_method('tv_guide_channels') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-tv-guide-channels', params, response_type: response_type)
      end
      define_method('tv_guide_countries') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fotmob-tv-guide-countries', params, response_type: response_type)
      end

      private

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
