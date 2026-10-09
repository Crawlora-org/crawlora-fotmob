# FotMob clients for Crawlora

Official Crawlora client packages for the hosted FotMob API. These packages send requests to Crawlora's API and require a Crawlora account and `CRAWLORA_API_KEY`; service usage follows your Crawlora account billing plan.

The packages do not run a browser or scrape FotMob locally. Crawlora is an independent service and is not affiliated with or endorsed by FotMob or its owners.

- JavaScript / TypeScript: [`@crawlora-org/fotmob`](javascript/README.md)
- Python: [`crawlora-fotmob`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-fotmob`](go.mod)
- Ruby: [`crawlora-fotmob`](ruby/README.md)
- Java: [`net.crawlora:crawlora-fotmob:0.1.4`](java/README.md)
- PHP: [`crawlora/fotmob`](php/README.md)
- Full endpoint and parameter reference: [docs/usage.md](docs/usage.md)
- Runnable samples: [examples/](examples/)

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-repository-api-docs).

## Install

```sh
npm install @crawlora-org/fotmob
python -m pip install crawlora-fotmob
go get github.com/Crawlora-org/crawlora-fotmob@latest
gem install crawlora-fotmob
composer require crawlora/fotmob
```

For Java, add `net.crawlora:crawlora-fotmob:0.1.4` to your Maven dependencies; see [java/README.md](java/README.md).

Set your Crawlora key in the environment before running a client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

Do not commit API keys. See the language-specific READMEs for sync and async use.

## PHP example

The Packagist package is available as `crawlora/fotmob`:

```sh
composer require crawlora/fotmob
```

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$apiKey = getenv('CRAWLORA_API_KEY');
if (!$apiKey) throw new RuntimeException('Set CRAWLORA_API_KEY before running this example.');
$client = new \Crawlora\FotMob\Client(apiKey: $apiKey);
$result = $client->request("fotmob-leagues", []);
print_r($result);
$client->close();
```

The same example and install details are in [php/README.md](php/README.md).

## License

MIT. See [LICENSE](LICENSE).
