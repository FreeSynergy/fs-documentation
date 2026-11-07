# Nautilus (GNOME-Dateien)

> Kategorie: [Dateien](../../index.md) · [Frontends](../index.md)

## Was es ist

Der Dateimanager des GNOME-Desktops. Wenige Optionen, viele Aufgaben in einem Fenster. ⚠️ (Projektangaben auf den unten genannten Seiten nicht gelesen.)

## Bemerkenswerte Ideen

- **Dasselbe Fenster für Netzwerkfreigaben:** „Dateien auf Servern oder Netzwerkfreigaben durchsuchen“ ist in der Hilfe eine normale Aufgabe ✅. WebDAV funktioniert mit `dav://` und `davs://` ✅ (Nextcloud-Handbuch).
- **Umbenennen behält die Dateiendung:** nur der Teil vor dem letzten Punkt wird markiert ✅.
- **Löschen ist für einige Sekunden rückgängig zu machen**, endgültiges Löschen (Umschalt+Entf) fragt nach ✅.
- **Musikdateien nach ihren eingebetteten Daten umbenennen** ✅ (im Hilfe-Index genannt).
- **Ordner vor Dateien sortieren** als Option, standardmäßig aus ✅.

## Gesehene Fähigkeiten

| Fähigkeit | Gesehen | Hinweis |
|-----------|---------|---------|
| Durchsuchen, kopieren, verschieben, löschen, Vorschau ohne Öffnen | ✅ | Hilfe-Index |
| Eine oder viele umbenennen; Rückgängig (Strg+Z); F2 | ✅ | |
| Papierkorb, wiederherstellen, leeren, endgültiges Löschen mit Bestätigung | ✅ | |
| Suche nach Name und Typ; sortieren nach Name, Größe, Typ, Zeit | ✅ | Hilfe-Index |
| Pfad in die Ortsleiste eintippen; Lesezeichen | ✅ | Hilfe-Index |
| Eigenschaften, Berechtigungen, Standard-Apps | ✅ | Hilfe-Index |
| Aufbewahrungsdauer für Papierkorb und temporäre Dateien | ✅ | Hilfe-Index |
| Per E-Mail teilen; Dateiverlauf kann begrenzt oder abgeschaltet werden | ✅ | Hilfe-Index |
| Auswahl nach Namensmuster; Dateien ausblenden; Vorlagen | ✅ | Hilfe-Index |
| Tabs, Listen- und Rasteransicht | ⚠️ | Auf den gelesenen Seiten nicht gefunden |

## Namensregeln

✅ https://help.gnome.org/users/gnome-help/stable/files-rename.html
- Zwei Elemente können in einem Ordner nicht denselben Namen haben; das Umbenennen wird blockiert.
- Namen unterscheiden Groß- und Kleinschreibung; `File.txt` und `FILE.txt` sind verschieden, davon wird aber abgeraten.
- Nur `/` ist verboten. `| \ ? * < " : >` sollte man vermeiden, weil andere Dateisysteme sie einschränken.
- Ein führender Punkt versteckt die Datei.
- Manche Dateisysteme begrenzen Namen auf 255 Zeichen.

Das kommt ADR 0055 am nächsten: Das Dateisystem setzt die Regeln, das Programm warnt.

## Was wir übernehmen

Umbenennen, das Namenskollisionen mit einer klaren Meldung blockiert. Eine Warnliste für Zeichen, die andere Systeme stören. Aufbewahrungsdauer für den Papierkorb als Einstellung. Dateiverlauf, der sich abschalten lässt (Datenschutz).

## Quellen (gelesen 2026-11-06)

- https://help.gnome.org/users/gnome-help/stable/files.html
- https://help.gnome.org/users/gnome-help/stable/files-rename.html
- https://help.gnome.org/users/gnome-help/stable/files-delete.html
- https://help.gnome.org/users/gnome-help/stable/nautilus-views.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html (WebDAV in Nautilus)
