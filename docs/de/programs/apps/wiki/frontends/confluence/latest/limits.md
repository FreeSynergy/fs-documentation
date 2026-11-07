# Confluence (Cloud, latest) · Grenzwerte

Quellen: S-Nummern verweisen auf [index.md](../index.md). Nur geprüfte Angaben werden als Fakten aufgeführt. Nicht recherchierte Punkte sind als "nicht recherchiert" markiert.

## API

| Grenzwert | Wert | Quelle |
|-----------|------|--------|
| REST-Kontingent | 65.000 Punkte pro Stunde (globaler Pool, Standard); pro Mandant nach Prüfung | [S5] |
| REST-Burst | Eigene Grenzwerte pro Sekunde; zusätzlich bei Permissions, Search, Admin | [S5] |
| GraphQL | 10.000 Punkte pro Währung pro Minute und Benutzer | [S8] |
| Antwort bei Ratenbegrenzung | HTTP 429, gesamte Anfrage wird abgelehnt | [S5][S8] |
| Wiederholung | `Retry-After` verwenden; nur idempotente Anfragen wiederholen | [S5] |
| Paginierung | v2 Cursor; v1 Offset | [S1][S2] |
| Veröffentlichungsfreigabe | REST-Seitenaktualisierung liefert HTTP 409 in Bereichen, die eine Freigabe verlangen (angekündigt 2026-09-28; Einführungsdatum nicht angekündigt) | [S9] |
| v1-Einschränkungen | Aktualisierung von v1-Inhaltsbeschränkungen erfordert jetzt Leserechte (Änderung vom 2026-10-15) | [S9] |

## Export

| Grenzwert | Quelle |
|-----------|--------|
| Nur veröffentlichte Inhalte werden exportiert | [S16] |
| Word-Export lässt sich nur in Microsoft Word öffnen | [S16] |
| PDF-Bereichsexport schließt Kommentare aus; Blogs sind vom PDF- und HTML-Bereichsexport ausgeschlossen; Team-Kalender sind von allen Bereichsexporten ausgeschlossen | [S16] |
| Organisationsadministratoren können Exporte pro Produkt oder Klassifizierungsstufe sperren | [S16] |
| Große Exporte: "100 Seiten exportieren" sollte in wenigen Minuten abgeschlossen sein; große Aufträge aufteilen | [S16] |
| Obergrenze für Bilder beim Word-Export (frühere Fassung: 50 Bilder) | Ungeprüft; nur ein Community-Beitrag erwähnt es |

## Plattform

| Punkt | Status |
|-------|--------|
| Maximale Seitengröße, Anhangsgröße, Anzahl der Bereiche, Anzahl der gespeicherten Versionen | Nicht recherchiert |
| Connect-Apps können nicht mehr im Marketplace veröffentlicht werden | [S11] |
| Neue Connect-Funktionen | Nur Forge [S11] |
| Beta-Felder in GraphQL können ohne Ankündigung geändert werden | [S8] |

## Data Center

| Punkt | Quelle |
|-------|--------|
| Ende der Lebensdauer 2029-03-28 (Lizenzen nur zum Lesen); neue Abonnements enden 2028-03-30 für bestehende Kunden | [S20] |
