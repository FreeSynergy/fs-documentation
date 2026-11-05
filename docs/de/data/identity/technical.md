# Identität (Web of Trust) – Technische Erklärung

## Grundsatz (Regel 1, vorläufig)

Beglaubigungen sind **eigene Objekte**, keine Felder am Profil:

`Attestation = { attestierender Akteur, bezogener Akteur, Aussage (z. B. „hat Key K“, „ist Person P“), Schlüssel, Zeit, Treffens-Methode/-Ort (optional) }`

Das deckt sich mit Antons Modell („build reputation through attestations over time“, ✅ gesichtet 2026-11-02).

## Speicherperspektive

- **Tabelle `attestation`**: `id` (ULID), `subject` (wer beglaubigt, IRI), `object` (wen/was, IRI), `claim_type` (Enum, eigene Festlegung: `person_key`/`identity_encounter`/`vouching`), `key_ref` (`publicKey`-ID des Objects oder `did:key`), `method` (`qr-in-person`/`remote`/…), `attested_at`, `place` (optional, Referenz auf [geodata/](../geodata/index.md)), `signature_ref`.
- **Keine Vertrauenswerte in der Tabelle:** ein Score ist eine **Berechnung** über die Kette, nicht gespeichert (sonst veraltet er stumm).

## Fluss im Envelope (Beschluss 2)

1. Zwei Personen treffen sich, scannen QR (Muster aus Antons Projekt).
2. Client erzeugt Attestation → `Create` auf einem **AS2-`Relationship`**-Objekt (✅ Vokabular gelesen): `subject` = Beglaubigender, `relationship` = Aussage-Typ, `object` = Beglaubigter.
3. Empfänger-Instanzen speichern die Attestation unverändert; Signaturprüfung nach Schlüsselrecherche (⚠️/❌ — Signatur-Mechanismen für ActivityPub sind bei uns noch **nicht belegt**, alte Referenz war 404; Antons Stack nutzt Ed25519/JWS als Indiz).

## Mapping-Skizze auf Antons WoT Spec (✅-Fakten aus standards.md; `mapping.md` noch offen)

| Stuck bei Anton | Bei uns |
|-----------------|---------|
| Attestation (Kernobjekt der WoT Spec) | AS2-`Relationship` + eigene Felder (`claim_type`, `method`) |
| `did:key` (Ed25519) | `publicKey` am Actor ↔ `cryptoKeys` in der Contact-Card |
| `wot-profiles` (JWS-signierte Profilveröffentlichung) | [profile/](../profile/index.md)-Projektion + Signatur (⚠️ Mechanismus offen) |
| UCAN-inspirierte Fähigkeiten | Autorisierungs-Schicht (Envelope/Instanz), nicht Datenmodell |
| RLTP (Gen 3) | beobachten; Migration folgt Gen 3 |

## Offene technische Punkte

- `identity/mapping.md` als eigene Datei erstellen (Auftrag aus [requirements.md §7](../requirements.md))
- Signatur-Mechanismus-Recherche (welcher ist real belegt?) — vor jeder Implementierung
- Vertrauensketten-Fragen (Tiefe, Verfallsfristen) als API, nicht als Schema
