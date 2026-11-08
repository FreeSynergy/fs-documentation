# Zoom In

## Beschreibung

Zoom In blendet ein Element ein, während es von einem Skalierungsfaktor unter 1 auf seine volle Größe (1) wächst. Meist kommt ein gleichzeitiges Einblenden dazu. Das Element "tritt" dadurch sichtbar auf die Bühne.

## Verwendung

- modale Dialoge und Lightboxen beim Öffnen heranziehen
- Galerien: ein Vorschaubild auf die volle Ansicht vergrößern
- neue Listeneinträge sanft erscheinen lassen (Eintrag hinzufügen)
- Kontextmenüs und Popover weich öffnen
- eine Kamera- oder Fotovorschau aus einer Ecke heranzoomen
- Erfolgsmeldungen und Badges durch Vergrößern hervorheben

## Dauer

- Typisch: 200–350 ms
- Standardwert: 250 ms
- Mit einer federnden Kurve (`cubic-bezier`) ist ein leichtes Überschwingen möglich

## Unterschied zu Scale In

- Zoom In: Einblenden mit einer Startskalierung unter 1, in der Regel kombiniert mit einem Einblenden der Deckkraft
- Scale In: reines Wachsen der Größe (z. B. 0 % → 100 %) ohne Änderung der Deckkraft
