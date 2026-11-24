# Podcast & Newsletter Sponsor Intelligence MCP Server (`io.github.Shoomaii/podcast-newsletter-sponsors`)

Pass podcast show names, Apple Podcasts links, RSS feeds, or Substack/Beehiiv newsletters to extract active brand sponsors, promo codes, vanity/UTM links, placement dates, and repeat-sponsor counts.

- **Streamable HTTP Endpoint:** `https://shoomaii--podcast-newsletter-sponsor-intel.apify.actor/mcp`
- **MCP Tool:** `extract_podcast_newsletter_sponsors`
- **Apify Store:** https://apify.com/shoomaii/podcast-newsletter-sponsor-intel

## Client Config

```json
{
  "mcpServers": {
    "podcast-newsletter-sponsors": {
      "type": "streamable-http",
      "url": "https://shoomaii--podcast-newsletter-sponsor-intel.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```
