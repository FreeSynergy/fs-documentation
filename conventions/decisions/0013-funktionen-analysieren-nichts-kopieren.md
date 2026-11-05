# 0013 – Funktionen analysieren, nichts kopieren; Programme nach Ideen auswählen

Status: akzeptiert (2026-11-05) · ersetzt in **0006** Punkt 2 (3–5 Masken) und 3.4 (2 nicht-OSS + 1 OSS);
ersetzt im Protokoll §20 P4 „vorhandene Programme kopieren“

## Kontext
Die bisherige Doku sammelte viele Programme pro Kategorie, um einen Überblick zu bekommen
(119 Masken). Der Überblick ist da; als Arbeitsgrundlage ist die Menge zu groß und zu gleichförmig.
Außerdem stand im Protokoll noch „von oben kopieren“. Das widerspricht dem Ziel: wir bauen
**Funktionen** nach, nicht Programme.

## Entscheidung
1. **Nichts wird kopiert** — kein Code, keine Texte, keine Grafiken, auch nicht aus OSS, auch
   wenn die Lizenz es erlaubt. Wir lesen, verstehen, beschreiben die Funktion in eigenen Worten
   und bauen sie neu. Ausnahmen gibt es nur für die Projekte aus ADR 0015 (wir *nutzen* und
   *erweitern* sie, wir kopieren nicht aus ihnen).
2. **Programme werden nach Ideen ausgewählt, nicht nach Menge.** Dokumentiert wird ein Programm,
   wenn es etwas Besonderes kann (Beispiel Wiki: Tango). Pro Kategorie gehören dazu die
   prägenden Programme (die, die Nutzer gelernt haben) und die mit guten neuen Ideen.
   `index.md` des Frontends sagt in einem Abschnitt **„Notable ideas“**, warum es hier steht.
3. **Was recherchiert wird, wird gespeichert.** Jede Recherche (auch Leo-Recherche) landet mit
   Quelle und Datum in der Doku, damit niemand — auch kein Modell — dieselbe Suche zweimal
   macht. Nur speichern, was ohnehin gesucht wurde; nicht auf Vorrat recherchieren.
4. **Belege**: wie bisher ✅ (an Primärquelle geprüft) / ⚠️ (ungeprüft), Fundstellen im
   `index.md` des Frontends.
5. Bestehende Programm-Dokus bleiben als Rohmaterial liegen; sie werden beim Umbau nicht
   gelöscht, aber auch nicht vervollständigt, wenn sie keine eigene Idee beitragen.

## Folgen
- `requirements.md` pro Kategorie (ADR 0006 Punkt 4) bleibt der Ort, an dem aus den Frontends
  die Pflichtmenge und die Kür werden.
- Die Freeze-Regel „3–5 Masken“ entfällt; `temp/apps-plan.md` ist als Abarbeitungsliste überholt.
