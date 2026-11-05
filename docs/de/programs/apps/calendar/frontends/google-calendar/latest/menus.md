# Google Kalender – Menü- und Navigationsstruktur (Web-Oberfläche, Stand 2026)

Google Calendar hat kein Quelltext-rezensionierbares Menü (closed Source). Diese Struktur ist **ausschließlich aus offiziellen deutschsprachigen Hilfeseiten** der Hilfezentrale und des Workspace-Admin-Wissens belegt (Fundstellen jeweils in Klammern; vollständige URLs in [index.md](../index.md)).

## Kopfzeile

| Element | Inhalt / Belege |
|---------|-----------------|
| „Heute“ (links oben) | Sprung zum heutigen Datum; daneben Pfeile zu nahe liegenden Daten (Hilfe „Tag, Woche oder Monat ansehen“) |
| Kleiner Kalender (links oben) | Datumsauswahl per Klick (ebenda) |
| „Eintragen“ (links) | Anlege-Menü; darin u. a. **„Terminplan“** für Reservierungsseiten (Hilfe „Terminplan erstellen“) |
| Suchen (oben) | Freitextsuche über Kalender/Termine (Spiegel der API-`q`-Suche) |
| Ansichten (rechts oben) | **Tag, Woche, 4 Tage, Monat, Jahr, Terminübersicht** – die zuletzt gewählte wird Standardansicht (Hilfe „Tag, Woche oder Monat ansehen“) |
| „Einstellungen“ (Zahnrad, rechts oben) | öffnet die Einstellungsseite (siehe unten) (ebenda) |
| Konto/Avatar (ganz rechts) | Google-Konto-Umschalter (Kontomultiplikation) |

## Linke Seitenleiste

- **Mini-Kalender** mit Monatsnavigation
- Kalenderlisten-Gruppen (Hilfe „Tag, Woche oder Monat ansehen“):
  - **„Meine Kalender“** – Kalender, deren Inhaber man ist (Anklicken blendet ein/aus)
  - **„Weitere Kalender“** – freigegebene Hauptkalender von Personen, Räumen oder Gruppen; Häkchen ausblenden, Abbestellen über Menü
- **„Weitere Kalender hinzufügen“** (Plus neben „Weitere Kalender“) mit den belegten Punkten:
  - **„Kalender abonnieren“** – Suche per E-Mail-Adresse (Hilfe „Kalender anderer Personen abonnieren“)
  - **„Per URL“** – öffentliche Kalender per Link/ICS-URL hinzufügen (ebenda)
  - (Kalender-Neuanlage erfolgt ebenfalls über diesen Bereich; die genaue Menübeschriftung war in der geprüften Hilfeseite nicht einzeln belegt)
- **Dreipunkt-Menü je Kalender** → **„Einstellungen und Freigabe“** – Unterseite „Kalendereinstellungen“ u. a. mit **„Kalender exportieren“** und den **iCal-Adressen** („Öffentliche Adresse im iCal-Format“, „Privatadresse im iCal-Format“) (Hilfe „Termine aus Ihrem Google Kalender exportieren“)
- **„Weitere Details“** (links) → Dashboard **„Ihre Zeit im Blick“** mit Zeitaufschlüsselung, „Personen, mit denen Sie in Kontakt sind“, „Angepinnte Personen verwalten“ (bis zu 10) (Hilfe „Nachsehen, wie viel Zeit Sie in Besprechungen verbringen“)

## Einstellungsseite (Zahnrad → „Einstellungen“)

Links kategorisiert; belegt sind:

- **„Ansichtsoptionen“** – Wochenbeginn, benutzerdefinierte Ansicht, Referenzkalender (Hilfe „Tag, Woche oder Monat ansehen“; Änderungen speichern automatisch)
- **„Importieren & Exportieren“** – „Exportieren“ (ZIP mit ICS aller Kalender) und Import (Hilfe „Termine aus Ihrem Google Kalender exportieren“)

Weitere Kategorien (Allgemein, Benachrichtigungen, App-/Add-on-Zugriff) sind in der Oberfläche vorhanden, aber in den abgerufenen Primärartikeln nicht einzeln benannt → **nicht verifiziert**.

## Terminbearbeitung (Dialog)

- Beim Klick auf eine Zeit: Termin-Quick-Editor; oben umschaltbar auf **„Fokuszeit“** (Hilfe „Fokuszeit verwenden“ – nur Tages-/Wochenansicht, mit fester Start-/Endzeit)
- Erweiterte Terminseite mit Gastrechten, Erinnerungen, Ort, Anhängen, Konferenz (Details je Feld nicht alle einzeln in den geprüften Artikeln belegt; API-Felder in [api.md](api.md))

## Terminplan-Editor (Reservierungsseite)

Über „Eintragen“ → „Terminplan“; Bereichsbezeichnungen laut Hilfe „Terminplan erstellen“:

1. **„Zeitplan für Terminreservierung“** (linker Bereich): Titel, **Termindauer** (auch „Benutzerdefiniert“), **Allgemeine Verfügbarkeit** (Tagesfenster; „Ganztags nicht verfügbar“, „Diesem Tag eine weitere Zeitspanne hinzufügen“, „Für alle Tage übernehmen“)
2. **„Zeitfenster für Reservierungen“**: max./min. Vorlaufzeit (Standard: mindestens 4 Stunden)
3. **„Angepasste Verfügbarkeit“** (Einzeltermine wie Feiertage)
4. **„Einstellungen für reservierte Termine“**: **Puffer**, **Maximale Anzahl von Reservierungen pro Tag**, **Berechtigungen für Gäste**
5. **„Kalender“**: Zielkalender (primär/sekundär)
6. Optionaler Einstieg: „Terminplan erstellen“ im Bereich **„Reservierungsseiten“**

## Google-Workspace-Administration (Admin-Konsole)

- **Admin-Konsole → Kalender → Erweiterte Einstellungen → „Appointment schedules with payments“** (ON/OFF für Stripe-Zahlungen in Terminplänen) (Workspace-Wissensartikel „Allow paid appointment schedules in Calendar“)
- Time Insights kann organisationell deaktiviert werden (Hilfe „Nachsehen, wie viel Zeit Sie in Besprechungen verbringen“)
- Export kann administrativ eingeschränkt werden (Hilfe Export)

## Mobile Apps (Android/iOS)

Die Apps haben eine eigene, schlankere Navigation (Tages-/Wochen-/Monatsansicht, Kalenderliste, „+“-Anlegen). Die Hilfeartikel zu Abonnieren/Terminplänen weisen ausdrücklich: **Kalender abonnieren und Terminpläne erstellen geht nur im Web-Browser auf dem Computer, nicht in der App**. Eine vollständige App-Menüstruktur wurde nicht aus Primärquellen extrahiert → bewusst nicht im Detail dokumentiert.
