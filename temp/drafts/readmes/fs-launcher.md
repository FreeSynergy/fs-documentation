# FreeSynergy Store — install and keep everything up to date

**One place to get FreeSynergy, with every download checked before it touches your machine.**

> Honest status first: this is the future app store. Today it is only the engine room and a design, kept in a repo called `fs-launcher` that is not public yet. There is nothing to download or click. When the store app is ready we will say so here.

The idea: you open the store, choose a program, a frontend, a component or a theme, and it installs. It keeps itself and everything else up to date, rolls an update back if it fails, and never replaces a program while it is running. Packages come from a list of Git sources. You can add your own. The built-in FreeSynergy source can be switched off but never removed, so you cannot lose the way back by accident.

What is different here: every package must carry a valid OpenPGP signature from a trusted key, or it cannot be installed at all. This is not a warning you can click away; in the code, an unsigned package cannot even be passed to the installer. A checksum alone does not count as a signature.

## What it can do today

Not yet released. Version 0.1.0 of the core, no tag.

- The rules in code: sources (user list plus the built-in reference source), package kinds (program, frontend, component, theme) and formats (rpm, Flatpak, AppImage, tar.gz).
- Signature check through the rPGP library against the built-in release key.
- Update with undo: check that the program is not running, install remembering the old version, and on error roll back.
- A source list as a TOML file.
- Tests: 27.

## What is not there yet

- No network access, no Git fetching, no real installers, no replacing of the running store itself.
- No window and no command line, and not yet a contract file in fs-interfaces.
- Checks for key expiry are not built.
- Names, including "Launcher" and "Store", are provisional.

## Part of FreeSynergy

The store is how people will get all the other programs. FreeSynergy is a family of programs that are free for everyone, forever, and that keep your data yours. The documentation, the manifesto and the overall plan live in [fs-documentation](https://github.com/FreeSynergy/fs-documentation); the reading version is at <https://freesynergy.github.io/fs-documentation/>. Start with the [manifesto](https://freesynergy.github.io/fs-documentation/en/manifesto/) if you want to know why we do this.


## For developers

- Workspace crates in `crates/`: `fs-launcher-core` (no input, no output, no network, only traits and values), `fs-launcher-pgp` (rPGP behind our signature trait; rPGP is MIT or Apache, we avoid LGPL), `fs-launcher-sources` (TOML source list). Engines and frontends are meant to be separate packages.
- Local repo name today: `fs-launcher`; the name `fs-store` is planned. There is no public repo yet.
- Build and test: `cargo build --workspace` and `cargo test --workspace`.
- Design, pattern map and the sketch of the contract: [DESIGN.md](DESIGN.md).
- Licence: MIT OR Apache-2.0.
