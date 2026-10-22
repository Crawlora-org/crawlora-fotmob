use crawlora_fotmob::{Client, FotmobLeaguesParams, ModelFotmobResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client.fotmob.leagues(Default::default()).await?;
    let data: ModelFotmobResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
