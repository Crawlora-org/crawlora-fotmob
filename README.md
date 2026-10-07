# FotMob clients for Crawlora

Official Crawlora client packages for the hosted FotMob API. These packages send requests to Crawlora's API and require a Crawlora account and `CRAWLORA_API_KEY`; service usage follows your Crawlora account billing plan.

The packages do not run a browser or scrape FotMob locally. Crawlora is an independent service and is not affiliated with or endorsed by FotMob or its owners.

- JavaScript / TypeScript: [`@crawlora-org/fotmob`](javascript/README.md)
- Python: [`crawlora-fotmob`](python/README.md)
- Full endpoint and parameter reference: [docs/usage.md](docs/usage.md)
- Runnable samples: [examples/](examples/)
- Source repository: [https://github.com/Crawlora-org/crawlora-fotmob](https://github.com/Crawlora-org/crawlora-fotmob)

## Install

```sh
npm install @crawlora-org/fotmob
python -m pip install crawlora-fotmob
```

Set your Crawlora key in the environment before running a client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

Do not commit API keys. See the language-specific READMEs for sync and async use.

## Contract

This package release is `0.1.0`. The generated client methods follow the bundled `openapi/public.json` contract at revision `sha256:d40e5ee2b400b1b40b5ca6998063cde26b6bb3e7f84da679b5047d26380f3fa1`. `scripts/generate.py` regenerates both language clients and the documentation from the shared source.

## License

MIT. See [LICENSE](LICENSE).
