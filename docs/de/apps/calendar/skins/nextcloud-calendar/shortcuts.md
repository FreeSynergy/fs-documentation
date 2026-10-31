# Nextcloud Calendar - Tastatur-Shortcuts

## Übersicht

Nextcloud Calendar dokumentiert **keine eigenen, app-spezifischen Tastatur-Shortcuts** (Stand: Calendar-App der 5.x-Reihe; ein entsprechender Wunsch in der Community ist seit Jahren offen). Bedient wird mit Maus, Touch und den üblichen Browser-Tasten; Dialoge und Formulare folgen den Standard-Tastaturen der Nextcloud-Vue-Komponenten. Diese Datei listet, was tatsächlich funktioniert, und markiert verbreitet angenommene Shortcuts ausdrücklich als **nicht dokumentiert**.

> Nach Updates an Nextcloud oder der Kalender-App sollte diese Liste erneut geprüft werden.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Bedienelement springen (Kopfzeile, Seitenleiste, Raster) |
| `Shift+Tab` | Zum vorherigen Bedienelement springen |
| `Enter` | Fokussierte Schaltfläche/Link auslösen (z. B. „Heute", Kalender-Eintrag) |
| `Space` | Checkboxen/Schalter umschalten (Kalender ein-/ausblenden) |
| `Esc` | Dialog, Dropdown oder Datumspopup schließen (sofern die Komponente es unterstützt) |
| `F5` / `Strg+R` | Seite neu laden (Kalender wird neu vom Server geladen) |
| `Alt+←` / `Alt+→` | Browser zurück/vor |
| `Strg+F` | Text auf der Seite suchen (Browser, nicht die App-Suche) |
| `Strg+P` | Kalenderansicht ausdrucken (Browser-Druckdialog) |
| `Strg+Plus` / `Strg+Minus` / `Strg+0` | Zoom der Oberfläche |

---

## Navigation im Kalender

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Schaltflächen der Werkzeugleiste und Kalender-Liste ansteuern |
| `Enter` | Ansicht wechseln, Kalender-Aktion öffnen |
| `↑` / `↓` | In Auswahllisten (Ansichts-Menü, Datumspicker, Empfänger-Suche) blättern |
| Klick auf „Heute"/Pfeile | Zum aktuellen bzw. vorherigen/nächsten Zeitraum springen (Maus) |

**Nicht dokumentiert (verbreitet angenommen, aber offiziell nicht vorhanden):**

| Angenommener Shortcut | Status |
|-----------------------|--------|
| `N` oder `C` für neues Ereignis | ❌ Nicht dokumentiert — Plus-Menü oder Klick ins Raster nutzen |
| `T` für „Heute" | ❌ Nicht dokumentiert — Schaltfläche „Heute" nutzen |
| `D` / `W` / `M` für Tag/Woche/Monat | ❌ Nicht dokumentiert — Ansichts-Menü nutzen |
| `←` / `→` für vorheriger/nächster Zeitraum | ❌ Nicht dokumentiert |
| `/` für die Suche | ❌ Nicht dokumentiert — Suchfeld anklicken oder `Tab` nutzen |
| `Entf` zum Löschen eines Termins | ❌ Nicht dokumentiert — Dialog mit „Löschen" nutzen |

---

## Ereignis erstellen und bearbeiten

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Felder im Ereignis-Editor durchlaufen (Titel, Zeit, Ort, Notiz) |
| `Enter` | Standardaktion auslösen („Speichern", Teilnehmer-Zugabe bestätigen) |
| `Space` | Switches umschalten (z. B. „ganztägig"), Auswahl öffnen |
| `↑` / `↓` | Werte in Datums-/Zeitfeldern und Auswahlen ändern |
| `Backspace` / `Entf` | Feldinhalt löschen |
| `Esc` | Editor/Dialog schließen (ungespeicherte Änderungen können verworfen werden) |

**Nicht dokumentiert:**

| Angenommener Shortcut | Status |
|-----------------------|--------|
| `Strg+Enter` zum Speichern | ❌ Nicht dokumentiert — `Enter` im Formular oder Speichern-Button |
| Tastatursteuerung für Drag & Drop (Termin verschieben) | ❌ Nicht dokumentiert — Datum/Uhrzeit im Editor ändern |
| `Strg+Z` Rückgängig im Kalender | ❌ Nicht dokumentiert — kurz nach dem Löschen die „Rückgängig"-Meldung nutzen |

### Erstellen per Maus/Touch (kein Shortcut, aber der schnelle Weg)

| Geste | Funktion |
|-------|----------|
| Klick auf freien Slot | Neuer Termin mit dieser Startzeit |
| Aufziehen über Slots | Termin mit gewählter Zeitspanne |
| Termin ziehen / Rand ziehen | Verschieben / Dauer ändern |
| Langes Drücken (Touch) | Termine in Mobilansichten antippen und im Editor ändern |

---

## Dialoge (Freigabe, Kalendereinstellungen, Umfragen)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Felder und Empfängerliste ansteuern |
| Text eingeben im Suchfeld | Nutzer/Gruppen/Räume suchen ( debounce, keine Kürzel) |
| `↑` / `↓` | Vorschlagsliste durchlaufen |
| `Enter` | vorgeschlagenen Empfänger auswählen bzw. Dialog bestätigen |
| `Esc` | Dialog ohne Änderung schließen |

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Strg`.

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden |
| `Cmd+P` | Drucken |
| `Cmd+F` | Text auf der Seite suchen (Browser) |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | Zoom |
| `Cmd+←` / `Cmd+→` | Browser zurück/vor |
| `Esc` | Dialog schließen |

**Nicht dokumentiert:** `Cmd+N` (neuer Termin), `Cmd+D/W/M` (Ansichten), `Cmd+Z` (Rückgängig) — diese Shortcuts stellt die Kalender-App nicht bereit.

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Kopfzeile, Seitenleiste, Werkzeugleiste und Dialoge vollständig erreichbar |
| `Enter` / `Space` | Aktionen auslösen (Kalender ein-/ausblenden, Dialoge öffnen) |
| `Esc` | Overlays und Menüs verlassen |
| `↑` / `↓` | Auswahlen und Vorschlagslisten bedienen |

Hinweis: Das Zeit-Raster selbst ist nicht vollständig tastaturbedienbar. Termine lassen sich aber über den Editor (Datum-/Zeitfelder) vollständig per Tastatur anlegen und korrigieren.

---

## Zusammenfassung

Nextcloud Calendar bietet **keine anwendungsspezifischen Shortcuts**. Nutzbar sind:

- **Browser-Tasten** für Neuladen, Drucken, Zoom und Textsuche
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in Dialogen, Formularen und Vorschlagslisten
- **Klick, Ziehen und Touch-Gesten** für das Erstellen und Verschieben von Terminen

Der schnellste „Kürzel-Ersatz" ist die Mausarbeit: Aufziehen im Raster erzeugt Termine in Sekunden, und Wiederserie-Vorlagen (Wiederholeinstellungen) ersetzen viele Einzelanlegen-Schritte.
