# Releases

How FreeSynergy programs reach people. **Status: being set up (2026-11-06), nothing published yet.** ADR 0051.

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

Shared workflows live in `fs-release`, so every repository releases the same way. Releases start as drafts, and become
public when they bring people something.
