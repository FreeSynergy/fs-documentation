# Geplante Komponenten

**Status: Vorschlag (2026-11-06), Programmnamen teils älter als der [Gesamtplan](../programs/apps/roadmap.md): Kanban ist jetzt Teil von Tasks, die Galerie Teil von Files.** Siehe auch [Diagramme](charts.md). Keine davon ist schon gebaut oder im Detail dokumentiert. Die Schichten folgen der bestehenden Struktur: Grundelemente, Widgets, Workbenches.

Wie bei allen Komponenten gehören Gesten nicht dazu; sie kommen vom Frontend (ADR 0037). Die Namen sind Vorschläge.

## Zuerst bauen: von mehreren Programmen genutzt

| Komponente | Schicht | Was sie tut | Genutzt von |
|------------|---------|-------------|-------------|
| `sortable-list` | widgets/data | Elemente umsortieren, auch zwischen Listen; funktioniert auch mit der Tastatur | Kanban, Umfragen, Dateien, Galerie-Alben |
| `share-dialog` | widgets/overlays | Personen und Berechtigungen auswählen | Dateien, Galerie, Kanban, Umfragen, Whiteboard |
| `avatar-group` | widgets/data | Mehrere Personen auf wenig Platz | Kanban, Whiteboard, Messenger |
| `transfer-list` | widgets/data | Laufende Uploads und Downloads mit Fortschritt | Dateien, Galerie, Messenger, Streaming |
| `lightbox` | widgets/overlays | Ein Element im Vollbild zeigen und durch Elemente blättern | Galerie, Dateien, Messenger, Kanban |

## Nach Programm

| Programm | Neu | Wiederverwendet oder geändert |
|----------|-----|-------------------------------|
| **Files** | Workbench `file-manager` (kompakt: `file-picker`); Widgets `file-tile`, `file-preview` | `tree-view`, `list-view`, `grid-view`, `breadcrumb`, `context-menu`, `search-field`; **ändern** `file-upload`: wiederaufnehmbar mit Fortschritt |
| **Tasks (kanban)** | Workbench `kanban-board`; Widgets `board-column`, `task-card`, `checklist` | `sortable-list`, `card`, `drawer`, `tags-input`, `date-picker`, `badge` (Limit erreicht), `timeline` (Aktivität), `message-list` (Kommentare) |
| **Surveys** | Workbenches `survey-builder`, `survey-form`; Widgets `question`, `matrix-question`, `ranking-list` | `field`, `radio-group`, `checkbox`, `rating`, `slider`, `date-input`, `wizard`, `progress`, `chart`, `table` |
| **Files (gallery)** | Workbench `gallery-browser` | `lightbox`, `carousel`, `image`, `video`, `map-view`, `timeline`, `description-list`; **ändern** `gallery`: große Sammlungen, virtuelles Scrollen, Gruppierung nach Datum |
| **Whiteboard** | Widgets `infinite-canvas`, `selection-handles`, `minimap`, `presence-cursors` | `toolbar`, `color-input`, `slider`, `tree-view` (Ebenen), `popover`, `image`; **überarbeiten** Workbench `whiteboard`: englische Variantennamen, kompakte Variante |
| **Streaming** | Workbench `stream-studio`; Widgets `stream-tile`, `level-meter` | `audio`, `video`, `call-controls`, `grid-view`, `message-list`, `badge` (live); **ändern** `media-player`: Live-Modus |

## Blinc als Basis

| Bedarf | In Blinc 0.6 (`.research-blinc`) | Danach |
|--------|----------------------------------|--------|
| `infinite-canvas` | `canvas`-Element mit direktem GPU-Zeichnen | Darauf aufbauen; früh mit vielen Elementen messen |
| `sortable-list` | Drag-Ereignisse existieren in `blinc_layout`; keine fertige sortierbare Liste gesehen | Eigene, Kandidat für einen Beitrag (`todo/upstream.md`) |
| `tree-view` | `tree` in `blinc_cn` | Adapter |
| `media-player`, `video` | `blinc_media`: Player, Frames, Kamera; OpenH264 auf dem Desktop | Live-Modus noch zu prüfen |
| Stiftdruck und Neigung | Fehlt | Beitrag bereits geplant |

Diese Tabelle stammt aus einem kurzen Blick in den Quelltext, nicht aus einem Test.

## Nächster Schritt

Nach den Entscheidungen zum Gesamtplan erhält jede Komponente das übliche Dokumentationsgerüst (`description`, `appearance`, `attributes`, `usage`) und einen Eintrag in `conventions/CONVENTIONS.md` §3.
