# 0009 – GUI: Blinc ist gesetzt

## Kontext
`programs/platform/crates/gui.md` vergleicht sieben GUI-Kandidaten (Blinc, Dioxus+Blitz, egui,
iced, Makepad, GPUI, Leptos+Blitz) nach Plattformen, Canvas, SVG, Animation, Gesten,
Komponenten, Tempo und Lizenz. Fazit dort: **Blinc ist der Hauptfavorit** — einziger Kandidat mit
echtem CSS **und** Canvas-Kits **und** VDOM-frei auf allen Plattformen inklusive Mobile. Der
Nutzer entscheidet am 2026-11-03: **Blinc**. Erste Anlaufstelle für die UI-Härtung (§20 P3).

## Entscheidung
- **Blinc ist das GUI-Fundament** für Grundmaske, Components und Programme. Rust, GPU-Rendering,
  CSS-Theming, feingranulare Reaktivität ohne VDOM.
- **Prototypen auf 0.6.x**, nicht auf 0.5.x einarbeiten (Builder-API-Änderung: CSS-first,
  Stateful Closures → Property-Bindings mit Signals). Auf 0.5.x einzusteigen wäre doppelte Arbeit.
- **Grenze bleibt:** die 84 Components sind die Obergrenze dessen, was eine Maske ausdrücken kann
  (Protokoll §2). Blinc bringt ~40 fertige shadcn-artige Komponenten (`blinc_cn`) — sie sind der
  Anfang, nicht die Menge. Was fehlt, bauen wir als eigene Components.
- **Fehlende Gesten** (generischer Swipe-Erkner, Zwei-Finger-Pan/Rotate) sind **unsere Arbeit**:
  Blinc bringt `TouchEvent` mit Finger-ID und Druck, Pinch ist vorhanden; die fehlenden Erkner
  bauen wir als State-Maschinen über den Pointer-Events (Referenz: Makepad, MIT/Apache-2.0 —
  Logik als Vorlage, nicht kopieren). Autor hat Erweiterungsbereitschaft signalisiert.
- **Absicherung:** Dioxus+Blitz als Fallback beobachten (bestes CSS, Canvas-Lücke). Kein Mischen
  zweier Frameworks in einer App.

## Folgen
- Neue Doku: **`programs/platform/crates/blinc.md`** — was Blinc kann, wie es benutzt wird
  (CSS-first, Signals, State-Machines, Animation-Engine), und der **Abgleich mit den 84
  Komponenten**: was Blinc schon liefert, was wir selbst bauen, was unklar ist.
  Englisch zuerst (ADR 0008), deutsch parallel.
- Der Abgleich ist **recherchepflichtig am Quelltext** (Release-Tag lesen, nicht Blogartikel) —
  gleiche Regel wie bei den Masken-Dokus.
- `components/*/usage.md` bekommen später einen Blinc-Abschnitt („so sieht die echte Umsetzung
  aus“), sobald die ersten Bausteine in Blinc stehen.
- Lizenz: Blinc ist Apache-2.0 ✅ — passend zur Projektlizenz.

## Bestätigt und abgesichert (2026-11-05)

Nach der Recherche `temp/research/blinc-health-and-parsers.md` (Bus-Faktor 1: 99 % der Commits vom
Autor; kaum fremde Nutzung; keine Barrierefreiheit; IME unvollständig) entscheidet der Nutzer:
**bei Blinc bleiben und den Autor unterstützen — besser unterstützen als neu anfangen.** Blinc kann
mehr als Komponenten: Effekte und Spielereien (Schnee, Regen, Animationen) — kleine menschliche
Dinge, die Menschen überzeugen. Kontakt besteht (Discord); der Autor ist offen für fehlende Gesten.

Absicherungen:
1. Blinc **nur hinter unserer Component-Schicht** — keine `blinc_*`-Typen im Programmcode.
2. **Nur Zeichnen** in Blinc; Textpuffer (`ropey`), Parsen, Hervorheben (`syntect` pure Rust) bei uns.
3. Version festschreiben, Fork bereithalten (Apache-2.0 erlaubt es).
4. Unsere Lücken **upstream** beheben (`todo/upstream.md`): Barrierefreiheit, IME, Hervorhebung
   über den ganzen Puffer, Gesten (Finger/Maus/Stift).
5. Neu bewerten, wenn: 3 Monate kein Commit · eines unserer Issues > 30 Tage unbeantwortet ·
   vor unserer ersten öffentlichen Version kein Plan für Barrierefreiheit.

Issues des Autors laufen über **git-bug** (`refs/bugs/*`); Stand: `temp/research/blinc-issues.md`.
Blincs Plan „cn → layout promotion“ (c422b97) deckt sich mit unserer Component-Schicht.

## Antwort des Autors (2026-11-05, über den Nutzer)

- **Barrierefreiheit:** laufende Arbeit; Tastatur-Navigation (Tab/Pfeile) für interaktive Elemente
  und Formulare ist in **0.6.0**; mobil noch in Arbeit, geplant für **0.6.1**.
- **IME mobil:** zurückgestellt zugunsten von Linux/Windows-Fehlern; geplant, evtl. 0.6.1.
- **Code-Editor:** Hervorhebung ist anpassbar — eigenen Trait implementieren und an die Komponente
  übergeben. Puffer statt Zeile evtl. schneller, nicht gemessen. Referenz: eine IDE auf einem Teil von
  Blinc (Repo `blinc_abi`, Sprache Haxe) kommt mit großen Texten gut zurecht.
- **cn-Komponenten:** keine Vorgaben, **Beiträge willkommen**.
- **Gesten/Eingabe:** Stift noch nicht unterstützt — **Beiträge willkommen**.
- **harfrust:** wird angesehen; Umstieg oder Benötigtes aus rustybuzz übernehmen.
- **Roadmap:** in **git-bug** (CLI installieren, um alle Issues zu holen).
- **Beitragen:** erst **git-bug-Issue**, im **GitHub-Issue** erwähnen (damit andere Maintainer es
  sehen); bei Änderungswünschen/neuen Funktionen zuerst im **RFC-Kanal** besprechen, dann PR.

Folge: Die Absicherung „Plan für Barrierefreiheit“ (Punkt 5) ist erfüllt — es gibt einen Plan.

