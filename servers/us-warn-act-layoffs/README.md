# US WARN Act Layoff Tracker MCP Server (`io.github.Shoomaii/us-warn-act-layoffs`)

Query official US state WARN Act mass-layoff and facility closure filings across **CA, NY, WA, MD, OR, WI, and IN** in one normalized schema with public stock ticker & domain mapping — hosted on Apify Standby.

- **Streamable HTTP Endpoint:** `https://shoomaii--us-warn-act-layoffs.apify.actor/mcp`
- **MCP Tool:** `search_warn_layoffs`
- **Apify Store:** https://apify.com/shoomaii/us-warn-act-layoffs

## Client Config

```json
{
  "mcpServers": {
    "us-warn-act-layoffs": {
      "type": "streamable-http",
      "url": "https://shoomaii--us-warn-act-layoffs.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```
