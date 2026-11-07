# Windows-Explorer (Datei-Explorer)

> Kategorie: [Dateien](../../index.md) · [Frontends](../index.md)

## Was es ist

Der Dateimanager von Windows. Befehlsleiste oder Menüband, Navigationsbereich, Cloud-Dateien neben lokalen angezeigt.

## Bemerkenswerte Ideen

- **Schnellzugriff / Start:** angeheftete Ordner plus zuletzt verwendete Elemente auf der Startseite ✅.
- **Suche umfasst PC und Cloud** ab Start, nach der Anmeldung am Cloud-Konto ✅.
- **Cloud-Dateien erscheinen als gewöhnliche Dateien** (OneDrive im Navigationsbereich) ✅.
- **Weitere Optionen anzeigen:** in Windows 11 verbirgt das kurze Kontextmenü das ältere lange hinter einem Link ✅.
- **Kontrollkästchen für Elemente** als Option zum Auswählen ohne Strg ✅.

## Gesehene Fähigkeiten

| Fähigkeit | Gesehen | Hinweis |
|-----------|---------|---------|
| Ausschneiden, kopieren, einfügen, umbenennen, teilen, löschen | ✅ | |
| Navigationsbereich, ein- oder ausblenden | ✅ | |
| Ansichtsmodi: Symbole, Liste, Details, kompakt | ✅ | |
| Startseite wählen; Dateierweiterungen und versteckte Elemente anzeigen | ✅ | Optionen |
| Ordner anheften und lösen | ✅ | |
| Suche inkl. Cloud | ✅ | |
| Vorschaubereich, Tabs, Rückgängig | ⚠️ | Nicht auf der gelesenen Seite; aus dem Produkt bekannt |

## Namensregeln

✅ https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file
- Verbotene Zeichen: `< > : " / \ | ? *`, NUL und Codes 1 bis 31.
- Reservierte Gerätenamen (`CON`, `PRN`, `AUX`, `NUL`, `COM1`..`COM9`, `LPT1`..`LPT9`), auch mit Erweiterung.
- Kein abschließendes Leerzeichen oder Punkt in der Shell.
- Keine Groß-/Kleinschreibung voraussetzen; `OSCAR`, `Oscar`, `oscar` zählen standardmäßig als ein Name.
- Pfadgrenze 260 Zeichen, in neueren Versionen per Konfiguration aufhebbar.

Ein unter Linux angelegter Ordner kann Namen enthalten, die Windows nicht anzeigen kann. Der Engine muss melden, welche Namen ein Backend oder Client nicht annehmen kann.

## Was wir übernehmen

Startseite mit angehefteten und zuletzt verwendeten Ordnern. Eine einzige Suche über lokal und entfernt. Auswahl-Kontrollkästchen für Touch. Die Liste der Gerätenamen-Regeln als Beispiel für „was das Betriebssystem erlaubt“ (ADR 0055).

## Quellen (gelesen 2026-11-06)

- https://support.microsoft.com/en-us/windows/file-explorer-in-windows-ef370130-1cca-9dc5-e0df-2f7416fe1cb1
- https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file
- Versucht und fehlgeschlagen (404): eine Microsoft-Such-Hilfeseite; Vorschaubereich und Tabs nicht überprüft.
