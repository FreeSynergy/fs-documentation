# Dateien — Frontends

Frontends bekannter Programme in dieser Kategorie, analysiert auf ihre **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm wird hier dokumentiert, weil es weit verbreitet ist oder weil es eine bemerkenswerte Idee hat. Unser eigenes Programm für diese Kategorie ist `FreeSynergy.Files` (ADR 0017); seine Fähigkeiten und sein Status stehen in den [Anforderungen](../requirements.md).

Recherchedatum: 2026-11-06. Jede Aussage ist mit ✅ (auf der zitierten offiziellen Seite an diesem Datum gelesen) oder ⚠️ (nicht überprüft; aus dem Produkt bekannt oder nur aus einer nicht offiziellen Seite) markiert. Versionsnummern wurden nicht geprüft, daher beschreibt jede Seite die aktuelle Dokumentation, nicht eine feste Version.

## Programme

| Programm | Art | Was es ist |
|----------|-----|------------|
| [Dolphin](dolphin/index.md) | lokaler Manager | Der Dateimanager von KDE Plasma. Viele Panels, geteilte Ansicht, eingebaute Suche. |
| [Nautilus (GNOME-Dateien)](nautilus/index.md) | lokaler Manager | Der Dateimanager von GNOME. Wenige Optionen, entfernte Server im selben Fenster. |
| [Windows-Explorer](windows-explorer/index.md) | lokaler Manager | Datei-Explorer von Windows. Menüband oder Befehlsleiste, Cloud-Dateien neben lokalen. |
| [Finder](finder/index.md) | lokaler Manager | Der Dateimanager von macOS. Vier Ansichtsmodi, Tags, Schnellansicht. |
| [Nextcloud Files](nextcloud-files/index.md) | selbst gehostet | Zugriff auf Dateien auf deinem eigenen Server über Web, Desktop und Mobilgerät. Starkes Teilen und Versionen. |
| [Seafile](seafile/index.md) | selbst gehostet | Bibliotheken als Einheit für Synchronisation, Freigabe und Verschlüsselung. |
| [Google Drive](google-drive/index.md) | Cloud | Cloud-Speicher mit einem Desktop-Client für Streamen oder Spiegeln und rollenbasiertem Teilen. |
| [rclone](rclone/index.md) | Kommandozeile, Typ S3-Browser | Ein Werkzeug für viele Speicherdienste: kopieren, synchronisieren, einbinden, bereitstellen. Steht auch für S3-Browser. |

## Was jede Seite enthält

```
programs/apps/files/frontends/<program>/
└── index.md        was es ist, bemerkenswerte Ideen, Fähigkeiten, Namensregeln, was wir übernehmen, Quellen
```

Der vollständige Dateisatz aus ADR 0012 (`<version>/description.md`, `features.md`, `layout.md`, `menus.md`, `shortcuts.md`, `api.md`, `themes/index.md`) ist **noch nicht geschrieben**. Diese Seiten sind die erste Analyse, um den Vertrag zu prüfen. Der Rest folgt, wenn ein Frontend in diesem Stil gebaut wird.

## Querschnittsbefunde

- **Namen.** Lokale Manager zeigen den echten Namen und überlassen dem Dateisystem, was nebeneinander bestehen darf. Linux verbietet nur `/` (✅ GNOME-Hilfe), Windows verbietet neun Zeichen und einige Gerätenamen (✅ Microsoft Learn). Die Groß-/Kleinschreibungsregeln unterscheiden sich (✅ GNOME, ✅ Microsoft Learn, ✅ rclone mount). Das passt zu ADR 0055; der Engine muss die Regeln des Backends melden, nicht eine einzige Menge erzwingen.
- **Löschen in zwei Schritten.** Jedes untersuchte Programm hat einen Papierkorb mit Wiederherstellung. Die Aufbewahrungsdauer unterscheidet sich: 30 Tage bei Nextcloud und Google Drive (✅). Das Wiederherstellen muss mit einem fehlenden übergeordneten Ordner zurechtkommen (✅ Nextcloud).
- **Konflikte.** Synchronisierende Programme behalten beide Kopien und benennen eine um: Seafile, rclone bisync (✅). Lokale Manager verweigern oder fragen nach (✅ GNOME).
- **Teilen ist ein eigenes Thema.** Rollen, Links mit Passwort und Ablaufdatum, Ordner nur zum Hochladen, Föderation, Eigentumsübertragung (✅ Nextcloud, ✅ Google Drive).
- **Streamen oder Spiegeln.** Zwei Arten, entfernte Dateien lokal anzuzeigen (✅ Google Drive für Desktop, ✅ Seafile-Drive-Client, ✅ rclone mount mit Cache-Modi).
- **Verschlüsselung der Namen.** rclone crypt kann Datei- und Ordnernamen verbergen; die Struktur bleibt sichtbar (✅). Seafile hat verschlüsselte Bibliotheken (✅ im Handbuch-Index genannt; Details ⚠️).
- **Unvollständige Uploads kosten Speicherplatz** und müssen aufgelistet und bereinigt werden (✅ S3 Browser, ✅ rclone cleanup).
