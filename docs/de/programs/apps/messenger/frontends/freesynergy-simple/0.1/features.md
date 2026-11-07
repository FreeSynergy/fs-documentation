# FreeSynergy Simple 0.1 — Funktionen

| Funktion | Fähigkeit (Anforderungen) |
|----------|---------------------------|
| Vollbild-Lesen, ungelesene zuerst | `conversation.list`, `message.open` |
| nächste / vorherige ungelesene | `message.open` |
| weiterleiten, löschen mit Rückgängig, antworten | `message.forward`, `message.delete`, `message.reply` |
| neue Nachricht von der Listenansicht aus | `message.send` |
| einfaches Textfeld zum Verfassen, Anhänge | `message.send`, `attachment.add` |
| Entwürfe | `draft.save` |
| Verschlüsselungsstatus bei jeder Nachricht; unverschlüsselte mit Link zur Anleitung markiert | `message.encryption` (ADR 0018, 0031) |
| Empfängerauswahl mit Live-Filter | Kontakt-Programm über seine Workbench (ADR 0037) |
| **Neuer Kontakt spontan:** Eingetippter Text, der niemandem entspricht, öffnet ein Formular mit den Feldern, die nötig sind, um die Person zu erreichen (Telefon, E-Mail, Matrix, Telegram, …); der eingetippte Text füllt das richtige Feld vor (E-Mail-Adresse → E-Mail, `+49…` → Telefon, `@name:server` → Matrix) ⚠️ Erkennungsregeln vorgeschlagen | Kontakte: `Create` JSContact-Karte |
| minimale Einstellungen: Konten, Benachrichtigungen, Theme, Textgröße | `account.*` |

## Was es NICHT tut (bewusst)
Ordner, Regeln, Suchfilter, Mehrfachauswahl, Formatierung, Reaktionen, Thread-Ansicht — das alles gehört zum
vollständigen Frontend (Nr. 2).
