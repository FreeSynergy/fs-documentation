# Kalendar - Menüpunkte

## Übersicht

Kalendar arbeitet — typisch für Kirigami-Apps — mit einer schmalen Kopfzeile, einer Seitenleiste und Inline-Menüs statt klassischer Menüleiste. Alle Funktionen sind über Seitenleiste, Kontextmenüs und das Hamburger-Menü erreichbar.

## Hauptnavigation (Seitenleiste / Hamburger-Menü)

| Menüpunkt | Beschreibung |
|-----------|--------------|
| Agenden | Listenansicht aller anstehenden Ereignisse (Standardansicht) |
| Tag | Tagesansicht mit Stundenraster |
| Woche | Wochenübersicht |
| Monat | Monatskacheln mit Ereignispunkten |
| Kalender hinzufügen | Neues Kalender-Backend anlegen (CalDAV, lokal, Geburtstage, Feiertage) |
| Einstellungen | Anzeige, Farben, Standardkalender, Benachrichtigungen |

## Kalender-Verwaltung

Über die Kalenderliste in der Seitenleiste:

- **Kalender auswählen/abwählen** - Sichtbarkeit ein/aus
- **Kalender bearbeiten** - Name, Farbe, Standardkalender
- **Kalender entfernen** - Abonnement oder lokaler Kalender löschen
- **Aktualisieren** - CalDAV-Kalender neu synchronisieren (Akonadi)

## Ereignis-Kontextmenü (Rechtsklick / Long-Press)

| Eintrag | Beschreibung |
|---------|--------------|
| Bearbeiten | Ereignis-Dialog öffnen |
| Duplizieren | Kopie mit gleichem Inhalt anlegen |
| Verschieben | Per Drag & Drop oder Dialog verschieben |
| Löschen | Ereignis löschen (Serien: alle/kommende/dieses) |
| Erledigt markieren | Status auf erledigt setzen |

## Neues Ereignis (Quick-Add)

Das Schnellanlage-Feld akzeptiert Natürlichsprache-Eingaben: `Mittagessen morgen 12:30 1h mit Anna` erzeugt Titel, Start, Dauer und Teilnehmer.

## Menüs nach Rolle

Kalendar ist ein Einzelplatz-Programm: Es gibt **keine Rollen-Menüs**. Rechte ergeben sich aus den CalDAV-Ordnern des Servers (Leserecht vs. Schreibrecht): readonly-Kalender zeigen keine Anlage-/Bearbeitungspunkte.

## Hinweis

- **Keine klassische Menüdatei**: Kalendar hat keine Menüleisten wie KOrganizer; die obigen Punkte entsprechen den Panels und Kontextmenüs der aktuellen Versionen (Kirigami 2 / KDE Gear).
- Änderungen am Server (Kalenderfreigaben, Zugriffsrechte) erscheinen erst nach der nächsten Akonadi-Synchronisation.
