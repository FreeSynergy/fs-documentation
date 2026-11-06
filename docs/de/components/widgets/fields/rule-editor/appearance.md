# Rule Editor (Regeleditor) - Aussehen

## Grundlayout

```
┌─────────────────────────────────────────────┐
│ [on]  If [Sender ▾] [contains ▾] [news@]    │
│       Then [Move to ▾] [Newsletter ▾]  [+][−]│
├─────────────────────────────────────────────┤
│ [+ Add rule]                                │
└─────────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|---|---|
| **list** | umrandete Zeilen, Ziehgriff links |
| **simple** | eine einzelne Zeile ohne Griff |

## Größen

| Größe | Höhe | Verwendung |
|---|---|---|
| `medium` | auto | Standard |
| `full` | 100% | Einstellungsseite |

## Farben und Zustände

| Zustand | Aussehen |
|---|---|
| Aktiviert | normaler Text |
| Deaktiviert | gedämpfte Zeile |
| Ungültig | Fehlerrahmen und Meldung an der Zeile |
| Ungespeichert | Akzentmarkierung |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|---|---|
| `background` | Zeilenhervorhebung |
| `border` | Ziehgriff wird sichtbar |

## Reaktiv

- Bedingung und Aktion stapeln sich auf schmalen Bildschirmen vertikal.
- Zum Umsortieren dienen Schaltflächen „nach oben“ und „nach unten“, wenn Ziehen nicht verfügbar ist.
