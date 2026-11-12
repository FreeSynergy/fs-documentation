# History — Anforderungen

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

Was `FreeSynergy.History` muss und kann, abgeleitet aus den [Frontends](frontends/index.md)
(ADR 0006, 0013). Jede Fähigkeit nennt ihren Datenstandard (ADR 0014) und unseren Stand.

Stand: `implemented` · `planned` · `proposed`

## Pflicht (gemeinsam in den analysierten Programmen)

| Fähigkeit | Gesehen in | Daten / Standard | Stand |
|------------|-------------|------------------|-------|

## Kür (bemerkenswerte Ideen)

| Fähigkeit | Gesehen in | Daten / Standard | Stand |
|------------|-------------|------------------|-------|
| Ort und Wetter zu einem Eintrag erfasst | Day One | Ort (GeoJSON), Wetter als einfache Felder | proposed |
| "An diesem Tag": Ereignisse desselben Datums aus früheren Jahren zeigen | Day One | Zeitleisten-Abfrage nach Datum | proposed |
| Automatische Erfassung von Aktivität, Rohereignisse bleiben erhalten, Zusammenfassungen auf Abruf | ActivityWatch | Ereignis-Buckets (JSON, Zeit nach RFC 3339) | proposed |
| Kategorisierungsregeln, die nach der Erfassung angewendet werden | ActivityWatch | Regelliste (reguläre Ausdrücke) | proposed |
| Import von Ereignissen anderer Programme über eine lokale Schnittstelle | ActivityWatch | HTTP/JSON, OpenTelemetry als Kandidat | proposed |
| Zusammenhänge zwischen unabhängigen Datenreihen | Exist.io | numerische Reihe je Tag | proposed |
| Wochenzusammenfassung | Exist.io | Digest | proposed |
| Doppelte Einträge einer Person vorschlagen und einzeln oder alle auf einmal zusammenführen; das Zusammenführen ist rückgängig machbar (`contact.mergeSuggest`, `contact.merge`) | Google Historys (Merge & fix); Apple Historys (merge or hide duplicates) | JSHistory RFC 9553 (das Ergebnis der Zusammenführung ist eine neue Kartenversion); Verlauf über AS2 `Update` | proposed |
| Eigene Kontaktdaten persönlich austauschen, mit Auswahl, welche Felder hinausgehen; nur Empfang möglich; überschreibt nie stillschweigend einen bestehenden Kontakt (`contact.shareNearby`) | Apple Historys (NameDrop) | JSHistory-Teilmenge der eigenen Karte; Übertragung offen (ADR 0059 lokaler Transport) ⚠️ | proposed |
| Adressen von Personen, an die nur geschrieben wurde, getrennt vom Adressbuch aufbewahren, bis sie übernommen werden (`contact.promote`) | Google Historys (Other contacts) | JSHistory `kind`, Herstellereigenschaft `freesynergy.net:known` ⚠️ | proposed |
| Änderungsverlauf eines Kontakts mit Rückgängig (`contact.history`) | Google Historys (History) | AS2-`Update`-Protokoll; Datenbereich für den Verlauf noch nicht definiert ⚠️ | proposed |
| Erinnern, wieder Kontakt aufzunehmen; zeigen, wann man zuletzt mit einer Person gesprochen hat (`contact.keepInTouch`) | Monica (Erinnerungen, "last spoke") | JSCalendar `Task` / Alarm; letzter Kontakt aus dem Nachrichten- und Ereignisprotokoll abgeleitet | proposed |
| Lebensereignisse und Meilensteine einer Person festhalten (`contact.lifeEvent`) | Monica | JSCalendar `Event`, verknüpft über `relatedTo` ⚠️ | proposed |

## Nicht geplant (bewusst)
</content>
