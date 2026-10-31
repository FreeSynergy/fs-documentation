# Homer - Tastatur-Shortcuts

## Übersicht

Homer bringt **keine eigenen Tastatur-Shortcuts** mit und dokumentiert keine. Die Seite besteht aus Links und einem Suchfeld; bedient wird mit den üblichen Browser-Tasten. Diese Datei listet, was tatsächlich verfügbar ist, und markiert verbreitet erwartete Shortcuts ausdrücklich als **nicht vorhanden**.

> Stand: aktuelle Homer-Versionen (v23/v24). Details können sich ändern; maßgeblich ist die mitgelieferte Dokumentation der eingesetzten Version.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Link bzw. Feld springen (Kopfzeile, Icon-Links, Suchfeld, Kacheln) |
| `Shift+Tab` | Vorheriges Element wählen |
| `Enter` | Fokussierten Link öffnen |
| `Esc` | Kein Verhalten in Homer; bricht allenfalls einen Browserdialog ab |
| `F5` / `Ctrl+R` | Neu laden, dadurch wird `config.yml` erneut geladen |
| `Alt+←` | Zurück (Browser), hilfreich nach dem Klick auf eine Kachel |
| `Strg+P` | Startseite ausdrucken |
| `Strg+D` | Startseite als Lesezeichen speichern |

---

## Navigation auf der Seite

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Gruppen und Kacheln in Lesereihenfolge ansteuern |
| `Enter` | Kachel öffnet das eingestellte Ziel (oft neuer Tab) |
| `Pos1` / `Ende` | Seitenanfang / Seitenende |
| `↑` / `↓` | Bildlauf (Standard des Browsers, keine Sprungliste) |
| `Leertaste` | Bildlauf abwärts (wenn kein Feld fokussiert ist) |
| `Shift+Leertaste` | Bildlauf aufwärts |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `/` für das Suchfeld | ❌ Nicht vorhanden — Feld muss angeklickt oder durchgetabbt werden |
| Ziffern `1`–`9` für Kacheln | ❌ Nicht vorhanden |
| Buchstaben-Schnellstart für eine Gruppe | ❌ Nicht vorhanden |
| Sprung zu Gruppe per `g` + Buchstabe | ❌ Nicht vorhanden — es existieren keine Anker-Sprünge |

---

## Suche

| Shortcut | Funktion |
|----------|----------|
| Klick ins Suchfeld + Text | Filtert Kacheln sofort (Name und `keywords`) |
| `Backspace` | Zeichen aus dem Suchtext entfernen |
| `Strg+A` | Suchtext markieren (Standard im Eingabefeld) |
| `Enter` | Kein eigener Effekt — Homer öffnet keinen Treffer, sondern zeigt nur die Filterliste |
| `Esc` | Leert das Feld nicht automatisch; Text mit `Strg+A` und `Entf` löschen |
| `Tab` | Aus dem Suchfeld heraus zur ersten Kachel springen |

**Hinweis**: Die Suche ist ein reiner Filter. Es gibt keine Vorschlagsliste, die mit Pfeiltasten durchlaufen werden könnte.

---

## Bearbeitung

Homer hat **keinen Bearbeitungsmodus** und keine Oberfläche zur Änderung der Seite.

| Shortcut | Funktion |
|----------|----------|
| — | ❌ Kein `e` für einen Editiermodus |
| — | ❌ Kein `Entf` zum Löschen einer Kachel |
| — | ❌ Kein `Strg+Z` (nichts wird in der Seite geändert) |
| — | ❌ Keine Pfeiltasten zum Verschieben von Kacheln |

Änderungen entstehen in `assets/config.yml` und werden durch Neuladen wirksam:

| Schritt | Weg |
|--------|-----|
| Datei bearbeiten | Editor, Git, Deployment |
| Wirksam machen | Seite neu laden (`F5` / `Ctrl+R`, Mac: `Cmd+R`) |
| Sichern | `git commit` oder Download der Konfiguration, falls aktiviert |

---

## Konfigurationsänderung außerhalb der Seite

| Schritt | Typischer Weg |
|---------|---------------|
| Datei öffnen | `assets/config.yml` im Editor oder im Git-Client |
| Änderung prüfen | `git diff` ausführen, danach die Seite neu laden |
| Ausrollen | Deployment, Volume-Tausch oder `git pull` auf dem Host |

## Icon-Links und Kopfzeile
| Shortcut | Funktion |
|----------|----------|
| `Tab` | Icon-Links in der Kopfzeile erreichen |
| `Enter` | Verknüpfung im eingestellten Ziel öffnen |
| `Shift+Klick` / `Strg+Klick` | Link in neuem Tab öffnen (Browser) |
| `Mittlere Maustaste` | Link in neuem Tab öffnen (Browser) |

---

## Dialoge (nur Browserdialoge)

| Shortcut | Funktion |
|----------|----------|
| `Esc` | Download- oder Bestätigungsdialog des Browsers schließen |
| `Enter` | Dialog bestätigen |
| `Tab` | Zwischen Dialogschaltflächen wechseln |

Der Konfigurations-Download erzeugt einen Browserdialog; Homer selbst öffnet keine Dialogfenster.

---

## Mac-Varianten

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden (neue Konfiguration laden) |
| `Cmd+F` | Text auf der Seite suchen (Browser) |
| `Cmd+T` | Neuer Tab |
| `Cmd+Klick` | Kachel in neuem Tab öffnen |
| `Cmd+D` | Lesezeichen anlegen |
| `Cmd+P` | Drucken |
| `Cmd+Plus` / `Cmd+Minus` | Zoom |
| `Cmd+0` | Zoom zurücksetzen |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang / -ende |

**Nicht vorhanden:** `Cmd+/` (Suchfeld), `Cmd+E` (Bearbeiten), `Cmd+Z` (Rückgängig).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Alle Kacheln und Links erreichbar |
| `Enter` | Link auslösen |
| `↑` / `↓` / `Leertaste` | Inhalt scrollen |
| `Pos1` / `Ende` | Schnell an den Anfang oder das Ende |
| `Shift+Tab` | Rückwärts navigieren |

Da Homer nur Links rendert, ist die Tastaturbedienung vollständig; es gibt keine komplexen Bedienelemente, die Mauskenntnisse erfordern.

---

## Zusammenfassung

Homer bietet **keine anwendungsspezifischen Shortcuts**. Nutzbar sind:

- **Browser-Tasten** für Neuladen, Textsuche, Drucken, Zoom und Lesezeichen
- **`Tab`, `Enter`** zum Erreichen und Öffnen von Kacheln
- **Tippen im Suchfeld** als einzige Interaktion der Seite

Alle Änderungen an der Struktur passieren in der Konfigurationsdatei — dort ersetzt der Editor jede Tastenkombination.
