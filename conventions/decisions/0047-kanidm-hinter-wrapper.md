# 0047 – Kanidm hinter eigenem Wrapper

Status: akzeptiert (2026-11-06) · ergänzt und schränkt ADR 0024 ein · Befunde: `temp/research/kanidm-control.md`

## Entscheidung (Nutzer)
- **Wir legen fest, was geschieht, und gleichen Kanidm an.** Kanidm ist per REST-API oder Client ferngesteuert.
- **Was Kanidm nicht kann, übernehmen wir.** Setzt Kanidm es später um, geben wir die Kontrolle zurück.
- PAM, RADIUS und Ähnliches sind Möglichkeiten, die in Betracht gezogen werden, keine Pflicht.
- RustFS wird ebenfalls stark genutzt, bleibt aber optional; die Zusammenarbeit wird gesucht.

## Umsetzung (nach Recherche, Quellcode 1.13.0-dev, nicht am laufenden System geprüft)
- REST v1 mit Service-Account-Token über einen eigenen schlanken Client. `kanidm_client`, an die Serverversion gebunden, nur
  für komplizierte Abläufe.
- **SCIM vorerst nicht**, entgegen ADR 0024: ausdrücklich instabil, allgemeines Anlegen wirkt defekt.
- Hierarchie, Art, Rollen, Einladungen liegen in `fs-groups` (Schlüssel: Gruppen-ID). Zyklen verhindern wir selbst.
- Ohne Kanidm laufen die Programme weiter (ADR 0024).
