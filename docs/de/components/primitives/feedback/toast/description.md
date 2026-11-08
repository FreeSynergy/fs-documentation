# Toast (Kurzmeldung)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `info`, `success`, `warning`, `error` |
| **Zustände** | `paused`, `dismissing` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `slide-in`, `fade-out`, `stagger` |
| **Verwandt** | `alert`, `badge`, `popover` |
| **Status** | dokumentiert |

## Beschreibung
Ein Toast ist eine Benachrichtigung als Pop-up. Sie erscheint meist oben rechts.

## Verwendungszweck

- Kurze Benachrichtigungen
- Erfolgsmeldungen
- Fehlermeldungen
- Informationsmeldungen

## Varianten

| Variante | Farbe | Beschreibung |
|----------|-------|--------------|
| **info** | blau | Informationsmeldung |
| **success** | grün | Erfolgsmeldung |
| **warning** | orange/gelb | Warnmeldung |
| **error** | rot | Fehlermeldung |

## Funktionen

- Automatisches Schließen
- Schließbar (vom Nutzer geschlossen)
- Aktions-Button
- Position (oben rechts, unten rechts usw.)

## Abgrenzung

- **Nicht verwechseln mit** [alert](../alert/): Ein Toast verschwindet von allein und
  verlangt keine Reaktion. Eine Alert-Meldung bleibt, bis sie geschlossen oder erledigt ist.
- **Nicht verwechseln mit** [alert-dialog](../../../widgets/overlays/alert-dialog/): Muss der Nutzer
  entscheiden, braucht es einen Dialog. Ein Toast ersetzt keine Entscheidung.
- **Nicht verwechseln mit** [popover](../../../widgets/overlays/popover/): Ein Popover hängt an
  einem Element, der Toast an einer Bildschirmecke.
- **Nicht verwechseln mit** [badge](../badge/): Ein Badge markiert dauerhaft etwas.
  Ein Toast meldet ein Ereignis einmalig.

## Best Practices

- Klarer Text
- Kurz
- Nicht aufdringlich
- Rückmeldung

## Layout

```
┌─────────────────────────────────────────┐
│ [✕]  📢 Titel                           │
│      Beschreibungstext...               │
└─────────────────────────────────────────┘
```

## Siehe auch

- [feedback – Übersicht](../index.md)
- [Alert](../alert/) — eine Meldung, die bleibt
- [Alert Dialog](../../../widgets/overlays/alert-dialog/) — wenn der Nutzer entscheiden muss
- [Base-Komponente](../../basics/base.md)
