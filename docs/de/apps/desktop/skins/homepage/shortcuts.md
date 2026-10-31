# Homepage - Tastatur-Shortcuts

## Übersicht

Homepage bringt **keine anwendungseigenen Tastatur-Shortcuts** mit. Es gibt keinen Bearbeitungsmodus, keine Befehlspalette und keine Springtasten zu Gruppen. Bedient wird über die Browser-Tastatur und die üblichen Eingabefeld-Tasten; geändert wird in YAML-Dateien, wofür der eigene Editor zuständig ist. Diese Datei listet, was tatsächlich funktioniert, und markiert verbreitet angenommene Tasten ausdrücklich als **nicht vorhanden**.

> Stand: aktuelle Homepage-Versionen (2.x). Nach Updates sollte diese Liste geprüft werden.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Link / Eingabefeld springen |
| `Shift+Tab` | Zum vorherigen Element springen |
| `Enter` | Fokussierte Kachel öffnen, Suchanfrage absenden |
| `Space` | Fokussiertes Element auslösen |
| `Esc` | Suchvorschläge schließen, Fokus aus dem Feld nehmen |
| `F5` / `Ctrl+R` | Seite neu laden (Layout und Widgets werden neu gerendert) |
| `Strg+P` | Übersicht ausdrucken |
| `Alt+←` / `Alt+→` | Browser zurück/vor (relevant bei geöffnetem Zieldienst im selben Tab) |
| `F12` | Entwicklerwerkzeuge (Fehlersuche bei Widget-Requests) |

---

## Navigation auf der Seite

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Kacheln in Lesereihenfolge ansteuern |
| `Enter` | Angezeigte Ziel-URL des Dienstes öffnen |
| `↑` / `↓` | In der Vorschlagsliste der Suchleiste blättern |
| `Enter` | Hervorgehobenen Suchvorschlag ausführen |
| `Backspace` | Suchtext löschen, wenn das Feld fokussiert ist |
| `Home` / `Ende` | Seitenanfang / -ende (Browser) |
| `Ctrl+F` | Text auf der Seite suchen (Browser, nicht Homepage) |

**Nicht vorhanden:**

| Erwarteter Shortcut | Status |
|---------------------|--------|
| `/` für Suchfeld | ❌ Nicht vorhanden – Feld muss angeklickt oder per `Tab` erreicht werden |
| `1`–`9` für Gruppen | ❌ Nicht vorhanden |
| Buchstabensprung zu einer Kachel | ❌ Nicht vorhanden |
| `g` dann `g` (Gruppe wechseln) | ❌ Nicht vorhanden |
| Sprungmarke pro Widget | ❌ Nicht vorhanden |

---

## Bearbeitung (Dashboard, Widgets)

Die Oberfläche von Homepage ist **schreibgeschützt**. Alle Änderungen entstehen in Dateien.

| Aktion | Weg | Shortcut |
|--------|-----|----------|
| Kachel hinzufügen | Eintrag in `config/services.yaml` | ❌ keiner in Homepage |
| Widget aktivieren | `_<dienst>` an der Kachel ergänzen | ❌ keiner |
| Reihenfolge ändern | `layout` in `config/settings.yaml` | ❌ keiner |
| Icon ändern | `icon:`-Schlüssel schreiben | ❌ keiner |
| Änderungen wirksam machen | Seite neu laden (`F5`) | ✅ Browser-Taste |
| Konfiguration prüfen | Container-Log lesen | ❌ keine UI-Ansicht |

**Nicht vorhanden:**

| Erwarteter Shortcut | Status |
|---------------------|--------|
| `e` für Bearbeitungsmodus | ❌ Nicht vorhanden – es gibt keinen Bearbeitungsmodus |
| `Entf` Kachel löschen | ❌ Nicht vorhanden – Eintrag in der YAML löschen |
| `Ctrl+Z` Änderung rückgängig | ❌ Nicht vorhanden – Versionskontrolle (Git) nutzen |
| `Ctrl+S` speichern | ❌ Nicht vorhanden – Dateien werden außerhalb gespeichert |
| Pfeiltasten zum Verschieben | ❌ Nicht vorhanden – kein Drag & Drop, kein Raster-Editing |

---

## Suche

| Shortcut | Funktion |
|----------|----------|
| Text im Suchfeld + `Enter` | Suchanfrage beim konfigurierten Provider öffnen |
| `↑` / `↓` | Vorschläge durchlaufen (`searchSuggestion`) |
| `Esc` | Vorschläge ausblenden |
| `Enter` (leeres Feld) | ❌ Keine Funktion |

**Hinweis**: Die Suchleiste wird nur angezeigt, wenn in `config/settings.yaml` ein Provider (`providers.search`) gesetzt ist. Eine lokale Suche über alle Dienste gibt es nicht.

---

## Konfigurationsdateien (Editor-Hinweise)

Diese Tasten stammen aus dem verwendeten Texteditor, nicht aus Homepage. Sie sind hier aufgeführt, weil die Arbeit an Homepage fast ausschließlich darin besteht:

| Shortcut | Funktion |
|----------|----------|
| `Ctrl+Shift+P` (VS Code) | Befehlspalette, YAML-Formatierung anstoßen |
| `Ctrl+Shift+I` / `Ctrl+Alt+F` | YAML-Datei formatieren |
| `Ctrl+K Ctrl+S` | Tastaturbelegung des Editors öffnen |
| `Strg+Shift+V` | Markdown-Vorschau für Notizen zur Config |
| `Ctrl+F` / `Ctrl+H` | Suchen/Ersetzen in `services.yaml` |

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Strg`.

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden (neue Config wird gerendert) |
| `Cmd+P` | Drucken |
| `Cmd+F` | Text auf der Seite suchen (Browser) |
| `Cmd+K` | Adressleiste fokussieren (Browser) |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang / -ende |
| `Cmd+Plus` / `Cmd+Minus` | Zoom |
| `Cmd+0` | Zoom zurücksetzen |
| `Esc` | Suchvorschläge schließen |

**Nicht vorhanden:** `Cmd+E` (Bearbeiten), `Cmd+/` (Suchfeld), `Cmd+B` (Sidebar – es gibt keine Sidebar), `Cmd+Z` (Änderung rückgängig).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Kopfzeile, Suchfeld und alle Kacheln erreichen |
| `Enter` / `Space` | Dienst öffnen |
| `Esc` | Vorschlagsliste verlassen |
| `↑` / `↓` | Suchvorschläge bedienen |
| `Shift+Tab` | Rückwärts navigieren |
| Browser-Zoom | Ohne Funktionsverlust nutzbar |

---

## Serverseitige Tasten und Befehle (Abkürzung statt Shortcut)

Für den Betrieb gibt es keine Tastenkombinationen, sondern Kommandos; vollständig in [../gethomepage/shortcuts.md](../gethomepage/shortcuts.md):

| Befehl | Funktion |
|--------|----------|
| `docker compose restart homepage` | Container neu starten (bei geändertem `.env`) |
| `docker logs -f homepage` | Konfigurationsfehler ansehen |
| `docker exec homepage cat /app/config/settings.yaml` | Aktive Konfiguration prüfen |

---

## Zusammenfassung

Homepage bietet **keine eigenen Shortcuts**. Nutzbar sind:

- **Browser-Tasten** für Neuladen, Drucken, Zoom und Textsuche
- **`Tab`, `Enter`, `Esc`, `↑`/`↓`** in der Suchleiste und auf Kacheln
- **Dateibearbeitung im eigenen Editor** für jede Änderung am Dashboard

Kurze Wege entstehen durch Konfigurationsdisziplin: klar benannte Gruppen, wenige, aussagekräftige Widgets und eine eingerichtete Suchleiste ersetzen jede Tastenkombination.
