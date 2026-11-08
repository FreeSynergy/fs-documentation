# Collapse

## Beschreibung

Collapse verkleinert die Höhe (optional die Breite) eines Elements Schritt für Schritt auf 0, bis der Platz, den es im Layout belegt, verschwindet. Der Inhalt wird dabei abgeschnitten, nicht skaliert.

## Verwendung

- einen Akkordeon-Eintrag schließen
- erweiterte Formularfelder ausblenden
- eine Seitenleiste oder einen Filterbereich wieder einklappen
- Tabellengruppen und verschachtelte Listen schließen
- ausblendbare Infoboxen ("weniger anzeigen")
- eine Navigationsgruppe in der Seitenleiste

## Dauer

- Typisch: 200–350 ms
- Standardwert: 250 ms

## Unterschied zu Expand

- Expand: die Gegenrichtung – die Höhe wächst von 0 auf die natürliche Inhaltshöhe.
- Fade Out: nur die Deckkraft sinkt, der Layoutplatz bleibt und fällt nicht zusammen.
- Scale Out: das ganze Element wird verkleinert (der Text skaliert mit). Collapse schneidet nur den Inhalt ab.
