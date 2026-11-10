# 0066 – Datentypen mit festen Components, vier Frontends je Programm

Status: akzeptiert (Nutzer, 2026-11-09) · ergänzt ADR 0021 (Motor und Frontend), 0050 (ein Standard, ein Programm), 0061 (Facetten, Admin-Frontend), 0065 (Fensterhülle)

## Anlass
Die Schnittstellen wurden beim Programmieren ausgesucht statt vorher festgelegt; sie blieben unscharf. `fs-people` setzt die JSContact-Beschreibung (`docs/en/data/people/jscontact/description.md`) kaum um. Jede App baute ihre Felder selbst. Der Nutzer: zuerst sagen, was wir brauchen, dann von zwei Seiten bauen – von den Daten und von den Vorbildern.

## Entscheidung
1. **Grundtypen:** kleine Werte mit festen Regeln (E-Mail-Adresse, Telefon, Name, Adresse, Ort, Datum, Sprache, Schlüssel, Verweis …), je mit Standard. Einmal festgelegt, gelten sie in allen Programmen. Liste: `docs/en/programs/map.md`.
2. **Datentypen** bestehen aus Grundtypen und gehören genau einem Programm (ADR 0050), z. B. `Person` = JSContact `Card` in `fs-people`.
3. **Das Backend meldet je Datentyp eine Typbeschreibung:** Felder, Grundtyp je Feld, Pflicht/mehrfach und die **Befehle** (anlegen, ändern, suchen, prüfen, vorschlagen …). Nicht das Aussehen, aber was möglich ist.
4. **Components je Grundtyp, einmal in `fs-components`:** *Eingabe*, *Anzeige*, *kompakt* (in einer Zeile), *Zelle* (in einer Liste). Ein Datentyp erbt sie von seinen Grundtypen. Ein Frontend entscheidet nur, wo es sie zeigt.
5. **Vier Frontends je Programm (und Facette):**
   - **Admin:** alle Felder, alle Einstellungen, alle Befehle. **Aus der Typbeschreibung erzeugt**, ein Code für alle Programme.
   - **Einfach:** für Menschen mit wenig Erfahrung, wenige große Elemente.
   - **Apple-Stil** und **Windows-Stil:** nach Maß nachgebaut – Abstände, Zeilenhöhen, Schriftgrößen, Ecken, Glas oder Fläche, Anordnung. Grundlage sind die öffentlichen Leitlinien (Apple Human Interface Guidelines, Microsoft Fluent 2) und Bildschirmfotos, die lokal bleiben. Der genaue Nachbau ist zugleich die Prüfung, was die GUI-Engine kann.
6. **Stile** (Maße, Farben, Effekte, **ein eigenes Iconset**) sind wiederverwendbar. Keine fremden Icons, Logos, Texte oder Schriften: SF Pro und Segoe UI sind nicht frei, wir nehmen offene Schriften mit ähnlichen Maßen.
7. **Reihenfolge:** Pilot `fs-people` (Grundtypen, `Person`, Typbeschreibung, Components, Admin), danach alle anderen Programme über das erzeugte Admin-Frontend.

## Ergänzung (Nutzer, 2026-11-09)
- **Admin-Frontend im Stil von SAP Fiori** (öffentliches Design-System für dichte Geschäftsdaten). Später ein **eigener FreeSynergy-Stil**, der ganz anders ist.
- **Apple-Stil: Apple ist dabei, mit Apples eigenen Apps als Vorlage,** weil sie gut aussehen. Erst 1:1 nachbauen, dann mit Funktionen füllen, später ändern, falls nötig (auch bei Ärger). Es ist nur ein Frontend; die Engine darunter ist das Wichtigere – beides soll die Menschen umhauen.
- **Windows-Stil: ebenfalls 1:1 nachbauen, je Kategorie ein Windows-Programm.** Bevorzugt Programme, die es unter Linux nicht gibt, damit alle mit offener Software davon profitieren. **Bewusst keine Linux-Programme als Vorlage** – die haben wir schon. Beim Aussehen ist es uns egal, wie nah es an Microsoft ist.
- **Haiku recherchiert und macht die Bildschirmfotos** für den Nachbau (nur lokal, nie in ein Repo).

## Regel: keine Darstellung im Programm (Nutzer, 2026-11-10)
- **Alles, was etwas zeigt, ist eine Component in `fs-components`** – vom Eingabefeld bis zu Kanban, Kalender, Editor und Writer. Dort stehen die Render-Logik und das Aussehen (Stile), sonst nirgends.
- **Das Programm** liefert nur Daten und die Schnittstelle (Trait, Typbeschreibung, Befehle), über die ein Frontend sie bekommt.
- **Das Frontend** setzt zusammen: welche Components, welcher Stil, welche Anordnung.
- Grund: Wiederverwendbarkeit. Was einmal als Component existiert, nutzen alle Programme und alle Frontends.
- Ein Programm setzt keine Component ein, die es in `fs-components` nicht gibt; fehlt eine, wird sie dort gebaut.

## Regel: Frontends sind das Ziel, Funktionen werden nur angeschaltet (Nutzer, 2026-11-10)
- Die Frontends werden **jetzt vollständig und 1:1** gebaut, mit allen Bedienelementen, auch für Funktionen, die der Kern noch nicht hat. Danach ändern sie sich nicht mehr; die Funktionen kommen Schritt für Schritt dazu.
- **Anschalten geschieht von selbst:** Die Typbeschreibung meldet je Befehl, ob er unterstützt ist. Ein Bedienelement für einen nicht unterstützten Befehl ist sichtbar, aber gesperrt, mit dem Hinweis „kommt noch“. Sobald der Kern den Befehl meldet, ist es frei – ohne Änderung am Frontend.
- Die verschiedenen Frontends sind unser **Maßstab**: Sie halten fest, was wir zugesagt haben.

## Regel: Vorbild ist das beste Programm (Nutzer, 2026-11-10, gilt immer)
Je Kategorie wird das Programm Vorbild, das in **Funktionen, UX und UI** am besten ist, egal ob Open Source, nur im Web oder eingestellt (z. B. das eingestellte Microsoft Whiteboard: wenn es das beste ist, ist das ein Grund, zu uns zu kommen). Gesucht wird gerade das, was es im Open-Source-Bereich **nicht** gibt; die Funktionen der Open-Source-Programme kommen zusätzlich hinein. Haiku sucht dazu je Kategorie alle bekannten Programme zusammen, Opus vergleicht und empfiehlt, der Nutzer entscheidet.

## Galerie und Studio (Nutzer, 2026-11-10)
- **Galerie** (Facette von `fs-files`) zeigt Bilder und Videos von hier **und von weiter weg**: YouTube, Vimeo, Odysee, PeerTube sind Quellen der Galerie, angebunden wie KIs in People (Anbieter hinter einer Schnittstelle).
- **Studio** (Facette von `fs-streaming`): Live-Produktion und Live-Schnitt, Szenen, Gäste, an mehrere Ziele senden (OBS, Restream, StreamYard, vMix …).

## Folgen
- Die Analysen der bekannten Programme je Kategorie bleiben Quelle für **Funktionen**; das Aussehen kommt aus den vier Frontends.
- Die Schnittstellen in `docs/en/interfaces/` werden aus den Typbeschreibungen abgeleitet und als Ziel v1 festgelegt (ADR 0045).
- Blinc wird am Apple- und Windows-Nachbau gemessen; die Entscheidung über das Toolkit fällt nach diesen Daten.
