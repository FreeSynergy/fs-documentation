# Apple Mail iOS 26 — Funktionen

Beschreibt das **fremde Programm**. Unser Umsetzungsstand steht nur in
[Anforderungen](../../../requirements.md) (ADR 0012). ✅ = gesehen · ⚠️ = nicht gesehen.
(mac) = nur in der aktuellen macOS-Version gesehen.

## Hauptfunktionen

### Posteingang
- Automatische Kategorien Primär, Transaktionen, Updates, Werbung als Chips; der aktive Chip zeigt seinen Namen ✅
- Sheet „Über Kategorien“: was jede Kategorie enthält und wie viele Mails letzte Woche sortiert wurden ✅
- Kategorien ein- und ausblenden, Kontaktfotos anzeigen (Menü Darstellung am Mac) ✅
- Zeile: Avatar oder Memoji, Absender, Zeit, Chevron, Betreff mit Emoji, zweizeilige Vorschau ✅; VIP-Stern links neben der Zeile ✅; Punkt für ungelesen ⚠️ (in den iOS-26-Bildern nicht sichtbar)
- Untertitel unter dem Titel: Konto und „gerade aktualisiert“ ✅
- Mailinglisten-Banner mit Abmeldung ✅; Hinweis „gefunden in <Mailbox>“ ✅

### Mailboxen
- Bearbeitbare Liste intelligenter Mailboxen mit Häkchenfeldern und Ziehgriffen: Posteingang, VIP, Markiert, Ungelesen, An/Cc, Anhänge, Thread-Benachrichtigungen, Erinnere mich, Nachverfolgen, Später senden, Stummgeschaltete Threads ✅
- Neue Mailbox (echter Ordner) ✅; Intelligente Mailboxen, definiert über Regeln, z. B. „Heute“, „Familienfotos“ (mac) ✅
- Alle Posteingänge / Alle Entwürfe / Alle gesendet über alle Konten (mac) ✅

### Lesen
- Pfeiltasten nach oben/unten zur vorherigen/nächsten Mail; Zurück-Schaltfläche mit Anzahl ungelesener Mails ✅
- Schaltfläche „Zusammenfassen“ oberhalb der Mail ✅
- Kopfzeile mit Avatar, Absender, Empfängern (aufklappbar), Zeit und Markierung ✅
- Reichhaltige Links in Mails (Karten-Standortkarte, Anleitungskarte mit „In Karten öffnen“) (mac) ✅

### Sichtung
- Wisch-Aktionen: Mehr, Markieren, Löschen ✅ (Wischen nach links)
- Aktionsblatt: Antworten, Allen antworten, Weiterleiten, Löschen (große Kacheln); Erinnere mich; Markierung aufheben; Zeile mit Markierungsfarben ✅
- Langdruck-Vorschau mit Menü: Antworten, Allen antworten, Weiterleiten, Markieren ›, Benachrichtigen, Stummschalten ✅
- Auswahlmodus → Verschieben in eine Mailbox über ein Sheet mit gestapelter Vorschau der Auswahl ✅
- Archivieren, Junk, Verschieben, Markieren aus der Werkzeugleiste (mac) ✅

### Verfassen
- Verfasser mit An, Cc, Betreff, Von, Signatur, Bildgröße, Nachrichtengröße (mac) ✅
- Schwebende Werkzeugleiste: Antwortmodus, Textformat (Aa), Emoji, Schreibwerkzeuge ⚠️ (Symbol), Kopffelder, Anhängen ›, Später senden ⚠️ (Uhr-Pfeil-Symbol) (mac) ✅
- Anhang-Menü: Dateien, Anhänge einbeziehen, Fotos, Foto aufnehmen / Dokumente scannen / Skizze von einem nahen iPad hinzufügen (mac) ✅
- Zitierte Antwort mit farbigem Balken markiert (mac) ✅
- Aliasse pro Konto und Absender-Auswahl (macOS 10.12) ✅
- Später senden und Erinnere mich (als Mailboxen und Sortierschlüssel) ✅

### Suche
- Suchkapsel unten mit Diktierfunktion ✅
- Bereich: alle Mailboxen / aktuelle Mailbox ✅
- Top-Treffer, dann weitere bzw. alle Treffer; Treffer-Wörter hervorgehoben ✅
- Vorschläge während der Eingabe („Betreff enthält …“, vervollständigte Wendungen) (mac) ✅

### Kontakte
- Kontaktkarte eines Absenders: Zu VIP hinzufügen, Mails dieses Kontakts suchen, Nachricht senden, Kontakt teilen, zu Favoriten hinzufügen, zu Liste hinzufügen ✅; Kontakt blockieren ⚠️ (teilweise verborgen)

### Datenschutz und Sicherheit
- Schalter „Mailaktivität schützen“ ✅
- Adressen markieren: Adressen außerhalb angegebener Domains hervorheben ✅

### Sortieren und Ansicht (Menü Darstellung am Mac) ✅
- Sortieren nach Anhängen, Datum, Erinnere mich, Später senden, Markierungen, Absender, Größe, Betreff, Empfänger, ungelesen; aufsteigend/absteigend; nur Posteingang / alle Mailboxen
- Filter; Spaltenlayout; Vorschau unten; Datum/Uhrzeit, An/Cc, Größe, Kontaktfoto, Kategorien anzeigen
- Unterhaltungen hervorheben; nach Unterhaltung ordnen; alle Unterhaltungen ein- und ausklappen

### Konten
- Konto über E-Mail-Adresse hinzufügen oder einen Anbieter aus einer Liste wählen ✅

## Was Apple Mail NICHT macht
- Keine Regeln unter iOS (Regeln gibt es am Mac ⚠️ — gesehen als Einstellungs-Registerkarte in macOS 10.12 ✅)
- Keine farbigen Kategorien/Labels über die Markierungsfarben hinaus ✅ (nur Markierungen gesehen)
- Kein Zurückholen gesendeter Mails, keine Lesebestätigungen ⚠️
- Kein OpenPGP ⚠️; keine Web-Version ⚠️
