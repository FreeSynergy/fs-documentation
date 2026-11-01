# Toast (Benachrichtigung)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `Info`, `Success`, `Warning`, `Error` |
| **Zustände** | `paused`, `dismissing` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `slide-in`, `fade-out`, `stagger` |
| **Verwandt** | `alert`, `badge`, `popover` |
| **Status** | dokumentiert |

## Beschreibung
Ein Toast ist eine Pop-up-Benachrichtigung, die meist oben rechts erscheint.

## Verwendungszweck

- Kurze Benachrichtigungen
- Erfolgs-Meldungen
- Fehler-Meldungen
- Informations-Meldungen

## Varianten

| Variant | Farbe | Beschreibung |
|---------|-------|--------------|
| **Info** | Blau | Informationsmeldung |
| **Success** | Grün | Erfolgsmeldung |
| **Warning** | Orange/Gelb | Warnmeldung |
| **Error** | Rot | Fehlermeldung |

## Features

- Auto-dismiss (Automatisches Schließen)
- Dismissible (Benutzerdefiniertes Schließen)
- Action Button
- Position (Top Right, Bottom Right, etc.)

## Abgrenzung

- **Nicht verwechseln mit** [alert](../alert/): ein Toast verschwindet von selbst und verlangt
  keine Reaktion; eine Alert-Meldung bleibt, bis sie geschlossen oder behoben ist.
- **Nicht verwechseln mit** [alert-dialog](../../overlays/alert-dialog/): wenn der Nutzer
  entscheiden muss, ist ein Dialog nötig — ein Toast überbrückt keine Entscheidung.
- **Nicht verwechseln mit** [popover](../../overlays/popover/): ein Popover ist an ein Element
  gebunden, der Toast an eine Bildecke.
- **Nicht verwechseln mit** [badge](../badge/): ein Badge markiert dauerhaft, ein Toast meldet
  einmalig ein Ereignis.

## Best Practices

- Klarer Text
- Short (Kurz)
- Non-intrusive (Nicht störend)
- Feedback

## Layout

```
┌─────────────────────────────────────────┐
│ [✕]  📢 Titel                           │
│      Beschreibungstext...               │
└─────────────────────────────────────────┘
```

## Siehe auch

- [feedback – Übersicht](../index.md)
- [Alert](../alert/) — Meldung, die stehen bleibt
- [Alert Dialog](../../overlays/alert-dialog/) — wenn der Nutzer entscheiden muss
- [Basiskomponente](../../basics/base/)
