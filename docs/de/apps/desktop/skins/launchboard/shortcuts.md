# LaunchBoard - Tastatur-Shortcuts

## Übersicht

LaunchBoard dokumentiert **keine freien Anwendungs-Shortcuts** für das Bauen von Boards. Bedient wird über Maus, Touch und die Standard-Tastatur der Webkomponenten (Dialoge, Formulare, Listen). Diese Datei listet, was tatsächlich funktioniert, und markiert verbreitet angenommene Tastenkombinationen ausdrücklich als **nicht vorhanden**. Da der Hersteller keine Shortcut-Referenz öffentlich führt, gelten die hier beschriebenen Grundlagen als das, was in aktuellen Versionen beobachtbar ist; Details prüft man im Kundenportal.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Bedienelement springen |
| `Shift+Tab` | Zum vorherigen Bedienelement springen |
| `Enter` | Ausgewählte Schaltfläche auslösen |
| `Space` | Schalter umschalten, markierte Kachel aktivieren |
| `Esc` | Dialog, Dropdown oder Menü schließen |
| `F5` / `Ctrl+R` | Seite neu laden |
| `Alt+←` / `Alt+→` | Browser zurück/vor |
| `Strg+P` | Board ausdrucken |
| `F12` | Entwicklerwerkzeuge (Fehlersuche bei Widget-Anfragen) |

---

## Navigation auf dem Board

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Kacheln und Links in Lesereihenfolge ansteuern |
| `Enter` | Fokussierte App-Kachel öffnet die Ziel-URL |
| `↑` / `↓` | In Dropdowns (Board-Auswahl, Integrations-Auswahl) blättern |
| `↑` / `↓` | In der Autocomplete-Liste der Suche blättern |
| `Enter` | Suchvorschlag ausführen |
| `Esc` | Vorschläge schließen, Fokus verlassen |
| `Backspace` | Suchtext löschen, wenn das Feld fokussiert ist |
| `Home` / `Ende` | Seitenanfang / -ende (Browser) |

**Nicht vorhanden:**

| Erwarteter Shortcut | Status |
|---------------------|--------|
| `/` für Suchfeld | ❌ Nicht dokumentiert – Feld muss angeklickt oder per `Tab` erreicht werden |
| `1`–`9` für Boards | ❌ Nicht vorhanden |
| Buchstabensprung zu einer Kachel | ❌ Nicht vorhanden |
| `g` dann `b` (Board wechseln) | ❌ Nicht vorhanden |

---

## Bearbeitung (Board und Widgets)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Schwebende Kachel-Werkzeuge (Bearbeiten, Duplizieren, Entfernen) erreichen |
| `Enter` | Einstellungsdialog der fokussierten Kachel öffnen |
| `Esc` | Dialog ohne Speichern schließen |
| `Enter` (im Dialog) | Standardaktion „Speichern“ auslösen |
| `Esc` (im Bearbeitungsmodus) | Modus verlassen, sofern kein Dialog offen ist |
| `Tab` / `Shift+Tab` | Felder innerhalb des Dialogs durchlaufen |
| `Space` | Auswahlliste öffnen, Schalter umschalten |
| `↑` / `↓` | Werte in Zahlenfeldern und Auswahlen ändern |

**Nicht vorhanden:**

| Erwarteter Shortcut | Status |
|---------------------|--------|
| `e` für Bearbeitungsmodus | ❌ Nicht vorhanden – nur über die Schaltfläche in der Kopfzeile |
| `Ctrl+Z` Rückgängig im Board | ❌ Nicht vorhanden – Layoutänderungen werden sofort gespeichert |
| `Entf` Kachel löschen | ❌ Nicht vorhanden – Werkzeugleiste oder Rechtsklick nutzen |
| Pfeiltasten zum Verschieben einer Kachel | ❌ Nicht vorhanden – Drag & Drop mit Maus oder Touch |
| `Ctrl+C` / `Ctrl+V` Kachel kopieren | ❌ Nicht vorhanden – „Duplizieren“ im Kontextmenü nutzen |
| `Ctrl+S` Speichern | ❌ Nicht vorhanden – es gibt keinen separaten Speicherschritt |

### Kachel verschieben und vergrößern

| Geste | Funktion |
|-------|----------|
| Ziehen am Greifpunkt (oben links) | Kachel im Raster verschieben, Zielbereich rastet ein |
| Ziehen an Ecke/Unterkante | Breite und Höhe in Rasterschritten ändern |
| Langes Drücken (Touch) | Kachel aufnehmen (Mobil-Layout) |
| Board-Optionen → Spaltenanzahl | Rasterdichte ändern, statt Kacheln zu stapeln |
| Ausrichtungslinien einblenden | Kanten an benachbarten Kacheln ausrichten |

---

## Suche und Startseitenfunktionen

| Shortcut | Funktion |
|----------|----------|
| Klick in die Suchleiste + Text | Treffer aus Boards, Apps und Links |
| `↑` / `↓` | Trefferliste durchlaufen |
| `Enter` | Hervorgehobenen Treffer öffnen oder Websuche starten |
| `Esc` | Suchfeld leeren bzw. Vorschläge schließen |

Kurzkommandos im Suchtext (Präfix je Suchmaschine) ersetzen keine Shortcuts; sie sind Teil des Suchfelds.

---

## Instanz- und Nutzerverwaltung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Tabellenzeilen und Aktionen ansteuern (Nutzer, Integrationen) |
| `Enter` | Bearbeiten-Dialog des ausgewählten Eintrags öffnen |
| `Esc` | Dialog schließen |
| `↑` / `↓` | Auswahlen (Rolle, Integrationstyp) wechseln |
| Text im Filterfeld | Liste einschränken – Fokus muss geklickt werden |

**Nicht vorhanden:** `/` zum Filtern, `Ctrl+F` als Anwendungs-Suche (der Browser durchsucht nur sichtbaren Text).

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Ctrl`.

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden |
| `Cmd+P` | Drucken |
| `Cmd+F` | Text auf der Seite suchen (Browser) |
| `Cmd+K` | Adressleiste fokussieren (Browser) |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang / -ende |
| `Cmd+Plus` / `Cmd+Minus` | Zoom der Oberfläche |
| `Cmd+0` | Zoom zurücksetzen |
| `Esc` | Dialog schließen |

**Nicht vorhanden:** `Cmd+E` (Bearbeiten), `Cmd+/` (Suchfeld), `Cmd+Z` (Layout rückgängig), `Cmd+D` (Duplizieren).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Kopfzeile, Kacheln, Dialogfelder erreichen |
| `Enter` / `Space` | Kachelaktionen und Schalter auslösen |
| `Esc` | Overlays und Menüs verlassen |
| `↑` / `↓` | Auswahlen und Vorschlagslisten bedienen |
| `Shift+Tab` | Rückwärts navigieren |

**Einschränkung**: Das Anordnen von Kacheln ist nur mit Zeigegerät möglich; es gibt keine Tastaturalternative für Verschieben und Skalieren.

---

## Browser- und Identity-Provider-Tasten (beim Login)

Der Login läuft oft über einen externen OIDC-Anbieter; dort gelten dessen Tasten (z. B. Tab-Navigation im Formular, `Enter` zum Absenden). Passworthilfen des Browsers (`Cmd+Shift+L` in manchen Browsern für Passwortverwaltung) sind Browserfunktionen, keine LaunchBoard-Funktionen.

---

## Zusammenfassung

LaunchBoard bietet **keine anwendungsspezifischen Shortcuts**. Nutzbar sind:

- **Browser-Tasten** für Neuladen, Drucken, Zoom und Textsuche
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in Dialogen, Menüs und Vorschlagslisten
- **Drag & Drop und Touch-Gesten** für jede Layout-Arbeit

Kurze Wege entstehen über die Organisation: wenige Boards, klare Kachelnamen, eine eingestellte Standard-Suchmaschine und häufig genutzte Board-Favoriten in der Kopfzeile.
