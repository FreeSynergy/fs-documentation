# Files — Design

**Status: Vorschlag (2026-11-06).** Zurück zum [Gesamtplan](../roadmap.md) · [Anforderungen](requirements.md).

## Idee

Zwei Dinge werden getrennt gehalten: **was wir über eine Datei wissen** und **wo ihre Bytes liegen**.

- **Metadaten** sind ein Objekt in `fs-store`, wie alle anderen Daten: Name, Medientyp, Größe, Prüfsumme, Ordner, Freigabe.
- **Bytes** liegen in einem Speicher-Backend hinter einer Schnittstelle. Welches Backend verwendet wird, macht für das Programm, die Frontends und andere Programme keinen Unterschied.

Andere Programme verweisen auf eine Datei über ihre Objekt-ID und lesen sie über die Fähigkeit `Blob` in `common.capnp`. Sie sehen nie Pfade oder Backends.

## Daten

| Teil | Standard | Hinweise |
|------|----------|----------|
| Datei | AS2 `Document` (`Image`, `Video`, `Audio`, wo zutreffend), `mediaType` | Felder folgen [Datei / Medien](../../../data/models.md) |
| Ordner | AS2 `Collection` | ADR 0037 behandelt Ordner, Gruppe und Verteiler als ein Konzept; für Dateien zu prüfen |
| Änderung | AS2-Aktivitäten im Protokoll | `Create`, `Update`, `Move`, `Delete` |
| Version | Lücke | Eigene Spezifikation oder einfacher Aktivitätsverlauf; offen |
| Freigabe, Berechtigungen | Lücke | Von allen Programmen geteilt, also einmal zu spezifizieren ([Frage 3](#offene-fragen)) |

Sensible Dateien werden nach ADR 0029 markiert.

## Speicher-Backends

```rust
//! Pattern: Strategy (backend), Decorator (encryption, cache), Repository (metadata).
#[async_trait]
pub trait BlobStore: Send + Sync {
    async fn put(&self, key: &BlobKey, data: ByteStream) -> Result<BlobInfo>;
    async fn get(&self, key: &BlobKey, range: Option<ByteRange>) -> Result<ByteStream>;
    async fn delete(&self, key: &BlobKey) -> Result<()>;
    async fn stat(&self, key: &BlobKey) -> Result<BlobInfo>;
}
```

Diese Skizze zeigt nur die Form. Die endgültige Form ergibt sich aus dem Vertrag.

| Backend | Für wen | Stufe |
|---------|---------|-------|
| **Lokaler Ordner** | Alle. Der Standard: kein Server, und Dateien bleiben gewöhnliche Dateien, die man mit allem öffnen kann | 1 |
| **S3** | Teams und Server. Funktioniert mit RustFS und jedem anderen S3-Speicher | 2 |
| **WebDAV** | Vorhandener Speicher wie Nextcloud | später |

### RustFS

[RustFS](https://github.com/rustfs/rustfs) ist ein S3-kompatibler Objektspeicher in Rust, unter Apache-2.0 (Version 1.0.4 am 2026-10-25). Er passt zu unseren Lizenz- und Sprachregeln und eignet sich als **empfohlenes Server-Backend**.

**Entschieden (2026-11-06): optional, aber stark genutzt, und wir hoffen, mit dem Projekt zusammenzuarbeiten,** auch bei der Auslieferung von Daten online. Es ist ein eigener Server, daher müssen auch ein Laptop oder ein Handy ohne ihn funktionieren (ADR 0017). Git ist eine weitere Option.

### Kandidaten

| Zweck | Crate (2026-11-06) | Hinweise |
|-------|--------------------|----------|
| Lokal + S3 + WebDAV hinter einer API | `opendal` 0.59 | Würde von unserem `BlobStore` umhüllt |
| Gleiches, enger | `object_store` 0.14 | Alternative |
| Prüfsummen | `blake3` 1.8 | `models.md` nennt derzeit `sha256:` als Beispiel; noch anzugleichen |
| Lokalen Ordner beobachten | `notify` | Stabil 8.x oder der 9.0-Release-Kandidat; zu prüfen |
| Dateityp erkennen | `infer` 0.22 | |

Wiederaufnehmbare Uploads sind für große Dateien nötig. Das Crate `tus` hat seit 2023 keine Veröffentlichung, daher ist es kein Kandidat.

## Schnittstellen-Skizze

| Schnittstelle | Fähigkeiten |
|---------------|-------------|
| `Files` (Wurzel) | `capabilities()`, gibt die anderen heraus |
| `Folders` | `folder.list`, `folder.create`, `file.move`, `file.rename`, `file.delete`, `file.restore` |
| `Transfer` | `file.upload` (wiederaufnehmbar), `file.download` (`Blob`) |
| `Search` | `file.search` |
| `Sharing` | `share.create`, `share.revoke` |
| `Backends` | `backend.list`, `backend.add`, `backend.remove` |
| `subscribe` | Live-Änderungen für andere Programme |

## Speichern und Exportieren

**Speichern und Exportieren sind verschiedene Dinge** (ADR 0046, aufbauend auf ADR 0042).

- Während du arbeitest, arbeitest du an einer **Kopie in der Datenbank**, die immer erhalten bleibt. Es gibt kein „Speichern“, das man vergessen könnte.
- Dateien sind Speicher und Sicherungen.
- Nur ein **Export** erzeugt eine Datei, die man weitergibt.

Texte und kleine Objekte liegen in der Datenbank. Große Dateien wie Videos können bei jeder Bearbeitung nicht ganz kopiert werden: Sie behalten ihre Bytes im Dateispeicher, und Versionen teilen unveränderte Blöcke.

**Nachfrage beim Verlassen:** Wir schlagen vor, nicht jedes Mal zu fragen, da Menschen solche Fragen wegklicken. Eine Aktion „Weitergeben“ bietet den Export an, wenn er gewünscht ist. Das Programm fragt nur, wenn eine Datei von außen geöffnet wurde, denn dann erwarten Menschen, dass sich diese Datei ändert: „Auch das Original aktualisieren?“

## Ansichten

Dieselben Dateien, auf verschiedene Arten gesehen. Dateien können aus dem Inhalt eine Ansicht vorschlagen und sie je Ordner merken; ob ein Frontend das nutzt, entscheidet das Frontend.

Liste, Baum, Raster, Zeitleiste, Karte, Personen, Musikbibliothek, Videothek, Leser, Dokumentenregal, letzte Aktivität, Duplikate. **Eine Galerie ist ein Frontend mit eingebautem Filter**: eine App, die wie ein eigenes Programm aussieht, auf derselben Engine.

Ideen zur Ausarbeitung:

- **Sammlungen statt Kopien:** Eine Datei kann in vielen Alben liegen, und ein Album kann auch eine gespeicherte Suche sein.
- **Metadaten-Extraktoren je Dateityp** hinter einer [Schnittstelle](../../../interfaces/index.md): Foto, Audio, Video, PDF. Jeder kann mit den Programmen verknüpft werden, die diesen Typ öffnen, ähnlich wie es ein Betriebssystem tut. Standards für jeden Typ kommen zuerst.
- **Eingebettet:** „alle Dateien dieses Projekts“ innerhalb einer Projekt- oder Wiki-Seite.
- Gesichtserkennung als optionaler, rein lokaler Extraktor (ADR 0029).

## Komponenten

Workbench `file-manager` mit der kompakten Variante `file-picker`, überall eingesetzt, wo ein Programm eine Datei auswählen oder anhängen muss. Siehe [geplante Komponenten](../../../components/planned.md).

## Stufen

1. Lokaler Ordner, Metadaten in `fs-store`, durchsuchen, verschieben, umbenennen, löschen mit Papierkorb, Suche nach Name, wiederaufnehmbarer Upload.
2. S3-Backend, Teilen, Versionen, Verschlüsselung auf dem Client.
3. Sync zwischen Geräten über `fs-hub`, Konfliktbehandlung, WebDAV.

## Offene Fragen

1. **Echte Ordner oder verwalteter Speicher?** Beides muss möglich sein. Mit der Arbeitskopie in der Datenbank sind echte Dateien die gespeicherte Form. Wie Änderungen von außen übernommen werden, bleibt offen.
2. **Ist ein Ordner hier dasselbe wie „Ordner = Gruppe = Verteiler“ aus ADR 0037?** Wenn ja, wäre das Teilen eines Ordners gleich dem Teilen mit einer Gruppe. Dafür braucht es eine Entscheidung.
3. **Freigabemodell:** Dateien, Galerie, Kanban und Umfragen brauchen es alle. Wir schlagen eine gemeinsame Spezifikation vor statt vier Lösungen.
4. **Verschlüsselung:** Sollen Bytes auf S3 immer auf dem Client verschlüsselt werden, mit dem Schlüsseltresor (ADR 0024)? Wir schlagen ja vor.
5. **Liegen die Daten an einem Ort?** Bytes liegen bewusst außerhalb von `fs-store`, daher müssen Sicherungen beides abdecken.
