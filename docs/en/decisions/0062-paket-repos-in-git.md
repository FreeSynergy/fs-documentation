# 0062 – Pakete liegen in Git: Katalog-Repo, ein Tag je Version, TUF, Spiegel überall

Status: akzeptiert (Nutzer, 2026-11-08) · füllt ADR 0036 („Format eines Paket-Repositorys festlegen“) · ergänzt ADR 0051, 0059, 0060, 0061

## Entscheidung (Nutzer)
Programme sollen auch ohne GitHub online gestellt werden können. Statt nur über HTTPS liegen sie in Git, mit einer festen Struktur, aus der der Laden (`fs-store`) sie holt. Standards: **TUF ganz übernehmen, wenn es geht.**

## Struktur
1. **Katalog-Repo** (unseres: `FreeSynergy/fs-catalog`): AppStream-Katalog (Name, Logo, Beschreibung, Facetten nach ADR 0061) plus **TUF-Metadaten** (The Update Framework, CNCF-Spezifikation): `root`, `targets`, `snapshot`, `timestamp`, je mit Version und Ablaufdatum, signiert. Rust: `tough` (Apache-2.0) prüfen; passt es nicht, eigene Umsetzung der Spezifikation, nichts erfinden.
2. **Paket-Repos:** Jede Version ist ein Git-Tag; darin die fertigen Pakete (tar.gz, rpm, …) und ihre OpenPGP-Signaturen. Der Laden holt mit `gix` nur diesen einen Tag (flach), nie die ganze Geschichte.
3. **Spiegel überall:** Jeder Ort, der Git kann (Codeberg, eigenes Forgejo, USB-Stick, später Radicle, ADR 0059). Echtheit hängt an den Signaturen und TUF, nicht am Ort. Ein Spiegel kann nichts Veraltetes unterschieben (TUF: Versionen, Ablaufdaten, Snapshot).
4. **HTTPS als zweiter Weg** erlaubt (z. B. GitHub-Releases); der Katalog nennt je Paket die Orte.
5. **Schlüssel:** Die TUF-Rolle `root` hängt am Projektschlüssel `16A4…4342` (offline beim Nutzer); `targets`/`snapshot`/`timestamp` signiert der Unterschlüssel bzw. eigene Schlüssel der Abläufe. Rollen- und Schlüsselverteilung legt Thread S als Vorschlag vor, der Nutzer bestätigt.

## Vorbilder (Funktionen, nichts kopiert)
Guix-Kanäle (Git-Repo mit signierten Commits), OSTree/Flatpak (Git-artige Ablage für Programme), F-Droid (signierter Index, Spiegel).

## Folgen
- Thread S baut Katalog und Paket-Repos nach diesem ADR; `fs-release` legt bei jedem Release den Tag im Paket-Repo an und aktualisiert die TUF-Metadaten.
- Was im Sprint nicht fertig wird, steht als `Unsupported` in der `DESIGN.md` von `fs-store`.
