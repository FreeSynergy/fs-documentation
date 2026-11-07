# FreeSynergy Release — one way to ship, free of charge

**This is a building block. It is why you can check that a download really is ours.**

FreeSynergy Release holds the shared build and release recipes for all FreeSynergy repositories. One recipe checks the code, one packages it, signs it and describes it. Every program gets the same treatment, so we do not maintain twenty different pipelines.

What is different here: everything is free of charge for you and for us. A release comes with a list of checksums and an OpenPGP signature, a software bill of materials and build provenance, so you can see what is inside and who built it. We say openly where we cannot do something yet: macOS and Windows builds are not signed by the platform vendors, and the repo explains how to open them anyway.

## What it can do today

No release tag yet. The workflows are used by the repos through a caller file.

- CI: formatting, lints, tests, our own code-rules checker and a licence policy check.
- Packages: Linux (tar.gz, deb, rpm, AppImage, Arch, optional Flatpak), Windows (zip, msi, exe), macOS (tar.gz, dmg), optional container image.
- A software bill of materials (SPDX), build provenance, checksums and OpenPGP signatures.
- A draft GitHub release, never published automatically.
- First real run was green on FreeSynergy/fs-capnpc as a draft release: tar.gz for Linux and macOS, deb, rpm, Arch, msi and zip, SBOM and checksums.

## What is not there yet

- Signing has not been shown in a real release run yet. AppImage, exe, dmg, Flatpak and containers have not been exercised either.
- Android and iOS are placeholders until the first Blinc app exists.
- macOS and Windows packages are unsigned by the vendors.
- A previous signing key was revoked on 2026-11-07, because an AI agent had created it and knew its passphrase. The current key and its fingerprint are in the repo. Do not trust the revoked one.

## Part of FreeSynergy

Release is the same pipeline for every repo. FreeSynergy is a family of programs that are free for everyone, forever, and that keep your data yours. The documentation, the manifesto and the overall plan live in [fs-documentation](https://github.com/FreeSynergy/fs-documentation); the reading version is at <https://freesynergy.github.io/fs-documentation/>. Start with the [manifesto](https://freesynergy.github.io/fs-documentation/en/manifesto/) if you want to know why we do this.


## For developers

- No Rust workspace: GitHub Actions workflows (`ci.yml`, `release.yml`), composite actions with shell and Python packaging scripts, and golden tests in `tests/`.
- Call it from your repo; see [docs/usage.md](docs/usage.md) and the example callers in `examples/callers/`. Signing: `docs/signing.md`; formats: `docs/formats.md`.
- Verify a release: import `release-signing-key.asc`, then `gpg --verify` the file and run `sha256sum -c SHA256SUMS.txt`.
- Design: [DESIGN.md](DESIGN.md).
- Licence: MIT OR Apache-2.0.
