# Surveys — Anforderungen

Was `FreeSynergy.Surveys` muss und kann.

**Vorläufig (2026-11-06).** Für diese Kategorie wurden keine Frontends analysiert, daher hat nichts hier die übliche Regel bestanden (ADR 0006, 0013). Alles stammt aus unserer Architektur (*Arch.*) oder ist allgemeines Wissen über solche Programme (⚠️) und muss vor dem Schreiben des Vertrags gegen analysierte Programme geprüft werden.

Status: `implemented` · `planned` · `proposed`

## Erforderlich

| Fähigkeit | Grundlage | Daten / Standard | Status |
|-----------|-----------|------------------|--------|
| Eine Umfrage anlegen und bearbeiten (`survey.create`, `survey.edit`) | ⚠️ | AS2 `Collection` + eigenes Profil | Vorschlag |
| Fragen hinzufügen, bearbeiten, sortieren (`question.add`, `question.edit`, `question.move`) | ⚠️ | AS2 `Question`; darüber hinaus Lücke | Vorschlag |
| Fragetypen: Einzel-, Mehrfachauswahl, Text, Zahl, Datum, Skala (`question.types`) | ⚠️ | `oneOf`, `anyOf`; Rest Lücke | Vorschlag |
| Pflichtfragen und Validierung (`question.validate`) | ⚠️ | Lücke | Vorschlag |
| Veröffentlichen, schließen, wieder öffnen (`survey.publish`, `survey.close`) | ⚠️ | AS2 `closed` | Vorschlag |
| Die Anonymitätsstufe wählen und den Befragten zeigen (`survey.anonymity`) | *Arch.* ([Design](design.md#anonymitat)) | Lücke | Vorschlag |
| Personen einladen (`survey.invite`) | ⚠️ | Kontakte, Messenger | Vorschlag |
| Öffnen, antworten, speichern und fortsetzen, absenden (`survey.open`, `response.save`, `response.submit`) | ⚠️ | Lücke | Vorschlag |
| Ergebnisse als Summen und Diagramme sehen (`result.summary`) | ⚠️ | abgeleitet | Vorschlag |
| Ergebnisse exportieren (`result.export`) | ⚠️ | CSV ⚠️; DDI ⚠️ | Vorschlag |
| Sensible Umfragen und Antworten markieren (`survey.classify`) | *Arch.* (ADR 0029) | DPV | Vorschlag |
| Eine Abstimmung in einem anderen Programm einbetten (`poll.embed`) | *Arch.* (ADR 0037) | AS2 `Question` | Vorschlag |
| Über Änderungen benachrichtigen (`subscribe`) | *Arch.* (ADR 0021) | AS2-Aktivitäten | Vorschlag |

## Optional

| Fähigkeit | Grundlage | Daten / Standard | Status |
|-----------|-----------|------------------|--------|
| Sprungregeln (`logic.set`) | ⚠️ | Lücke | Vorschlag |
| Matrix- und Rangfragen (`question.types`) | ⚠️ | Lücke | Vorschlag |
| Eine Antwort je Person bei Anonymität (`survey.tokens`) | *Arch.* | Lücke | Vorschlag |
| Öffentlicher Link für alle (`survey.publicLink`) | ⚠️ | Lücke | Vorschlag |
| Terminabstimmung, Ergebnis geht in den Kalender (`poll.date`) | ⚠️ | JSCalendar `Event` | Vorschlag |
| Vorlagen und eine Fragensammlung (`template.use`) | ⚠️ | Wiki-Vorlagen (ADR 0031) | Vorschlag |
| Ergebnisse filtern und kreuzweise auswerten (`result.filter`) | ⚠️ | abgeleitet | Vorschlag |
| Übersetzte Umfragen (`survey.translate`) | ⚠️ | AS2 `nameMap` | Vorschlag |
| Föderierte Abstimmung an andere Server (`poll.federate`) | *Arch.* | AS2 `Question`, ActivityPub | Vorschlag |

## Nicht geplant (bewusst)

- Bindende Wahlen: Sie brauchen deutlich stärkere Garantien und gehören zur Demokratie-Suite.
- Verfolgen von Befragten (Werbung, Geräte-Fingerprints): widerspricht dem Zweck des Programms.
- Automatische Auswertung der Antworten durch externe Dienste: Antworten dürfen das Programm nicht verlassen.
