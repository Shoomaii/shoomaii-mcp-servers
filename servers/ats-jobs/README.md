# Company Jobs & Salaries MCP Server (`io.github.Shoomaii/ats-jobs`)

Live open roles, extracted salaries, seniority levels, ISO-2 country codes, and remote flags across **Greenhouse, Lever, Ashby, SmartRecruiters, Recruitee, and Personio** — hosted on Apify Standby.

- **Streamable HTTP Endpoint:** `https://shoomaii--ats-jobs-actor.apify.actor/mcp`
- **MCP Tool:** `search_company_jobs`
- **Apify Store:** https://apify.com/shoomaii/ats-jobs-actor

## Client Config

```json
{
  "mcpServers": {
    "company-jobs-salaries": {
      "type": "streamable-http",
      "url": "https://shoomaii--ats-jobs-actor.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```
