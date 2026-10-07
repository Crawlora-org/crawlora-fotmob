# Crawlora FotMob Ruby client

This gem calls the Crawlora hosted API at `https://api.crawlora.net/api/v1`. It does not call or scrape FotMob directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-fotmob"
```

Create an account at [crawlora.net](https://crawlora.net/signup), open the [Crawlora console](https://crawlora.net/app) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/fotmob"

client = Crawlora::Fotmob::Client.new
result = client.request("fotmob-search", JSON.parse("{\"term\": \"Premier League\"}"))
puts result
client.close
```

Use a generated operation method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem contains 31 operations and follows contract revision `sha256:d40e5ee2b400b1b40b5ca6998063cde26b6bb3e7f84da679b5047d26380f3fa1`.

```ruby
client = Crawlora::Fotmob::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<contract parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON transport. The gem follows contract revision `sha256:d40e5ee2b400b1b40b5ca6998063cde26b6bb3e7f84da679b5047d26380f3fa1` and contains 31 operations.

See [Crawlora](https://crawlora.net/), the [API documentation](https://crawlora.net/docs), and [the package repository](https://github.com/Crawlora-org/crawlora-fotmob) for account setup, the generated operation reference, and release history.
