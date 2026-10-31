# Collapse

## Beschreibung

Collapse reduziert die Höhe (optional die Breite) eines Elements schrittweise auf 0, bis der belegte Platz im Layout verschwindet. Der Inhalt wird dabei beschnitten, nicht skaliert.

## Verwendung

- Akkordeon-Eintrag zuklappen
- Erweiterte Formularfelder ausblenden
- Seitenleiste oder Filterbereich einziehen
- Tabellen-Gruppen und verschachtelte Listen schließen
- Ausblendbare Info-Boxen („Weniger anzeigen“)
- Navigationsgruppe in der Seitenleiste

## Dauer

- Typisch: 200–350 ms
- Standardwert: 250 ms

## Unterschied zu Expand

- Expand: gegenläufig - die Höhe wächst von 0 auf die natürliche Inhaltshöhe
- Fade Out: nur die Deckkraft sinkt, der Layout-Platz bleibt erhalten und kollabiert nicht
- Scale Out: das ganze Element wird verkleinert (Text skaliert mit); Collapse schneidet den Inhalt nur ab
