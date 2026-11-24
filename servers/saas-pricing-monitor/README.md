# B2B SaaS Pricing Extractor & Change Monitor MCP Server (`io.github.Shoomaii/saas-pricing-monitor`)

Auto-discover SaaS `/pricing` pages and deterministically extract structured plan tiers (monthly/annual price, seat vs. usage billing, free tier, free trial, Contact Sales, and Enterprise SSO paywall) — hosted on Apify Standby.

- **Streamable HTTP Endpoint:** `https://shoomaii--saas-pricing-monitor.apify.actor/mcp`
- **MCP Tool:** `extract_saas_pricing`
- **Apify Store:** https://apify.com/shoomaii/saas-pricing-monitor

## Client Config

```json
{
  "mcpServers": {
    "saas-pricing-monitor": {
      "type": "streamable-http",
      "url": "https://shoomaii--saas-pricing-monitor.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```
