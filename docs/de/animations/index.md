# Animationen

Animationen beschreiben die zeitlich gesteuerte Veränderung von Elementen (Eingang,
Ausgang, Feedback, Zustandswechsel). Sie liegen in **8 Kategorien**, jede Animation hat
ein eigenes Verzeichnis mit drei Dateien.

## Kategorien

| Kategorie | Verzeichnis | Anzahl | Inhalt |
|-----------|-------------|--------|--------|
| Eingang | [entrance](entrance/) | 8 | Elemente erscheinen lassen |
| Ausgang | [exit](exit/) | 7 | Elemente verschwinden lassen |
| Feedback | [feedback](feedback/) | 9 | Antwort auf eine Eingabe |
| Endlos | [loop](loop/) | 4 | wiederholte Signale |
| Laden | [loading](loading/) | 4 | Wartezeit überbrücken |
| Zustandswechsel | [transition](transition/) | 6 | Zustand wechseln, ohne Elemente zu erzeugen |
| Bewegung | [movement](movement/) | 1 | scrollabhängige Ebenen |
| Organisation | [organization](organization/) | 2 | Startzeitpunkte über Kinder verteilen |

**41 dokumentierte Animationen** (Stand dieser Datei).

## Übersicht

| # | Animation | Kategorie | Beschreibung |
|---|-----------|-----------|--------------|
| 1 | **Fade In** | entrance | Element erscheint allmählich (Deckkraft 0 → 1) |
| 2 | **Fade Out** | exit | Element verschwindet allmählich (Deckkraft 1 → 0) |
| 3 | **Slide In** | entrance | Element gleitet von außen herein (links/rechts/oben/unten) |
| 4 | **Slide Out** | exit | Element gleitet nach außen hinaus |
| 5 | **Zoom In** | entrance | Element skaliert von klein auf volle Größe |
| 6 | **Zoom Out** | exit | Element skaliert von voller Größe auf null |
| 7 | **Bounce In** | entrance | Element federt beim Eintreffen ein |
| 8 | **Bounce Out** | exit | Element federt vor dem Verschwinden |
| 9 | **Pop In** | entrance | Einblenden mit kurzem Overshoot (Chips, Badges) |
| 10 | **Pop Out** | exit | Kurz ausholen, dann wegklappen |
| 11 | **Flip** | transition | Element dreht sich um 180° (Vorder-/Rückseite) |
| 12 | **Rotate** | transition | Element dreht sich um die eigene Achse |
| 13 | **Spin** | loop | Dauerhaftes Drehen (Loader, Aktivität) |
| 14 | **Scale In** | entrance | Element wächst von 0 % auf 100 % |
| 15 | **Scale Out** | exit | Element schrumpft von 100 % auf 0 % |
| 16 | **Collapse** | exit | Höhe/Breite wird auf 0 reduziert (Akkordeon zu) |
| 17 | **Expand** | entrance | Höhe/Breite wächst von 0 auf Inhalt (Akkordeon auf) |
| 18 | **Unfold** | entrance | Element klappt wie ein Blatt aus |
| 19 | **Shake** | feedback | Element rüttelt kurz horizontal (Fehler) |
| 20 | **Wiggle** | feedback | Element wackelt leicht (Bearbeitungsmodus) |
| 21 | **Press** | feedback | Element sinkt beim Drücken minimal ab |
| 22 | **Lift** | feedback | Element hebt sich bei Hover/Fokus (Schatten wächst) |
| 23 | **Tick Draw** | feedback | Erfolgshäkchen wird als Linie gezeichnet |
| 24 | **Pulse** | loop | Zyklisches An-/Abschwellen (Aufmerksamkeit) |
| 25 | **Heartbeat** | loop | doppelter Puls im Rhythmus einer Herzfrequenz |
| 26 | **Ripple** | feedback | Welle breitet sich vom Klickpunkt aus |
| 27 | **Highlight** | feedback | Hintergrund leuchtet kurz auf (Fundstelle) |
| 28 | **Glow** | loop | Leuchten um die Kontur (Auswahl, Live-Status) |
| 29 | **Progress** | loading | Fortschrittsanzeige (Balken, Kreis) |
| 30 | **Skeleton** | loading | Platzhalter-Schimmer während des Ladens |
| 31 | **Typing** | loading | Tipp-Indikator (drei Punkte in Chats) |
| 32 | **Dots** | loading | Drei Ladekugeln als kompakter Aktivitätsindikator |
| 33 | **Elastic** | feedback | Element federt über die Endposition hinaus |
| 34 | **Rubber Band** | feedback | Übermäßiges Ziehen federt zurück (Over-Scroll) |
| 35 | **Morph** | transition | Form wandelt sich weich in eine andere Form |
| 36 | **Cross Fade** | transition | Zwei Elemente überblenden einander |
| 37 | **Cross Slide** | transition | Zwei Elemente schieben sich gegenseitig aus dem Bild |
| 38 | **Reorder** | transition | Listenelemente tauschen weich ihre Plätze (FLIP) |
| 39 | **Parallax** | movement | Ebenen bewegen sich unterschiedlich schnell |
| 40 | **Stagger** | organization | Kind-Elemente starten nacheinander versetzt |
| 41 | **Cascade** | organization | Versetzter Start entlang einer Richtung |

## Baum

Die Verzeichnisse sind der Baum. Innerhalb der Kategorien sind die Animationen zu
**Familien** zusammengefasst: Eingang und Ausgang sind stets dieselbe Animation in
Gegenrichtung.

```
animations/
│
├── entrance/          fade-in, slide-in, zoom-in, scale-in,
│                      bounce-in, pop-in, expand, unfold
│     Transparenz ···· fade          Größe ·········· zoom, scale, bounce, pop
│     Position ······· slide         Layoutgröße ····· expand      (drop ⁺, wipe ⁺,
│                                                        swing ⁺, blur ⁺)
│
├── exit/              fade-out, slide-out, zoom-out, scale-out,
│                      bounce-out, pop-out, collapse
│     dieselben Familien, Richtung out  (fold ⁺ als Gegenstück zu unfold)
│
├── feedback/          shake, wiggle, ripple, press, lift,
│                      tick-draw, highlight, elastic, rubber-band
│     Abwehr ········· shake, wiggle            (nudge ⁺)
│     Bedienung ······ press, lift, ripple      Bestätigung · tick-draw (cross-draw ⁺)
│     Physik ········· elastic, rubber-band     (tilt ⁺)
│     Signal ········· highlight                (flash ⁺, count-up ⁺)
│
├── loop/              spin, pulse, heartbeat, glow
│     Signal ········· pulse, heartbeat, glow   (breathing ⁺, blink ⁺)
│     Drehung ········ spin
│
├── loading/           progress, skeleton, typing, dots
│     Aktivität ······ dots, typing             Struktur ···· skeleton
│     Wert ··········· progress                 (barber-pole ⁺)
│
├── transition/        flip, rotate, morph, cross-fade,
│                      cross-slide, reorder
│     2D ············· flip, morph, cross-fade, cross-slide
│     Layout ········· reorder                  (resize ⁺, magic-line ⁺)
│     Ebene / 3D ····· –                         (shared-element ⁺, page-transition ⁺,
│     cube ⁺)
│
├── movement/          parallax
│     Ambiente ······· parallax                 (float ⁺, drift ⁺, marquee ⁺,
│     wave ⁺, ken-burns ⁺)
│
└── organization/      stagger, cascade
      Zeitsteuerung ·· stagger, cascade         (sequence ⁺, orchestration ⁺)
```

⁺ = noch nicht dokumentiert (Kandidat, siehe [Weitere Animationen](#weitere-animationen-kandidaten))

## Familien: dieselbe Animation in zwei Richtungen

Die Richtungspaare sind Redundanz. Ein Dokument pro Familie deckt beide Seiten über
Attribute ab – die Namen bleiben als Kurzform erhalten (`animation: "fade-in"` ist eine
Abkürzung für `fade` + `direction: in`).

| Familie | Dokumente | Zusammengefasst durch |
|---------|-----------|----------------------|
| `fade` | [fade-in](entrance/fade-in/description.md), [fade-out](exit/fade-out/description.md) | `direction: in \| out`, `fromOpacity`, `toOpacity` |
| `slide` | [slide-in](entrance/slide-in/description.md), [slide-out](exit/slide-out/description.md) | `direction`, `from: left \| right \| top \| bottom`, `distance` |
| `zoom` | [zoom-in](entrance/zoom-in/description.md), [zoom-out](exit/zoom-out/description.md) | `direction`, `fromScale`, `toScale` |
| `scale` | [scale-in](entrance/scale-in/description.md), [scale-out](exit/scale-out/description.md) | `direction`, `origin` |
| `bounce` | [bounce-in](entrance/bounce-in/description.md), [bounce-out](exit/bounce-out/description.md) | `direction`, `amplitude`, `bounces` |
| `pop` | [pop-in](entrance/pop-in/description.md), [pop-out](exit/pop-out/description.md) | `direction`, `overshoot`, `anticipation` |
| `collapse` | [expand](entrance/expand/description.md), [collapse](exit/collapse/description.md) | `direction`, `dimension: height \| width \| both` |
| `rotate` | [rotate](transition/rotate/description.md), [spin](loop/spin/description.md) | `iterationCount: infinite` macht aus Rotate ein Spin |
| `pulse` | [pulse](loop/pulse/description.md), [heartbeat](loop/heartbeat/description.md) | `waveform: pulse \| heartbeat`, `intensity` |
| `fade` + Weichzeichner | – | bereits abgedeckt: Attribut `blur` in [Fade In](entrance/fade-in/attributes.md) |

**Möglich:** 41 Dokumente → **32 Familien-Dokumente** (9 Paare verschmelzen). Bewusst noch
nicht gemacht: die Zusammenlegung würde alle Querverweise und die Navigation in
`mkdocs.yml` erneut ändern. Zusätzlich sind Skeleton/Shimmer und Typing/Dots
Überschneidungen, die als *Varianten* in den bestehenden Dokumenten geführt werden.

## Animationen als Verzeichnis

Jede Animation hat ein eigenes Verzeichnis nach dem Muster
`animations/<kategorie>/<name>/`:

| Datei | Inhalt |
|-------|--------|
| `description.md` | Was ist die Animation? Wozu dient sie? Wann einsetzen? |
| `attributes.md` | Attribute/Optionen (Dauer, Timing, Amplitude, Callbacks) |
| `appearance.md` | Wie sieht sie aus? ASCII-Verlauf, Varianten, Dauer |

Jede Kategorie hat eine eigene Übersicht (`<kategorie>/index.md`), diese Datei führt alle.

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

Richtungen von Familien-Paaren werden zusätzlich abgebildet:

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `direction` (Familie) | string | `in` | `in` (Eingang) oder `out` (Ausgang) |
| `mirrorOf` | string | - | Name der Gegenanimation (`fade-in` → `fade-out`) |

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
- Bewegungen im Sichtfeld (Parallax, Lift, Reorder) sind die stärksten Auslöser –
  immer abschaltbar halten
- Blinkende und aufleuchtende Signale (`glow`, geplant `blink`/`flash`) nie länger als
  fünf Zyklen ohne Nutzeraktion

## Weitere Animationen (Kandidaten)

Sinnvolle Ergänzungen, sortiert nach Kategorie. Priorität: **hoch** = in jedem UI nötig,
mittel = hängt am Feature, niedrig = Schmuck. Bereits angelegte Kandidaten stehen nicht
mehr in dieser Liste.

### entrance / exit

| Kandidat | Beschreibung | Prio |
|----------|--------------|------|
| `drop-in` / `drop-out` | Element fällt mit Schwerkraft ein, prellt beim Aufkommen | mittel |
| `wipe` / `reveal` | Sichtbar über Maske (`clip-path`), diagonal oder radienförmig | mittel |
| `swing-in` / `swing-out` | Pendelt um einen Aufhänger (Menüs an Leisten) | mittel |
| `blur-in` / `blur-out` | Unschärfe → scharf (Fokus, Hintergrund-Overlay); `blur` ist schon Attribut von Fade | mittel |
| `fold` | Gegenstück zu Unfold (Papier- bzw. Akkordeon-Klappung) | niedrig |

### feedback

| Kandidat | Beschreibung | Prio |
|----------|--------------|------|
| `cross-draw` | Kreuz wird gezeichnet (Abbrechen, Fehler im Feld) | mittel |
| `count-up` | Zahl blättert hoch (Zähler, Summen, Statistik) | mittel |
| `flash` | Kurze Helligkeitsänderung statt Flächenfarbe | mittel |
| `nudge` | Mini-Shake vertikal: „nicht wählbar“, ohne Fehler zu signalisieren | mittel |
| `tilt` | Element neigt sich 3D zum Zeiger (Karten, Kacheln) | niedrig |

### loop / loading

| Kandidat | Beschreibung | Prio |
|----------|--------------|------|
| `breathing` | Langsames, tiefes An-/Abschwellen (KI aktiv, Verbindung hält) | mittel |
| `blink` | Cursor-/Aufnahme-Indikator (an/aus im Takt) | mittel |
| `barber-pole` | Streifenmuster wandert (unbestimmter Fortschritt) | mittel |

### transition

| Kandidat | Beschreibung | Prio |
|----------|--------------|------|
| `resize` | Größenänderung eines Containers weich nachgeführt (Panel, Split-View) | mittel |
| `magic-line` | Markierungslinie wandert von einem Tab zum nächsten | mittel |
| `shared-element` | Dasselbe Element wandert von Liste zu Detailansicht | mittel |
| `page-transition` | Ganzseitiger Übergang zwischen Programmen/Bereichen | mittel |
| `cube` | Würfelrotation mit vier Seiten (Wizard-Schritte) | niedrig |

### movement

| Kandidat | Beschreibung | Prio |
|----------|--------------|------|
| `float` | Element schwebt ruhig auf und ab (Illustrationen, Onboarding) | mittel |
| `marquee` | Text läuft durch sein Feld (Überschriften, Notizen) | mittel |
| `ken-burns` | Bild schwenkt/zoomt langsam (Hintergrund, Diashow) | niedrig |
| `wave` / `drift` | Wellenförmige Bewegung von Punkt- oder Icon-Reihen | niedrig |

### organization

| Kandidat | Beschreibung | Prio |
|----------|--------------|------|
| `sequence` | Abfolge mehrerer Animationen als Timeline (über `onAnimateEnd` verkettet) | mittel |
| `orchestration` | Eltern-Element startet, Kinder folgen, beim Ausgang umgekehrt | mittel |

## Siehe auch

- [Gesten](../gestures/) — Shake, Wiggle als Feedback zu Gesten
- [Components](../components/) — `toast`, `modal`, `drawer`, `accordion` nutzen Animationen
- [Standardisierte Daten](../data/) — Felder wie `animation`, `duration` in Komponenten-Attributen
