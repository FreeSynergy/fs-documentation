# Alert (Warnung)

## Beschreibung

Ein Alert ist eine Status-Meldung (Info, Warning, Error, Success).

## Verwendungszweck

- Status-Meldungen anzeigen
- Fehler anzeigen
- Erfolge anzeigen
- Warnungen anzeigen

## Varianten

| Variant | Farbe | Beschreibung |
|---------|-------|--------------|
| **Info** | Blau | Informationsmeldung |
| **Success** | Grün | Erfolgsmeldung |
| **Warning** | Orange/Gelb | Warnmeldung |
| **Error** | Rot | Fehlermeldung |

## Layout

```
┌─────────────────────────────────────────┐
│ [✕]                                     │
│ 📢 Titel                                │
│ Beschreibungstext...                    │
│                                         │
│ [Aktion]                                │
└─────────────────────────────────────────┘
```

## Features

- Dismissible (Schließbar)
- Icon
- Title
- Description
- Action Button

## Best Practices

- Klarer Text
- Konsistente Farben
- Action-Buttons
- Accessibility
