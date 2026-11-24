# Company Hiring Intelligence & Tech Stack MCP Server (`io.github.Shoomaii/company-hiring-intelligence`)

Auto-discovers any company's ATS board from its domain and returns open role counts, Engineering / GTM / AI mix, seniority distribution, USD salary medians, and 80+ internal tech tools mined from live job descriptions.

- **Streamable HTTP Endpoint:** `https://shoomaii--company-hiring-intelligence.apify.actor/mcp`
- **MCP Tool:** `enrich_company_hiring`
- **Apify Store:** https://apify.com/shoomaii/company-hiring-intelligence

## Client Config

```json
{
  "mcpServers": {
    "company-hiring-intelligence": {
      "type": "streamable-http",
      "url": "https://shoomaii--company-hiring-intelligence.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```
