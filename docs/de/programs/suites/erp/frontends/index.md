# Erp — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Erp` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Axelor](axelor/index.md) | [latest](axelor/latest/description.md) | Axelor Open Suite (AGPL, Java) verbindet ERP (CRM, Sales, Purchasing, Stock, Manufacturing, Account, HR, Project) mit Low-Code/BPM: Masken, Modelle und Workflows werden im „App Builder“ modelliert;… |
| [Dolibarr](dolibarr/index.md) | [latest](dolibarr/latest/description.md) | Dolibarr (GPL, PHP) ist das schlanke KMU-ERP/CRM: Dritte, Angebote/Bestellungen, Rechnungen, Lager, Projekte, Basis-Buchhaltung — einfach zu hosten (LAMP), stabiler Funktionskern, Extension-Markt. |
| [ERPNext](erpnext/index.md) | [latest](erpnext/latest/description.md) | ERPNext (GPLv3) ist das vollständige Open-Source-ERP auf dem Frappe-Framework (Python/MariaDB): Accounting, Inventory, Buying/Selling, HR, Manufacturing, Projects — komplett ohne Lizenzkosten, mit … |
| [Odoo](odoo/index.md) | [latest](odoo/latest/description.md) | Odoo ist die offene Business-Suite (LGPL-Core + kommerzielle Enterprise-Apps): CRM, Vertrieb, Einkauf, Lager, Fertigung, Buchhaltung, Projekte, HR — als integrierte Module mit gemeinsamer ORM-Schicht. |
| [Sage](sage/index.md) | [latest](sage/latest/description.md) | „Sage“ ist ein kommerzieller Suite-Verbund (Sage Group) für Rechnungswesen/ERP: Sage Business Cloud (SaaS-Buchhaltung, z.B. |
| [Tryton](tryton/index.md) | [latest](tryton/latest/description.md) | Tryton (GPL, Python) ist das ruhige, modulare ERP für technische Anwender: Module für Buchhaltung, Vertrieb, Einkauf, Lager, Projekte, Zeiterfassung — mit starker Datenintegrität, Desktop-Client (G… |

## Dateisatz pro Programm (ADR 0012)

```
programs/suites/erp/frontends/<program>/
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
