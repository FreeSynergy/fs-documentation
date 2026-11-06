# Message Composer (Nachrichtenverfasser) - Aussehen

## Grundlayout

```
┌─────────────────────────────────────────┐
│ To   [Anna 🔒] [Ben ⚠] [ + ]            │
│ Subject  ___________________________    │
├─────────────────────────────────────────┤
│ Text of the message …                   │
├─────────────────────────────────────────┤
│ 📎 file.pdf   [😊] [@]        [ Send ]  │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|---|---|
| **chat** | eine Zeile, die bis zu einer Grenze wächst; Senden-Schaltfläche am Ende |
| **mail** | Kopfzeilen über dem Editor |
| **reply** | eine Zeile, keine Werkzeugleiste |

## Größen

| Größe | Höhe | Verwendung |
|---|---|---|
| `small` | 80 px | Antwortfeld |
| `medium` | 300 px | Standard |
| `large` | 500 px | Mailfenster |
| `full` | 100% | gesamter Bereich |

## Farben und Zustände

| Zustand | Aussehen |
|---|---|
| Standard | Oberfläche des Themes |
| Fehler | Fehlerrahmen an der fehlerhaften Stelle |
| Wird gesendet | Bedienelemente deaktiviert, Fortschrittsanzeige |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|---|---|
| `background` | Schaltflächen-Hover |
| `cursor` | Textcursor im Editor |

## Reaktiv

- Die Chat-Variante wächst bis zu einer maximalen Höhe und scrollt danach.
- Anhänge und Emojis wandern auf schmalen Bildschirmen in eine Werkzeugzeile.
