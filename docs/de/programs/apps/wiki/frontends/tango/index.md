# Tango

> Kategorie: [Wiki](../../index.md)

## Was es ist

Tango macht aufgezeichnete Klicks zu Schritt-für-Schritt-Anleitungen; kein Wiki, dokumentiert wegen seiner Idee von der Aufnahme zur Anleitung.

Es ist ein Produkt für Prozessdokumentation und Anleitungen innerhalb der Anwendung. Es ist kein allgemeines Wiki und keine Wissensdatenbank. Das eigene Hilfezentrum beschreibt Tango als Werkzeug „for documenting processes“ mit Guide Me, Pins, einem KI-Agenten, Arbeitsbereichen und den Tarifen Free, Pro, Enterprise ([Hilfezentrum, llms.txt](https://help.tango.ai/llms.txt)).

## Identitätsprüfung: tango.io ist nicht dieses Produkt

- `tango.io` zeigt eine Seite eines Dienstleistungsunternehmens namens „Tango“ (Produktentwicklung, KI-Pilotprojekte, Staff Augmentation; „© 2026 Tango“). Sie beschreibt kein Produkt zur Aufnahme oder für Anleitungen ([tango.io](https://tango.io/)).
- Das Produkt liegt unter `tango.ai` (Hilfezentrum `help.tango.ai`). Drittanbieter-Einträge zeigen auch den älteren Namen „tango.us“ ([TrustRadius-Vergleich](https://www.trustradius.com/compare-products/stack-overflow-for-teams-vs-tango.us)). Der Update-Feed des Anbieters kündigt eine Umbenennung am 2026-09-30 an ([Updates](https://updates.tango.ai/)); der Inhalt der Umbenennung wurde nicht gelesen.
- Andere Produkte namens „Tango“ (Tango Card Prämien-API, Tango Analytics Immobilienplattform, eine Bundes-Datenschnittstelle) sind nicht verwandt.

## Bemerkenswerte Ideen (verifiziert)

- **Von der Aufnahme zur Anleitung.** Der Nutzer arbeitet ganz normal in der Anwendung. Die Browser-Erweiterung zeichnet jeden Klick als Schritt auf und erzeugt automatisch Screenshot, Hervorhebung und Beschreibung ([Aufnahme starten](https://help.tango.ai/en/articles/5971654-how-do-i-start-capturing-a-workflow), [Anleitung zur Dokumentation](https://help.tango.ai/en/articles/7966907-how-do-i-use-tango-for-documentation)).
- **Sprachtranskription** kann Schritttitel und Beschreibungen während der Aufnahme schreiben (nur Browser-Aufnahme, laut [Wo es funktioniert](https://help.tango.ai/en/articles/17359491-where-does-tango-work)). Tarifbindung: siehe [Funktionen](latest/features.md).
- **Dieselbe Anleitung, mehrere Betrachter.** Eine Anleitung wird als scrollbare Link-Ansicht, als Einbettungs-Diashow, als interaktiver Durchlauf „Guide Me“ in der laufenden Anwendung oder als Export gezeigt ([Anleitung zur Dokumentation](https://help.tango.ai/en/articles/7966907-how-do-i-use-tango-for-documentation)).
- **Guide Me und Pins** zeigen Hinweise in der laufenden Web-Anwendung. Enterprise listet „Pins, Guide Me, and Automations“ ([Preise](https://www.tango.ai/pricing)).
- **Mehrpfad-Workflows** (Verzweigungen) lassen eine Anleitung mehrere gültige Pfade abdecken ([Verzweigung](https://help.tango.ai/en/articles/14063444-how-does-branching-work-in-tango)). Nur Enterprise laut [Preise](https://www.tango.ai/pricing).
- **Schwärzung bei der Aufnahme.** Live Blur blendet Elemente während der Aufnahme aus; Secure Blur und eigene Schwärzungen sind Enterprise ([Secure Blur](https://help.tango.ai/en/articles/7225709-how-to-use-secure-blur)).
- **Auslieferung an KI-Assistenten.** Tango MCP lässt einen KI-Assistenten aus den Anleitungen eines Teams antworten. Seit 2026-11-04 auf Enterprise verfügbar ([Updates](https://updates.tango.ai/), [MCP](https://help.tango.ai/en/collections/19799192-tango-mcp)).

## Versionsangaben

Der Anbieter veröffentlicht für das Web-Produkt keine Versionsnummer. Die Dokumentation hier ist `latest/` = Stand, wie am 2026-11-07 gesehen. Der Anbieter nennt außerdem eine **Tango Desktop 2.0**-App ([Hilfezentrum](https://help.tango.ai/llms.txt), [Desktop-Sammlung](https://help.tango.ai/en/collections/3462416-desktop)).

| Version | Stand | Dateien |
|---|---|---|
| [latest](latest/description.md) | 2026-11-07 | Beschreibung, Funktionen, Layout, Menüs, Tastenkürzel, API, Themes, Grenzen, Abhängigkeiten |

Keine changelog.md: nur eine Version ist dokumentiert.

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Vorhandene Pflichtdateien |
|---------|------------------------|
| [latest](latest/description.md) | 7/7 |
<!-- /gen:versions -->

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen es passt |
| [features.md](latest/features.md) | Was das Programm kann – und was nicht |
| [layout.md](latest/layout.md) | Fensteraufbau, Bereiche, Panels |
| [menus.md](latest/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](latest/shortcuts.md) | Tastenkürzel |
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Ratenlimits |
| [themes/index.md](latest/themes/index.md) | Themes: Farben, Typografie, Abstände – was nachgebaut werden kann |
| [limits.md](latest/limits.md) | Bekannte Einschränkungen |
| [dependencies.md](latest/dependencies.md) | Welche unserer Komponenten ein Frontend in diesem Stil braucht |

## Quellen

- Hilfezentrum: https://help.tango.ai/en/
- Preise: https://www.tango.ai/pricing
- Produktseite: https://www.tango.ai/product/create
- Update-Feed: https://updates.tango.ai/
- Weitere Artikel: jeweils inline in den einzelnen Dateien zitiert.
