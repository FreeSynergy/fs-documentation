# VectorCraft als Vektor-Grundlage – Kurzprüfung (nur gelesen)

Stand 2026-11-12 (Opus, Entwurf, kein ADR, kein Code). Klon `/srv/FreeSynergy/.scratch/vendor-read/vectorcraft`, Commit `7f3a046` (2026-11-11), nichts gebaut, kein Skript/`build.rs` ausgeführt; Lizenzen über crates.io-API, Aktivität über GitHub-API. **[nicht geprüft]** = nicht belegt.

**Crates ohne egui:** Das Projekt erzwingt selbst, dass unterhalb der UI-Schicht nichts von egui/winit abhängt (`cargo xtask layers`, `docs/architecture.md`).

| Crate | Größe / Tests | Abhängigkeiten | Für uns |
|---|---|---|---|
| `vectorcraft-geom` | 5,2k Zeilen / 114 | `kurbo` 0.13, `serde`, `thiserror` (21 im Baum), kein `build.rs` | **nehmen**: Anker-Pfadmodell, Formen, Treffer, Fangen |
| `vectorcraft-pathops` | 15,6k / 291 + proptest | `geom`, `linesweeper` (23 im Baum) | **nehmen**: Boolesch (kurvenerhaltend), Offset, Kontur, Vereinfachen |
| `-doc` / `-svg` / `-render` | 42k / 22k / 37k | 94 / 211 / 212 im Baum; `render` = `vello_cpu` | `doc` nur als Projektion; `svg` später als Import-Agent; `render` nein (zweiter Renderer neben Blinc, ADR 0015 Pkt. 4) |
| `-engine` / `-mcp` | 302k / 11,5k | alles (PDF, EPS, CAD …), 284 im Baum | nein, nur Vorbild (`Session` = ganzer Programmzustand) |
| `-plugins` | 11,4k | `doc`, `wasmi` 2.0.0 | Vorbild |

**Lizenzen:** Projekt `MIT OR Apache-2.0` (Cargo, README, beide LICENSE-Dateien; GitHub erkennt nur Apache). Baum `geom`+`pathops`: nur MIT/Apache (+ Unicode-3.0). Weiterer Baum (213 Crates): Zlib, BSD, Unicode-3.0, `jpeg-encoder` mit IJG-Hinweispflicht (nur `render`); kein GPL/AGPL/MPL gefunden. Git-Quellen `craft-libs` MIT OR Apache-2.0. `engine`-Baum nur teilweise geprüft.

**Stabilität/Aktivität:** nicht auf crates.io; eine Workspace-Version für alle (0.24.0), neue Minor-Version alle 2–3 Tage seit 2026-09-30, keine API-Zusage. 11 024 Commits in 6 Wochen, drei Konten ≈ 73 %, `AGENTS.md`/`CLAUDE.md` vorhanden; 11,6k Sterne, 853 offene / 1 250 geschlossene Issues. Qualität: `unsafe` verboten, keine Panics (Clippy), Importer gefuzzt. Wasm: Web-App vorhanden, aber kein wasm32-Bau in der CI gefunden. **Falle:** Ihr `[patch.crates-io]` (u. a. `linesweeper` → craft-libs `481f66d`) greift bei Nutzern nicht; wir müssen ihn nachziehen. Rust ≥ 1.95 (wir 1.99.1).

**Passung Blinc:** Blinc hat eigenen `Path` (f32, `cubic_to`) und `blinc_svg`, aber kein Vektormodell und keine Booleans. Aufteilung: VectorCraft = Geometrie, Blinc = Darstellung, fs-whiteboard-core = Wahrheit. Es fehlen ein Adapter `BezPath → blinc Path` in fs-components und eine Szenenbeschreibung (ADR 0045). Text bleibt bei Blinc (`vectorcraft-text` wäre doppelt). Zwei `kurbo`-Versionen (Blinc 0.11, VC 0.13) sind unschädlich.

**Passung Whiteboard/Loro:** `doc` taugt nicht als Wahrheit (`NodeId(u64)` = Zähler je Dokument, kollidiert über Geräte; geordnete `Vec` statt Ordnungsschlüssel; kein Merge). Unser Modell (UUID, `order`-Schlüssel, Merge je Eigenschaft, später Loro) bleibt. Neu nötig: Art `path` im `whiteboard.capnp`-Union (anhängen), lokal zu `frame`; Merge-Einheit zuerst der ganze Pfad, je Anker erst mit Loro. Boolesch = ein Command (Quellen `deleted`, neuer Pfad).

**Vorbild Module/KI:** Plug-ins als `.wasm` in `wasmi` (reines Rust, auch wasm32): ohne WASI/Datei/Netz/Uhr, Befehlsbudget + Zeitlimit, 512 MiB-Deckel, frische Instanz je Lauf, Rechte im Manifest; Arten Filter, Live-Effekt, Exporter, Importer → passt für „Shader/Effekte später als Module“. MCP: jede Handlung ist ein Befehl mit fester Id + JSON-Schema aus einer Registry (Menü, CLI, MCP gleich), Headless-Rendern als Rückmeldung an Agenten, Lese-/Schreib-Wurzeln begrenzen Agenten (passt zu ADR 0021/0066).

**Empfehlung Zusammenarbeit (ADR 0015):**
1. Nur `geom` + `pathops` als Git-Abhängigkeit auf festen Commit, hinter eigener Schnittstelle in fs-whiteboard-core; ihren `linesweeper`-Patch nachziehen, ihre Tests als Gegenprobe; Quellen beim Release mitspiegeln (ADR 0068).
2. In die ADR-0015-Liste aufnehmen: „VectorCraft – Vektor-Geometrie/Pfad-Operationen, MIT OR Apache-2.0, nutzen auf festem Commit; `ui-egui`, `render`, `text` nicht.“
3. Wünsche in `todo/upstream.md`; das Issue schreibt der Nutzer.

**Issue-Entwurf (nicht gesendet):**
> Would you consider publishing `vectorcraft-geom` and `vectorcraft-pathops` on crates.io?
> We (FreeSynergy, MIT OR Apache-2.0, Rust) want to use them as geometry for our whiteboard with our own GUI; your layer rule already makes that possible, thanks.
> Today we must pin a git revision, and your `[patch.crates-io]` for `linesweeper` (craft-libs `481f66d`) does not reach downstream users.
> One workspace version for all crates also hides whether `geom`/`pathops` changed their API.
> Could you publish both (own 0.x versions) and upstream or publish the `linesweeper` changes? We are glad to help with a PR.
