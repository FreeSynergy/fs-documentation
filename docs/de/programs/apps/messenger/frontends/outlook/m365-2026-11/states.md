# Outlook m365-2026-11 — UI-Zustände

✅ = in einem Screenshot gesehen · ⚠️ = erschlossen.

| Zustand | Auslöser | Nächste Zustände |
|-------|---------|-------------|
| Online (normal) | Standard | offline, Senden |
| Offline (neues Outlook) | Einstellung „offline“ aktiv; Netz verloren ⚠️ | online — Mails/Kalender/Personen der gewählten Ordner und Tage bleiben lesbar ✅ |
| Offline arbeiten (klassisch) | Menüband-Schaltfläche „Offline arbeiten“ ✅ | online; Statusleiste zeigt „Offlinemodus“ ✅ |
| Senden/Empfangen läuft (klassisch) | „Alle Ordner senden/empfangen“ ✅ | fertig; abgebrochen („Alle abbrechen“) ✅; Fortschrittsfenster („Fortschritt anzeigen“) ✅ |
| Entwurf gespeichert | automatisches Speichern beim Schreiben ✅ | Senden; verworfen |
| Senden, Rückgängig-Fenster | „Senden“ mit Verzögerung > 0 ✅ | gesendet (nach 0–10 s, vom Benutzer gesetzt) ✅; zurück zum Entwurf („Rückgängig“) ✅ |
| Terminiert | „Versand terminieren“ mit einer Uhrzeit ✅ | gesendet zu dieser Zeit ⚠️; bearbeitet/abgebrochen ⚠️ |
| Gesendet | Verzögerung abgelaufen | Zurückrufen angefordert ✅ |
| Zurückruf angefordert | „Nachricht zurückrufen“ + Bestätigungsdialog ✅ | Zurückruf-Bericht erscheint im Posteingang ✅ |
| Zurückgestellt | Zurückstellen mit einer Uhrzeit ✅ | zurück im Posteingang zur Uhrzeit ⚠️; bis dahin in einem Ordner „Zurückgestellt“ aufgelistet ✅ |
| Markiert / Nachverfolgung | Markierung mit Fälligkeitsdatum und Erinnerung ✅ | Erinnerung wird ausgelöst ⚠️; erledigt ✅; entfernt ✅ |
| Angeheftet | „Anheften“ ✅ | Anheftung aufgehoben ⚠️ |
| Ungelesen / gelesen | öffnen oder „als ungelesen markieren“ ✅ | — |
| Fokussiert / Andere | automatische Sortierung ✅; zwischen ihnen verschieben ⚠️ | — |
| Einladung unbeantwortet | Besprechungs-Mail ✅ | angenommen / vorläufig / abgelehnt / neuer Termin vorgeschlagen ✅ |
| Benachrichtigungen an/aus je Typ | Einstellungen ✅ | — |
| Leere Liste / nichts ausgewählt | keine Auswahl | — (leerer Lesebereich nicht gesehen ⚠️) |
| Einstellungen geändert | Änderung im Einstellungsdialog ✅ | gespeichert / verworfen ✅ |

Übergänge werden über eine untere Leiste mit einer Aktion angekündigt („wird gesendet… rückgängig“) ✅ und über Mails (Zurückruf-Bericht) ✅.
