# FreeSynergy installieren

**Pre-release. Bitte lies das zuerst.** FreeSynergy steht noch am Anfang. Was du heute installieren kannst, ist eine erste Version für Leute, die Dinge ausprobieren und uns sagen wollen, was falsch ist. Rechne mit rauen Kanten und spiel nichts darauf, das du nicht verlieren könntest.

## Die Idee: den Store einmal holen, dann alles aus dem Store

Ein Programm installierst du von Hand: [FreeSynergy.Store](../programs/platform/store.md). Danach installierst, aktualisierst und entfernst du jedes weitere FreeSynergy-Programm von dort aus, mit einem Klick, und jede Datei wird geprüft, bevor sie deinen Rechner erreicht. Du musst nicht immer wieder Dinge von Hand herunterladen.

## Schritt 1: den Store holen

Der Store wird als **Pre-release** auf GitHub veröffentlicht: <https://github.com/FreeSynergy/fs-store/releases>.

Wähle das neueste Release, das als „Pre-release“ markiert ist. Ein Release enthält diese Dateien (die genaue Auswahl kann sich von Release zu Release ändern, schau also in die Liste dort):

| Für | Datei |
|-----|-------|
| Fedora und andere rpm-Systeme | `.rpm` |
| Debian und Ubuntu | `.deb` |
| Arch | `.pkg.tar.zst` |
| jedes Linux, ohne root-Rechte nötig | `.tar.gz` oder `.AppImage` (x86_64 und aarch64) |
| macOS | `.dmg` |
| zum Prüfen | `SHA256SUMS.txt`, eine `.asc`-Signatur neben jeder Datei, der Release-Schlüssel `FreeSynergy-release-key.pgp` |

Windows ist noch nicht im Release. Der macOS-Build ist nicht mit einem bezahlten Apple-Zertifikat signiert: Öffne unter macOS die App einmal, dann Systemeinstellungen > Datenschutz & Sicherheit > „Trotzdem öffnen“. Die OpenPGP-Signaturen und Prüfsummen sind der Vertrauensweg.

!!! warning "Stand am 2026-11-08"
    Das neueste Pre-release am 2026-11-08 ist `v0.1.0-rc.5`. Das erste (`v0.1.0-rc.1`) ist als „Do not use“ markiert: Es kann keine Pakete prüfen, die vom Release-Workflow signiert wurden. Nimm immer das neueste Pre-release der Liste.

## Schritt 2: die Signatur prüfen

Jede Datei ist mit OpenPGP signiert. Der Projektschlüssel lautet:

```text
16A4 A3EE 563A EF51 FCF0 C55D ED7B 57C4 A190 4342
```

Releases sind mit einem Signatur-Subkey dieses Schlüssels signiert: `372A 583D 05BF 8362 604C F25D E26A 2347 F2B1 C097`.

Mit `gpg`, im Ordner mit deinen Downloads:

```bash
gpg --import FreeSynergy-release-key.pgp
gpg --fingerprint 16A4A3EE563AEF51FCF0C55DED7B57C4A1904342     # mit der Zeile oben vergleichen
gpg --verify SHA256SUMS.txt.asc SHA256SUMS.txt                 # muss "Good signature" ausgeben
sha256sum --ignore-missing -c SHA256SUMS.txt                   # jede Datei, die du heruntergeladen hast: OK
```

Die Releases enthalten auch einen Herkunftsnachweis (SLSA), den du mit `gh attestation verify <Datei> --repo FreeSynergy/fs-store` prüfen kannst, und eine SBOM (`*.spdx.json`).

Vertrau der Schlüsseldatei nicht nur deshalb, weil sie mit dem Release kam. Vergleiche den Fingerabdruck mit dieser Seite und mit der Schlüsseldatei im [Dokumentations-Repository](https://github.com/FreeSynergy/fs-documentation). Schlägt eine Prüfung fehl, installiere nichts und sag uns Bescheid.

## Schritt 3: den Store installieren

- **Fedora:** `sudo dnf install ./fs-store-*.rpm` (root-Rechte fragt dein System ab, nicht wir).
- **Ohne root:** Entpack die `.tar.gz` irgendwo in deinem Home-Ordner, oder mach die `.AppImage` ausführbar und starte sie.

Der Store ist ein Programm, `fs-store`. Ohne Argumente gestartet, öffnet er sein Fenster. In der Kommandozeile funktioniert er wie `git`: `fs-store sources`, `fs-store available`, `fs-store install <package>`, `fs-store installed`. Was heute schon funktioniert, steht unter [der Store](../programs/platform/store.md).

## Schritt 4: alles Weitere aus dem Store

Installier die Programme, die du willst, aus dem Store, zum Beispiel Tasks oder People. Der Store prüft den Katalog und jedes Paket gegen den Projektschlüssel, behält bei einem Update die alte Version, rollt zurück, wenn ein Update fehlschlägt, und aktualisiert sich selbst auf dieselbe Weise.

## Was noch fehlt

- Eine fertige App für normale Nutzerinnen und Nutzer. Die Fenster sind vorläufig, und sie sagen das auch.
- Die Katalogquelle wird gerade eingerichtet; bis dahin kommen Pakete direkt aus den Releases der einzelnen Programme.
- Windows und die Anmeldung. Was als Nächstes kommt, steht im [Gesamtplan](../programs/apps/roadmap.md).

Ist dir etwas kaputt oder unklar aufgefallen? Siehe [Wie du helfen kannst](help.md).
