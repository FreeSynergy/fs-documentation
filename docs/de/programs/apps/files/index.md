# Files

## Kurz gesagt

Files kümmert sich um deine Dateien und Ordner. Es weiß, was jede Datei ist, wie groß sie ist und wo sie liegt, sodass andere Programme auf eine Datei verweisen können, ohne je einen Pfad zu sehen. Es beantwortet die Frage: Wo ist diese Datei, und wer braucht sie noch?

## Was hier anders ist

- Mit dem standardmäßigen lokalen Backend liegen Dateien in einem gewöhnlichen Ordner unter ihren echten Namen, etwa `Urlaub/Foto.jpg`. Du kannst diesen Ordner mit jedem anderen Werkzeug öffnen.
- Die Bytes können auch in S3-kompatiblem Speicher wie RustFS liegen.
- Löschen geht zuerst durch den Papierkorb. Ein Namenskonflikt überschreibt nie stillschweigend: Du lehnst ihn ab oder behältst beide.
- Uploads überleben einen Neustart und setzen dort fort, wo sie abbrachen.
- Andere Programme sollen eine Datei über ihre ID ansprechen, sodass eine Datei nicht in jedes Programm kopiert werden muss.

## Wo es heute steht

Neueste Version: `v0.6.0`. Ordner, Umbenennen, Verschieben, Kopieren, Papierkorb, Wiederherstellen und endgültiges Löschen funktionieren, ebenso fortsetzbare Uploads mit Prüfsumme, Suche, Sortierung und Filter. „Rescan“ übernimmt Dateien, die von außen in den Ordner gelegt wurden, und löscht nichts. Ein kleiner Server bietet all das über einen lokalen Socket an. Das S3-Backend wurde einmal gegen einen echten RustFS-Server getestet, nicht in den automatischen Tests.

Noch nicht da: ein Fenster, Freigabe, Versionen, Verschlüsselung von Dateiinhalten, Synchronisation, WebDAV und Vorschauen. Eine Datei zu ersetzen wird nicht angeboten. Die Oberfläche ist ein als vorläufig markierter Entwurf, und noch nichts nutzt sie.

## Geplante Facetten

Vorgeschlagen, nicht gebaut:

- Galerie: deine Bilder.
- Musik: deine Musik.
- Videos: deine Videos.
- Dokumente: deine Dokumente.

`FreeSynergy.Files` (`fs-files`) speichert, ordnet und teilt jede Art von Datei. Andere Programme, etwa die Galerie, legen ihre Bytes hier ab, statt einen eigenen Speicher zu bauen.

Der [Code liegt hier](https://github.com/FreeSynergy/fs-files). Siehe den [Gesamtplan](../roadmap.md).

- [Design](design.md): wie es gebaut wird, Speicher-Backends, offene Fragen
- [Anforderungen](requirements.md): was es können muss (vorläufig)

- [Frontends](frontends/index.md): acht Programme auf ihre Funktionen analysiert (erster Durchgang)

## Frontends

<!-- gen:frontends (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
Analysierte Programme (8), nach Funktion, nichts kopiert (ADR 0012/0013):

- [Dolphin](frontends/dolphin/index.md) — Der Dateimanager von KDE Plasma.
- [Finder](frontends/finder/index.md) — Der Dateimanager von macOS.
- [Google Drive](frontends/google-drive/index.md) — Cloud-Speicher von Google: Web, Apps und ein Desktop-Client.
- [Nautilus (GNOME Files)](frontends/nautilus/index.md) — Der Dateimanager der GNOME-Desktopumgebung.
- [Nextcloud Files](frontends/nextcloud-files/index.md) — Die Files-App von Nextcloud: Weboberfläche, Desktop- und mobile Synchronisation, WebDAV, auf einem Server, den du selbst betreibst.
- [rclone (and the S3-browser type)](frontends/rclone/index.md) — Ein Kommandozeilenprogramm, das Dateien über viele Speicherdienste hinweg kopiert, synchronisiert, einbindet und bereitstellt.
- [Seafile](frontends/seafile/index.md) — Quelloffene Dateisynchronisation, Freigabe und Dokumentenzusammenarbeit.
- [Windows Explorer (File Explorer)](frontends/windows-explorer/index.md) — Der Dateimanager von Windows.

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
