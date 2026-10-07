import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class FotMobClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  audioMatches(params?: OperationParamsMap["fotmob-audio-matches"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fifaRankingPeriods(params: OperationParamsMap["fotmob-fifa-ranking-periods"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fifaRankings(params: OperationParamsMap["fotmob-fifa-rankings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  latestNews(params?: OperationParamsMap["fotmob-latest-news"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  league(params: OperationParamsMap["fotmob-league"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leagues(params?: OperationParamsMap["fotmob-leagues"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  lineupBuilderPlayers(params: OperationParamsMap["fotmob-lineup-builder-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  lineupBuilderTeam(params: OperationParamsMap["fotmob-lineup-builder-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  match(params: OperationParamsMap["fotmob-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchMedia(params: OperationParamsMap["fotmob-match-media"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matches(params: OperationParamsMap["fotmob-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  news(params: OperationParamsMap["fotmob-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsArticle(params: OperationParamsMap["fotmob-news-article"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params: OperationParamsMap["fotmob-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerMatchStats(params: OperationParamsMap["fotmob-player-match-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerMatches(params: OperationParamsMap["fotmob-player-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerStats(params: OperationParamsMap["fotmob-player-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["fotmob-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  seasons(params: OperationParamsMap["fotmob-seasons"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  stats(params: OperationParamsMap["fotmob-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  statsCategories(params: OperationParamsMap["fotmob-stats-categories"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  table(params: OperationParamsMap["fotmob-table"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["fotmob-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamFixtures(params: OperationParamsMap["fotmob-team-fixtures"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamNews(params: OperationParamsMap["fotmob-team-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  transfers(params?: OperationParamsMap["fotmob-transfers"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendingNews(params?: OperationParamsMap["fotmob-trending-news"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendingSearches(params?: OperationParamsMap["fotmob-trending-searches"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tvGuide(params: OperationParamsMap["fotmob-tv-guide"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tvGuideChannels(params: OperationParamsMap["fotmob-tv-guide-channels"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tvGuideCountries(params?: OperationParamsMap["fotmob-tv-guide-countries"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  audioMatches(params?: OperationParamsMap["fotmob-audio-matches"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fifaRankingPeriods(params: OperationParamsMap["fotmob-fifa-ranking-periods"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fifaRankings(params: OperationParamsMap["fotmob-fifa-rankings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  latestNews(params?: OperationParamsMap["fotmob-latest-news"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  league(params: OperationParamsMap["fotmob-league"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leagues(params?: OperationParamsMap["fotmob-leagues"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  lineupBuilderPlayers(params: OperationParamsMap["fotmob-lineup-builder-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  lineupBuilderTeam(params: OperationParamsMap["fotmob-lineup-builder-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  match(params: OperationParamsMap["fotmob-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchMedia(params: OperationParamsMap["fotmob-match-media"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matches(params: OperationParamsMap["fotmob-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  news(params: OperationParamsMap["fotmob-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsArticle(params: OperationParamsMap["fotmob-news-article"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params: OperationParamsMap["fotmob-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerMatchStats(params: OperationParamsMap["fotmob-player-match-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerMatches(params: OperationParamsMap["fotmob-player-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerStats(params: OperationParamsMap["fotmob-player-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["fotmob-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  seasons(params: OperationParamsMap["fotmob-seasons"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  stats(params: OperationParamsMap["fotmob-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  statsCategories(params: OperationParamsMap["fotmob-stats-categories"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  table(params: OperationParamsMap["fotmob-table"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["fotmob-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamFixtures(params: OperationParamsMap["fotmob-team-fixtures"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamNews(params: OperationParamsMap["fotmob-team-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  transfers(params?: OperationParamsMap["fotmob-transfers"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendingNews(params?: OperationParamsMap["fotmob-trending-news"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendingSearches(params?: OperationParamsMap["fotmob-trending-searches"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tvGuide(params: OperationParamsMap["fotmob-tv-guide"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tvGuideChannels(params: OperationParamsMap["fotmob-tv-guide-channels"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tvGuideCountries(params?: OperationParamsMap["fotmob-tv-guide-countries"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  audioMatches(...args: OperationRequestArgs<"fotmob-audio-matches">): Promise<OperationResponseMap["fotmob-audio-matches"]>;
  fifaRankingPeriods(...args: OperationRequestArgs<"fotmob-fifa-ranking-periods">): Promise<OperationResponseMap["fotmob-fifa-ranking-periods"]>;
  fifaRankings(...args: OperationRequestArgs<"fotmob-fifa-rankings">): Promise<OperationResponseMap["fotmob-fifa-rankings"]>;
  latestNews(...args: OperationRequestArgs<"fotmob-latest-news">): Promise<OperationResponseMap["fotmob-latest-news"]>;
  league(...args: OperationRequestArgs<"fotmob-league">): Promise<OperationResponseMap["fotmob-league"]>;
  leagues(...args: OperationRequestArgs<"fotmob-leagues">): Promise<OperationResponseMap["fotmob-leagues"]>;
  lineupBuilderPlayers(...args: OperationRequestArgs<"fotmob-lineup-builder-players">): Promise<OperationResponseMap["fotmob-lineup-builder-players"]>;
  lineupBuilderTeam(...args: OperationRequestArgs<"fotmob-lineup-builder-team">): Promise<OperationResponseMap["fotmob-lineup-builder-team"]>;
  match(...args: OperationRequestArgs<"fotmob-match">): Promise<OperationResponseMap["fotmob-match"]>;
  matchMedia(...args: OperationRequestArgs<"fotmob-match-media">): Promise<OperationResponseMap["fotmob-match-media"]>;
  matches(...args: OperationRequestArgs<"fotmob-matches">): Promise<OperationResponseMap["fotmob-matches"]>;
  news(...args: OperationRequestArgs<"fotmob-news">): Promise<OperationResponseMap["fotmob-news"]>;
  newsArticle(...args: OperationRequestArgs<"fotmob-news-article">): Promise<OperationResponseMap["fotmob-news-article"]>;
  player(...args: OperationRequestArgs<"fotmob-player">): Promise<OperationResponseMap["fotmob-player"]>;
  playerMatchStats(...args: OperationRequestArgs<"fotmob-player-match-stats">): Promise<OperationResponseMap["fotmob-player-match-stats"]>;
  playerMatches(...args: OperationRequestArgs<"fotmob-player-matches">): Promise<OperationResponseMap["fotmob-player-matches"]>;
  playerStats(...args: OperationRequestArgs<"fotmob-player-stats">): Promise<OperationResponseMap["fotmob-player-stats"]>;
  search(...args: OperationRequestArgs<"fotmob-search">): Promise<OperationResponseMap["fotmob-search"]>;
  seasons(...args: OperationRequestArgs<"fotmob-seasons">): Promise<OperationResponseMap["fotmob-seasons"]>;
  stats(...args: OperationRequestArgs<"fotmob-stats">): Promise<OperationResponseMap["fotmob-stats"]>;
  statsCategories(...args: OperationRequestArgs<"fotmob-stats-categories">): Promise<OperationResponseMap["fotmob-stats-categories"]>;
  table(...args: OperationRequestArgs<"fotmob-table">): Promise<OperationResponseMap["fotmob-table"]>;
  team(...args: OperationRequestArgs<"fotmob-team">): Promise<OperationResponseMap["fotmob-team"]>;
  teamFixtures(...args: OperationRequestArgs<"fotmob-team-fixtures">): Promise<OperationResponseMap["fotmob-team-fixtures"]>;
  teamNews(...args: OperationRequestArgs<"fotmob-team-news">): Promise<OperationResponseMap["fotmob-team-news"]>;
  transfers(...args: OperationRequestArgs<"fotmob-transfers">): Promise<OperationResponseMap["fotmob-transfers"]>;
  trendingNews(...args: OperationRequestArgs<"fotmob-trending-news">): Promise<OperationResponseMap["fotmob-trending-news"]>;
  trendingSearches(...args: OperationRequestArgs<"fotmob-trending-searches">): Promise<OperationResponseMap["fotmob-trending-searches"]>;
  tvGuide(...args: OperationRequestArgs<"fotmob-tv-guide">): Promise<OperationResponseMap["fotmob-tv-guide"]>;
  tvGuideChannels(...args: OperationRequestArgs<"fotmob-tv-guide-channels">): Promise<OperationResponseMap["fotmob-tv-guide-channels"]>;
  tvGuideCountries(...args: OperationRequestArgs<"fotmob-tv-guide-countries">): Promise<OperationResponseMap["fotmob-tv-guide-countries"]>;
}
export { FotMobClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default FotMobClient;
