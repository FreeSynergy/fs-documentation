# Marketplace — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Marketplace` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Arcemall](arcemall/index.md) | [latest](arcemall/latest/description.md) | Arcemall ist eine Low-Code-Plattform für eigene Marktplätze (Open-Source-Ansatz): Marktplatz-Modelle (Produkte/Dienstleistungen, Buchungen, Zahlungen, Suche/Karte) werden mit Own-Code-Bausteinen un… |
| [CS-Cart Multi-Vendor](cs-cart-multivendor/index.md) | [latest](cs-cart-multivendor/latest/description.md) | CS-Cart Multi-Vendor (kommerzielle Software, PHP) verwandelt einen Shop in einen Marktplatz mit vielen Anbieter:innen: Produkte, Lager, Versand, Zahlungs-Gateways, Anbieter-Provisionen, Admin-Konso… |
| [eBay](ebay/index.md) | [latest](ebay/latest/description.md) | eBay ist der globale Marktplatz für C2C/B2C mit Auktions- und Festpreisformaten. |
| [Etsy](etsy/index.md) | [latest](etsy/latest/description.md) | Etsy (börsgelistet) ist der Kuratierungs-Marktplatz für Handgemachtes, Vintage und Design mit digitalen Produkten. |
| [Kleinanzeigen](kleinanzeigen/index.md) | [latest](kleinanzeigen/latest/description.md) | Kleinanzeigen (ehem. eBay Kleinanzeigen, Nowint/AVENUE A) ist der größte regionale Kleinanzeigen-Marktplatz in Deutschland: Private und gewerbliche Anbieter inserieren Anzeigen mit Ortsbezug, Kommu… |
| [Sharetribe](sharetribe/index.md) | [latest](sharetribe/latest/description.md) | Sharetribe ist die führende Marktplatz-Software: Open-Source (Marktplatz zum Selbstbauen, Ruby on Rails — „Sharetribe Flex“: API-first mit Web App/Marketplace Console) sowie SaaS-Versionen (Sharetr… |

## Dateisatz pro Programm (ADR 0012)

```
programs/suites/marketplace/frontends/<program>/
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
