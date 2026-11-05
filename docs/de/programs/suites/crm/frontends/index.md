# Crm — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Crm` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [CiviCRM](civicrm/index.md) | [latest](civicrm/latest/description.md) | CiviCRM ist das offene CRM für Verbände, NGOs und Vereine („Constituent Relationship Management“): Kontakte, Spenden, Mitgliedschaften, Veranstaltungen, Kampagnen und Fälle — eingebettet in ein CMS… |
| [EspoCRM](espocrm/index.md) | [latest](espocrm/latest/description.md) | EspoCRM ist ein schlankes, schnelles Open-Source-CRM (PHP + Backbone/JS, SPA): Leads, Opportunities, Accounts, Kontakte und Aktivitäten — mit grafischem Entity-Manager, Workflows und sauberer REST-… |
| [HubSpot](hubspot/index.md) | [latest](hubspot/latest/description.md) | HubSpot ist die Marketing-first-CRM-Suite (SaaS): freies CRM (Kontakte, Firmen, Deals, Tickets) plus kostenpflichtige Hubs für Marketing (E-Mail, Kampagnen, Landing Pages), Sales (Sequenzen, Pipeli… |
| [Pipedrive](pipedrive/index.md) | [latest](pipedrive/latest/description.md) | Pipedrive ist ein cloud-basiertes Sales-CRM, das um die Vertriebspipeline strukturiert ist: Deals wandern in Spalten (Stages) von der Qualifizierung bis zum Abschluss, ergänzt um Leads, Kontakte, F… |
| [Salesforce](salesforce/index.md) | [latest](salesforce/latest/description.md) | Salesforce ist die führende kommerzielle CRM-Plattform (SaaS): Leads, Accounts, Contacts, Opportunities und Dutzende Clouds (Service, Marketing, Commerce, Analytics) auf einem modellierbaren Datenk… |
| [SuiteCRM](suitecrm/index.md) | [latest](suitecrm/latest/description.md) | SuiteCRM ist ein quelloffenes CRM (AGPL-3.0), das 2013 als Fork der offenen SugarCRM-Suite entstand und heute von der Community um SalesAgility weiterentwickelt wird. |

## Dateisatz pro Programm (ADR 0012)

```
programs/suites/crm/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
