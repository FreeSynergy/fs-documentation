# Cascade

## Beschreibung

Cascade übernimmt wie [Stagger](../stagger/description.md) die Zeitsteuerung der Kindanimationen, fügt aber eine Richtung und einen veränderlichen Schritt hinzu. Der Start wandert durch das Layout (von links nach rechts, von oben nach unten, von außen nach innen), und der Abstand zwischen den Starts kann pro Element wachsen oder kleiner werden. Der Effekt wirkt wie eine Welle, die über eine Fläche läuft.

## Verwendung

- Menüeinträge kaskadiert aus der Leiste herunterfahren
- ein Fotoraster diagonal von der oberen linken Ecke erscheinen lassen
- lange Listen beschleunigt starten lassen (kleiner werdender Abstand)
- Dashboard-Karten von außen nach innen aufbauen
- einen Ausgang als auslaufende Welle, sodass sich eine Fläche "von rechts nach links" leert
- Assistenten-Schritte, die nacheinander aufgebaut werden

## Dauer

- Typisch: 30–80 ms Abstand pro Element, insgesamt wie bei Stagger
- Ein wachsender Schritt: Start bei 20 ms, +10 ms pro Element
- Richtungsabhängig: lange Listen besser abbremsen (`stepLimit`), sonst wirkt es träge

## Unterschied zu Stagger

- Stagger nutzt einen festen Versatz pro Index. Cascade richtet die Starts am Layout aus und darf den Schritt verändern.
- Stagger hat keine Richtung. Cascade braucht eine `richtung` (oder leitet sie aus dem Layout ab).
