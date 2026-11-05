# Outlook-Kalender – Dokumentation

Kalenderkomponente der Microsoft-Outlook-Linie: Web-App (outlook.com / Outlook on the web), neues und klassisches Outlook für Windows, Outlook für Mac und iOS/Android – Daten im Postfach von **Exchange Online**, Automatisierung über **Microsoft Graph v1.0** (REST/OAuth/OData). Markantes API-Merkmal im Serienvergleich: **echte Webhooks** (Graph change notifications) – und eine hart gezogene Protokollgrenze: **kein CalDAV**, EWS-Abschaltung in Exchange Online laufend (Okt 2026–Apr 2027).

- **Kategorie:** calendar (SaaS-Groupware-Oberfläche + proprietäre API)
- **Lizenz:** proprietär (Microsoft-Dienst; Clients teils mit Microsoft-365-Abo, Web-Apps für Privatkonten kostenfrei)
- **Aktuell dokumentierte Version:** Microsoft Graph **v1.0** (stabil) + beta; Client-Stand „neues Outlook für Windows“ / Outlook on the web, Prüfdatum **2026-11-02**
- **Entwicklungsstatus:** hochaktiv (Schrittveröffentlichungen; EWS→Graph-Migration erzwungen; Kalender-Sharing-Migration MAPI→REST 2026)

## Dateistruktur dieser Sektion

| Datei | Inhalt |
|-------|--------|
| [description.md](latest/description.md) | Was das Programm macht, Vorteile, Abgrenzung (u. a. zu Google Kalender, Nextcloud Calendar, Davical, Merkuro), technische Details, Für-wen-geeignet |
| [features.md](latest/features.md) | Verifizierte Funktionsliste + „Was Outlook-Kalender NICHT bietet“ |
| [api.md](latest/api.md) | Graph v1.0: Kalender-/Event-Endpunkte, Auth/Scopes, Webhooks, Limits, SDKs, EWS-Abschaltung |
| [menu.md](latest/menus.md) | Navigationsstruktur (neues Outlook, klassisches Outlook, Admin-Ebene) aus offiziellen Layout-Artikeln |
| [shortcuts.md](latest/shortcuts.md) | Offizielle Tastenkürzel (neues/klassisches Outlook, Web) + Direkt-Workflows |
| [structure.md](latest/layout.md) | Bauschichten, Datenmodell (changeKey/iCalUId/Serien), Konfiguration, Deployment |

## Quellen

Alle Aussagen vom offiziellen Quelltext der Doku-Seiten; Prüfdatum 2026-11-02. **Outlook ist Closed Source – Primärquelle sind daher die offiziellen API-/Hilfeseiten von Microsoft (nicht Quelltext-Dateien wie bei den Open-Source-Skins dieser Serie).**

1. **EWS-Deprecation (offiziell):** `https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-ews-exchange-online` – Timeline (2018/2023/Okt 2026/Apr 2027), Midnight Blizzard, Parity-Lücken, Tools.
2. **Graph calendar-Ressource:** `https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0` (Seite zuletzt aktualisiert **2026-10-15**, vollständig gelesen) – Methoden inkl. calendarView/delta/getSchedule/findMeetingTimes, Properties inkl. `calendarPermissions`-Assoziation, Gruppen-Grenzen.
3. **Graph event-Ressource:** `https://learn.microsoft.com/en-us/graph/api/resources/event?view=graph-rest-1.0` (Seite zuletzt aktualisiert 2025-05-15, vollständig gelesen) – Aktionen, Properties (iCalUId, seriesMasterId, cancelledOccurrences, changeKey, allowNewTimeProposals, webLink, recurrence/`type`, transactionId, sensitivity, onlineMeetingProvider), 500-Teilnehmer-Limit, ImmutableId, dokumentierte Deep-Link-Formate `…/calendar/item/{id}`.
4. **Graph Webhooks:** `https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks?view=graph-rest-1.0` – Zustellvertrag (3 s, 4 h Retry), slow/drop, Lifecycle, Event Hubs/Event Grid.
5. **Graph-Throttling:** `https://learn.microsoft.com/en-us/graph/throttling` – 429/Retry-After, Graph Data Connect.
6. **Graph-Outlook-API-Konzept:** `https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/office-365-rest-apis-for-mail-calendars-and-contacts` (Stand 2021-10-11) – OAuth2/OData/JSON.
7. **Tastenkürzel (offiziell):** `https://support.microsoft.com/en-us/accessibility/outlook/keyboard-shortcuts-for-outlook` – Tabs New Outlook / Classic Outlook / Web; Kalender-, Navigations-, VBA-Kürzel.
8. **Layout (offiziell):** `https://support.microsoft.com/en-us/accessibility/outlook/use-a-screen-reader-to-explore-and-navigate-outlook-calendar` – Regionen des neuen Outlook (Nav-Leiste, Ribbon, Navigationsfenster, Toolbar) und des klassischen Outlook (Folder pane, Ribbon, Statusleiste), Settings-Unterreiter.
9. **CalDAV-Grenze (offiziell):** `https://support.microsoft.com/en-us/outlook/sync-your-icloud-calendar-with-outlook-for-mac` – „Outlook for Mac doesn't support the CalDAV or CardDAV Internet standards“.
10. **Sekundärquellen (als solche gekennzeichnet):** techcommunity-Beitrag „Outlook for Windows: Timelines…“ (kostenlose Konten ab Jan 2025 kein Rückweg zum klassischen Outlook); office365itpros.com 2026-05 + admin365.blog 2026-07 (Kalender-Sharing MAPI→REST, Frist März 2027); petri.com/windowsforum (EAS ≥ 16.1 ab 2026).
11. **Graph-Berechtigungen (Nachtrag, verifiziert 2026-11-02):** `https://learn.microsoft.com/en-us/graph/permissions-reference` (Calendars-Abschnitt per Offset-Abruf) – Scopes `Calendars.Read/ReadBasic/ReadWrite` (App + delegiert), `.Shared` (delegiert, inkl. Delegaten/Freigaben), `.Read.All`/`.ReadWrite.All` (nur App, exklusiv Arbeitszeiten & Orte); delegierte Calendars-Scopes ausdrücklich mit **persönlichen Microsoft-Konten** konsentierbar; application access policy für Postfach-Eingrenzung.
12. **Nicht verifiziert (bewusst offengehalten):** Graph-„Service-specific limits"-Zahlen (Seite am Recherchetag 404); Protokoll-Abschaltungsdetails für kostenlose Outlook.com-Konten (Support-Seite nicht erreichbar); Mac-Kürzel; Consumer-Verfügbarkeit einzelner Komfort-Endpunkte (z. B. findMeetingTimes).

Wiederholungs-Rezept: Seiten 1–5+7–9 direkt abrufen (learn/support.microsoft.com sind ohne Login erreichbar; ältere /office/-Slugs von support.microsoft.com teils 404/403 – dann /accessibility/-Pfade verwenden); Permissions-Referenz ist ~495k Zeichen lang – Calendars-Abschnitt liegt bei Zeichenoffset ~56000–61000; Änderungen an EWS-Timeline und Graph-Ressourcenseiten mit dieser Doku abgleichen; Sekundärquellen auf neue Stände prüfen.
