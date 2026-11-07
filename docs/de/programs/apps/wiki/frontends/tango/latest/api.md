# Tango: API und Integration

## Öffentliche API

**Keine dokumentiert.** Im Hilfezentrum oder im Update-Feed wurden keine REST-API, keine API-Schlüssel, keine SDKs, keine Ratenlimits und keine Webhooks gefunden. Suchen nach „Tango API“, „webhooks“ und „developer docs“ ergaben nur unverwandte Produkte (Tango Card API, eine Bundes-Datenschnittstelle) ([Suche](https://www.tango.ai/integrations)).

Das Hilfezentrum sagt, dass Freigaben keine API benötigen: Links, HTML kopieren, Einbettungen ([Integrationen](https://help.tango.ai/en/articles/5952635-does-tango-integrate-with-other-tools)).

Status: keine öffentliche API Stand 2026-11-07. Prüfe das Hilfezentrum erneut, bevor du dich darauf verlässt.

## Vorhandene Integrationswege

| Weg | Tarif | Quelle |
|---|---|---|
| Freigabe-Link | Free | [Freigabe](https://help.tango.ai/en/articles/6695745-how-do-i-share-a-tango) |
| Einbettung (iframe) in eine Wissensdatenbank: Notion, Confluence, Zendesk mit einem Klick; SharePoint benötigt Admin-Rechte | Free | [Einbettung](https://help.tango.ai/en/articles/7142097-how-do-i-embed-a-tango-into-my-website-or-knowledge-base) |
| HTML kopieren, in Google Docs, Confluence, Notion einfügen | Free | [Wo es funktioniert](https://help.tango.ai/en/articles/17359491-where-does-tango-work) |
| PDF, Markdown, HTML exportieren | Pro, Ent | [Preise](https://www.tango.ai/pricing) |
| Tango MCP: KI-Assistenten (ChatGPT, Claude, Microsoft 365 Copilot, Cursor und andere) verbinden sich per Remote-MCP mit OAuth-Anmeldung | Ent | [MCP](https://help.tango.ai/en/articles/17890447-what-is-tango-mcp), [verbinden](https://help.tango.ai/en/articles/17890522-how-do-i-connect-tango-to-my-ai-assistant), [Updates](https://updates.tango.ai/) |

Vom MCP-Server bereitgestellte Tool-Liste: nicht verifiziert (Artikel nicht vollständig gelesen).

## Authentifizierung

- Nutzer: Anmeldung bei Tango (SSO bei Enterprise; [Preise](https://www.tango.ai/pricing)).
- MCP: OAuth-Anmeldung, laut Zusammenfassung des Verbindungsartikels.

## Nicht dokumentiert

Endpunkte, Parameter, Antwortformate, Fehlercodes, Paginierung: keine. Es gibt nichts, wogegen man implementieren könnte.
