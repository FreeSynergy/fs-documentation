# Geplante Komponenten

**Status: Vorschlag (2026-11-06), Programmnamen teils älter als der [Gesamtplan](../programs/apps/roadmap.md): Kanban ist jetzt Teil von Tasks, die Galerie Teil von Files.** Siehe auch [Charts](charts.md). Keine
ist bisher gebaut oder im Detail dokumentiert. Die Ebenen folgen der bestehenden Struktur: Primitives, Widgets, Workbenches.

Wie bei allen Komponenten sind Gesten nicht Teil davon; sie kommen vom Frontend (ADR 0037). Die Namen sind Vorschläge.

## Was es schon gibt (`fs-components` v0.2.0, 2026-11-06)

Veröffentlicht: der Reader, `text-view`, `avatar-group`, `transfer-list`, `sortable-list`, `lightbox`, `share-dialog`. Sie wurden geprüft, aber
ohne echtes Fenster getestet; bisher hat sie niemand von Hand benutzt. **Nicht veröffentlicht, obwohl im selben Tag enthalten:** `charts`, das offene Blocker hat, die fünf Chat-Komponenten,
die noch geprüft werden, und die Kalenderarbeit.

## Zuerst bauen: von mehreren Programmen genutzt

| Komponente | Ebene | Was sie tut | Genutzt von |
|-----------|-------|--------------|---------|
| `sortable-list` | widgets/data | Einträge neu ordnen, auch zwischen Listen; funktioniert auch mit der Tastatur | Kanban, Umfragen, Dateien, Galerie-Alben |
| `share-dialog` | widgets/overlays | Personen und Berechtigungen auswählen | Files, Galerie, Kanban, Umfragen, Whiteboard |
| `avatar-group` | widgets/data | Mehrere Personen auf wenig Platz | Kanban, Whiteboard, Messenger |
| `transfer-list` | widgets/data | Laufende Uploads und Downloads mit Fortschritt | Files, Galerie, Messenger, Streaming |
| `lightbox` | widgets/overlays | Ein Element vollbildschirm zeigen und durch Elemente blättern | Galerie, Files, Messenger, Kanban |

## Nach Programm

| Programm | Neu | Wiederverwendet oder geändert |
|---------|-----|-------------------|
| **Files** | Workbench `file-manager` (kompakt: `file-picker`); Widgets `file-tile`, `file-preview` | `tree-view`, `list-view`, `grid-view`, `breadcrumb`, `context-menu`, `search-field`; **ändern** `file-upload`: wiederaufnehmbar mit Fortschritt |
| **Tasks (Kanban)** | Workbench `kanban-board`; Widgets `board-column`, `task-card`, `checklist` | `sortable-list`, `card`, `drawer`, `tags-input`, `date-picker`, `badge` (Grenze erreicht), `timeline` (Aktivität), `message-list` (Kommentare) |
| **Umfragen** | Workbenches `survey-builder`, `survey-form`; Widgets `question`, `matrix-question`, `ranking-list` | `field`, `radio-group`, `checkbox`, `rating`, `slider`, `date-input`, `wizard`, `progress`, `chart`, `table` |
| **Files (Galerie)** | Workbench `gallery-browser` | `lightbox`, `carousel`, `image`, `video`, `map-view`, `timeline`, `description-list`; **ändern** `gallery`: große Sammlungen, virtuelles Scrollen, Gruppierung nach Datum |
| **Whiteboard** | Widgets `infinite-canvas`, `selection-handles`, `minimap`, `presence-cursors` | `toolbar`, `color-input`, `slider`, `tree-view` (Ebenen), `popover`, `image`; **überarbeiten** Workbench `whiteboard`: englische Variantennamen, kompakte Variante |
| **Assistant** | Workbench `llm-chat`; Widgets `agent-tree`, `tool-call` | `message-list`, `message-composer`, Langtextansicht auf unserem Textkern |
| **Streaming** | Workbench `stream-studio`; Widgets `stream-tile`, `level-meter` | `audio`, `video`, `call-controls`, `grid-view`, `message-list`, `badge` (live); **ändern** `media-player`: Live-Modus |

## Blinc als Grundlage

| Bedarf | In Blinc 0.6 (`.research-blinc`) | Danach |
|------|----------------------------------|------|
| `infinite-canvas` | `canvas`-Element mit direktem GPU-Zeichnen | Darauf aufbauen; früh mit vielen Elementen messen |
| `sortable-list` | Drag-Ereignisse gibt es in `blinc_layout`; keine fertige sortierbare Liste gesehen | Eigene Komponente, Kandidat für einen Beitrag (`todo/upstream.md`) |
| `tree-view` | `tree` in `blinc_cn` | Adapter |
| `media-player`, `video` | `blinc_media`: Player, Frames, Kamera; OpenH264 auf dem Desktop | Live-Modus muss geprüft werden |
| Stiftdruck und Neigung | Fehlt | Beitrag ist schon geplant |

Diese Tabelle stammt aus einem kurzen Blick in den Quellcode, nicht aus einem Test.

## Nächster Schritt

Nach den Entscheidungen zum Fahrplan bekommt jede Komponente das übliche Dokumentationsgerüst
(`description`, `appearance`, `attributes`, `usage`) und einen Eintrag in `conventions/CONVENTIONS.md` §3.
