# Prediction Markets Arbitrage & L2 Slippage MCP Server (`io.github.Shoomaii/prediction-markets-arb`)

Cross-venue **Polymarket and Kalshi** arbitrage scanner and L2 orderbook slippage API. Walks live CLOB and Kalshi books, computes fee-adjusted net arb % and executable VWAP at $100 / $1,000 / $10,000, and flags UMA vs. CFTC resolution risk.

- **Streamable HTTP Endpoint:** `https://shoomaii--prediction-markets-arb.apify.actor/mcp`
- **MCP Tools:** `find_prediction_market_arbitrage`, `get_orderbook_depth_slippage`
- **Apify Store:** https://apify.com/shoomaii/prediction-markets-arb

## Client Config

```json
{
  "mcpServers": {
    "prediction-markets-arb": {
      "type": "streamable-http",
      "url": "https://shoomaii--prediction-markets-arb.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```
