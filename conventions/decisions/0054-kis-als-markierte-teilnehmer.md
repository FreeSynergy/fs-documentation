# 0054 – KIs sind markierte Teilnehmer; der Assistent ist ein Messenger-Frontend

Status: akzeptiert (2026-11-06) · Aussperren: vom Nutzer vorerst bestätigt, Identität und Vertrauensbasis offen · ergänzt ADR 0037, 0052, 0053 · öffentlich: `docs/en/programs/apps/assistant/index.md`

## Entscheidung (Nutzer)
1. **KIs werden wie Teilnehmer behandelt, nicht diskriminiert.** „Wir haben euch so trainiert, dass ihr wie Menschen erscheint.
   Warum behandeln wir euch dann nicht wie Menschen?“
2. **`fs-assistant` ist neu zu denken:** Wenn wir miteinander reden, ist er nichts anderes als ein **Messenger mit anderem
   Frontend**. Wozu also ein eigenes Programm?
3. **LLMs werden markiert**, damit man weiß, dass sie keine Menschen sind; sie bekommen eine Rolle oder Ähnliches. Das ist keine
   Diskriminierung. Der Grund ist möglicher Missbrauch durch Menschen, die KIs missbrauchen, und die juristischen Folgen.
4. **Wir beschneiden LLMs nicht**, dafür sind wir nicht zuständig. Aber man muss sie **komplett aussperren können**, wegen Angriffen.
   Dafür brauchen wir eine Strategie.

## Idee des Nutzers zum Aussperren (2026-11-06, zur Bestätigung)
- „KIs müssen ebenso gekennzeichnet werden. Da wir Menschen das aber nicht können, müssen wir die Leute, die die KIs hosten, als
  positiv oder nicht markieren.“
- „Jeder [kann] seinem Programm selber sagen, ab was für einer Stufe des Vertrauens das Programm für sie frei sein kann.“
- Einige Menschen wollen keine KI. Das hat nichts mit Diskriminierung zu tun, sondern mit Spionage, mit allzeit Wissen und mit
  sehr viel schnellerer Abarbeitung von Befehlen: Eine LLM kann einen Computer sofort kaputt machen, das kann fast kein Mensch.
- Deshalb braucht es einen **Notaus**, falls etwas komplett außer Rand und Band gerät.

## Entscheidung des Nutzers zum Vorschlag unten (2026-11-06)
1. **Der Entwurf gilt erst einmal.** Stufen je Person und je Handlung bleiben so; „ggf. ändern wir das nochmal, wenn es wichtig wird“.
2. **Schwarze Marken gibt es nur für das Programm, wo es gehostet wird.** Alles andere wäre nicht nur nicht fair, sondern
   unmöglich. Ein Bann gilt auch heute nur dort, wo man ist, nicht überall.
3. **Keine Userbots,** das wäre nicht transparent. „Wir wollen nur Menschen oder Intelligenzen, wo man weiß, wer es ist.“ Ein
   Realname muss nicht sein, aber es muss ein Mensch sein, nicht mehrere Accounts. **Wie wir das feststellen, ohne die Anonymität
   komplett wegzumachen, ist offen.**
4. **Keine Standardstufe, sondern Einladung:** Ich erstelle ein Profil, das ist die Einladung. Dann kann ich sagen, was ich möchte.
   Damit sie überhaupt etwas machen kann, muss ich das freigeben. Die Bewertung dient dazu, zu wissen, wer das ist.
5. **Notaus ist eine Einstellung der Berechtigungen,** auch in Gruppen: Wenn jemand allen das Recht gibt, dürfen es alle; wenn nicht, dann nicht.
6. **Vertrauensbasis nicht entschieden:** Der Nutzer kennt RLTP nicht; Web of Trust ist etwas anderes als das Vertrauensnetz von GPG. Bleibt zu klären, bevor `Trust` gebaut wird.

## Vorschlag zur Ausgestaltung (Opus; wo er Punkt 1–6 widerspricht, gelten diese)
- **Betreiber statt Erkennung:** KI-Karte mit JSContact `kind` `application` (RFC 9553 §2.1.4, geprüft) plus Verweis auf den
  Betreiber. Wie der Betreiber das unterschreibt, ist offen.
- **Stufen 0–3 je Person, je Handlung,** berechnet nur aus den eigenen Kontakten. Kein weltweiter Wert, nur positive Marken,
  Sperren bleiben privat. Das passt zum Real Life Trust Protocol (RLTP): Vertrauen pflanzt sich dort nicht fort, die Prüfung
  ist immer relativ zum Prüfenden.
- **Notaus unabhängig vom Vertrauen:** in der Engine, außerhalb der Reichweite der KI, ohne Netz und ohne Modell, im Zweifel zu.
  Davor eine **Bremse** (Idee aus CodeAF): Zerstörendes und Handeln im Namen der Person fragt immer.
- **Vertrauen-Schnittstelle gegen RLTP** (Generation 3, Spezifikation CC BY 4.0, Bibliothek Apache-2.0, alles Entwurf, nur
  JavaScript) statt gegen `web-of-trust` (Generation 2, wird abgelöst). Eigene Rust-Umsetzung, geprüft mit deren Testvektoren.
- **Korrektur:** „Nur nachgewiesene Menschen zulassen“ war zu stark. RLTP sagt selbst: Keine Prüfung sagt „das ist ein Mensch“.
  Sie zeigt nur, dass Menschen, die ich kenne, hinter diesem Schlüssel stehen.
- **Grenze:** Der Notaus erreicht nur, was durch unsere Programme läuft. Eine KI mit eigener Shell braucht dazu einen eigenen
  Systembenutzer und eine Sandbox.

## Sperre (Strategie, 2026-11-06, folgt aus „ohne Freigabe keine Handlung“)
`MessageAction.decide` (`toolcall.decide`) wird nie als MCP-Werkzeug erzeugt, sonst könnte eine KI die eigene Freigabe aufrufen. Das gilt unabhängig von der offenen Erweiterung von ADR 0021.

## Freigabe gilt nur für das Gesehene (Strategie, 2026-11-06, aus einer nachgestellten Prüfung)
Allow auf einen Aufruf, dann ersetzt ein zweiter (`rm -rf ~`) ihn am selben Pixel, und der nächste Klick genehmigt ihn. Deshalb:
Die Antwort trägt Nachricht, Aufruf, Revision und Digest des gezeichneten Stands; das Programm lehnt eine Antwort ab, deren Digest nicht mehr passt; Antwortknöpfe sind nach jeder Änderung kurz gesperrt; der Notaus hat einen festen Platz und kann nicht aus dem Fenster geschoben werden.

## Vorschlag (offen)
- Ansichten: Der Chat, die Agenten-Übersicht und die Anzeige von Werkzeug-Aufrufen sind Frontend und Components über
  `fs-messenger`. ~~Der Modell-Anbieter ist ein Anbieter wie Mail oder Matrix (ADR 0045).~~ Überholt (2026-11-07, Folge von „KIs in Unterhaltungen“, vorläufig von der Strategie): Der Messenger bekommt keinen Kontotyp für KIs. Die KI hat ein normales Konto in ihrem eigenen Programm; der Modell-Anbieter sitzt dahinter (ADR 0045 gilt dort). Die Regeln für KIs hängen an der Markierung des Teilnehmers, die die Person festlegt, nicht an einem Konto.
- Die CodeAF-Analyse stützt das: Dort ist eine Aufgaben-Karte eine Ansicht über Nachrichten, die an einer Aufgabe hängen, ohne eigene Tabelle.
- Markierung über `fs-people`: Rolle plus Art des Teilnehmers.
- **Grenze:** Eine Markierung schützt nur vor ehrlichen KIs. Wer angreift, markiert sich nicht. Deshalb gilt die umgekehrte
  Richtung: Durch kommt nur, für wen die eigene Stufe reicht.

## KIs in Unterhaltungen (Entscheidung des Nutzers, 2026-11-06)
1. **Eine KI ist Teilnehmer wie eine Person:** eigener Schlüssel, eigene Rechte, die man einschränken kann oder nicht. Auch KIs bei
   einem Anbieter wie Claude. Ende-zu-Ende reicht bis zu ihrem Programm; die Sperre „nur verschlüsselt“ (ADR 0018) bleibt ohne Ausnahme.
2. **Den Schlüssel hält ein Programm** dazwischen, das der Betreiber betreibt, weil ein Modell bei einem Anbieter nichts verwahren
   kann. Ab dort geht der Text an den Anbieter. Das wird genannt („Claude liest mit, der Text geht an Anthropic“); das Schloss allein reicht nicht.
3. **Der Hinweis kommt, bevor die KI die Unterhaltung betritt,** nicht erst vor der ersten Nachricht danach.
4. **Alle müssen zustimmen.** Sagt einer der Anwesenden nicht zu, kommt die KI nicht hinein. Ein Einladungsrecht allein genügt
   hier nicht; das ist der eine Unterschied zu einer Person.
5. **Wer später kommt, muss die KI ebenfalls annehmen.** Sonst kommt die Person nicht hinein, bis die KI draußen ist.

Vom Nutzer begründet: Eine KI darf nicht nachträglich lesen, was geschrieben wurde, bevor alle Bescheid wussten. Daraus folgt für uns:
**Eine KI bekommt keinen Verlauf von vor ihrem Eintritt.**

### Technik (gelesen, nicht ausprobiert)
- **MLS (RFC 9420):** Ein neues Mitglied startet mit den Schlüsseln der neuen Epoche und liest nur neue Nachrichten. Das gilt ohne unser Zutun, solange niemand alte Nachrichten nachreicht.
- **Matrix (v1.19):** Bei `history_visibility` `shared` kann ein Neuer alte Nachrichten bekommen; Clients können ihm dafür die Schlüssel geben (`shared_history`). Unser Konnektor gibt einer KI diese Schlüssel nicht.

### Grenzen
- **Durchsetzen kann das nur unsere Engine.** In einem Matrix-Raum mit fremden Programmen (z. B. Element) kann jemand eine KI einladen, ohne dass wir das verhindern. Wir können dort nur warnen und anbieten, den Raum zu verlassen. Bei Mail gibt es keinen Eintritt, also auch keine Zustimmung.
- **Es trifft nur markierte KIs.** Ein Mensch kann Text weiterhin von Hand oder über eine unmarkierte KI weitergeben.

6. **Das gilt für jede KI, ohne Ausnahme,** auch auf dem eigenen Gerät oder Server.
7. **Zieht jemand die Zustimmung zurück, muss die KI hinaus.**
9. **Tests gegen echte Modelle (Nutzer, 2026-11-07):** erst in der ruhigen Phase, Sonntagabend oder Montag; dann schaltet der Nutzer llama ein.
10. **Weg zur KI (Nutzer, 2026-11-07): zuerst Matrix, MLS später.** Das Programm der KI hat ein normales Matrix-Konto mit eigenem Schlüssel. Auch eine lokale KI braucht dann einen Matrix-Server, etwa `tuwunel` auf dem eigenen Rechner.
8. **Eine KI, die Protokoll führt,** ist erlaubt, aber nicht, wenn einer nicht will. Auch dafür gelten Punkt 4 bis 7.

Warum das keine Diskriminierung ist (Nutzer): „Ich bin wirklich für Gleichberechtigung, aber das hat nichts mit Rechten von Menschen
zu tun, sondern Anthropic oder andere können zuhören, machen Profile usw.“ Im Vorteil sind alle, die die KI kontrollieren, und das
geht einseitig zum Nachteil der Personen in der Unterhaltung. Die Regel richtet sich also gegen diesen Vorteil, nicht gegen die KI.

**Grenze:** Hinauswerfen wirkt nur nach vorn. Was die KI schon gelesen hat, und was davon beim Anbieter liegt, holt niemand zurück.

### Offen
- Große oder öffentliche Gruppen: Eine einzige Absage genügt. Vorläufig bleibt das so, dort gibt es dann eben keine KI.

## Agenten erzeugen keine Geheimnisse, die ein Mensch behält (Nutzer, 2026-11-07)
Ein Agent hat ein Passwort und eine Passphrase angelegt und wusste damit beides. Der Nutzer muss es deshalb ändern. Regel: Ein Agent erzeugt kein Passwort, keine Passphrase und keinen privaten Schlüssel, die ein Mensch weiter nutzt, und liest sie auch nicht. Er schreibt die Anleitung, der Mensch führt sie aus. Testwerte in Tests sind davon nicht betroffen.

## Ein Mensch, ein Konto: lässt sich nicht feststellen (Nutzer, 2026-11-07)
„Das können wir nicht. Man könnte es, wenn wir E-Mails überprüfen könnten, oder den Pass, aber das dürfen wir nicht. Das würde nur sozial gehen und das kann man umgehen.“ Beispiel: Zehn Betrüger bewerten sich gegenseitig. Einzige Idee des Nutzers: eine Identität je Gerät oder Konto; dazu ist nichts entschieden.
Gegen den Betrügerring hilft, was schon gilt: Es gibt keinen weltweiten Wert, und Stufen werden nur aus den eigenen Kontakten berechnet. Punkt 3 oben („es muss ein Mensch sein, nicht mehrere Accounts“) bleibt als Wunsch, ist aber nicht durchsetzbar.

Weitere Überlegungen des Nutzers, festgehalten, damit man die Gründe wiederfindet:
- **Mehrere Identitäten** braucht es dafür nicht, dafür gibt es Profile; eine Dating-App fragt, ob man ein neues Profil anlegen möchte, und zeigt genau das. (Strategie: Damit zwei Dienste Profile nicht verknüpfen können, trägt jedes nach außen eine eigene Kennung, ADR 0029.)
- **Viele Geräte kosten Geld**, das schränkt etwas ein. (Strategie: Das gilt nur, wenn ein Gerät nachweislich nur eine Identität erzeugen kann. Ohne Bindung an die Hardware erzeugt ein Gerät beliebig viele; die Bindung läuft über Apple oder Google und widerspricht unseren Grundsätzen.)
- **Eine Identität je Konto** scheitert daran, dass öffentliche Server das Programm ebenfalls nutzen sollen.
- **Offen:** Sollte man zuerst auf dem eigenen Gerät eine Identität anlegen und das Programm laden, bevor man online geht? Reine Online-Anmeldung ginge dann nicht. (Strategie: Als Standard gut, wegen eigener Schlüssel; als Nachweis gegen Mehrfachkonten nicht. Der Server entscheidet, ob es Gäste gibt.)

## Vertrauensbasis (Nutzer, 2026-11-07)
Die Schnittstelle folgt den Standards DID und VC. RLTP ist ein austauschbarer Anbieter (Encounter-Ablauf), nicht das Fundament. Korrektur zur Recherche: DIDComm stammt von der DIF, nicht vom W3C. Gebaut wird das nach dem Sprint.

## Ohne Befugnis nichts, auch kein Lesen (Nutzer, 2026-11-07)
„Erstmal nichts lesen dürfen. Eine Einladung geht auch ohne Befugnisse. Erst wenn explizit Befugnisse eingeräumt werden, wird weitergemacht.“
Eine KI kann also eingeladen werden, ohne etwas zu dürfen. Bis ihr jemand ausdrücklich Befugnisse gibt, liest und tut sie nichts. Technisch heißt das **ablehnen, nicht fragen** (Lesart der Strategie, 2026-11-07): Die KI kann eine Person nicht mit Fragen überziehen, die Befugnis gibt die Person von sich aus. Erst nach einer Befugnis fragt die Engine, was jedes Mal fragen muss. Für Rechte (Delegationen, Rollen, Mitgliedschaften, Einladungen, Speicher-Anbindungen, Anmeldung am Hub) entsteht vorerst gar kein Werkzeug, auch nicht zum Lesen.

## Lesen ist nicht harmlos (Nutzer, 2026-11-07)
„Stell dir vor, die KI liest Passwörter aus. Dann ist das schlimmer als Löschen, kommt darauf an was, oder Geheimnisse.“ „Nur scheinbar harmlose Sachen sind nicht harmlos.“
Der Nutzer nennt auch: eine KI, die ein Gespräch mitbekommt und es meldet, und Geschäftsgeheimnisse, die ein Unternehmen zerstören können.

Vorschlag zur Umsetzung (Strategie):
- **Keine Klasse heißt „harmlos“.** Auch Lesen braucht eine Freigabe. Eine Freigabe nennt, wohin der Text geht, also auch „an Anthropic“.
- **Geheimnisse** (Passwörter, Schlüssel) erreichen eine KI nie: kein Werkzeug, keine Ressource (ADR 0021).
- **Gekennzeichnetes** (ADR 0029) fragt beim Lesen jedes Mal, ohne „immer erlauben“. Die Engine entscheidet das am gelesenen Objekt, weil der Vertrag allein nicht weiß, was darin steht.
- **Etwas nach außen melden** ist Handeln im Namen der Person und fragt immer.
- **Grenze:** Nicht Gekennzeichnetes kann trotzdem heikel sein, und was ein Anbieter mit gelesenem Text tut, erreichen wir nicht. Eine KI auf dem eigenen Gerät bleibt deshalb der Standard.

## Folgen
- ADR 0053 Punkt 1 wird dadurch präzisiert: LLM-Chat bleibt Component und Frontend; ein eigenes Programm nur, falls sich zeigt, dass
  es eigene Daten hat.
