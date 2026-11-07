# rclone (und der Typ S3-Browser)

> Kategorie: [Dateien](../../index.md) · [Frontends](../index.md)

## Was es ist

Ein Kommandozeilenprogramm, das Dateien über viele Speicherdienste kopiert, synchronisiert, einbindet und bereitstellt. Sein S3-Backend spricht mit jedem S3-Speicher. Es steht hier für den ganzen Typ der Werkzeuge, mit denen man S3-Objekte durchsucht und verschiebt, einschließlich des Windows-Clients S3 Browser. MIT-Lizenz ⚠️ (nicht gelesen).

## Bemerkenswerte Ideen

- **Ein Satz von Befehlen für alle Speicher:** `copy`, `sync`, `move`, `check`, `ncdu` (interaktive Größen), `mount`, `serve`, `bisync` ✅.
- **`--dry-run`**, um eine Synchronisierung zuerst zu testen; **`--bwlimit`** mit einem Zeitplan nach Wochentagen ✅.
- **bisync:** vergleicht mit einer gespeicherten Liste des letzten Laufs; bei einem Konflikt behält es beide und hängt `conflict1/2` an, oder wählt einen Gewinner nach neuer, älter, größer usw.; bricht ab, wenn mehr als 50 % gelöscht würden; `--resync` für den ersten Lauf ✅.
- **crypt:** verschlüsselt Inhalte (64-KiB-Blöcke) und standardmäßig auch Datei- und Ordnernamen; die Ordnerstruktur, die Größe bis auf 16 Byte und die Zeiten bleiben sichtbar; ein Passwortwechsel verlangt erneutes Hochladen ✅.
- **Backends union** und **chunker** ✅ (genannt).
- **Mount mit Cache-Modi:** aus, minimal, Schreibvorgänge, vollständig; ohne Cache-Modus nur sequenzielles Schreiben ✅.
- **rcd mit Weboberfläche:** API zur Fernsteuerung, optionale Anmeldung per Basic oder htpasswd, ZIP-Download ✅.
- **S3-Besonderheiten:** Änderungszeit als Objekt-Metadaten; MD5 in den Metadaten bei Multipart; Auflistung der Versionen; `cleanup` entfernt unvollständige Multipart-Uploads, die älter als 24 Stunden sind ✅. Leere Verzeichnisse verschwinden bei Bucket-Speichern, sofern keine Marker verwendet werden ✅. Schlüssel mit `//` werden nicht unterstützt ✅.
- **S3 Browser (Windows-Client):** listet unvollständige Multipart-Uploads auf, bricht sie ab und setzt sie fort, indem die Quelldatei erneut gewählt wird; sie laufen nie ab und kosten Speicherplatz ✅ (Herstellerseite). Die Funktionsliste gab 404 zurück, daher der Rest ⚠️.

## Gesehene Fähigkeiten

| Fähigkeit | Gesehen | Hinweis |
|-----------|---------|---------|
| Kopieren, verschieben, synchronisieren, prüfen | ✅ | |
| Zweiseitige Synchronisierung mit Konfliktregeln | ✅ | |
| Als Laufwerk einbinden, mit Cache | ✅ | Braucht WinFsp, macFUSE oder FUSE-T, fusermount |
| Vor dem Speichern verschlüsseln | ✅ | |
| Größen interaktiv auflisten | ✅ | |
| Unterbrochenen Upload fortsetzen | ⚠️ | Auf der S3-Seite nicht beschrieben; rclone beschreibt das Bereinigen unvollständiger Teile |
| RustFS | ⚠️ | Auf der S3-Seite nicht aufgeführt |

## Namensregeln

Bei S3 jeder gültige UTF-8-Schlüssel, aber `/`, NUL, `.` und `..` als Namen werden ersetzt ✅. Mount: Linux unterscheidet Groß- und Kleinschreibung; Windows und macOS nicht, bewahren sie aber ✅; die Unicode-Normalisierung ist auf macOS wichtig ✅.

## Was wir übernehmen

Testlauf (Dry-run) und eine Löschgrenze als Sicherheit beim Synchronisieren. Konfliktstrategie als Einstellung. Auflisten und Bereinigen unvollständiger Uploads (`Upload.received` ist ein guter Anfang; eine Liste ausstehender Uploads fehlt). Die Idee der Cache-Modi für einen Streaming-Modus. Verschlüsselte Namen als Option der clientseitigen Verschlüsselung.

## Quellen (gelesen 2026-11-06)

- https://rclone.org/docs/
- https://rclone.org/commands/rclone_mount/
- https://rclone.org/commands/rclone_rcd/
- https://rclone.org/bisync/ (die ersten 100000 Zeichen)
- https://rclone.org/crypt/
- https://rclone.org/s3/ (die ersten 100000 Zeichen)
- https://s3browser.com/uncompleted-multipart-uploads.aspx
