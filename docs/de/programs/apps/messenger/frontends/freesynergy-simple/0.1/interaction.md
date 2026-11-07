# FreeSynergy Simple 0.1 — Interaktion

Gesten gehören zum Frontend, nicht zum Programm oder zum Verfassen-Feld (ADR 0037).

## Lesebildschirm
| Geste | Aktion | Fähigkeit |
|-------|--------|-----------|
| nach links wischen | nächste ungelesene Nachricht | `conversation.open` / `message.open` |
| nach rechts wischen | vorherige ungelesene Nachricht ⚠️ Richtung vorgeschlagen | `message.open` |
| nach oben wischen | weiterleiten | `message.forward` |
| nach unten wischen | löschen (Toast mit Rückgängig) | `message.delete` |
| Doppeltippen | antworten | `message.reply` |

## Verfassen-Bildschirm
| Geste | Aktion | Fähigkeit |
|-------|--------|-----------|
| nach oben wischen | senden | `message.send` |
| nach unten wischen | abbrechen (Toast mit Rückgängig; Entwurf bleibt bis zum Ende der Rückgängig-Frist erhalten) | — |
| nach links wischen | als Entwurf speichern und schließen ⚠️ vorgeschlagen | `draft.save` |
| nach rechts wischen | anhängen (Foto, Datei) ⚠️ vorgeschlagen | `attachment.add` |
| Tippen auf 👤+ | Empfänger hinzufügen → Empfängerauswahl | — |

## Barrierefreiheit (jede Geste hat ein Gegenstück)
- **Sichtbare Hinweise** bei der ersten Nutzung (Pfeile am Rand), die danach ausblenden.
- **Langes Drücken** → Menü mit denselben Aktionen wie die Gesten.
- **Tastatur:** ← → nächste/vorherige ungelesene, ↑ weiterleiten, Entf löschen, Enter antworten; beim Verfassen Strg+Enter senden, Esc abbrechen.
- **Bildschirmleser:** Die Aktionen werden als benannte Aktionen an der Nachricht angeboten (braucht Barrierefreiheitsunterstützung in Blinc — `todo/upstream.md`).
- Gesten werden für Finger, Maus (Ziehen) und Stift gleichermaßen erkannt (ADR 0015).
