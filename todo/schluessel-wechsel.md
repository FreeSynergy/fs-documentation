# Signaturschlüssel wechseln

Für den Nutzer, von Hand, **in einem eigenen Terminal und nicht in einer KI-Sitzung** (ADR 0054). Keine Passphrase, kein privater Schlüssel in einen Chat, eine Datei im Repo oder einen Befehl.

**Warum neu statt neue Passphrase:** Ein Agent hat `C40F 0FBA 5C4C F71D 7BEB  B5C6 5478 A473 8FFE EB69` erzeugt und die Passphrase gekannt. Wer eine alte Kopie hat, kann mit der alten Phrase weiter signieren.

**Stand (2026-11-07):** Öffentlich ist damit nichts signiert. Es gibt einen Entwurf `capnp-compiler v0.1.1` in `fs-capnpc`, der damit signiert wurde. Die Secrets `GPG_PRIVATE_KEY` und `GPG_PASSPHRASE` liegen in `fs-capnpc` und `fs-hub`. Jeder Tag `v*` in `fs-capnpc` signiert automatisch mit dem alten Schlüssel.

## 1. Alte Secrets entfernen (eine Minute, am besten zuerst)
```bash
for r in fs-capnpc fs-hub; do
  gh secret delete GPG_PRIVATE_KEY -R FreeSynergy/$r
  gh secret delete GPG_PASSPHRASE -R FreeSynergy/$r
done
```
Der Workflow in `fs-capnpc` hat danach nichts mehr zum Signieren. Ob er dann scheitert oder ohne Signatur baut, ist nicht geprüft.

## 2. Neuen Schlüssel erzeugen
Am besten auf einem Rechner ohne Netz, sonst auf einem verschlüsselten USB-Stick. Die Passphrase ist neu und wird nirgends sonst benutzt; das Programm fragt selbst danach.
```bash
export GNUPGHOME=/pfad/zum/stick/gnupg-freesynergy
mkdir -m 700 "$GNUPGHOME"
gpg --quick-generate-key "FreeSynergy Release <support@freesynergy.net>" ed25519 sign 3y
gpg --list-keys --fingerprint
```
Das Widerrufszertifikat legt GnuPG selbst an: `$GNUPGHOME/openpgp-revocs.d/<Fingerabdruck>.rev`. Sichere den ganzen Ordner auf einen zweiten Stick.

## 3. Öffentlichen Teil ausgeben
```bash
gpg --armor --export <NEUER-FINGERABDRUCK> > release-signing-key.asc
```
Hochladen auf <https://keys.openpgp.org/upload> und den Link in der Mail bestätigen.

## 4. Alten Schlüssel widerrufen
Du brauchst den öffentlichen Schlüssel aus `fs-release/release-signing-key.asc` und dein offline gesichertes Widerrufszertifikat. Dieses gilt erst, wenn man im Zertifikat in der Zeile `:-----BEGIN PGP PUBLIC KEY BLOCK-----` den Doppelpunkt am Anfang entfernt.
```bash
gpg --import alter-oeffentlicher-schluessel.asc
gpg --import altes-widerrufszertifikat.rev
gpg --armor --export C40F0FBA5C4CF71D7BEBB5C65478A4738FFEEB69 > alter-widerrufen.asc
```
`alter-widerrufen.asc` ebenfalls auf <https://keys.openpgp.org/upload> hochladen.

## 5. Der Strategie-Sitzung melden
Nur den **neuen Fingerabdruck** und den Pfad zu `release-signing-key.asc`. Das sind öffentliche Angaben. Sie zieht `fs-release`, `docs/en/programs/platform/releases.md` und die Notizen nach und löscht den Entwurf `capnp-compiler v0.1.1`.

## Für später
Neue Secrets erst setzen, wenn wirklich ein Release ansteht. Wer in ein Repo pushen darf, kann einen Workflow ändern und damit an dessen Secrets kommen, auch ein Agent. Vorher entscheiden wir, ob Releases von Hand signiert werden.
