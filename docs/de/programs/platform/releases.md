# Veröffentlichungen

So erreichen FreeSynergy-Programme die Menschen. **Status: wird eingerichtet (2026-11-06), noch nichts veröffentlicht.** ADR 0051.

## Nur kostenlose Wege

Wir nutzen nur, was nichts kostet, im Einklang mit dem [Manifest](../../manifesto.md). Niemand sollte einer Plattform bezahlen müssen, um freie Software verteilen zu dürfen, also tun wir es nicht.

| Plattform | Formate | Hinweis |
|-----------|---------|---------|
| Linux | deb, rpm, tar.gz, AppImage, Flatpak, Arch | |
| Windows | msi, exe, zip | Unsigniert, daher zeigt Windows eine Warnung. Ein kostenloses Signierprogramm für Open-Source-Projekte wird erwogen |
| macOS | Universelles dmg | Unsigniert, daher zeigt macOS eine Warnung. Wir zahlen Apple nichts; ein gespendetes Konto wäre akzeptabel |
| Android | F-Droid | |
| iOS | Nur Build | Kein kostenloser Weg zur Verteilung |

## Vertrauen

| Was | Standard |
|-----|----------|
| Signatur | OpenPGP, die offene Option, bei Linux-Paketen üblich |
| Inhalt | SPDX SBOM (ISO/IEC 5962:2021) |
| Herkunft | SLSA-Provenance |
| Versionen | SemVer |
| Selbst bauen | Reproduzierbare Builds |

## Wie

Gemeinsame Workflows liegen in `fs-release`, damit jedes Repository gleich veröffentlicht. Veröffentlichungen beginnen als Entwürfe und werden öffentlich, wenn sie Menschen etwas bringen.
