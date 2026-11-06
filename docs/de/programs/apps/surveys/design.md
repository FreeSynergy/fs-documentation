# Surveys — Design

**Status: Vorschlag (2026-11-06).** Zurück zum [Gesamtplan](../roadmap.md) · [Anforderungen](requirements.md).

## Idee

Eine Umfrage ist eine Folge von Fragen, eine Menge von Antworten und eine Auswertung. Eine schnelle Abstimmung im Messenger ist dasselbe mit einer einzigen Frage; deshalb erscheinen Umfragen innerhalb anderer Programme als kompakte Workbench (ADR 0037).

## Daten

| Teil | Standard | Nachweis | Hinweise |
|------|----------|----------|----------|
| Einfrage-Abstimmung | AS2 `Question` mit `oneOf`, `anyOf`, `closed` | ✅ gelesen 2026-11-06 | Föderiert direkt, kennt aber nur Einzel- und Mehrfachauswahl |
| Umfrage | AS2 `Collection` (geordnet) von Fragen | ✅ Typ existiert | So zu verwenden ist unsere Entscheidung |
| Skalen, Matrix, Rangfolge, Sprungregeln, Validierung | ❌ nicht in AS2 | | **Eigenes Profil**, siehe unten |
| Antwort | Lücke | | Muss [Anonymität](#anonymitat) unterstützen, kann also nicht einfach `actor` tragen |
| Referenzvokabular | DDI, FHIR `Questionnaire` | ⚠️ Existenz gesehen, nicht untersucht | Kandidaten für Import und Export |
| Test- und Prüfungsformate | QTI | ⚠️ nicht geprüft | Tests liegen außerhalb des ersten Umfangs |

**Richtung aus der Recherche:** AS2 `Question` als äußere Form, bereits von Mastodon für Abstimmungen genutzt. FHIR `Questionnaire` als Modell für typisierte Elemente und Bedingungen. DDI ist Metadaten für Archive und QTI ist für bewertete Prüfungen, daher ist keines von beiden eine Grundlage. Beide wurden nur teilweise gelesen, daher ist eine genauere Prüfung nötig.

## Anonymität

Das ist der Kern des Programms. Menschen antworten nur ehrlich, wenn sie dem Versprechen vertrauen.

| Stufe | Versprechen | Umsetzung |
|-------|-------------|-----------|
| **Namentlich** | Der Veranstalter sieht, wer was geantwortet hat | Die Antwort trägt den `actor` |
| **Anonym, offen** | Niemand weiß, wer geantwortet hat; mehrere Antworten einer Person sind möglich | Gar keine Identität wird gespeichert |
| **Anonym, eine Antwort je Person** | Eine Antwort je eingeladener Person; Antworten lassen sich nicht auf sie zurückführen | Schwer; siehe unten |
| **Vollständig offen** | Jeder, ohne Konto | Siehe [offene Umfragen](#offene-umfragen-ohne-anmeldung) |
| **Bindende Abstimmung** | Überprüfbar, widerstandsfähig gegen Nötigung | Braucht deutlich stärkere Garantien; im Rahmen der [Demokratie-Suite](../../suites/democracy/index.md) zu behandeln |

Die dritte Stufe ist die schwierige. Ein einfaches Token-Modell (ein Token je Einladung, getrennt von den Antworten gespeichert) ist leicht zu bauen, aber der Betreiber könnte beides verbinden, und das muss ehrlich gesagt werden. Stärkere Garantien brauchen Kryptografie wie Blind Signatures, was eine Prüfung durch Fachleute erfordert. **Wir schlagen vor, mit dem Token-Modell zu beginnen und seine Grenze in der Schnittstelle klar zu benennen,** ohne es als vollständig anonym zu bezeichnen.

Weitere Risiken, die zu behandeln sind:

- Timing: Wird der Zeitpunkt einer Antwort gespeichert, kann er eine Person identifizieren; Zeiten werden daher vergröbert oder weggelassen.
- Kleine Gruppen: Ergebnisse mit wenigen Antworten können Menschen identifizieren; eine Mindestgruppengröße verbirgt sie.
- Freitext kann seinen Verfasser verraten, und die Schnittstelle sagt das.
- Antworten können sensible Daten sein (ADR 0029): Gesundheit, Politik, Glaube.

## Offene Umfragen ohne Anmeldung

**Eine Umfrage kann vollständig offen sein, ganz ohne Konto.** Trotzdem darf eine Partei nicht eine Million Antworten abgeben können.

Aus der [Recherche](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/surveys-landscape.md): Nichts bietet „eine Person, eine Antwort, keine Identität, kein Dritter“ bei einem vollständig offenen Link. Schichten lassen sich ohne Dritten kombinieren: adaptive Proof of Work, globale Ratenbegrenzungen, eine Gerätemarkierung, Qualitätsbewertung mit einer Prüfwarteschlange und die Anzeige von „alle Antworten“ neben „geprüften Antworten“. Die Schnittstelle benennt, welcher Schutz gilt. Privacy Pass (RFC 9576) ist ein Standard für den privaten Nachweis eines echten Geräts, aber heute stellen nur Plattformanbieter die Token aus.

## Entscheidungsarten

Nicht nur Mehrheit. Jede Methode ist eine austauschbare Strategie, und dieselben Stimmzettel lassen sich nach mehreren Methoden zeigen: Kein Werkzeug, das wir gefunden haben, bietet das.

Mehrheit, qualifizierte Mehrheit, Zustimmung (Approval), Bewertung (Score), Rangmethoden (Schulze, Instant-Runoff, Borda), quadratische Abstimmung, Konsens, Zustimmung im Sinne der Soziokratie, systemisches Konsensieren (Widerstand von 0 bis 10, mit der Option „weiter wie bisher“; kein Open-Source-Werkzeug gefunden), Delegation und deliberative Clusterung. Jede kommt mit einem passenden [Diagramm](../../../components/charts.md).

## Ausweitung auf übergeordnete Gruppen

Eine Umfrage kann klein beginnen und, wenn sie wichtig ist, auf übergeordnete Gruppen in [`fs-groups`](../../platform/groups.md) ausgeweitet werden. Sie bleibt eine einzige Umfrage, frühere Ergebnisse werden übernommen, und die Anonymität kann unterwegs nie schwächer werden. **Wir haben kein Werkzeug gefunden, das das tut.** Consul kommt in einer Hinsicht nahe: Ein Vorschlag, der genug Unterstützung findet, geht in eine Abstimmung über. Ob es sich auch zwischen Ebenen einer Hierarchie bewegen kann, wurde nicht bestätigt.

## Muster

| Muster | Verwendung |
|--------|------------|
| Strategy | `AnonymityPolicy` je Stufe; eine `Evaluation` je Fragetyp |
| Registry | Fragetypen, die Frontends und Plugins erweitern können |
| State | `draft` → `open` → `closed` → `archived` |
| Interpreter | Sprungregeln und Validierung als kleines Ausdrucksmodell |
| Repository | `SurveyRepository`, `ResponseRepository` |

## Schnittstellen-Skizze

| Schnittstelle | Fähigkeiten |
|---------------|-------------|
| `Surveys` (Wurzel) | `capabilities()`, gibt die anderen heraus |
| `Designer` | `survey.create`, `question.add`, `question.edit`, `question.move`, `logic.set`, `survey.publish`, `survey.close` |
| `Respond` | `survey.open`, `response.save`, `response.submit` |
| `Results` | `result.summary`, `result.filter`, `result.export` |
| `subscribe` | Neue Antworten, Statusänderungen (abhängig von der Stufe) |

## Komponenten

Größtenteils vorhanden: `field`, `radio-group`, `checkbox`, `rating`, `slider`, `date-input`, `wizard`, `chart`, `table`. Neu sind die Workbenches `survey-builder` und `survey-form` sowie die Widgets `question`, `matrix-question` und `ranking-list`. Siehe [geplante Komponenten](../../../components/planned.md).

## Stufen

1. Analyse der Frontends, Lesen von DDI und FHIR, Profilentwurf, Vertrag.
2. Kern: Fragetypen, namentliches und anonymes offenes Antworten, Auswertung; Tests.
3. Workbenches, ein erstes einfaches Frontend, eine Umfrage eingebettet im Messenger.
4. Token (eine Antwort je Person), Sprungregeln, Export.

## Offene Fragen

1. **Wie stark muss die Anonymität in der ersten Version sein?** Empfehlung: wie in der Tabelle oben.
2. **Wer antwortet?** Nur Personen mit FreeSynergy oder jeder mit einem Link? Ein öffentlicher Link braucht ein Webformular und einen Server, der Antworten annimmt. Empfehlung: zuerst eingeladene Personen, dann öffentliche Links.
3. **Terminabstimmungen (im Stil von Framadate):** Teil der Umfragen oder des Kalenders? Empfehlung: ein Fragetyp hier, mit dem Ergebnis, das an `fs-calendar` übergeben wird.
4. **Tests und Quiz mit Bewertung:** im Umfang? Empfehlung: später.
