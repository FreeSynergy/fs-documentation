# Veröffentlichungen

## Kurz gesagt

So erreichen FreeSynergy-Programme dich. Ein gemeinsamer Satz an Build- und Veröffentlichungsrezepten prüft, paketiert, signiert und beschreibt jedes Programm, sodass alle gleich behandelt werden. Ziel ist, dass du prüfen kannst, dass ein Download wirklich von uns stammt.

## Was hier anders ist

- Alles ist kostenlos, für dich und für uns.
- Jede Veröffentlichung kommt mit Prüfsummen, einer OpenPGP-Signatur, einer Software Bill of Materials und Build-Provenienz, sodass du siehst, was drinsteckt und wer es gebaut hat.
- Wir sagen offen, was wir noch nicht können. macOS- und Windows-Builds sind nicht von den Plattformherstellern signiert, und das Repository erklärt, wie du sie trotzdem öffnest.
- Veröffentlichungen beginnen als Entwürfe und werden nie automatisch veröffentlicht.
- Die Store-App, FreeSynergy.Store, soll jedes Paket ohne gültige Signatur ablehnen. Sie ist noch nicht öffentlich, und es gibt nichts zum Herunterladen.

## Wo es heute steht

Es gibt noch kein Veröffentlichungs-Tag. Die gemeinsamen Workflows existieren, und die Repositories nutzen sie. Der erste echte Lauf, auf `fs-capnpc`, erzeugte einen Entwurf einer Veröffentlichung mit Linux-, macOS- und Windows-Paketen, einer Bill of Materials und Prüfsummen. Die Signatur wurde in einem echten Veröffentlichungslauf noch nicht gezeigt. AppImage, exe, dmg, Flatpak, Container und mobile Plattformen sind nicht ausprobiert. Der Store ist geplant: Heute existiert er nur als Entwurf und als Kernbibliothek, in einem Repository, das nicht öffentlich ist.

So erreichen FreeSynergy-Programme die Menschen. **Status (2026-11-06): Die gemeinsamen Workflows existieren. `capnp-compiler` 0.1.1 ist auf crates.io; seine signierte Veröffentlichung auf GitHub ist noch ein Entwurf.** ADR 0051.

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
| Signatur | OpenPGP, die offene Option und bei Linux-Paketsignaturen üblich |
| Inhalt | SPDX SBOM (ISO/IEC 5962:2021) |
| Herkunft | SLSA-Provenienz |
| Versionen | SemVer |
| Selbst bauen | Reproduzierbare Builds |

## Wie

Gemeinsame Workflows liegen in [`fs-release`](https://github.com/FreeSynergy/fs-release), damit jedes Repository gleich veröffentlicht.
Veröffentlichungen beginnen als Entwürfe und werden öffentlich, wenn sie Menschen etwas bringen.

**Bisher ausprobiert:** tar.gz für Linux und macOS universal, deb, rpm, Arch, Windows msi und zip, SPDX SBOM, Prüfsummen.
OpenPGP-Signaturen ebenfalls, mit dem [Veröffentlichungsschlüssel](https://github.com/FreeSynergy/fs-release/blob/main/release-signing-key.asc), Fingerabdruck `16A4 A3EE 563A EF51 FCF0  C55D ED7B 57C4 A190 4342`, gültig bis 2029-11-07, vom Projektverantwortlichen selbst erstellt (2026-11-07). **Vertraue dem früheren Schlüssel nicht** `C40F 0FBA 5C4C F71D 7BEB  B5C6 5478 A473 8FFE EB69`: Ein KI-Agent hat ihn erstellt und kannte seine Passphrase. Damit wurde nichts Öffentliches signiert, und er wurde am 2026-11-07 widerrufen.
**Noch nicht ausprobiert:** AppImage, exe, dmg, Flatpak, Container, mobile Plattformen.
