import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class FotMobClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-fotmob-js/0.1.1" });
    this["audioMatches"] = (...args) => this.request("fotmob-audio-matches", ...args);
    this["fifaRankingPeriods"] = (...args) => this.request("fotmob-fifa-ranking-periods", ...args);
    this["fifaRankings"] = (...args) => this.request("fotmob-fifa-rankings", ...args);
    this["latestNews"] = (...args) => this.request("fotmob-latest-news", ...args);
    this["league"] = (...args) => this.request("fotmob-league", ...args);
    this["leagues"] = (...args) => this.request("fotmob-leagues", ...args);
    this["lineupBuilderPlayers"] = (...args) => this.request("fotmob-lineup-builder-players", ...args);
    this["lineupBuilderTeam"] = (...args) => this.request("fotmob-lineup-builder-team", ...args);
    this["match"] = (...args) => this.request("fotmob-match", ...args);
    this["matchMedia"] = (...args) => this.request("fotmob-match-media", ...args);
    this["matches"] = (...args) => this.request("fotmob-matches", ...args);
    this["news"] = (...args) => this.request("fotmob-news", ...args);
    this["newsArticle"] = (...args) => this.request("fotmob-news-article", ...args);
    this["player"] = (...args) => this.request("fotmob-player", ...args);
    this["playerMatchStats"] = (...args) => this.request("fotmob-player-match-stats", ...args);
    this["playerMatches"] = (...args) => this.request("fotmob-player-matches", ...args);
    this["playerStats"] = (...args) => this.request("fotmob-player-stats", ...args);
    this["search"] = (...args) => this.request("fotmob-search", ...args);
    this["seasons"] = (...args) => this.request("fotmob-seasons", ...args);
    this["stats"] = (...args) => this.request("fotmob-stats", ...args);
    this["statsCategories"] = (...args) => this.request("fotmob-stats-categories", ...args);
    this["table"] = (...args) => this.request("fotmob-table", ...args);
    this["team"] = (...args) => this.request("fotmob-team", ...args);
    this["teamFixtures"] = (...args) => this.request("fotmob-team-fixtures", ...args);
    this["teamNews"] = (...args) => this.request("fotmob-team-news", ...args);
    this["transfers"] = (...args) => this.request("fotmob-transfers", ...args);
    this["trendingNews"] = (...args) => this.request("fotmob-trending-news", ...args);
    this["trendingSearches"] = (...args) => this.request("fotmob-trending-searches", ...args);
    this["tvGuide"] = (...args) => this.request("fotmob-tv-guide", ...args);
    this["tvGuideChannels"] = (...args) => this.request("fotmob-tv-guide-channels", ...args);
    this["tvGuideCountries"] = (...args) => this.request("fotmob-tv-guide-countries", ...args);
  }
}

export { FotMobClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.1";
export default FotMobClient;
