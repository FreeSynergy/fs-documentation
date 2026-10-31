# Pol.is - Struktur und UI/UX

## Conversations-Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ „Was braucht unser Platz?“   [Dein Kommentar………]  [Senden]     │
├───────────────┬─────────────────────────────────────────────────┤
│ Kartenstapel  │  Meinungskarte (Scatter, Gruppen A/B/C)         │
│ „Park gebühren│   ●A  ●●B        ⌒ Konsenszone                  │
│  frei“        │  ●C ●     ●A                                   │
│  [👍][👎][pass]│  Gruppen-Chips: A=28% B=35% C=19%              │
└───────────────┴─────────────────────────────────────────────────┘
```

## UI/UX

- Kartenstapel-Mechanik (wie Dating-App) senkt Mitmach-Hürde extrem
- Gruppenfarben durchgängig; „important“-Flag für wichtige Karten

## Interaktionen

- Bewerten per Klick/Tastaturknöpfe; Kommentar-Editor mit Zeichengrenze
- Live-Aktualisierung ohne Reload (Gruppenzahlen bewegen sich)

## Responsive Design

- voll mobiltauglich (Kernziel: Teilnahme per Handy)

## Accessibility

- Basis-Web; Bewertungen auch per Tastatur (Buttons fokussierbar)

## Performance

- Cluster-Berechnung sekundenschnell; sehr große Conversations mit Karten-Paging
