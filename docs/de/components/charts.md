# Diagramme

**Status: Vorschlag (2026-11-06).** Diagramme sind Komponenten, die Umfragen, Projektmanagement, ERP und mehr brauchen. Wir listen alle auf, ohne zu sagen, dass wir alle bauen. Die Schnittstelle soll ein Standard sein, damit Diagramme Plugins sein können.

[Vollständiger Katalog](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/charts-catalogue.md): rund 235 Diagrammtypen, sortiert nach der Frage, die sie beantworten, jeweils mit der Datenform, die sie brauchen, und einer Priorität.

## Priorität A, nach Zweck

| Zweck | Diagramme |
|-------|-----------|
| Vergleichen | Säulen-, Balken-, gruppiertes und gestapeltes Balkendiagramm, 100-%-gestapeltes Balkendiagramm, Bullet, divergierender Balken |
| Veränderung über die Zeit | Linie, Fläche, gestapelte Fläche, Sparkline |
| Teil eines Ganzen | Kreis, Donut |
| Verteilung | Histogramm, Boxplot |
| Beziehung | Streudiagramm, Heatmap |
| Projekt | Gantt, Meilensteine, Burn-down und Burn-up, Ressourcenauslastung, Risikomatrix |
| Entscheidungen | Parlamentsdiagramm, Rangwahl-Runden, Widerstandsbalken, Likert-divergierender Balken, Heatmap der Matrix, Quorum-Anzeige |
| Status | KPI-Karte, Tachoanzeige, Fortschrittsring, Rot-Gelb-Grün-Status |
| Geld | Wasserfall, Budget gegen Ist, S-Kurve, Altersstufen |

## Was Blinc hat

Linie, Fläche, Balken (gestapelt und horizontal), Sparkline, Schwellenlinie, Histogramm, Vergleichsbalken, Kreis und Donut.

Zwei Lücken: [unsere Seite zur Diagramm-Komponente](widgets/data/chart/description.md) nennt Streudiagramm, Heatmap und Radar, die Blinc nicht hat, und der Diagrammcode von Blinc hat keine Textalternative und keine ARIA-Unterstützung, die unsere Dokumentation verlangt. Beides sind Kandidaten für einen Beitrag zu Blinc.

## Schnittstellen-Vorschlag

- **Basis-Vokabular: eine geprüfte Teilmenge von Vega-Lite** (BSD-3-Clause), die Daten und Darstellung trennt.
- **Eigenes Register für das, was fehlt,** etwa Gantt, Tachoanzeige, Parlamentsdiagramm und KPI-Karte.
- **Ein verpflichtender Barrierefreiheits-Block,** damit jedes Diagramm eine Beschreibung hat.
- **Unser eigener Rust-Interpreter,** da die vorhandenen Rust-Optionen eine JavaScript-Engine einbetten.
- **Als Plugins:** Ein Diagramm gibt eine Szenenbeschreibung zurück, und der Host zeichnet sie. Siehe [Plugin-Form](../interfaces/index.md#plugin-form).

Das wurde noch nicht ausprobiert oder gemessen.
