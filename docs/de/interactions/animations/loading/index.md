# Laden (Loading)

Lade-Animationen überbrücken eine Wartezeit und beantworten drei verschiedene Fragen:
*Was passiert gerade?* (Punkte), *wie lange noch?* (Fortschritt) und *was kommt?* (Skeleton).

## Elemente

- **progress** – messbarer Fortschritt (Balken, Kreis)
- **skeleton** – Platzhalterformen im Layout des späteren Inhalts
- **typing** – Tippanzeige (drei Punkte in Chats)
- **dots** – drei Punkte als Lade-Kugeln, als kompakte Aktivitätsanzeige

## Welche zuerst?

| Fall | Animation |
|------|-----------|
| Layout des Inhalts bekannt | skeleton |
| Fortschritt messbar | progress |
| unter 1 s Wartezeit | keine – sonst flackert es |
| kurze Anfrage, unbekannter Umfang | dots |
| Antwort von einem Chatpartner | typing |

## Siehe auch

- [Übersicht Animationen](../index.md)
- [Schleife](../loop/) – dauerhafte Signale ohne Ladebezug
- [Listenansicht](../../../components/widgets/data/list-view/description.md) – Skeleton in Listen
