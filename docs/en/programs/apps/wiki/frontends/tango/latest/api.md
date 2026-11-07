# Tango: API and integration

## Public API

**None documented.** No REST API, no API keys, no SDKs, no rate limits, no webhooks were found in the help centre or the updates feed. Searches for "Tango API", "webhooks" and "developer docs" returned only unrelated products (Tango Card API, a federal data API) ([search](https://www.tango.ai/integrations)).

The help centre says that sharing needs no API: links, Copy HTML, embeds ([integrations](https://help.tango.ai/en/articles/5952635-does-tango-integrate-with-other-tools)).

Status: no public API as of 2026-11-07. Re-check the help centre before relying on this.

## Integration paths that exist

| Path | Plan | Source |
|---|---|---|
| Share link | Free | [share](https://help.tango.ai/en/articles/6695745-how-do-i-share-a-tango) |
| Embed (iframe) in knowledge base: Notion, Confluence, Zendesk one-click; SharePoint needs admin | Free | [embed](https://help.tango.ai/en/articles/7142097-how-do-i-embed-a-tango-into-my-website-or-knowledge-base) |
| Copy HTML, paste into Google Docs, Confluence, Notion | Free | [where it works](https://help.tango.ai/en/articles/17359491-where-does-tango-work) |
| Export PDF, Markdown, HTML | Pro, Ent | [pricing](https://www.tango.ai/pricing) |
| Tango MCP: AI assistants (ChatGPT, Claude, Microsoft 365 Copilot, Cursor, others) connect via remote MCP with OAuth sign-in | Ent | [MCP](https://help.tango.ai/en/articles/17890447-what-is-tango-mcp), [connect](https://help.tango.ai/en/articles/17890522-how-do-i-connect-tango-to-my-ai-assistant), [updates](https://updates.tango.ai/) |

Tool list exposed by the MCP server: unverified (article not read in full).

## Authentication

- Users: sign in to Tango (SSO on Enterprise; [pricing](https://www.tango.ai/pricing)).
- MCP: OAuth sign-in, per the connect article summary.

## Not documented

Endpoints, parameters, response formats, error codes, pagination: none. Nothing to implement against.
