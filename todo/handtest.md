# Handtest: fs-people-app und fs-tasks-app (Stand 2026-11-07)

Diese Anleitung ist für Kal. Alle Befehle unten habe ich auf diesem Rechner selbst ausgeführt (siehe letzter Abschnitt).
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

---

## Teil 1: fs-people-app (Personen)

**Zweig:** `gui` im Repo `fs-people` (Stand beim Test: Commit `67d0da6`).

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
8. **Fenster klein ziehen:** Bei sehr schmalem Fenster (ca. 420 Pixel) rutscht die Einzelansicht **unter** die Liste, statt daneben zu stehen. Nichts darf überlappen oder abgeschnitten werden, die E-Mail-Spalte darf mit „...“ gekürzt sein.
9. **Menü:** Diese App hat bisher **keine Menüleiste**, nur die Knöpfe im Fenster.

### Das geht bekanntermaßen noch nicht (steht so in der DESIGN.md)
- Gruppen und ihre Mitglieder, Beziehungen zwischen Personen, „gleiche Person“-Vorschläge, Rollen vergeben, KI-Markierung setzen.
- Bearbeiten von Spitznamen, Titeln, Adressen, Links, Notizen, Stichwörtern (die Daten bleiben erhalten, nur nicht änderbar).
- „Sensibel“-Markierung setzen. Karten mit dieser Markierung lehnt der Speicher bisher ab, weil er **nicht verschlüsselt** ist (der Schlüsselverwalter, ADR 0024, fehlt noch). Du wirst so etwas im Test nicht erzeugen können.
- Dateiauswahl-Fenster für Import und Export: nur Pfade auf der Kommandozeile.
- Rückgängig, Live-Aktualisierung (Änderungen eines anderen Programms siehst du erst nach neuem Laden), Anmeldung (der Benutzer ist fest „owner“), Entwurf bleibt nach Schließen nicht erhalten.
- Die Liste lädt 200 Personen, mehr über „Show more“. Ein langsamer Server kann das Fenster bis zu 30 Sekunden einfrieren (das ist kein Absturz).
- Beim vCard-Export steht bei aus Version 3.0 eingelesenen Karten manchmal weiter `VERSION:3.0`.

### Auffälliges notieren
Eine Zeile pro Fund in `~/fs-handtest/funde-people.txt`, Form: `Was ich geklickt habe -> was ich erwartet habe -> was passiert ist`.

---

## Teil 2: fs-tasks-app (Aufgaben)

**Zweig:** `gui` im Repo `fs-tasks` (Stand beim Test: Commit `08c832d`).

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
10. **Fenster klein ziehen:** Bei ca. 400 Pixel Breite rutscht die Einzelansicht unter die Liste, die Spalten werden gekürzt („...“). In der Statusansicht läuft die Reihe der Spalten über den Rand (Failed, Cancelled sind dann nur halb zu sehen), das ist bekannt. Ein sehr kleines Fenster zeigt laut Entwurf eine „kompakte Ansicht“ mit offenen Aufgaben.

### Das geht bekanntermaßen noch nicht (steht so in der DESIGN.md)
- **Keine echten Boards/Kanban:** nur fünf feste Spalten (der Status der Aufgabe), keine eigenen Spalten, Reihenfolge innerhalb einer Spalte (richtet sich nach Fälligkeit; zieht man eine Karte woandershin, springt sie zurück und das wird gesagt), keine Bahnen, keine Spaltenlimits.
- Aufgaben zuweisen, Beziehungen zwischen Aufgaben, Checklisten, Zeitleiste, Kommentare, Anhänge, Erinnerungen, Rückgängig, Wiederholung bearbeiten.
- Wiederkehrende Aufgaben: Status lässt sich nicht verschieben (wird mit Grund abgelehnt).
- Ein Status, der aus den Teilnehmern berechnet wird, wird beim Verschieben fest und kann in der App nicht zurück.
- Fälligkeit ohne Uhrzeit, Zeitzonenwahl, Dateiauswahl-Fenster für Import/Export.
- Keine Live-Aktualisierung, keine Wiederverbindung (stoppt der Server, kommt bei der nächsten Aktion ein Fehler), keine Anmeldung („meine nächsten Aufgaben“ sind alle offenen). Ein langsamer Server kann das Fenster bis zu 30 Sekunden einfrieren.
- Karten mit „sensibel“-Markierung werden nie geöffnet und beim Export weggelassen (mit `--export-sensitive <uid>` freizugeben). Du wirst so etwas im Test nicht erzeugen können.

### Auffälliges notieren
Eine Zeile pro Fund in `~/fs-handtest/funde-tasks.txt`, gleiche Form wie oben.

---

## Was ich getestet habe und was nicht
**Getestet, hat geklappt (2026-11-07, frische Klone von `https://github.com/FreeSynergy/...` unter `.scratch/t4-handtest/`, Zweig `gui`):**
- **Frischer Klon baut:** ja, beide. fs-people in 1:51 min, fs-tasks danach in 26 s (`-j 4`, gemeinsames Build-Verzeichnis). Abhängigkeiten kommen von Git (fs-store `v0.2.0` und fs-interfaces `v0.34.0` per Tag). Die GUI-Bausteine (`fs-components`) sind per **Commit-Nummer** (`rev=8c38a3b1...`) festgehalten, nicht per Tag: das gleicht dem Ziel „nur Tags“ nicht ganz, ist aber ohne lokale Pfade. Pfad-Abhängigkeiten gibt es nur zwischen den Crates innerhalb desselben Repos.
- **Klonen über HTTPS ohne Anmeldung** ging (Repos waren erreichbar).
- **Server starten:** ja. Der Socket erscheint (`people.sock`, `tasks.sock`, Rechte 600). Der Datenordner muss Rechte 700 haben, sonst: „must belong to this user alone (0700)“ (hatte ich beim ersten Versuch falsch, daher das `-m 700` oben). Nach `Strg+C` (SIGINT) verschwindet der Socket, die leere `.lock`-Datei bleibt (harmlos, wird durch das Aufräumen mit entfernt).
- **App im Bildschirmfoto-Modus** (`--snapshot`): zeigte in beiden Fällen die Oberfläche wie oben beschrieben, People mit 1000x700 und 420x600, Tasks Liste mit 1100x700 und 400x600, Tasks Statusansicht mit 1100x700. Ich habe die PNG-Dateien angesehen.
- **Import und Export per Kommandozeile:** people (2 Personen importiert, zweiter Import „0 imported, 2 already known“, Export schreibt gültige vCard 4.0, zweiter Export in dieselbe Datei wird abgelehnt) und tasks (3 importiert, Export enthält 3 `VTODO`, Daten blieben nach Neustart des Servers erhalten).
- Eine ICS-Datei an `fs-people-app --import` gibt sauber „holds no vCard“ (Exitcode 1).

**Nicht getestet:**
- **Kein echtes Fenster** (`DISPLAY`/Wayland wäre da gewesen, aber laut Auftrag nur du). Klicks, Tippen, Tastatur, Verschieben in der Statusansicht, Anlegen/Bearbeiten/Löschen im Fenster, Menü-Klicks und das echte Verhalten beim Kleinziehen sind ungetestet. Was oben bei „klick das“ steht, folgt der DESIGN.md und den Bildschirmfotos, nicht eigener Bedienung. Der Unterschied „kleines Fenster“ ist nur über Bildschirmfotos belegt, nicht über das Ziehen in einem echten Fenster.
- Sensible Karten/Aufgaben, `--export-sensitive`, `--view status` im echten Fenster, Wiederholungsaufgaben, sehr lange Listen (Show more).
- fs-calendar, fs-files, fs-maps sind nicht Teil dieses Tests.
