# Notion — bekannte Grenzen (2026-11-07)

Nur Grenzen mit Quelle. Zahlen für andere als die genannten Tarife werden nicht angegeben.

## API

| Grenze | Wert | Quelle |
|--------|------|--------|
| Anfragen pro Verbindung | 180 pro Minute (die meisten Tarife); 600 pro Minute (Business, Enterprise) | [S2] |
| Datenquellen-Abfragen | etwa 3 pro Sekunde pro Verbindung | [S2] |
| Gemeinsame Grenze für den gesamten Arbeitsbereich | vorhanden; Wert nicht angegeben | [S2] |
| Blockkinder pro Anfrage | 100 | [S18, S20] |
| Blöcke pro Anfrage | 1000 | [S2] |
| Nutzlast pro Anfrage | 500 KB | [S2] |
| Rich-Text-Inhalt, URL | je 2000 Zeichen | [S2] |
| Gleichungsausdruck | 1000 Zeichen | [S2] |
| Mehrfachauswahl-Optionen pro Anfrage | 100 | [S2] |
| Relationen oder Personen pro Anfrage | 100 | [S2] |
| Paginierung der Ergebnisse | 10.000 Ergebnisse (Changelog 20. Apr.) | [S8] |
| Zu große Seitenbearbeitungen | HTTP 400 (Changelog 2. Okt., vorher 500) | [S8] |
| Blocklimits kostenloser Arbeitsbereiche gelten auch für die API | ja (Changelog 1. Sep.); Zahlen nicht angegeben | [S8] |
| Versionsunterstützung | `2022-06-28` und früher werden von SDK v5 und neuer nicht unterstützt | [S1] |

## Datenmodell

| Grenze | Quelle |
|--------|--------|
| Eine neue Seite kann nicht mit `block_id` als übergeordnetem Element erstellt werden | [S20] |
| Die Suche umfasst nur Seiten und Datenquellen, nicht alle Inhaltstypen | [S10] |
| Der Abruf einer Seite liefert keinen Blockinhalt | [S19] |
| Die Integration sieht nur Seiten, die mit ihr geteilt wurden (interne Integrationen) | [S3] |
| Ansichten: Sperren verhindert Änderungen an Eigenschaften und Ansichten, nicht an Daten | [S13] |

## Löschen und Verlauf

| Punkt | Wert | Quelle |
|-------|------|--------|
| Aufbewahrung im Papierkorb | 30 Tage, danach endgültiges Löschen | [S14] |
| Nach dem endgültigen Löschen | weitere 30 Tage erhalten, danach für alle verloren (Enterprise-Eigentümer können dies anpassen) | [S14] |
| Wiederherstellen | aus dem Papierkorb; eine im Papierkorb liegende Seite kann bis zur Wiederherstellung nicht bearbeitet werden | [S14] |
| Datenbank wiederherstellen | bringt Seiten und Eigenschaften zurück, nicht den Text darin | [S14] |
| Versionsverlauf | 7 Tage (Free), 30 (Plus), 90 (Business), beliebig lang (Enterprise) | [S14] |

## Plattform

| Punkt | Quelle |
|-------|--------|
| Kleiner Text und volle Breite: nur Desktop und Web | [S15] |
| Einstellungen zur Seitendiskussion auf dem Handy liegen unter "Customize page" | [S15] |
| Webhooks benötigen HTTPS und eine öffentliche URL | [S4] |

## Ungeprüft

- Funktionsgleichheit und Grenzen auf dem Handy.
- Blockanzahl-Grenze in kostenlosen Tarifen (auf den gelesenen Seiten nicht veröffentlicht).
- Maximale `page_size` für Listen-Endpunkte.
