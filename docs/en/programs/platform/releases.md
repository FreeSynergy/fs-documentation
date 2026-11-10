# Releases

## In short

This is how FreeSynergy programs reach you. One shared set of build and release recipes checks, packages, signs and describes every program, so each one is treated the same way. The aim is that you can check that a download really is ours.

## What is different here

- Everything is free of charge, for you and for us.
- Each release comes with checksums, an OpenPGP signature, a software bill of materials and build provenance, so you can see what is inside and who built it.
- We say openly what we cannot do yet. macOS and Windows builds are not signed by the platform vendors, and the repository explains how to open them anyway.
- Releases start as drafts and are never published automatically.
- The store app, FreeSynergy.Store, is planned to refuse any package without a valid signature. It is not public yet, and there is nothing to download.

## Where it stands today

There is no release tag yet. The shared workflows exist and the repositories use them. The first real run, on `fs-capnpc`, produced a draft release with Linux, macOS and Windows packages, a bill of materials and checksums. Signing has not been shown in a real release run yet. AppImage, exe, dmg, Flatpak, containers and mobile are untried. The store is planned: today it exists only as a design and a core library, in a repository that is not public.

How FreeSynergy programs reach people. **Status (2026-11-06): the shared workflows exist. `capnp-compiler` 0.1.1 is on crates.io; its signed release on GitHub is still a draft.** ADR 0051.

## Only free ways

We use only what costs nothing, in line with the [manifesto](../../manifesto.md). Nobody should have to pay a platform
for the right to hand out free software, so we don't.

| Platform | Formats | Note |
|----------|---------|------|
| Linux | deb (Debian 13, Ubuntu 24.04), rpm, tar.gz, AppImage, Flatpak, Arch | |
| Windows | zip (with the `.exe`), msi, setup.exe | Not yet signed with a Windows certificate, so SmartScreen warns (see below). A free signing programme for open-source projects is being considered (SignPath, ADR 0051) |
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

**Tried so far:** tar.gz for Linux and macOS universal, deb, rpm, Arch, Windows zip, msi and setup.exe, SPDX SBOM, checksums.
OpenPGP signatures too, with the [release key](https://github.com/FreeSynergy/fs-release/blob/main/release-signing-key.asc), fingerprint
`16A4 A3EE 563A EF51 FCF0  C55D ED7B 57C4 A190 4342`, until 2029-11-07, made by the project owner himself (2026-11-07). **Do not trust the earlier key** `C40F 0FBA 5C4C F71D 7BEB  B5C6 5478 A473 8FFE EB69`: an AI agent created it and knew its passphrase. Nothing public was signed with it, and it was revoked on 2026-11-07.
**Not tried yet:** AppImage, dmg, Flatpak, containers, mobile.

## Tested before the draft exists

Every package is installed on the system it is meant for, every program is started once and the package is removed again;
if one step fails, there is no release. `deb` is tried in a Debian 13 and an Ubuntu 24.04 container (x86_64 and aarch64), the
Windows `zip`, `msi` and `setup.exe` on a Windows runner. Not tested this way yet: `rpm`, AppImage, dmg.

## Windows: the SmartScreen warning

A Windows certificate costs money every year, and Microsoft would be the only one earning from free software. So the Windows
files are **not signed with a Windows certificate yet**. When you start the `.msi` or the `-setup.exe`, Windows shows "Windows
protected your PC". That is no sign of a problem with the file, only of the missing certificate. Click **More info**, then
**Run anyway**. The `.zip` has no installer: unpack it and start the `.exe` inside (SmartScreen may ask the same once).

What you can check instead is the OpenPGP signature (`.asc` next to every file) and `SHA256SUMS.txt` against the
[release key](https://github.com/FreeSynergy/fs-release/blob/main/release-signing-key.asc). As soon as SignPath (a free signing
service for open-source projects) agrees, the Windows files get a real signature and the warning goes away over time.
