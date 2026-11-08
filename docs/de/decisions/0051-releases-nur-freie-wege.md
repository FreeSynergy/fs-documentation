# 0051 – Releases: `fs-release`, nur kostenlose Wege, offene Signatur

Status: akzeptiert (2026-11-06) · öffentlich: `docs/en/programs/platform/releases.md` · Umsetzung: freesynergy-32

## Entscheidung (Nutzer)
1. **`fs-release`:** gemeinsames Repo mit wiederverwendbaren CI- und Release-Abläufen für alle Repos.
2. **Nur was kostenlos ist.** „Apple bekommt von mir kein Geld.“ Ein gespendetes Konto wäre annehmbar.
3. **OpenPGP/GPG zum Signieren:** Bei mehreren Möglichkeiten immer die offene Variante.
4. **Android über F-Droid.** Getestet wird mit dem, was schon da ist.

## Von freesynergy-32 gemeldet (Nutzerwortlaut hier nicht geprüft)
- Formate: Linux deb, rpm, tar.gz, AppImage, Flatpak, Arch; Windows msi, exe, zip unsigniert; macOS Universal-dmg unsigniert;
  iOS nur Build.
- Releases nur als **Entwürfe**; öffentlich nur, „wenn es etwas bringt“.
- Dazu SPDX-SBOM (ISO/IEC 5962:2021), SLSA-Herkunftsnachweis, SemVer, reproduzierbare Builds.
- SignPath (kostenlose Windows-Signatur für OSS): **Nutzer am 2026-11-13 erneut fragen.**
- Die erste Blinc-App auf Android und iOS testet zugleich Blincs Mobil-Schicht; Korrekturen gehen als PR an den Autor.

## Folgen
- Unsignierte Programme lösen unter macOS und Windows Warnungen aus. Die Installationsanleitung muss das ehrlich erklären.
