# Prediction Markets Odds MCP Server (`io.github.Shoomaii/prediction-markets-odds`)

Live normalized probabilities, bid/ask spreads, 24h USD volume, and close dates across **Polymarket and Kalshi** — hosted on Apify Standby with sub-second cached responses.

- **Streamable HTTP Endpoint:** `https://shoomaii--prediction-markets-odds.apify.actor/mcp`
- **MCP Tool:** `get_prediction_market_odds`
- **Apify Store:** https://apify.com/shoomaii/prediction-markets-odds

## Client Config

```json
{
  "mcpServers": {
    "prediction-markets-odds": {
      "type": "streamable-http",
      "url": "https://shoomaii--prediction-markets-odds.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```
