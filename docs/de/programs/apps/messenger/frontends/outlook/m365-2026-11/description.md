# Outlook m365-2026-11 — Beschreibung

Dokumentiert am 2026-11-05 anhand von Screenshots, die der Projektverantwortliche gesammelt hat (intern, nicht veröffentlicht,
ADR 0038). Microsoft nennt im neuen Outlook keine Versionsnummer; dieser Ordner beschreibt den **aktuellen Microsoft-365-Stand
vom November 2026** („neues Outlook“ für Windows und Web sowie die mobile App). Einige Screenshots zeigen **klassisches Outlook**
(das Win32-Desktop-Programm) oder ältere Web-Zustände; diese sind entsprechend markiert.

✅ = in einem Screenshot gesehen · ⚠️ = erschlossen oder anderweitig bekannt, nicht gesehen

## Überblick
Outlook ist Microsofts Mail- und Kalender-Client innerhalb von Microsoft 365. Die aktuelle Generation („neues Outlook“) ist auf Windows und im Browser dieselbe Webanwendung ✅; die mobile App folgt denselben Ideen in einem Telefon-Layout ✅. Klassisches Outlook existiert daneben weiter und unterscheidet sich in den Menüs (volles Menüband, Datei-Backstage, Registerkarte Senden/Empfangen) ✅.

## Was es macht
- Mehrere Mailkonten verschiedener Anbieter in einem Fenster — Microsoft 365, Outlook.com, Gmail, Yahoo, iCloud, IMAP ✅.
- Unterhaltungsliste, aufgeteilt in einen Strom „Fokussiert“ und „Andere“, mit angehefteten Mails oben und Datumsgruppen (heute, gestern, diese Woche) ✅.
- Zeitgesteuerte Mailverarbeitung: Versand terminieren, Senden rückgängig machen, Zurückstellen („erneut erinnern“), Nachverfolgungs-Markierungen mit Erinnerungen, eine gesendete Nachricht zurückrufen ✅.
- Kalenderfunktionen direkt in der Mail: Einladungen im Lesebereich beantworten, ein Chip „bevorstehender Termin“ in der Titelleiste, ein vollständiges Kalendermodul ✅.
- Offline-Modus mit einer gewählten Auswahl an Ordnern und Tagen ✅ (Einstellung im neuen Outlook; klassisches Outlook hat einen Schalter „Offline arbeiten“) ✅.
- KI-Assistent (Copilot) für Zusammenfassungen, Schreibhilfe und generierte Themes ✅ — für uns außerhalb des Umfangs, außer als Ideenliste (siehe [Funktionen](features.md)).

## Für wen es passt
Büroangestellte in Organisationen, die Microsoft 365 nutzen; Menschen, die Mail und Kalender gemeinsam nutzen. Viele Menschen haben den Umgang mit Mails hier *gelernt* — dies ist das Referenz-Frontend „was alle kennen“ aus ADR 0038 ⚠️ (Einschätzung).

## Abgrenzung

### Outlook vs. Apple Mail
Outlook ist dicht, werkzeugleistengesteuert und desktop-orientiert (Menüband, drei Bereiche, Kontextmenüs per Rechtsklick); Apple Mail ist sparsam, gestengesteuert und telefonorientiert (Wisch-Aktionen, Sheets, große Titel). Beide sortieren den Posteingang inzwischen automatisch (Fokussiert/Andere bzw. Kategorien) ✅.

### Neues Outlook vs. klassisches Outlook
Neues Outlook: vereinfachtes einzeiliges Menüband, Einstellungen in einem dreispaltigen Dialog, Web-Technik ✅. Klassisch: volles Menüband mit vielen Registerkarten, Datei-Backstage für Konto- und Profileinstellungen, Gruppen Senden/Empfangen, Statusleiste mit konfigurierbaren Zählern, COM-Add-ins (gesehen: Menübänder von Drittanbietern) ✅.

## Technische Details
- Plattformen: Windows-App und Browser (gleiche Oberfläche) ✅, Android/iOS-App ✅, klassisches Windows-Desktop-Programm ✅.
- Speicherung/Synchronisation: serverseitiges Postfach (Exchange Online) mit optionaler lokaler Offline-Kopie ✅ (Einstellung); Synchronisationsprotokoll nicht sichtbar ⚠️ (siehe [API](api.md)).
- Verschlüsselung: eine Sensibilitäts- und Schutzsteuerung (Schild-Symbol) im Verfasser ✅; S/MIME und Microsoft-Purview-Nachrichtenverschlüsselung sind bekannt ⚠️.
- Selbst hosten: nein — nur Microsoft-Cloud (Exchange Server vor Ort existiert ⚠️).
