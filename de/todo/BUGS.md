# Bekannte Bugs

[← Zurück zum Index](../INDEX.md) | [TODO](TODO.md)

---

## Kritisch (🔴)

| Bug | Beschreibung | Fix |
|---|---|---|
| Window X-Button | Funktioniert nur im maximierten Zustand | Custom-Chrome fixen oder system decorations |
| Keine Speicherung | NICHTS wird persistent gespeichert — kein SQLite implementiert | Phase A1 |
| Store TOML Parse-Error | Catalog TOML hat Inline-Record-Fehler | Format fixen |

## Hoch (🟡)

| Bug | Beschreibung | Fix |
|---|---|---|
| Widgets nicht draggable | Können nicht per Drag & Drop verschoben werden | DraggableWidget (Phase D1) |
| Fenster/Widgets nicht resizable | Keine Resize-Handles an den Rändern | ResizableContainer (Phase D2) |
| Scrollbars fehlen | An vielen Stellen kein Scroll möglich | .fsn-scrollable überall (Phase A4) |
| Theme-Kontraste | Teilweise miserabler Kontrast, Text kaum lesbar | Theme-Überarbeitung (Phase B2) |

## Mittel (🟠)

| Bug | Beschreibung | Fix |
|---|---|---|
| Bilder nicht uploadbar | Kein Hintergrund-Upload möglich | FileEngine (Phase D4) |
| Store: Nichts installierbar | Install-Button funktioniert nicht | Phase C2-C4 |
| Alter Container Manager-Code | Nutzt Podman-Socket (funktioniert nicht) | Phase E1 |

## Mittel (🟠) — Store UI

| Bug | Beschreibung | Fix |
|---|---|---|
| Dropdown öffnet nach oben | Der Dropdown-Button bei installierten Paketen öffnet das Menü nach oben statt nach unten | Dropdown-Richtung fixen: immer nach unten |
| Löschen-Option falsche Farbe | Der "Löschen"-Eintrag im Dropdown hat keine Hintergrundfarbe; sollte Rot + gleiche Schrift wie die Einträge darüber | Hintergrund rot, Schrift weiß |
| Kein Bestätigungsdialog beim Löschen | Klick auf "Löschen" löscht sofort ohne Bestätigung | Modal: "Wirklich löschen?" mit Bestätigen / Abbrechen |
| Detailansicht zeigt Vollständigkeits-Check | Die Detailansicht zeigt ob alle Felder gesetzt sind — das ist für den Nutzer irrelevant. Stattdessen sollen die Paket-Metadaten angezeigt werden (Typ, Pfad, Autor, Tags, Abhängigkeiten usw.) | Detailansicht mit ResourceMeta befüllen |

## Gering (🟢)

| Bug | Beschreibung | Fix |
|---|---|---|
| Leere Menüpunkte | Einige Menüpunkte ohne Funktion | Phase K4 |
| Stubs im Code | `todo!()`, `unimplemented!()` | Phase K9 |
