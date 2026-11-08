# 0065 – Ein Standard für jedes Fenster: Menü, Version, Hilfe, Meldungen

Status: akzeptiert im Grundsatz (Nutzer, 2026-11-08: „Bevor wir uns hier kaputt programmieren, sollten wir einen Standard machen.“), Einzelheiten Vorschlag der Strategie bis zur Bestätigung · ergänzt ADR 0021 (Motor und Frontend), 0061 (Admin-Frontend), 0063 (ein Befehl)

## Entscheidung
Jedes Fenster jedes Programms (und jeder Facette) erfüllt dieselbe **Mindest-Hülle**. Sie ist ein Vertrag (Trait in `fs-components`), kein Aussehen: Wie ein Frontend sie darstellt, entscheidet das Frontend; **dass** es sie gibt, ist Pflicht. Ein Frontend darf mehr anbieten, nie weniger.

## Pflichtteile (Vorschlag)
1. **Standard-Menü** mit festen Einträgen und festen Tastenkürzeln:
   - *Programm*: Einstellungen (öffnet das Admin-Frontend, ADR 0061), Beenden (Strg+Q).
   - *Ansicht*: die Ansichten des Programms; Vollbild.
   - *Hilfe*: Hilfe (F1), Über.
2. **Über**: Name (`FreeSynergy.<Name>`), **Version** (v0.0.N), Herkunft (Quelle/Katalog aus dem Store), Lizenz, Link zum Repository. Die Version ist immer mit einem Klick zu sehen.
3. **Hilfe**: Ist das Wiki installiert, zeigt die Hilfe die passende Seite aus dem Wiki (über den Vertrag `texts`); sonst die Seite auf der Doku-Seite bzw. GitHub. Später: Hilfe von beliebigen Quellen. Jede Ansicht hat eine Hilfe-Adresse.
4. **Meldungen** (Ergebnis einer Aktion, Fehler): gehören zu ihrem Anlass. Erfolg verschwindet von selbst nach kurzer Zeit oder beim Wechsel der Ansicht; ein Fehler bleibt, bis man ihn schließt oder behebt. Nie eine veraltete Meldung in einer anderen Ansicht. Muster: Observer mit Lebensdauer je Meldung.
5. **Fehler sind immer sichtbar**, nie still (vgl. Store-Handtest).
5a. **Menüs verhalten sich überall gleich** (Nutzer, 2026-11-08: „eine eindeutige Sache“): Klick auf einen Menütitel öffnet, ein zweiter Klick auf denselben Titel schließt; Klick außerhalb oder Esc schließt; ist ein Menü offen, wechselt Hover über einen anderen Titel direkt dorthin; Pfeiltasten bewegen, Enter wählt; ein gewählter Eintrag schließt das Menü. Menüs öffnen ohne spürbare Verzögerung. Gleiches gilt für das Dreipunkt-Menü (⋮) auf Karten.
6. **Tastatur**: Tab-Folge in Lesereihenfolge, sichtbarer Fokus, Esc schließt Dialoge.
7. **Nach einem Update eines laufenden Programms**: Das Programm erkennt, dass seine Datei ersetzt wurde, und startet sich neu (Zustand vorher sichern) oder bietet „Jetzt neu starten“ an. Es benutzt nie den Pfad der gelöschten alten Datei.

## Folgen
- `fs-components`: Trait `Shell` (Name vorläufig) mit diesen Teilen und einer Standard-Umsetzung; jede App nutzt sie.
- Store, Tasks, People werden zuerst umgestellt.
