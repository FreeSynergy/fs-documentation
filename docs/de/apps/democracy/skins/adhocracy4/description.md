# Adhocracy4 - Beschreibung

## Was das Programm macht

Adhocracy4 strukturiert kommunale Beteiligung in nachvollziehbaren Phasen-Modulen — vom Brainstorming über Sichtung bis zur Kiezkasse. Es ist das Framework hinter mehreren deutschen Stadtportalen und damit die pragmatische Mitte zwischen Decidims Formalismus und Consul Formatmix.

## Vorteile

- bewährt in Großstädten (Berlin, viele Kommunen im STADTLAND-Verbund)
- saubere REST-API für Auswertungs-Skins
- Geo-Fokus (Ideen auf Stadtplan) — natürliche Brücke zu Maps-Skins

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Decidim** | prozess-/komponenten-strenger; A4 Phasen-module |
| **Consul** | Formatkacheln + Polls; A4 Sichtung + Kiezkasse |
| **pol.is** | Massen-Deliberation; A4 kuratierte Projekte |

## Technische Details

- **Stack**: Python/Django, PostgreSQL, Leaflet-Karten
- **Auth**: Konten (kommunale Login-Verfahren andockbar)
- **Lizenz**: AGPL; Deploy: Django-Hosting/Docker
- **Wurzeln**: liqd (liquid democracy e.V.) → STADTLAND

## Für wen geeignet

- Kommunen, die Beteiligung mit Verwaltungs-Rückkopplung betreiben
- FreeSynergy-Skins: Ideen/Rating/Geo als Modell (→ [modelle.md](../../../../data/modelle.md) + [Standpunkte](../../../maps/standpunkte.md))
