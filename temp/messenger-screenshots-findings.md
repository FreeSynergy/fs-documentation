# Messenger — Befunde aus den Bildschirmfotos (Outlook M365, Apple Mail)

Stand 2026-11-05 · Grundlage: private Bildschirmfotos (nicht veröffentlicht, ADR 0038) ·
Doku: `docs/en/programs/apps/messenger/frontends/outlook/m365-2026-11/`, `.../apple-mail/ios-26/`.
Ids sind Vorschläge im Format `<objekt>.<aktion>` (wie in `requirements.md`).

## Outlook (Microsoft 365, neues Outlook + Mobil + teils klassisch)

### Fähigkeiten, die in `requirements.md` noch fehlen
- `message.recall` — gesendete Nachricht zurückrufen (nur innerhalb der Organisation; Rückruf-Bericht als Mail)
- `conversation.pin` — anheften, Gruppe „Angeheftet" oben in der Liste (Zeile „Pin conversations" existiert ohne Id, bisher nur El)
- `message.followup` — Nachverfolgung mit Start-/Fälligkeitsdatum und Erinnerung (heute/morgen/diese/nächste Woche/eigene); erledigt markieren
- `view.save` — gespeicherte Suche als Ordner (kategorisierter Suchordner in Favoriten); gleiche Idee wie Apples intelligente Postfächer
- `message.classify` — Posteingang automatisch teilen (Relevant/Sonstige); bei Apple Kategorien
- `sync.scope` — Offline: welche Ordner, wie viele Tage, Anhänge ja/nein (bisher nur allgemein „Work offline … (`sync`)")
- `sync.now` — manuell senden/empfangen, Fortschritt, abbrechen (klassisch)
- `conversation.ignore` — Unterhaltung ignorieren (künftige Antworten gleich löschen) — Abgrenzung zu Stummschalten (`conversation.notify`)
- `message.sweep` — Aufräumen: alle/alte Mails eines Absenders löschen/verschieben
- `macro.run` — Quick Steps: mehrere Aktionen mit einem Klick (eigene Kombinationen)
- `autoreply.set` — Abwesenheitsnotiz / automatische Antworten
- `account.delegate` — Stellvertretung: andere dürfen lesen/antworten im eigenen Namen
- `message.priority` — hohe/niedrige Wichtigkeit
- `message.retain` — Aufbewahrungsrichtlinie zuweisen
- `message.summarize` — Zusammenfassung (KI) — offen, ob wir das wollen (lokal?)
- `text.check` — Rechtschreib-/Grammatikvorschläge im Composer ⚠️ (lokal, ohne Cloud)
- Bestehende Zeilen, bei denen „Seen in" um **Ou ✅** ergänzt werden kann (bisher ⚠️): `message.schedule`, `conversation.snooze`, Undo-Send (mit einstellbarer Verzögerung 0–10 s), `message.react` (Reaktionen auf Mails), `presence.set` (Präsenzpunkt), `message.flag`, `message.reply`, `message.status` (Lesebestätigung verfolgen, ausgegraut gesehen), `conversation.notify` (Benachrichtigung je Art: Mail/Reaktion/Erwähnung)

### Gesten / Interaktion (für die Gesten-Doku)
- Maus: Rechtsklick → langes Kontextmenü mit Untermenüs (gesehen)
- Maus: Split-Button (linker Teil = Standard, Pfeil = Auswahl) bei Neu, Senden, Löschen (gesehen)
- Maus: Überfahren einer Person → Kontaktkarte (Präsenz, Rolle, Kontaktdaten, Vorgesetzte:r) (gesehen)
- Maus: Pfeil an der Zeile klappt die Unterhaltung auf (gesehen)
- Maus: „Quick Click" auf die Fahnen-Spalte setzt eine vorgewählte Fahne (Menüeintrag gesehen)
- Maus: Schnellaktionen beim Überfahren der Zeile, konfigurierbar (Menüeintrag gesehen, Knöpfe selbst ⚠️)
- Maus/Drag: Ordner in Favoriten ziehen (Hinweis gesehen); Mails auf Ordner ziehen ⚠️
- Schieberegler für die Undo-Verzögerung (gesehen)
- Finger (mobil): schwebender „Neue E-Mail"-Knopf mit Ausklapp-Pfeil (gesehen); Wisch-Aktionen ⚠️ **nicht gesehen**

## Apple Mail (iOS 26, dazu aktuelles macOS; iOS-27-Bild wirkt wie ein Konzept)

### Fähigkeiten, die in `requirements.md` noch fehlen
- `view.save` — intelligente Postfächer (VIP, Markiert, Ungelesen, An/Kopie, Anhänge, Erinnerung, Rückfragen, Später senden, Stumm …), ein-/ausblenden und per Ziehen ordnen
- `message.classify` — automatische Kategorien (Wichtiges, Transaktionen, Neuigkeiten, Werbung) + erklärende Übersicht „wie viele wohin"
- `contact.vip` — Person als VIP markieren (Stern in der Liste, eigenes Postfach) — Kontakt bleibt im Kontakte-Programm (ADR 0020), nur die Markierung ist Messenger-Sache
- `privacy.proxy` — „E-Mail-Aktivität schützen": IP verbergen, fremde Inhalte privat vorladen (über „nicht fernladen" hinaus)
- `recipient.warn` — „Adressen markieren": Empfänger außerhalb erlaubter Domains hervorheben
- `list.unsubscribe` — Banner „Mailingliste" mit Abmelden (RFC 8058 ⚠️)
- `message.followup` — Postfach „Rückfragen": gesendete Mails ohne Antwort wieder vorlegen
- `account.alias` — mehrere Absenderadressen je Konto, Absender im Composer wählen (macOS 10.12)
- `message.flag` erweitern — Fahnenfarben (7 Farben)
- `message.summarize` — „Zusammenfassen" (wie Outlook)
- Bestehende Zeilen mit neuem Beleg **Ap ✅**: `conversation.snooze` (Erinnerung), `message.schedule` (Später senden), `conversation.notify` (Mitteilen / Stumm), `message.search` (Bereich alle/aktuelles Postfach, Top-Treffer, Vorschläge), Sortieren/Gruppieren (macOS-Darstellungsmenü), `conversation.move` (Auswählen → Bewegen), Remote-Inhalt nicht laden

### Gesten / Interaktion (für die Gesten-Doku)
- Finger: **Wischen nach links** auf Zeile → drei runde Knöpfe mit Beschriftung: Mehr (grau), Markieren (orange), Löschen (rot) (gesehen); ganz durchwischen = letzte Aktion ⚠️
- Finger: Wischen nach rechts → gelesen/ungelesen ⚠️ (nicht gesehen)
- Finger: **Langes Drücken** → angehobene Vorschau der Mail + Menü (Antworten, Allen antworten, Weiterleiten, Markieren ›, Mitteilen, Stumm) (gesehen)
- Finger: „Auswählen" → Mehrfachauswahl → Bewegen-Blatt mit gestapelter Vorschau der Auswahl (gesehen)
- Finger: Ziehgriffe → Reihenfolge der Postfächer ändern (gesehen)
- Finger: Tippen auf Kategorie-Chip filtert (gesehen); Chips seitlich scrollen ⚠️
- Finger: Pfeile hoch/runter in der offenen Mail → nächste/vorige Mail (gesehen)
- Finger: Tippen auf Absender → Kontaktkarte als Blatt (gesehen)
- Finger: Farbpunkt im Aktionsblatt → Fahne in dieser Farbe (gesehen)
- Stimme: Mikrofon im Suchfeld (Diktat) (gesehen)
- Blatt nach unten wischen zum Schließen, Ziehen zum Aktualisieren ⚠️
- Stift: „Skizze hinzufügen" vom iPad in den Mac-Composer (gesehen, Continuity)

## Offene Punkte
- `view.save` und `message.classify` kommen in **beiden** Programmen vor → Kandidaten für Required/Optional prüfen.
- Outlook-Wisch-Aktionen mobil: Bildschirmfoto fehlt.
- Offizielle Outlook-Tastenkürzel noch holen (shortcuts.md sagt „später").
- Das „iOS 27"-Bild nicht als Apple-Stand werten, bis es belegt ist.
