require_relative "lib/crawlora/fotmob/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-fotmob"
  spec.version = Crawlora::Fotmob::VERSION
  spec.summary = "FotMob client for the Crawlora hosted API"
  spec.description = "Credential-free FotMob API access through Crawlora's hosted service."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-fotmob", "documentation_uri" => "https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fotmob-ruby-api-docs", "rubygems_mfa_required" => "true" }

end
