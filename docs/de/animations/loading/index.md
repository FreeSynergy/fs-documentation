# Laden (loading)

Ladeanimationen überbrücken eine Wartezeit und beantworten drei verschiedene Fragen:
*Was passiert gerade?* (Dots), *Wie lange noch?* (Progress) und *Was kommt?* (Skeleton).

## Elemente

- **progress** - messbarer Fortschritt (Balken, Kreis)
- **skeleton** - Platzhalterformen im Layout des späteren Inhalts
- **typing** - Tipp-Indikator (drei Punkte in Chats)
- **dots** - drei punktierte Ladekugeln als kompakter Aktivitätsindikator

## Welche zuerst?

| Fall | Animation |
|------|-----------|
| Layout der Inhalte bekannt | skeleton |
| Fortschritt messbar | progress |
| unter 1 s Wartezeit | keine – sonst flackert es |
| kurze Anfrage, unbekannter Umfang | dots |
| Antwort aus einem Chat-Partner | typing |

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Endlos (loop)](../loop/) - dauerhafte Signale ohne Ladebezug
- [Liste (list-view)](../../components/data/list-view/description.md) - Skeleton in Listen
