import { FotMobClient } from "../src/index.js";

const client = new FotMobClient({ apiKey: "test-key" });
void client.fifaRankingPeriods({"gender": "men"});
void client.request("fotmob-fifa-ranking-periods", {"gender": "men"});
const streamResponse: Promise<Response> = client.request("fotmob-fifa-ranking-periods", {"gender": "men"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("fotmob-fifa-ranking-periods", {"gender": "men"}, { responseType: "stream" });
const directStream: Promise<Response> = client.fifaRankingPeriods({"gender": "men"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("fotmob-fifa-ranking-periods", {"gender": "men"}, { responseType: "text" });
const rawText: Promise<string> = client.request("fotmob-fifa-ranking-periods", {"gender": "men"}, { responseType: "text" });
void rawText;


void client.audioMatches();
void client.request("fotmob-audio-matches");
// @ts-expect-error The selected operation requires its documented params.
void client.fifaRankingPeriods();
