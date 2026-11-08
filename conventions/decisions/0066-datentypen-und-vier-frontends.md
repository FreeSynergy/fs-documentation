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

## Folgen
- Die Analysen der bekannten Programme je Kategorie bleiben Quelle für **Funktionen**; das Aussehen kommt aus den vier Frontends.
- Die Schnittstellen in `docs/en/interfaces/` werden aus den Typbeschreibungen abgeleitet und als Ziel v1 festgelegt (ADR 0045).
- Blinc wird am Apple- und Windows-Nachbau gemessen; die Entscheidung über das Toolkit fällt nach diesen Daten.
