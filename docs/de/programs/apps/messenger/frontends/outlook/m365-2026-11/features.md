# Outlook m365-2026-11 — Funktionen

Beschreibt das **fremde Programm**. Unser Umsetzungsstand steht nur in [Anforderungen](../../../requirements.md) (ADR 0012). ✅ = in einem Screenshot gesehen · ⚠️ = nicht gesehen.
„klassisch“ = nur im klassischen Outlook gesehen.

## Hauptfunktionen

### Konten
- Mehrere Konten verschiedener Anbieter in einem Ordnerbaum — Microsoft 365, Outlook.com, Gmail, Yahoo, iCloud, IMAP ✅
- Dialog „Konto hinzufügen“, der auf dem Gerät bereits bekannte Konten vorschlägt, plus erweiterte Einrichtung ✅
- Kontoeinstellungen auf einer Backstage-Seite: Kontoeinstellungen, Namens- und Synchronisationseinstellungen, delegierter Zugriff, globales Adressbuch herunterladen, Profile wechseln/verwalten, Add-ins verwalten (klassisch) ✅
- Automatische Antworten (Abwesenheit), Signaturen, mobile Geräte, Speicher pro Konto ✅ (Einstellungsliste)
- Verteilerlisten, verwaltet über die Einstellungen ✅ (Einstellungsliste)

### Posteingang und Liste
- Aufteilung des Posteingangs in Fokussiert / Andere ✅ (auch mobil ✅)
- Mail oben in der Liste anheften (Gruppe „Angeheftet“) ✅
- Datumsgruppen in der Liste (Angeheftet, Heute, Gestern, Diese Woche, Letzter Monat) ✅
- Unterhaltungsansicht mit Chevron pro Zeile zum Aufklappen ✅
- Ungelesen erkennbar an fettem Absender, blauem Betreff und einem blauen Balken am linken Rand ✅
- Eingebetteter Besprechungs-Chip mit Datum und einer Antwortschaltfläche (RSVP) direkt in der Listenzeile ✅
- Eingebettete Bildvorschaubilder in der Listenzeile (älterer Web-Zustand) ✅
- Kategorie-Tag in der Zeile angezeigt ✅; Erwähnungs-Marker (@) in der Zeile ✅
- Reaktionszähler in der Zeile auf dem Telefon ✅
- Markierungen „intern“ / „extern“ beim Absender auf dem Telefon ✅
- Filter- und Sortierschaltflächen über der Liste ✅; Umschalter für den Auswahlmodus ✅
- Klassisch: Schnellfilter Alle / Ungelesen / Erwähnungen ✅

### Lesen
- Lesebereich mit Absender, Empfängern, Zeit, Symbolen für Antworten / Allen antworten / Weiterleiten ✅
- Präsenzpunkt an Kontakt-Avataren ✅
- Reaktionen auf empfangene Mails (Emoji mit Zähler) ✅
- KI-Zusammenfassungskarte oberhalb einer langen Unterhaltung, mit Feedback-Schaltflächen ✅
- Kalendereinladung direkt beantworten: Zeit, Link zur Online-Besprechung, Konfliktprüfung, Option „Organisator benachrichtigen“, optionale Nachricht, annehmen / vorläufig / ablehnen / neuen Termin vorschlagen ✅
- Verfolgung von Lesebestätigungen (als deaktivierter Menüeintrag gesehen) ✅
- Feier-Animationen (abschaltbar), wenn eine Mail Wörter wie „Glückwunsch“ enthält ✅

### Verfassen
- Antwort direkt im Lesebereich oder in einem eigenen Verfassfenster ✅
- Senden-Split-Schaltfläche: sofort senden oder **Versand terminieren** mit zwei Voreinstellungen und einer Auswahl für Datum und Uhrzeit ✅
- **Senden rückgängig machen**: Verzögerung von 0–10 Sekunden (Regler), eine Leiste unten mit „Rückgängig“ während des Sendens ✅
- Automatisches Speichern von Entwürfen mit „Entwurf gespeichert um <Uhrzeit>“ ✅
- Empfängerchips mit Präsenz- und Gültigkeitsmarkierung; Cc/Bcc auf Abruf ✅
- Auswahl „Von“ pro Konto ✅
- Formatierungsleiste: Schriftart, Größe, fett, kursiv, unterstrichen, durchgestrichen, hervorheben, Textfarbe, Formatvorlagen, Absatzabstand ✅
- Datei anhängen, Link einfügen, Signatur, hohe/niedrige Wichtigkeit ✅
- Vertraulichkeits- und Schutzsteuerung (Schild) ✅
- Grammatik- und Stilvorschläge in einem kleinen Popover (Editor) ✅
- Schrägstrich-Befehl im Text („/ eingeben, um Dateien und mehr einzufügen“) ✅
- Diktier-Schaltfläche, Loop-Komponenten, Apps/Add-ins im Menüband ✅ (als Menüband-Schaltflächen gesehen)
- Adressbuchsuche, Namen prüfen (klassisch) ✅

### Ordnung
- In Ordner verschieben / kopieren; archivieren; löschen; Aufräumen (Mails eines Absenders bereinigen) ✅
- Kategorien mit Name und Farbe; anlegen, bearbeiten, löschen ✅
- **Kategorisierter Suchordner**: Eine Kategorie mit Stern versehen legt einen Ordner dafür unter Favoriten ab ✅
- Abschnitt Favoriten oberhalb des Ordnerbaums ✅
- **Zurückstellen** („erneut erinnern“): später heute, morgen, dieses Wochenende, nächste Woche oder ein gewähltes Datum; zurückgestellte Mails werden in einem eigenen Ordner gesammelt ✅
- **Nachverfolgungs-Markierungen**: heute, morgen, diese Woche, nächste Woche, kein Datum, benutzerdefiniert (Startdatum, Fälligkeitsdatum, Erinnerung mit Uhrzeit und Ton), als erledigt markieren, Markierung entfernen (klassisch) ✅
- Schnellschritte (mehrstufige Aktionen mit einem Klick) ✅; Schnellaktionen beim Überfahren ✅ (Menüeintrag „Schnellaktionen festlegen“, klassisch)
- Regeln ✅; Unterhaltung ignorieren ✅; melden / als Junk / Absender blockieren ✅
- Verwandte suchen (gleicher Absender / gleiche Unterhaltung) ✅
- Gesendete Nachricht zurückrufen (entfernt sie aus den Postfächern der Empfänger innerhalb der Organisation, mit einer Zurückruf-Bericht-Mail) ✅
- Aufbewahrungsrichtlinie zuweisen; Aufgabe aus einer Mail erstellen ✅
- An OneNote senden, Schnelldruck (klassisch) ✅

### Offline und Synchronisation
- Offline-Einstellung: an/aus, welche Ordner (Standard + Favoriten), wie viele Tage (z. B. 30), Anhänge einschließen ✅
- Klassisch: alle Ordner senden/empfangen, Ordner aktualisieren, alle senden, Gruppen senden/empfangen, Fortschritt anzeigen, alle abbrechen, nur Kopfzeilen herunterladen, zum Herunterladen markieren / Markierung aufheben, Schalter „offline arbeiten“, „Offlinemodus“ in der Statusleiste ✅

### Benachrichtigungen
- Je Typ an/aus: Mail (neue Mails, Reaktionen, Erwähnungen), Kalender (Terminerinnerungen), Dokumente (Kommentare, Bearbeitungen, Erwähnungen) ✅
- Glockensymbol mit einem Panel in der Titelleiste ✅

### Darstellung
- Modus hell / dunkel / System ✅; Bild-Themes und KI-generierte Themes ✅ (Desktop und Mobil)
- Dichte-Einstellung auf dem Telefon ✅; Ansichtseinstellungen: Unterhaltungen, Nachrichtenvorschau, Zoom, Menüband, Ordnerbereich, Lesebereich, Dichte, Immersive Reader ✅

### Kalender (übernommenes Modul, zum Kontext gezeigt)
- Tag / Arbeitswoche / Woche / Monat / geteilte Ansicht, teilen, drucken ✅
- Wetter und Arbeitsort (Büro / Homeoffice) pro Tag ✅; Beitreten-Schaltfläche bei Online-Besprechungen ✅
- Mehrere Kalender mit Farben (Geburtstage, Feiertage, persönlich) ✅

## Was Outlook NICHT macht
- Keine Ende-zu-Ende-Verschlüsselung standardmäßig; keine chatartige Unterhaltungsansicht ⚠️
- Wisch-Aktionen auf dem Telefon sind bekannt, aber **nicht gesehen** ⚠️
- Kein Selbst-Hosting des neuen Outlook ⚠️
- Zurückrufen funktioniert nur innerhalb derselben Organisation ⚠️
