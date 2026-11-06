# Whiteboard — Design

**Status: Vorschlag (2026-11-06).** Zurück zum [Gesamtplan](../roadmap.md) · [Anforderungen](requirements.md).

Das Programm heißt `FreeSynergy.Whiteboard` (`fs-whiteboard`). Der Doku-Ordner heißt noch `whiteboards`; die Umbenennung in Anlehnung an ADR 0017 steht aus, da in diesem Ordner gerade anderes Werk läuft.

## Idee

Eine unendliche Fläche, auf der Menschen zeichnen, Formen platzieren und Notizen schreiben, allein oder gemeinsam. Jedes Element ist ein Objekt mit einer ID, sodass Elemente durchsucht, referenziert und wiederverwendet werden können. Ein Board ist nicht nur ein Bild.

## Daten

| Teil | Standard | Hinweise |
|------|----------|----------|
| Board | AS2 `Collection` | |
| Element: Form, Verbindung, Notiz, Bild, Strich | ❌ keiner | **Eigene Spezifikation** ([Standards](../../../data/standards.md) hält die Lücke fest) |
| Text in Notizen | Dasselbe Textmodell wie im Wiki (ADR 0033, 0042) | |
| Bild auf einem Board | Verweis auf ein Objekt von `fs-files` | |
| Handschrift | InkML ⚠️ | Bisher schwache Belege; vor der Nutzung zu prüfen |
| Export | SVG, PNG, PDF ⚠️ | Exportformate, nicht das Datenmodell (ADR 0042) |

Die eigene Spezifikation ist ein echter Beitrag: Soweit wir gefunden haben, beschreibt kein offener Standard ein Whiteboard als abfragbares Modell. Sie ist ein Kandidat für die Einreichung (ADR 0014).

## Gemeinsames Arbeiten in Echtzeit

Drei verschiedene Arten von Daten mit unterschiedlichen Anforderungen:

| Art | Beispiel | Behandlung |
|-----|----------|------------|
| **Dauerhaft, je Objekt** | Eine Form verschieben | Aktivitätsprotokoll, die letzte Änderung je Eigenschaft gewinnt |
| **Dauerhaft, wachsend** | Freihand-Strich | Jeder fertige Strich ist ein neues Objekt, sodass Striche nicht kollidieren |
| **Vorübergehend** | Die Cursor der anderen | Nur ein Live-Kanal; wird nie gespeichert |

**Empfehlung: zuerst Synchronisation je Objekt, hinter einer Schnittstelle,** was zu der bereits entschiedenen Synchronisation auf Objektebene passt (ADR 0019). Konflikte sind selten, weil zwei Personen selten dieselbe Eigenschaft derselben Form ändern. Gemeinsam bearbeitete Notizen sind die Ausnahme: Erweist sich das als unzureichend, kann für den Notizentext allein ein CRDT (`yrs` 0.28, `automerge` 0.12) ergänzt werden. Der vorübergehende Kanal existiert noch nicht, und Streaming sowie der Messenger könnten ihn ebenfalls nutzen.

**Wie im Spiel (entschieden 2026-11-06):** Du siehst, was andere tun, während sie es tun: Cursor, Auswahl, eine Form, die gerade gezogen wird. Das ist der Live-Kanal, eine gemeinsame [`Presence`-Schnittstelle](../../../interfaces/index.md). Ein CRDT ist eine eigene Sache: Er führt Änderungen korrekt zusammen, und wir nutzen ihn nur dort, wo Eigenschaften nicht reichen, also für Text. Änderungen an Eigenschaften brauchen eine logische Uhr statt Uhrzeit, und jede Eigenschaft wird für sich zusammengeführt, damit die Farbänderung der einen Person nicht die Verschiebung einer anderen rückgängig macht.

## Muster

| Muster | Verwendung |
|--------|------------|
| Composite | Gruppen von Elementen als ein Element |
| Command | Jede Änderung hat `apply` und `invert`, für Rückgängig (ADR 0042) |
| State | Werkzeuge: Auswählen, Zeichnen, Verbinden, jeweils mit eigenem Verhalten |
| Strategy | Exportformat; Verbindungsführung; Einrasten |
| Observer | Änderungen und Präsenz |
| Flyweight | Gemeinsame Stil-Objekte, wenn Boards viele Elemente halten |

## Rendering

Blinc hat ein [`canvas`](https://github.com/project-blinc/Blinc)-Element mit direktem GPU-Zeichnen, das ist die Grundlage. Der Kern hängt nicht von Blinc ab: Er berechnet die Szene, und die Komponente zeichnet sie.

| Zweck | Crate (2026-11-06) |
|-------|--------------------|
| Sichtbare Elemente schnell finden | `rstar` 0.14 |
| Formen in Dreiecke zerlegen, falls Blinc es nicht abdeckt | `lyon` 1.0 |
| SVG-Import und -Export | `usvg`, `resvg` 0.49 |

Stiftdruck und Neigung fehlen in Blinc; sie sind als unser Beitrag an Blinc geplant.

## Schnittstellen-Skizze

| Schnittstelle | Fähigkeiten |
|---------------|-------------|
| `Whiteboard` (Wurzel) | `capabilities()`, gibt die anderen heraus |
| `Boards` | `board.open`, `board.create`, `board.delete` |
| `Board` | `shape.add`, `stroke.draw`, `note.add`, `element.move`, `element.style`, `element.delete`, `element.group`, `element.reorder` |
| `Presence` | Live-Cursor und Auswahl |
| `Export` | `board.export` |
| `subscribe` | Live-Änderungen |

Die IDs folgen den [Anforderungen](requirements.md).

## Komponenten

Workbench `whiteboard` (dokumentiert, muss überarbeitet werden), mit einer kompakten Variante nur zum Lesen oder Einbetten. Neu: `infinite-canvas`, `selection-handles`, `minimap`, `presence-cursors`. Siehe [geplante Komponenten](../../../components/planned.md).

## Stufen

1. Entwurf der Datenspezifikation, Kern: Elemente, Gruppen, Rückgängig, räumlicher Index, Tests.
2. `infinite-canvas` auf Blinc: Verschieben, Zoomen, Formen, Zeichnen. Eine Messung vieler Elemente entscheidet, ob der Ansatz trägt.
3. Workbench, ein erstes einfaches Frontend, Notizen, Verbindungen, Bilder, Export.
4. Gemeinsames Arbeiten in Echtzeit mit Präsenz, Kommentaren, Vorlagen.

## Offene Fragen

1. **Synchronisation je Objekt oder CRDT?** Siehe oben; Empfehlung: zuerst je Objekt.
2. **Was kommt zuerst: Zeichnen oder Diagramme mit Verbindungen?** Die Frontends teilen sich in beide Lager. Wir schlagen zuerst Freihand und einfache Formen vor, Verbindungen in Stufe 3.
3. **Der Stift:** Wie wichtig ist er für die erste Version? Dafür muss zuerst zu Blinc beigetragen werden.
4. **Die bestehende Komponente `whiteboard`** trägt noch deutsche Variantennamen (`zeichnung`, `formen`, `notizen`, `vorlage`) und wird überarbeitet.
