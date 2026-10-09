# Crawlora FotMob Ruby client

This gem calls the Crawlora hosted API at `https://api.crawlora.net/api/v1`. It does not call or scrape FotMob directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-fotmob"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/fotmob"

client = Crawlora::Fotmob::Client.new
result = client.request("fotmob-search", JSON.parse("{\"term\": \"Premier League\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 31 API operations.

```ruby
client = Crawlora::Fotmob::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-fotmob) for account setup, the API operation reference, and release history.
