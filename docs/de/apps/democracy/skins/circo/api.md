# Circo - API Dokumentation

## Übersicht

Circo publiziert **keine offene Entwickler-API**. Integrationen laufen über Ergebnis-Exporte und projektspezifische Vereinbarungen mit dem Anbieter. Diese Seite dokumentiert bewusst nur die gesicherten Austauschwege.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Exporte (CSV/PDF-Berichte) | Ergebnissicherung | offiziell |
| REST/Webhooks | — | ❌ öffentlich dokumentiert |
| Projektindividuelle Schnittstellen | SSO/Datenanbindung | nach Vereinbarung |
| GraphQL | — | ❌ |

## Praktischer Austauschweg

```
Circo-Projekt → Export-Bericht (CSV/PDF)
             → FreeSynergy-Import-Skript (Datensätze in Wiki-/Dokumente-Bereich)
             → Verweis auf Projektseite (Originalbezug erhalten)
```

## Feldhinweise (Export-Praxis)

- Beitrags-ID, Verfasser-Kennung ( pseudonymisiert je Projekt), Phase, Bewertungsaggregate
- Spaltenbenennung je Projekt gleich halten ([felder.md](../../../../data/felder.md))

## Skin-Hinweis

Als Skin-Muster gilt der **Export-Reader** (Import + Verlinkung), nicht Live-API; bei Beschaffung explizit Schnittstellen-Klausel verhandeln.
