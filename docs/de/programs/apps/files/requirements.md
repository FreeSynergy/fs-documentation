# Files — Anforderungen

Was `FreeSynergy.Files` muss und kann.

**Vorläufig (2026-11-06).** Für diese Kategorie wurden keine Frontends analysiert, daher hat nichts hier die übliche Regel bestanden (ADR 0006, 0013). Alles stammt aus unserer Architektur (*Arch.*) oder ist allgemeines Wissen über solche Programme (⚠️) und muss vor dem Schreiben des Vertrags gegen analysierte Programme geprüft werden.

Status: `implemented` · `planned` · `proposed`

## Erforderlich

| Fähigkeit | Grundlage | Daten / Standard | Status |
|-----------|-----------|------------------|--------|
| Inhalt eines Ordners auflisten (`folder.list`) | ⚠️ | AS2 `Collection` | Vorschlag |
| Ordner anlegen, umbenennen, löschen (`folder.create`, `folder.rename`, `folder.delete`) | ⚠️ | AS2 `Collection`, Aktivitäten | Vorschlag |
| Eine Datei hochladen, wiederaufnehmbar (`file.upload`) | *Arch.* (große Aufnahmen, Fotos) | AS2 `Document`, `mediaType` | Vorschlag |
| Eine Datei herunterladen oder einen Teil davon lesen (`file.download`) | *Arch.* (`Blob` in `common.capnp`) | `Blob`-Fähigkeit | Vorschlag |
| Dateien verschieben, kopieren, umbenennen (`file.move`, `file.copy`, `file.rename`) | ⚠️ | Aktivitäten `Move`, `Update` | Vorschlag |
| Löschen mit Rückweg (`file.delete`, `file.restore`) | ⚠️ | `Delete` + Tombstone | Vorschlag |
| Suche nach Name und Metadaten (`file.search`) | ⚠️ | Lücke | Vorschlag |
| Gängige Typen als Vorschau anzeigen (`file.preview`) | ⚠️ | abgeleitete Daten | Vorschlag |
| Eine Datei aus anderen Programmen referenzieren (`file.resolve`) | *Arch.* (ADR 0017, 0037) | Objekt-ID + `Blob` | Vorschlag |
| Ein Speicher-Backend wählen (`backend.list`, `backend.add`, `backend.remove`) | *Arch.* | lokal, S3, WebDAV | Vorschlag |
| Sensible Dateien markieren (`file.classify`) | *Arch.* (ADR 0029) | DPV | Vorschlag |
| Über Änderungen benachrichtigen (`subscribe`) | *Arch.* (ADR 0021) | AS2-Aktivitäten | Vorschlag |

## Optional

| Fähigkeit | Grundlage | Daten / Standard | Status |
|-----------|-----------|------------------|--------|
| Mit Personen oder per Link teilen (`share.create`, `share.revoke`) | ⚠️ | Lücke, gemeinsame Spezifikation | Vorschlag |
| Dateiversionen (`file.versions`, `file.revert`) | ⚠️ | Aktivitätsprotokoll oder Lücke | Vorschlag |
| Auf dem Client verschlüsseln, bevor gespeichert wird (`file.encrypt`) | *Arch.* (ADR 0024) | zu entscheiden | Vorschlag |
| Sync zwischen Geräten (`sync.configure`) | ⚠️ | Aktivitätsprotokoll (ADR 0019) | Vorschlag |
| Schlagwörter und Favoriten (`file.tag`) | ⚠️ | AS2 `tag` | Vorschlag |
| Duplikate per Prüfsumme finden (`file.duplicates`) | ⚠️ | Prüfsumme | Vorschlag |
| Volltextsuche in Dokumenten (`file.searchContent`) | ⚠️ | Lücke | Vorschlag |

## Nicht geplant (bewusst)

- Dokumente bearbeiten: Das gehört zu den Programmen für jede Art von Inhalt.
- Selbst ein S3-Server sein: Betreiber können RustFS oder einen anderen Server laufen lassen.
