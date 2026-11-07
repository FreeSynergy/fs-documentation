# Handtest: fs-people-app und fs-tasks-app (Stand 2026-11-07)

Diese Anleitung ist für Kal. Alle Befehle unten habe ich auf diesem Rechner selbst ausgeführt (siehe letzter Abschnitt). Zweite Fassung vom 2026-11-07: neu sind das Blättern mit „Show more“ per Cursor und das atomare Speichern mit Konfliktmeldung.
Ein echtes Fenster habe ich nicht geöffnet, das machst du. Die Oberfläche ist bisher **englisch** (Übersetzung ist noch nicht dran, ADR 0053).

## Das Prinzip in drei Sätzen
- Es laufen immer **zwei** Programme: der **Server** (hält die Daten, hat kein Fenster) und die **App** (das Fenster).
- Beide reden über eine Datei, den **Socket** (`people.sock` bzw. `tasks.sock`). Ohne laufenden Server sagt die App „cannot reach ... server“ und beendet sich. Das ist richtig so.
- Der Server legt seine Daten in einen Ordner, der **nur dir gehören** darf (Rechte 700). Sonst weigert er sich zu starten.

## Einmal vorbereiten (für beide Apps)
Terminal öffnen und kopieren:

```bash
# Arbeitsordner für den Test (liegt im Arbeitsspeicher, ist nach einem Neustart weg)
mkdir -p -m 700 "$XDG_RUNTIME_DIR/fs-handtest/people-data" "$XDG_RUNTIME_DIR/fs-handtest/tasks-data"
mkdir -p ~/fs-handtest && cd ~/fs-handtest

# Programme holen (Zweig "gui") und bauen. Das dauert beim ersten Mal ein paar Minuten.
git clone https://github.com/FreeSynergy/fs-people && git -C fs-people checkout gui
git clone https://github.com/FreeSynergy/fs-tasks  && git -C fs-tasks  checkout gui
export CARGO_TARGET_DIR=~/fs-handtest/target
(cd fs-people && cargo build -j 4 --workspace)
(cd fs-tasks  && cargo build -j 4 --workspace)
```

Fertig, wenn am Ende `Finished` steht. Die Programme liegen dann in `~/fs-handtest/target/debug/`.
Hinweis: Das Bauen holt Pakete aus dem Netz (GitHub, crates.io). Wenn der Klon fehlschlägt, weil das Repo privat ist, brauchst du eine Anmeldung bei GitHub.

Zwei kleine Beispieldateien zum Importieren (einfach kopieren):

```bash
cat > ~/fs-handtest/kontakte.vcf <<'E'
BEGIN:VCARD
VERSION:4.0
UID:urn:uuid:11111111-1111-4111-8111-111111111111
FN:Anna Beispiel
N:Beispiel;Anna;;;
EMAIL:anna@example.org
TEL:+4915112345678
ORG:Beispiel GmbH
END:VCARD
BEGIN:VCARD
VERSION:4.0
UID:urn:uuid:22222222-2222-4222-8222-222222222222
FN:Bernd Muster
N:Muster;Bernd;;;
EMAIL:bernd@example.org
END:VCARD
E

cat > ~/fs-handtest/aufgaben.ics <<'E'
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//handtest//DE
BEGIN:VTODO
UID:aufgabe-1@example.org
DTSTAMP:20261107T100000Z
SUMMARY:Einkaufen gehen
DUE:20261110T120000Z
PRIORITY:1
STATUS:NEEDS-ACTION
END:VTODO
BEGIN:VTODO
UID:aufgabe-2@example.org
DTSTAMP:20261107T100000Z
SUMMARY:Steuer machen
STATUS:IN-PROCESS
END:VTODO
BEGIN:VTODO
UID:aufgabe-3@example.org
DTSTAMP:20261107T100000Z
SUMMARY:Blumen giessen
STATUS:COMPLETED
END:VTODO
END:VCALENDAR
E
```

Eine große Beispieldatei zum Blättern (je 300 Einträge). Das kleine Skript schreibt sie:

```bash
cat > ~/fs-handtest/gen.sh <<'E'
#!/usr/bin/env bash
# Aufruf: gen.sh people|tasks ANZAHL DATEI
n=$2; f=$3; : > "$f"
if [ "$1" = people ]; then
 for i in $(seq 1 "$n"); do u=$(printf '%08d' "$i")
  printf 'BEGIN:VCARD\nVERSION:4.0\nUID:urn:uuid:%s-0000-4000-8000-000000000000\nFN:Person %s\nN:Person;%s;;;\nEMAIL:p%s@example.org\nEND:VCARD\n' "$u" "$u" "$u" "$i" >> "$f"; done
else
 printf 'BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//handtest//DE\n' >> "$f"
 for i in $(seq 1 "$n"); do
  printf 'BEGIN:VTODO\nUID:aufgabe-%s@example.org\nDTSTAMP:20261107T100000Z\nSUMMARY:Aufgabe %s\nSTATUS:NEEDS-ACTION\nEND:VTODO\n' "$i" "$i" >> "$f"; done
 printf 'END:VCALENDAR\n' >> "$f"
fi
E
chmod +x ~/fs-handtest/gen.sh
~/fs-handtest/gen.sh people 300 ~/fs-handtest/viele.vcf
~/fs-handtest/gen.sh tasks  300 ~/fs-handtest/viele.ics
```

---

## Teil 1: fs-people-app (Personen)

**Zweig:** `gui` im Repo `fs-people` (Stand beim Test: Commit `a310509`).

### Befehle
**Terminal 1: Server starten** (bleibt offen, schreibt nichts, wenn alles gut ist):

```bash
~/fs-handtest/target/debug/fs-people-server \
  --socket "$XDG_RUNTIME_DIR/fs-handtest/people.sock" \
  --data   "$XDG_RUNTIME_DIR/fs-handtest/people-data"
```

**Terminal 2: App starten** (mit den zwei Beispiel-Personen):

```bash
~/fs-handtest/target/debug/fs-people-app \
  --socket "$XDG_RUNTIME_DIR/fs-handtest/people.sock" \
  --import ~/fs-handtest/kontakte.vcf
```

Unten im Fenster steht dann „Imported 2, 0 already known“. Startest du die App ein zweites Mal mit `--import`, steht dort „Imported 0, 2 already known“ (schon bekannte Personen werden übersprungen, nie überschrieben). Ohne `--import` startest du einfach mit den gespeicherten Personen.

**Alle exportieren** (schreibt eine neue Datei und beendet sich, ohne Fenster; eine vorhandene Datei wird nie überschrieben, dann kommt „the file exists“):

```bash
~/fs-handtest/target/debug/fs-people-app --socket "$XDG_RUNTIME_DIR/fs-handtest/people.sock" --export ~/fs-handtest/ausgabe.vcf
```

**Beenden:** Fenster schließen. Server in Terminal 1 mit `Strg+C` beenden (er räumt seinen Socket selbst weg).
**Aufräumen** (löscht auch alle Testdaten):

```bash
rm -rf "$XDG_RUNTIME_DIR/fs-handtest" ~/fs-handtest
```

### So sieht der Start aus
Links oben ein Suchfeld und der blaue Knopf **New**, darunter die Liste mit Spalten Name und E-mail (Anna Beispiel, Bernd Muster). Rechts die Einzelansicht der gewählten Person mit **Edit** und **Delete**, unten eine Statuszeile.

### Klick das, du solltest das sehen
1. **Liste:** Anna und Bernd stehen links. Klick auf Bernd: rechts erscheint Bernd mit seiner E-Mail.
2. **Ansehen:** Anna zeigt Abschnitte „Contact“ (E-Mail, Telefon), „Organisation“ (Beispiel GmbH) und „Kept on the card“ (heißt: es gibt Daten, die die App noch nicht zeigt, sie bleiben aber erhalten).
3. **Suche:** Tippe `anna` ins Suchfeld. Nur Anna bleibt übrig. Feld leeren: beide sind wieder da. Probiere auch `bernd@` und `+4915`.
4. **Anlegen:** **New** klicken, Name und E-Mail eintragen, speichern. Die Person erscheint in der Liste. Ein ganz leeres Formular wird abgelehnt (kein Name, Spitzname, E-Mail, Telefon oder Organisation).
5. **Bearbeiten:** Person wählen, **Edit**, die Telefonnummer ändern, speichern. Die Änderung steht rechts. Alles, was die App nicht zeigt, bleibt unverändert erhalten.
6. **Löschen:** **Delete** drücken. Es muss **ein zweites Mal** gedrückt werden, erst dann ist die Person weg.
7. **Export/Import:** Siehe die Befehle oben. Die ausgegebene `.vcf`-Datei kannst du mit einem Texteditor öffnen. Danach `--import` mit dieser Datei: „already known“.
8. **Viele Einträge, „Show more“:** Am besten mit leerem Datenordner (oder erst Aufräumen, dann neu anfangen). App mit `--import ~/fs-handtest/viele.vcf` starten: unten „Imported 300, 0 already known“. Die Liste zeigt die ersten 200 („Person 00000001“ ...), darunter der Knopf **Show more**. Klick darauf: es kommen die restlichen 100 dazu, ohne dass die Liste vorn von vorn anfängt. Kein Name darf doppelt vorkommen, am Ende ist „Person 00000300“ die letzte. Danach verschwindet der Knopf. Die Suche blättert ebenso: `Person 0000` eintippen, **Show more** klicken, es geht weiter.
9. **Zwei Fenster, „Jemand anderes hat dies geändert“:** Zwei Terminals, zweimal dieselbe App (`fs-people-app --socket ...`) auf **demselben** Server. Fenster A und B zeigen beide Anna. In **B** (bleibt offen) **Edit** klicken und die Telefonnummer **nicht** speichern, noch warten. In **A** **Edit**, Telefonnummer ändern, speichern. Jetzt in **B** die Telefonnummer anders ändern und speichern. Erwartet: Es wird **nichts geschrieben**, B zeigt die Meldung „Someone else changed this person since you started.“ (englisch). Dein eingetippter Text bleibt im Formular stehen, die Version von A ist die gespeicherte. Ein **zweiter Klick auf Save** schreibt deine Änderung bewusst darüber (es werden nur die Felder geschrieben, die du selbst geändert hast).
10. **Fenster klein ziehen:** Bei sehr schmalem Fenster (ca. 420 Pixel) rutscht die Einzelansicht **unter** die Liste, statt daneben zu stehen. Nichts darf überlappen oder abgeschnitten werden, die E-Mail-Spalte darf mit „...“ gekürzt sein.
11. **Menü:** Diese App hat bisher **keine Menüleiste**, nur die Knöpfe im Fenster.

### Das geht bekanntermaßen noch nicht (steht so in der DESIGN.md)
- Gruppen und ihre Mitglieder, Beziehungen zwischen Personen, „gleiche Person“-Vorschläge, Rollen vergeben, KI-Markierung setzen.
- Bearbeiten von Spitznamen, Titeln, Adressen, Links, Notizen, Stichwörtern (die Daten bleiben erhalten, nur nicht änderbar).
- „Sensibel“-Markierung setzen. Karten mit dieser Markierung lehnt der Speicher bisher ab, weil er **nicht verschlüsselt** ist (der Schlüsselverwalter, ADR 0024, fehlt noch). Du wirst so etwas im Test nicht erzeugen können.
- Dateiauswahl-Fenster für Import und Export: nur Pfade auf der Kommandozeile.
- Rückgängig, Live-Aktualisierung (Änderungen eines anderen Programms siehst du erst nach neuem Laden), Anmeldung (der Benutzer ist fest „owner“), Entwurf bleibt nach Schließen nicht erhalten.
- Die Liste zeigt 200 Personen, mehr über „Show more“ (liest ab dem Cursor weiter). Wie viele es insgesamt gibt, steht nirgends (kein Zähler). Zwei Fenster auf einem Adapter stören sich beim Blättern.
- **Fristen:** Ein hängender oder sehr langsamer Server friert das Fenster bis zu **30 Sekunden pro Aktion** ein (das ist kein Absturz). Das Verbinden gibt nach 5 Sekunden auf. Eine Aktion, die abbricht, kann trotzdem schon geschrieben sein.
- **Kein Wiederverbinden:** Stoppst du den Server, kommt bei der nächsten Aktion ein Fehler. Danach die App neu starten (und vorher den Server).
- Wer etwas anderes ändert, siehst du nicht live, erst beim nächsten Laden (nur beim Speichern kommt die Konfliktmeldung). Das atomare Speichern gilt nur innerhalb **eines** Serverprozesses.
- **KI-Erkennung:** Eine Karte, die als KI (Software) markiert ist, trägt in Liste und Einzelansicht die Marke „AI“, Rollen sieht man nur lesend („Roles“). Du kannst keine KI markieren und keine Rolle vergeben, also nichts davon selbst erzeugen. Die Marke hat nur Anzeigewirkung, sie sperrt nichts.
- Beim vCard-Export steht bei aus Version 3.0 eingelesenen Karten manchmal weiter `VERSION:3.0`.

### Auffälliges notieren
Eine Zeile pro Fund in `~/fs-handtest/funde-people.txt`, Form: `Was ich geklickt habe -> was ich erwartet habe -> was passiert ist`.

---

## Teil 2: fs-tasks-app (Aufgaben)

**Zweig:** `gui` im Repo `fs-tasks` (Stand beim Test: Commit `ef100c2`).

### Befehle
**Terminal 1: Server:**

```bash
~/fs-handtest/target/debug/fs-tasks-server \
  --socket "$XDG_RUNTIME_DIR/fs-handtest/tasks.sock" \
  --data   "$XDG_RUNTIME_DIR/fs-handtest/tasks-data"
```

**Terminal 2: App** (mit drei Beispiel-Aufgaben; nur beim ersten Mal `--import`):

```bash
~/fs-handtest/target/debug/fs-tasks-app \
  --socket "$XDG_RUNTIME_DIR/fs-handtest/tasks.sock" \
  --import ~/fs-handtest/aufgaben.ics
```

Unten steht „Imported 3, 0 already known. Notes: ... version set to 2.0“. Die „Notes“ sind harmlos (die Datei wurde auf das neue Format umgestellt).
Direkt in der Statusansicht starten: zusätzlich `--view status`. Die Programme `fs-people-app` und `fs-tasks-app` und ihre Server dürfen gleichzeitig laufen (eigene Sockets).

**Alle exportieren** (neue Datei, ohne Fenster):

```bash
~/fs-handtest/target/debug/fs-tasks-app --socket "$XDG_RUNTIME_DIR/fs-handtest/tasks.sock" --export ~/fs-handtest/ausgabe.ics
```

**Beenden und aufräumen:** wie bei people (Fenster zu, Server `Strg+C`, dann `rm -rf "$XDG_RUNTIME_DIR/fs-handtest" ~/fs-handtest`).

### So sieht der Start aus
Oben die Leiste „FreeSynergy Tasks“ mit den Menüs **Task** und **View**. Darunter Suchfeld und drei Knöpfe **List**, **Status**, **New**. Links die Liste (Title, Due, Priority, Status): „Einkaufen gehen“ (fällig 2026-11-10 12:00, Priorität 1, To do), „Blumen giessen“ (Done), „Steuer machen“ (In progress). Rechts die Einzelansicht mit **Edit** und **Delete**, dem Kasten **Move to** (To do, In progress, Done, Failed, Cancelled) und „Details“.

### Klick das, du solltest das sehen
1. **Liste:** Die drei Aufgaben stehen da. Klick auf eine: rechts erscheinen ihre Angaben.
2. **Suche:** `steuer` eintippen: nur „Steuer machen“ bleibt.
3. **Anlegen:** **New** (oder Menü Task, dann New): Titel, Beschreibung, Fälligkeit, Priorität, Status, Stichwörter. Speichern: die Aufgabe steht in der Liste. Die Fälligkeit braucht eine **Uhrzeit** (nur ein Tag geht noch nicht).
4. **Bearbeiten:** Aufgabe wählen, **Edit**, Titel ändern, speichern.
5. **Löschen:** **Delete**.
6. **Verschieben / Statusansicht:** Knopf **Status** (oder Menü View, dann Status): fünf Spalten To do, In progress, Done, Failed, Cancelled. „Einkaufen gehen“ liegt in To do, „Steuer machen“ in In progress, „Blumen giessen“ in Done. Verschiebe eine Aufgabe mit den Knöpfen unter **Move to** (oder mit der Tastatur). Sie wechselt die Spalte, und oben steht ein rosa Hinweis. **Wichtig:** Das ist kein „Board nur für dich“. Das Verschieben ändert den Status der Aufgabe **für alle**. Das schreibt die App selbst so an den Bildschirm.
7. **Zurück zur Liste:** **List**. Der neue Status steht in der Spalte „Status“.
8. **Import/Export:** siehe Befehle oben. Wiederholter Import: „Imported 0, 3 already known“. Die Exportdatei enthält drei `VTODO`-Blöcke.
9. **Menü:** nur Task, New und View, List, Status (nur echte Befehle).
10. **Viele Aufgaben, „Show more“:** Server mit leerem Datenordner, App mit `--import ~/fs-handtest/viele.ics`. Unten steht „Imported 300, 0 already known. Notes: ...“ gefolgt von sehr vielen gleichen Zeilen „version set to 2.0“ (sieht unschön aus, ist harmlos, die Zeile ist abgeschnitten). Die Liste zeigt 200 Aufgaben (sortiert nach Titel, „Aufgabe 1“, „Aufgabe 10“, „Aufgabe 100“ ...), darunter **Show more**: Klick, es kommen die restlichen 100 dazu, nichts doppelt. In der Statusansicht steht über der Spalte „To do (200)“, ebenfalls mit **Show more**. **Achtung, anders als bei people:** Die Tasks-App blättert (noch) **nicht** per Cursor. Bei jedem Laden liest sie intern die ganze Liste (je 100 pro Seite) und zeigt davon einen Ausschnitt. Das Ergebnis sieht gleich aus, nur bei sehr vielen Aufgaben wird es langsamer (siehe DESIGN.md, „Other limits“).
11. **Zwei Fenster, „Someone else changed this task in the meantime.“:** Wie bei people: zwei Fenster auf demselben Server, in B **Edit** öffnen, in A dieselbe Aufgabe ändern und speichern, dann in B speichern. Erwartet: nichts geschrieben, Meldung „Someone else changed this task in the meantime.“ (englisch), der Text bleibt. Das gilt auch für **Move to** in der Statusansicht: Wurde die Aufgabe inzwischen woanders verändert, wird nicht verschoben, sondern die neue Fassung gezeigt. Wer die Meldung nach einem Klick bekommt, darf einfach noch einmal klicken.
12. **Fenster klein ziehen:** Bei ca. 400 Pixel Breite rutscht die Einzelansicht unter die Liste, die Spalten werden gekürzt („...“). In der Statusansicht läuft die Reihe der Spalten über den Rand (Failed, Cancelled sind dann nur halb zu sehen), das ist bekannt. Ein sehr kleines Fenster zeigt laut Entwurf eine „kompakte Ansicht“ mit offenen Aufgaben.

### Das geht bekanntermaßen noch nicht (steht so in der DESIGN.md)
- **Keine echten Boards/Kanban:** nur fünf feste Spalten (der Status der Aufgabe), keine eigenen Spalten, Reihenfolge innerhalb einer Spalte (richtet sich nach Fälligkeit; zieht man eine Karte woandershin, springt sie zurück und das wird gesagt), keine Bahnen, keine Spaltenlimits.
- Aufgaben zuweisen, Beziehungen zwischen Aufgaben, Checklisten, Zeitleiste, Kommentare, Anhänge, Erinnerungen, Rückgängig, Wiederholung bearbeiten.
- Wiederkehrende Aufgaben: Status lässt sich nicht verschieben (wird mit Grund abgelehnt).
- Ein Status, der aus den Teilnehmern berechnet wird, wird beim Verschieben fest und kann in der App nicht zurück.
- Fälligkeit ohne Uhrzeit, Zeitzonenwahl, Dateiauswahl-Fenster für Import/Export.
- Keine Live-Aktualisierung, keine Anmeldung („meine nächsten Aufgaben“ sind alle offenen).
- **Kein Wiederverbinden:** Stoppt der Server, kommt bei der nächsten Aktion ein Fehler. Danach App (und vorher Server) neu starten.
- **Fristen:** Ein hängender Server friert das Fenster bis zu 30 Sekunden pro Aufruf ein, und eine Aktion (Speichern, Verschieben, Löschen) macht bis zu zwei Aufrufe, also bis zu **60 Sekunden**. Verbinden: 5 Sekunden. Es gibt noch keine „Bitte warten“-Anzeige.
- **Blättern ohne Cursor** (s. o.): jedes Laden liest alles. Ein Server-Lesen kann zwischen zwei Seiten verändert werden, dann kann eine Aufgabe einmal doppelt oder gar nicht erscheinen (das nächste Laden ist richtig). Eine einzelne kaputte gespeicherte Aufgabe lässt Liste und Export scheitern.
- Ein geschlossenes Fenster verliert eine ungespeicherte Änderung.
- Karten mit „sensibel“-Markierung werden nie geöffnet und beim Export weggelassen (mit `--export-sensitive <uid>` freizugeben). Du wirst so etwas im Test nicht erzeugen können.

### Auffälliges notieren
Eine Zeile pro Fund in `~/fs-handtest/funde-tasks.txt`, gleiche Form wie oben.

---

## Was ich getestet habe und was nicht
**Getestet, hat geklappt (2026-11-07, frische Klone von `https://github.com/FreeSynergy/...` unter `.scratch/t4-handtest2/`, Zweig `gui`; Stand `fs-people` `a310509`, `fs-tasks` `ef100c2`; Aufruf der Programme über `limited.sh`):**
- **Frischer Klon baut:** ja, beide. fs-people in 1:03 min, fs-tasks danach in 18 s (`-j 4`, gemeinsames Build-Verzeichnis, ein Bau zur Zeit).
- **Server starten:** ja, beide, Sockets erscheinen. Nach `Strg+C` (SIGINT) sind die Sockets weg. Mit gestopptem Server sagt `fs-people-app`: „cannot reach the people server at ...“ (Exitcode 1).
- **Viele Einträge per Kommandozeile:** Beispieldateien mit 300 Karten bzw. 300 Aufgaben (das `gen.sh` oben). people: „Imported 300, 0 already known“, zweiter Import „Imported 0, 300 already known“, Export schreibt 300 `VCARD`, keine doppelte `UID`, zweiter Export in dieselbe Datei: „the file exists“ (Exitcode 1). tasks: „Imported 300, 0 already known“ (plus 300 mal „version set to 2.0“ in der Statuszeile), Export schreibt 300 `VTODO`, keine doppelte `UID`.
- **`--snapshot`:** people (1000x700): erste Zeilen „Person 00000001“ ..., unten der Knopf „Show more“, Statuszeile „Imported 300, 0 already known“. tasks Liste (1100x700): sortiert nach Titel, „Show more“ unten; tasks Statusansicht (`--view status`): Spalte „To do (200)“, rosa Hinweis „für alle“, andere Spalten leer, „Cancelled“ halb abgeschnitten. Ich habe die PNG-Dateien angesehen.
- **Die automatischen Tests der Apps zu den neuen Funktionen** (laufen gegen den echten Server, echten Socket, echten Speicher, aber ohne Fenster): people `tests/cursor.rs` 5 von 5 ok (u. a. „Show more continues from the cursor“, „search continues from the cursor“, „a person added after the first page does not break Show more“), people `tests/atomic.rs` 1 von 1 ok („a write between read and save is a conflict and nothing is lost“), tasks `tests/atomic.rs` 5 von 5 ok (Konflikt beim Speichern und beim Verschieben, jeweils mit Kontrollversuch ohne zweiten Schreiber). Das ist der Beleg für Teil 1 Nr. 8 und 9 und Teil 2 Nr. 10 und 11, **nicht** eine Bedienung von zwei echten Fenstern.

**Nicht getestet:**
- **Kein echtes Fenster** (laut Auftrag nur du). Klicken, Tippen, Tastatur, „Show more“ im echten Fenster, die Konfliktmeldung im echten Fenster (also Wortlaut und Aussehen auf dem Bildschirm, ob der Text im Formular stehen bleibt, ob der zweite Klick auf Save überschreibt), Menü-Klicks, Kleinziehen, Verschieben in der Statusansicht. Was bei „Klick das“ steht, folgt der DESIGN.md, den Tests und den Bildschirmfotos. Die Meldungstexte habe ich aus `words.rs` gelesen.
- **Zwei echte Apps auf einem Server** und das Zusammenspiel von „Show more“ mit Änderungen in einem zweiten Fenster.
- Ob die Tasks-App mit sehr vielen Aufgaben (Tausende) spürbar langsam wird: nur mit 300 ausprobiert und nicht gemessen.
- KI-Marke/Rollen (kann man ohne Rollenvergabe nicht erzeugen), sensible Karten/Aufgaben, `--export-sensitive`, Wiederholungsaufgaben, hängender Server (30-Sekunden-Frist) und Wiederverbinden (nur das Fehlen bei gestopptem Server, nicht das Einfrieren).
- fs-calendar, fs-files, fs-maps sind nicht Teil dieses Tests.
