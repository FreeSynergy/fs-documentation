# Releases

How FreeSynergy programs reach people. **Status (2026-11-06): the shared workflows exist. `capnp-compiler` 0.1.1 is on crates.io; its signed release on GitHub is still a draft.** ADR 0051.

## Only free ways

We use only what costs nothing, in line with the [manifesto](../../manifesto.md). Nobody should have to pay a platform
for the right to hand out free software, so we don't.

| Platform | Formats | Note |
|----------|---------|------|
| Linux | deb, rpm, tar.gz, AppImage, Flatpak, Arch | |
| Windows | msi, exe, zip | Unsigned, so Windows shows a warning. A free signing programme for open-source projects is being considered |
| macOS | Universal dmg | Unsigned, so macOS shows a warning. We pay Apple nothing; a donated account would be acceptable |
| Android | F-Droid | |
| iOS | Build only | No free way to distribute |

## Trust

| What | Standard |
|------|----------|
| Signature | OpenPGP, the open option and native to Linux package signing |
| Contents | SPDX SBOM (ISO/IEC 5962:2021) |
| Where it came from | SLSA provenance |
| Versions | SemVer |
| Building it yourself | Reproducible builds |

## How

Shared workflows live in [`fs-release`](https://github.com/FreeSynergy/fs-release), so every repository releases the same way.
Releases start as drafts, and become public when they bring people something.

**Tried so far:** tar.gz for Linux and macOS universal, deb, rpm, Arch, Windows msi and zip, SPDX SBOM, checksums.
OpenPGP signatures too, with the [release key](https://github.com/FreeSynergy/fs-release/blob/main/release-signing-key.asc), fingerprint
`C40F 0FBA 5C4C F71D 7BEB  B5C6 5478 A473 8FFE EB69`, until 2029-11-05.
**Not tried yet:** AppImage, exe, dmg, Flatpak, containers, mobile.
