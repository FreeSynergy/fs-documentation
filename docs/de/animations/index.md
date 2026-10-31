# Animationen

Animationen beschreiben die zeitlich gesteuerte Veränderung von Elementen (Eingang, Ausgang, Feedback, Zustandswechsel).

## Übersicht

| # | Animation | Gruppe | Beschreibung |
|---|-----------|--------|--------------|
| 1 | **Fade In** | Eingang | Element erscheint allmählich (Deckkraft 0 → 1) |
| 2 | **Fade Out** | Ausgang | Element verschwindet allmählich (Deckkraft 1 → 0) |
| 3 | **Slide In** | Eingang | Element gleitet von außen herein (links/rechts/oben/unten) |
| 4 | **Slide Out** | Ausgang | Element gleitet nach außen hinaus |
| 5 | **Zoom In** | Eingang | Element skaliert von klein auf volle Größe |
| 6 | **Zoom Out** | Ausgang | Element skaliert von voller Größe auf null |
| 7 | **Bounce In** | Eingang | Element federt beim Eintreffen ein |
| 8 | **Bounce Out** | Ausgang | Element federt vor dem Verschwinden |
| 9 | **Flip** | Zustandswechsel | Element dreht sich um 180° (Vorder-/Rückseite) |
| 10 | **Rotate** | Zustandswechsel | Element dreht sich um die eigene Achse |
| 11 | **Spin** | Endlos | Dauerhaftes Drehen (Loader, Aktivität) |
| 12 | **Scale In** | Eingang | Element wächst von 0 % auf 100 % |
| 13 | **Scale Out** | Ausgang | Element schrumpft von 100 % auf 0 % |
| 14 | **Collapse** | Ausgang | Höhe/Breite wird auf 0 reduziert (Akkordeon zu) |
| 15 | **Expand** | Eingang | Höhe/Breite wächst von 0 auf Inhalt (Akkordeon auf) |
| 16 | **Unfold** | Eingang | Element klappt wie ein Blatt aus |
| 17 | **Shake** | Feedback | Element rüttelt kurz horizontal (Fehler) |
| 18 | **Wiggle** | Feedback | Element wackelt leicht (Bearbeitungsmodus) |
| 19 | **Pulse** | Endlos | Zyklisches An-/Abschwellen (Aufmerksamkeit) |
| 20 | **Heartbeat** | Endlos | doppelter Puls im Rhythmus einer Herzfrequenz |
| 21 | **Ripple** | Feedback | Welle breitet sich vom Klickpunkt aus |
| 22 | **Highlight** | Feedback | Hintergrund leuchtet kurz auf (Fundstelle) |
| 23 | **Glow** | Endlos | Leuchten um die Kontur (Auswahl, Live-Status) |
| 24 | **Progress** | Endlos | Fortschrittsanzeige (Balken, Kreis, Skelett) |
| 25 | **Skeleton** | Endlos | Platzhalter-Schimmer während des Ladens |
| 26 | **Typing** | Endlos | Tipp-Indikator (drei Punkte in Chats) |
| 27 | **Elastic** | Feedback | Element federt über die Endposition hinaus |
| 28 | **Rubber Band** | Feedback | Übermäßiges Ziehen federt zurück (Over-Scroll) |
| 29 | **Morph** | Zustandswechsel | Form wandelt sich weich in eine andere Form |
| 30 | **Cross Fade** | Zustandswechsel | Zwei Elemente überblenden einander |
| 31 | **Parallax** | Bewegung | Ebenen bewegen sich unterschiedlich schnell |
| 32 | **Stagger** | Organisation | Kind-Elemente starten nacheinander versetzt |

## Gruppen

### Eingang (Enter)

Fade In, Slide In, Zoom In, Scale In, Bounce In, Expand, Unfold

### Ausgang (Exit)

Fade Out, Slide Out, Zoom Out, Scale Out, Bounce Out, Collapse

### Feedback (Interaktion)

Shake, Wiggle, Ripple, Highlight, Elastic, Rubber Band

### Endlos (Loop)

Spin, Pulse, Heartbeat, Glow, Progress, Skeleton, Typing, Parallax

### Zustandswechsel (Transition)

Flip, Rotate, Morph, Cross Fade

### Organisation

Stagger

## Animationen als Verzeichnis

Jede Animation hat ein eigenes Verzeichnis nach dem Muster `animations/<name>/`:

| Datei | Inhalt |
|-------|--------|
| `description.md` | Was ist die Animation? Wozu dient sie? Wann einsetzen? |
| `attributes.md` | Attribute/Optionen (Dauer, Timing, Amplitude, Callbacks) |
| `appearance.md` | Wie sieht sie aus? ASCII-Verlauf, Varianten, Dauer |

## Standard-Attribute (für alle Animationen)

Attributnamen folgen der Konvention aus [data/konventionen.md](../data/konventionen.md): `camelCase` und ASCII. Begriffe mit Umlaut werden englisch benannt (`overshoot`, `dotSize`, `intensity`).

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `none` | Name der Animation |
| `duration` | number | `300` | Dauer in ms |
| `timingFunction` | string | `ease` | `linear`, `ease-in`, `ease-out`, `ease-in-out`, `cubic-bezier(...)` |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `iterationCount` | number \| `infinite` | `1` | Anzahl Wiederholungen |
| `direction` | string | `normal` | `normal`, `reverse`, `alternate`, `alternate-reverse` |
| `fillMode` | string | `none` | `none`, `forwards`, `backwards`, `both` |
| `playState` | string | `running` | `running`, `paused` |
| `onAnimateStart` | function | - | Wird beim Start ausgeführt |
| `onAnimateEnd` | function | - | Wird beim Ende ausgeführt |

## Konfiguration (global)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animationsEnabled` | boolean | Animationen global aktivieren? |
| `defaultDuration` | number | Standarddauer für alle Animationen |
| `respectReducedMotion` | boolean | `prefers-reduced-motion` respektieren? |
| `staggerStep` | number | Versatz zwischen Kind-Elementen in ms |

## Dauer-Richtwerte

| Bereich | Dauer | Verwendung |
|---------|-------|------------|
| Mikro | 100–200ms | Hover, Tap-Feedback |
| Standard | 200–400ms | Fenster, Menüs, Listen |
| Aufmerksam | 400–800ms | Onboarding, Highlights |
| Loop | 800–2000ms | Loader, Pulse, Skeleton |

## Barrierefreiheit

- `prefers-reduced-motion: reduce` → Animationen auf 0ms oder Fade reduzieren
- Endlos-Animationen pausieren, wenn das Element nicht sichtbar ist
- Farbanimationen nie als einzige Information (immer Icon/Text ergänzen)

## Siehe auch

- [Gesten](../gestures/) — Shake, Wiggle als Feedback zu Gesten
- [Components](../components/) — `toast`, `modal`, `drawer`, `accordion` nutzen Animationen
- [Standardisierte Daten](../data/) — Felder wie `animation`, `duration` in Komponenten-Attributen
