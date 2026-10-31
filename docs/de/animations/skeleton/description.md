# Skeleton

## Beschreibung

Skeleton zeigt während des Ladens statische Platzhalterformen im Layout des späteren Inhalts – Balken, Kreise und Blöcke mit einem wandernden Schimmer.
Der Nutzer erkennt die kommende Struktur, bevor die Daten eintreffen, und beim Einsetzen der echten Inhalte entsteht kein Layout-Sprung.

## Verwendung

- Listenansichten vor dem ersten Dateneingang, siehe [list-view](../../components/lists/list-view/description.md)
- Rasteransichten beim Nachladen, siehe [grid-view](../../components/lists/grid-view/description.md)
- Tabellen beim Seitenaufbau, siehe [table](../../components/lists/table/description.md)
- Detailseiten und Karten, die asynchron befüllt werden
- Ladezustände: Ersatz für Spinner, wenn das Layout der Inhalte bekannt ist

## Dauer

- Typisch: 1200–1800 ms pro Schimmer-Zyklus

## Unterschied zu Progress und Glow

- Progress: zeigt einen messbaren Wert (z. B. 40 %); Skeleton macht keine
  Aussage darüber, wie weit das Laden fortgeschritten ist.
- Glow: Leuchten als Statussignal (Auswahl, Live); Skeleton ist ein
  Platzhalter, der verschwindet, sobald echte Inhalte angekommen sind.
