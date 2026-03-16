# Search — Die Suche

[← Zurück zum Index](../../INDEX.md)

---

## Suchebenen

Die Suche arbeitet in Schichten:

### Ebene 1: Service-Suche (lokal)
Jeder Service kennt seine Datenstruktur am besten und durchsucht seine eigenen Daten. Forgejo durchsucht Repos, Outline durchsucht Wiki-Seiten, Vikunja durchsucht Aufgaben.

### Ebene 2: Host-Suche (Bus-aggregiert)
Der [Message Bus](../../konzepte/bus.md) leitet die Suchanfrage an alle lokalen Services weiter, sammelt die Ergebnisse und **führt sie zusammen**. Die Ergebnisse werden normalisiert und dedupliziert.

### Ebene 3: Projekt-Suche
Wenn ein Projekt mehrere Hosts hat, werden die Host-Ergebnisse zusammengeführt.

### Ebene 4: Föderale Suche
Die [Föderation](../../konzepte/foederation.md) leitet die Suche an alle Mitglieder weiter — aber NUR an Services mit `search`-Recht. Ergebnisse werden wieder zusammengeführt.

## Ergebnis-Abstraktion

Die Suche ist nutzlos wenn man vor Ergebnissen zugeballert wird. Deshalb:
- Ergebnisse werden nach Relevanz sortiert
- Gruppiert nach Service-Typ (Wiki-Ergebnisse zusammen, Chat-Ergebnisse zusammen)
- Mit Preview (Titel + Kurztext + Link zum Original)
- Mit Quelle (welcher Service, welcher Host, welches Projekt)

## Search als Service

Search kann als eigenständiger Service installiert werden wenn das System die Kapazität hat einen eigenen Suchindex aufzubauen. Ist optional — ohne funktioniert die Suche trotzdem über die Service-APIs.

---

Weiter: [Bus](../../konzepte/bus.md) | [Föderation](../../konzepte/foederation.md)
