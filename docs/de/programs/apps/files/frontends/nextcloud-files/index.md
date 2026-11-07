# Nextcloud Files

> Kategorie: [Dateien](../../index.md) · [Frontends](../index.md)

## Was es ist

Die Dateien-App von Nextcloud: Weboberfläche, Synchronisation für Desktop und Mobilgerät, WebDAV, auf einem Server, den du betreibst. Freie Software. ⚠️ (Lizenz nicht gelesen.)

## Bemerkenswerte Ideen

- **Versionen mit einer Ausdünnungsregel:** eine neue Version höchstens alle zwei Minuten; ältere werden ausgedünnt (Sekunden, Minuten, Stunden, Tage, Wochen); benannte Versionen laufen nie ab; der Versionsspeicher ist auf 50 % des freien Speicherplatzes begrenzt ✅.
- **Papierkorb mit Regeln:** standardmäßig mindestens 30 Tage, begrenzt auf 50 % des verbleibenden Kontingents, älteste zuerst; die Wiederherstellung landet im Stammordner, wenn der alte Ordner fehlt; Versionen wandern mit der Datei; der Papierkorb zählt nicht zum Kontingent ✅.
- **Viele Freigabeziele:** öffentlicher Link, Benutzer, Gruppen, Kreise, Talk-Unterhaltungen, föderierte Server ✅.
- **Dateiablage:** Hochladen in einen Ordner, ohne dessen Inhalt zu sehen ✅.
- **Andere mit Zugriff:** zeigt, wer über die Freigabe eines übergeordneten Ordners auf eine Datei zugreift ✅.
- **Föderierte Freigaben**, eingebunden als `user@server` ✅.
- **Eigentum übertragen**, **Systemschlagwörter**, **externer Speicher**, **Upload großer Dateien**, **Verschlüsselung auf dem Server und Ende-zu-Ende** sind Kapitel des Handbuchs ✅ (nur Titel).

## Gesehene Fähigkeiten

| Fähigkeit | Gesehen | Hinweis |
|-----------|---------|---------|
| Web, WebDAV, Synchronisation für Desktop und Mobilgerät | ✅ | |
| Versionen, wiederherstellen, eine benennen, eine löschen | ✅ | |
| Papierkorb, wiederherstellen, endgültig löschen | ✅ | |
| Freigabelink mit Passwort, Ablauf, Notiz, Download verbergen, mehrere Links mit unterschiedlichen Rechten | ✅ | |
| Freigaberecht pro Empfänger; automatisch annehmen oder genehmigen | ✅ | |
| Speicherkontingent | ✅ | WebDAV-Clients können den freien Platz nicht anzeigen (Windows) |
| Systemschlagwörter | ✅ | Nur Titel |
| Sperren, Kommentare, Favoriten | ⚠️ | Im Inhalt des Handbuchs nicht genannt |

## Namensregeln

Wiederherstellen bei einem Namenskonflikt ergibt einen eindeutigen Namen ✅. Andere Regeln ⚠️.

## API

WebDAV unter `/remote.php/dav/files/USERNAME/`; für Fremd-Clients wird ein App-Passwort empfohlen, weil normale Passwörter es verlangsamen ✅. Öffentliche Freigaben über `public.php/dav/files/` mit dem Token als Benutzername ✅. Chunked-Upload ist eine eigene Seite, nicht gelesen ⚠️.

## Was wir übernehmen

Versionen mit Ablaufregeln und benannte (angeheftete) Versionen. Aufbewahrung des Papierkorbs als Einstellungen. Das Freigabemodell als Eingabe für die gemeinsame Spezifikation (Entwurf, Frage 3). Kontingent für den Nutzer sichtbar. WebDAV als späteres Backend (Entwurf: Stufe 3).

## Quellen (gelesen 2026-11-06)

- https://docs.nextcloud.com/server/latest/user_manual/en/files/index.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/version_control.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/deleted_file_management.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/sharing.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html
