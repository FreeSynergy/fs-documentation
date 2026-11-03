# Cascade

## Beschreibung

Cascade übernimmt wie [Stagger](../stagger/description.md) die Zeitsteuerung der Kind-Animationen, ergänzt aber eine Richtung und eine veränderliche Schrittweite: Der Start wandert über das Layout (von links nach rechts, von oben nach unten, von außen nach innen), und der Abstand zwischen den Starts kann pro Element wachsen oder schrumpfen. Der Effekt liest sich wie eine Welle, die über eine Fläche läuft.

## Verwendung

- Menüeinträge von der Leiste aus herunterkaskadieren
- Foto-Raster diagonal von der oberen linken Ecke erscheinen lassen
- Lange Listen beschleunigt starten lassen (kleiner werdender Abstand)
- Dashboard-Karten von außen nach innen aufbauen
- Ausgang als ablaufende Welle, damit eine Fläche „von rechts nach links“ leer wird
- Wizard-Schritte, die sich nacheinander aufbauen

## Dauer

- Typisch: 30–80 ms Abstand pro Element, gesamt wie bei Stagger
- Wachsende Schrittweite: Start bei 20 ms, pro Element +10 ms
- Richtungsabhängig: lange Listen besser abbremsen (`stepLimit`), sonst wirkt es träge

## Unterschied zu Stagger

- Stagger nutzt einen festen Offset pro Index; Cascade richtet die Starts am Layout aus und darf die Schrittweite verändern.
- Stagger ist richtungslos; Cascade braucht eine `richtung` (oder leitet sie aus dem Layout ab).
