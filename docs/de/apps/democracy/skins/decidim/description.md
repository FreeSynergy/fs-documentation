# Decidim - Beschreibung

## Was das Programm macht

Decidim strukturiert Beteiligungsprozesse so, wie Verwaltungen sie brauchen: klar abgegrenzte Prozesse, nachvollziehbare Phasen, Vorschläge mit Unterstützungen, Ergebnisse als Rechenschaftsberichte. Die Plattform trägt die formale Hülle der Beteiligung.

## Vorteile

- **institutionensicher** (Nachvollziehbarkeit, Moderation, Statistiken)
- GraphQL-API vorbildlich offen
- große Community, deutschsprachige Installationen verbreitet

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Consul** (Consulado) | ähnlicher Zweck, anderes Tech-Setup; Decidim prozess-strenger |
| **Liquid Feedback** | delegative Entscheidung innerhalb von Gruppen; Decidim Prozess-Bühne |
| **pol.is** | Massen-Deliberation (Meinungsspektrum); Decidim strukturierter Katalog |

## Technische Details

- **Stack**: Ruby on Rails, PostgreSQL; Module als Engines
- **Auth**: eigene Konten + Verifizierungs-Workflows (je Organisation konfigurierbar)
- **Lizenz**: AGPL; Deploy: Docker/Decidim-Zoom-Hosting-Angebote

## Für wen geeignet

- Kommunen/Verbände mit formalen Beteiligungsverfahren
- FreeSynergy-Skins: Prozess-/Komponentenmodell als Vorbild partizipativer Abläufe ([modelle.md](../../../../data/modelle.md) → Antrag/Support/Phase)
