# Zoom In

## Beschreibung

Zoom In blendet ein Element ein, während es von einer Skalierung unter 1 auf seine volle Größe (1) skaliert – meist begleitet von einem gleichzeitigen Fade In. Das Element kommt dadurch sichtbar „auf die Bühne“.

## Verwendung

- Modal-Dialoge und Lightboxen beim Öffnen aufziehen
- Galerien: Thumbnail zur Großansicht heranziehen
- Neue Listenelemente sanft erscheinen lassen (Add-Item)
- Kontextmenüs und Popovers weich aufklappen
- Kamera- oder Foto-Vorschau aus einer Ecke heranzoomen
- Erfolgsmeldungen und Badges durch Aufskalieren hervorheben

## Dauer

- Typisch: 200–350ms
- Standardwert: 250ms
- Mit Federkurve (`cubic-bezier`) ist leichtes Überschwingen möglich

## Unterschied zu Scale In

- Zoom In: Einblenden mit Start-Skalierung unter 1, in der Regel kombiniert mit Fade In der Deckkraft
- Scale In: Reines Wachstum der Größe (z. B. 0 % → 100 %) ohne Änderung der Deckkraft
