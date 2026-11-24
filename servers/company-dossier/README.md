# Company Dossier & Signals API MCP Server (`io.github.Shoomaii/company-dossier`)

Assemble a complete company intelligence dossier in `<3s` per domain: site summary & pricing/careers/docs links, Cloudflare DoH MX/SPF/DMARC security grade, tech stack, Trust Center vendor, `llms.txt`, live ATS headcount, and GitHub organization pulse — hosted on Apify Standby.

- **Streamable HTTP Endpoint:** `https://shoomaii--company-dossier.apify.actor/mcp`
- **MCP Tool:** `get_company_dossier`
- **Apify Store:** https://apify.com/shoomaii/company-dossier

## Client Config

```json
{
  "mcpServers": {
    "company-dossier": {
      "type": "streamable-http",
      "url": "https://shoomaii--company-dossier.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```
