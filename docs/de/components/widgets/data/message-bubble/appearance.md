# Message Bubble (Nachrichtenblase) - Aussehen

## Grundlayout

```
 Anna · 10:42                    🔒
┌──────────────────────────────┐
│ ↳ Re: Meeting at 3?          │
│ Yes, see you there.          │
│ 📎 agenda.pdf                │
└──────────────────────────────┘
 👍 2  ❤ 1                      ✓✓
```

## Varianten

| Variante | Aussehen |
|---|---|
| **incoming** | neutrale Fläche, links, Spitze links |
| **own** | Akzentfläche, rechts, Status am Ende |
| **compact** | ohne Fläche, eine Zeile mit Absender und Auszug |

## Größen

| Größe | Höhe | Verwendung |
|---|---|---|
| `small` | auto | kompakt |
| `medium` | max. 480 px | Standard |
| `large` | max. 640 px | breite Fenster |

## Farben und Zustände

| Zustand | Aussehen |
|---|---|
| Standard | Oberfläche der Absenderseite |
| Ausgewählt | Akzentrahmen |
| Bearbeitet | kleine Markierung „bearbeitet“ |
| Gelöscht | gedämpfter Text „Nachricht gelöscht“ |
| Fehlgeschlagen | Fehlerrahmen mit Hinweis zum erneuten Senden |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|---|---|
| `background` | leichte Hervorhebung, wenn Aktionen verfügbar sind |
| – | die Aktionsleiste stellt der Host bereit |

## Reaktiv

- Maximal 80 % der Breite des Containers auf schmalen Bildschirmen.
- Anhänge werden verkleinert; die Reaktionsleiste bricht um.
