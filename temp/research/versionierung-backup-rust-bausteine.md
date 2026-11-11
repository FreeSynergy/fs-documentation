# Rust-Bausteine für Versionierung und Backup

Stand: 2026-11-11. Gehört zu `versionierung-backup.md`. Korrekturen laut Opus-Nachprüfung sind mit „laut Korrektur“ markiert.

## gix (gitoxide)

**Quellen:** https://crates.io/api/v1/crates/gix (Version 0.90.0, aktualisiert 2026-10-22, Lizenz MIT OR Apache-2.0, Repo https://github.com/GitoxideLabs/gitoxide); crate-status.md: https://raw.githubusercontent.com/GitoxideLabs/gitoxide/main/crate-status.md (per Fetch-Zusammenfassung gelesen, Seite markiert sich als generiert; bitte im Original prüfen)

**Lizenz:** MIT OR Apache-2.0.

**Reife:** Version 0.90.0, pre-1.0 (API kann brechen). Sehr viele Downloads (gesamt ca. 56 Mio.).

**Schreiben (laut crate-status, Zusammenfassung):**
- Commit aus Tree anlegen: vorhanden (unsigniert; Signierung nicht).
- Index schreiben: V2/V3 ja, V4 nein; Einträge hinzufügen/entfernen fehlt.
- Tree schreiben: Änderungen an Trees ja; Tree aus Index erzeugen fehlt.
- Push: fehlt.
- Fetch: weitgehend vorhanden (Shallow, Negotiation); FETCH_HEAD und Remote-Speicherung fehlen.
- Checkout: Low-Level ja; Submodule, Sparse und Porcelain-Befehle (switch, restore, reset) fehlen.

**Fazit:** Für lokale Commits und Tree-Edits brauchbar; Push und vollständiges Index-Schreiben fehlen. Für Versions-Speicherung ohne Push ausreichend.

## git2 (libgit2-Bindings)

**Quellen:** https://crates.io/api/v1/crates/git2 (Version 0.21.0, aktualisiert 2026-10-06, Lizenz MIT OR Apache-2.0, Repo https://github.com/rust-lang/git2-rs)

**Lizenz:** MIT OR Apache-2.0 (Bindings). libgit2 selbst: GPL-2.0 mit Linking-Exception (nach Kenntnisstand, nicht auf dieser Seite gelesen).

**Reife:** 0.21.0, pre-1.0 Bindings, aber lange genutzt. Schreib-API (Commit, Index, Tree, Push, Fetch) laut Beschreibung vollständig, Details nicht geprüft.

## rustic_core

**Quellen:** https://crates.io/api/v1/crates/rustic_core (Version 0.13.0, aktualisiert 2026-08-16); https://github.com/rustic-rs/rustic_core/blob/main/README.md

**Lizenz:** Apache-2.0 OR MIT.

**Reife/API:** "early development stage", API kann sich ändern (laut README). Mindestens Rust 1.91.0. Unterstützt Init, Backup, Restore, Check; Prune nicht in den Beispielen belegt. **Laut Korrektur:** `lib.rs` exportiert `forget`, `prune`, `copy`, `repair`; die API bricht alle 1 bis 3 Monate (0.x), die Bibliothek ist nur synchron (rayon, crossbeam).

## restic-Repository-Format

**Quelle:** https://raw.githubusercontent.com/restic/restic/master/doc/design.rst

**Kernpunkte (eigene Worte):** Unveränderliche Dateien, Benennung per SHA-256, Content-Defined Chunking mit Rabin-Fingerprint, Packs mit verschlüsseltem Header, AES-256-CTR plus Poly1305-AES, Schlüssel per scrypt in Key-Dateien. Das Format ist dokumentiert und wird von restic und rustic genutzt.

## Empfehlung (kurz)

- Git-Teil: gix oder git2; für nur lokale Versionen reicht gix (MIT/Apache), Push fehlt bei gix.
- Backup-Teil: restic-Format über rustic_core ist interessant, aber 0.x mit instabiler API; Bindung an ein Format ist eine Architekturentscheidung für später.
