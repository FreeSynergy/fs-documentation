# LibrePhotos - Menüpunkte

## Hauptnavigation (linke Leiste)

| Menü | Beschreibung |
|------|--------------|
| Suche | Volltext und semantische Suche (CLIP), Filterleiste |
| Orte | Karte, Ortsliste, „Places“-Gruppen |
| Alben | eigene Alben, Auto-Alben (Datum, Ereignis) |
| Menschen | erkannte Gesichter, Namen, Zusammenführen |
| Fotos / Videos | Filter nach Typ und Aufnahmedatum |
| Favoriten | markierte Aufnahmen |
| Geteilt | von anderen Nutzern geteilte Alben |
| Gelöscht | Papierkorb mit Wiederherstellung |

## Einstellungen (Zahnrad)

| Bereich | Inhalt |
|---------|--------|
| Konto | Passwort, Sprache, Theme, Zwei-Faktor |
| Gallery | Zeitleistengruppierung, Miniaturgröße, NSFW-Filter |
| ML | Gesichts-/Objekterkennung an/aus, Modellwahl, Durchführung |
| Upload | Importordner, Duplikatverhalten |

## Administration (nur Admin)

| Menü | Inhalt |
|------|--------|
| Benutzer | Konten, Gruppen, Quota, Einladungen |
| Scan-Jobs | „Full Scan“, „Face Scan“, „CLIP-Index“, Status/Abbruch |
| Aufgaben | laufende Hintergrund-Jobs (Celery) einsehen |
| Speicher | Pfad-Layout (`MEDIA_ROOT`), Bereinigung |

## Kontextmenüs

| Objekt | Aktionen |
|--------|----------|
| Aufnahme | Favorit, Download, Löschen, Ähnliche suchen, Person zuweisen, Album |
| Mehrfachauswahl | Album hinzufügen, Teilen, Taggen, Löschen |
| Album | Bearbeiten, Cover, Teilen (Benutzer/Link), Herunterladen (ZIP) |
| Person | Benennen, Gesichtsschnitt, Zusammenführen, ausschließen |

## Menüs nach Rolle

| Rolle | Sichtbar |
|-------|----------|
| Benutzer | Suche, eigene Alben, geteilte Inhalte |
| Admin | zusätzlich Administration und Scan-Steuerung |
| Gast | nur geteilte Alben (Lesen, Download je nach Freigabe) |
