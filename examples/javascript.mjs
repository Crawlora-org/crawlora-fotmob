import { FotMobClient } from "@crawlora-org/fotmob";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new FotMobClient({ apiKey });

  const leagues = await client.leagues({  });
  console.log("leagues", leagues);
  const search = await client.search({ term: "Premier League" });
  console.log("search", search);
