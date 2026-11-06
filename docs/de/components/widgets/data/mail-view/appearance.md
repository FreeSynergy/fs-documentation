# Mail View (Mailansicht) - Aussehen

## Grundlayout

```
┌─────────────────────────────────────────┐
│ From     anna@example.org   🔒 ✔ signed │
│ To       team@example.org               │
│ Subject  Meeting notes                  │
│ Date     05 Nov 2026, 10:42             │
├─────────────────────────────────────────┤
│ body (text or sanitised HTML)           │
├─────────────────────────────────────────┤
│ 📎 notes.pdf   📎 plan.png              │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|---|---|
| **full** | Kopfblock, Trennlinie, Text, Anhangszeile |
| **compact** | zwei Zeilen: Absender und Betreff, Auszug |
| **source** | Originaltext in Monospace ⚠️ |

## Größen

| Größe | Höhe | Verwendung |
|---|---|---|
| `small` | 200 px | Listenvorschau |
| `medium` | 400 px | Standard |
| `full` | 100% | Lesebereich |

## Farben und Zustände

| Zustand | Aussehen |
|---|---|
| Standard | Oberfläche des Themes |
| Unverschlüsselt | fehlerfarbene Markierung über [encryption-state](../../../primitives/feedback/encryption-state/) |
| Signatur ungültig | Fehlermarkierung im Kopf |
| Externe Inhalte blockiert | Infoleiste über dem Text |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|---|---|
| `background` | Kopfzeilen werden für Adressaktionen hervorgehoben |
| `tooltip` | vollständige Adresse und Signaturdetails |

## Reaktiv

- Der Kopf reduziert sich auf Absender und Betreff; der Rest klappt beim Antippen auf.
- Anhänge brechen unter dem Text um.
