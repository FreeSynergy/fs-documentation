# Seafile

> Kategorie: [Dateien](../../index.md) · [Frontends](../index.md)

## Was es ist

Freie Software zum Synchronisieren, Teilen und gemeinsamen Bearbeiten von Dokumenten. Die Einheit ist die **Bibliothek**, nicht der Ordner. ✅ (Startseite des Administratorhandbuchs.) Desktop-Synchronisations-Client unter GPLv2 ✅.

## Bemerkenswerte Ideen

- **Bibliothek als Einheit** für Synchronisation, Freigabe, Verlauf und Verschlüsselung ✅ (Themen-Titel im Handbuch).
- **Verschlüsselte Bibliotheken** ✅ (nur Titel; Details ⚠️).
- **Zwei Clients:** Synchronisations-Client (kopiert) und Drive-Client SeaDrive (virtuelles Laufwerk unter `~/SeaDrive`, begrenzter Cache, braucht FUSE 2) ✅.
- **Synchronisationsoptionen:** bestehende Ordner, selektive Synchronisierung von Unterordnern, nur-lesende Synchronisierung, Synchronisierungsintervall, Dateien ausschließen ✅ (Titel).
- **Bibliotheksverlauf und Snapshots** mit einer Aufbewahrungsdauer ✅ (Titel).
- **Sperren von Dateien** ✅ (Titel).
- **Konfliktdatei:** der erste Upload gewinnt; die andere Kopie wird umbenannt in `name (SFConflict user@example.com 2015-03-07-11-30-28)` ✅.
- **Speicher-Backends:** S3, Ceph, OpenStack Swift, mehrere gleichzeitig ✅. Server-Werkzeuge FSCK und GC ✅ (Titel).
- **WebDAV- und FUSE-Erweiterungen**, Web-API v2.1 ✅ (Titel).

## Gesehene Fähigkeiten

| Fähigkeit | Gesehen | Hinweis |
|-----------|---------|---------|
| Bibliotheken, Gruppen, Ordnerberechtigung, Abteilungen | ✅ | Titel |
| Virtuelles Laufwerk mit Cache | ✅ | Nachladen bei Bedarf ist angedeutet, nicht ausdrücklich genannt |
| Verlauf mit Aufbewahrung | ✅ | Titel |
| Sperren | ✅ | Titel |
| Metadatenfunktion | ✅ | Titel |
| Deduplizierung nach Blöcken | ⚠️ | Auf den gelesenen Seiten nicht |

## Namensregeln

Nur die Benennung bei Konflikten (siehe oben). Andere ⚠️.

## Was wir übernehmen

Konfliktbehandlung, die beide Kopien behält und Autor und Zeit benennt. Nur-lesende und selektive Synchronisierung als Optionen von `sync.configure`. Eine Cache-Grenze für den Streaming-Modus. Aufbewahrung des Verlaufs als Einstellung.

## Quellen (gelesen 2026-11-06)

- https://manual.seafile.com/latest/
- https://help.seafile.com/ (Themenliste)
- https://help.seafile.com/drive_client/drive_client_for_linux/
- https://help.seafile.com/syncing_client/file_conflicts/
- Fehlgeschlagen (404): Seite zu verschlüsselten Bibliotheken.
