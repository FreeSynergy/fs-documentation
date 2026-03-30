# fs-crypto

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

`fs-crypto` ist das Kryptographie-Primitiv für FreeSynergy.
Es stellt alle kryptographischen Bausteine bereit: Verschlüsselung, Signierung,
Schlüsselableitung, Zertifikatsgenerierung und Token-Erstellung.

`fs-crypto` ist ein reines Library-Crate ohne Container oder Daemon.
Alle Algorithmen sind hinter dem `CryptoProvider`-Trait abstrahiert —
Code programmiert immer gegen das Interface, nie gegen konkrete Typen.

---

## Architektur

```
CryptoProvider        ← Trait: encrypt / decrypt / sign / verify / hash

AgeEncryptor          ← CryptoProvider  (age X25519 pubkey)
AgeDecryptor          ← CryptoProvider  (age X25519 privkey)
AgePassphraseEncryptor← CryptoProvider  (age scrypt passphrase)
AgePassphraseDecryptor← CryptoProvider  (age scrypt passphrase)

HmacProvider          ← CryptoProvider  (HMAC-SHA256, shared key)

FsSigningKey          ← CryptoProvider  (Ed25519 sign)
FsVerifyingKey        ← CryptoProvider  (Ed25519 verify)
PackageSignature      ← detached Ed25519 signature (64 bytes)

CaBundle              ← self-signed CA-Zertifikat (rcgen)
CertBundle            ← server / client PEM-Zertifikat

KeyGen                ← random_bytes / random_secret / random_hex / derive_key
JoinToken             ← Cluster-Join-Token (fsn1.<base64url>)
```

---

## Features (alle optional)

| Feature | Typ | Beschreibung |
|---|---|---|
| `age` | Verschlüsselung | age X25519 Public-Key + Passphrase (armored ASCII) |
| `hmac` | Authentifizierung | HMAC-SHA256, constant-time verify |
| `signing` | Signierung | Ed25519 Paket-Signierung + Verifikation (SHA-256 über Daten) |
| `mtls` | PKI | CA generieren, Server-/Client-Zertifikate ausstellen (rcgen) |
| `keygen` | Zufallsdaten | Zufallsbytes, Hex, Base64url, PBKDF2-HMAC-SHA256 |
| `tokens` | Tokens | `JoinToken` (fsn1-Format), `generate_recovery_token()` |

---

## `CryptoProvider`-Trait

```rust
pub trait CryptoProvider {
    fn encrypt(&self, plaintext: &[u8])            -> Result<Vec<u8>, FsError>;
    fn decrypt(&self, ciphertext: &[u8])           -> Result<Vec<u8>, FsError>;
    fn sign(&self, data: &[u8])                    -> Result<Vec<u8>, FsError>;
    fn verify(&self, data: &[u8], sig: &[u8])      -> Result<(), FsError>;
    fn hash(&self, data: &[u8])                    -> Result<Vec<u8>, FsError>;
}
```

Alle Methoden haben Default-Impls die `FsError::Internal("not supported")` zurückgeben.
Jeder Provider implementiert nur die für ihn sinnvollen Operationen.
Object-safe: `Box<dyn CryptoProvider>` funktioniert.

---

## Algorithmen

### age (Feature `age`)

- `AgeEncryptor` / `AgeDecryptor` — X25519 Public-Key-Verschlüsselung
- `AgePassphraseEncryptor` / `AgePassphraseDecryptor` — scrypt + ChaCha20-Poly1305
- Output: ASCII-armored age-Format
- Anwendung: `vault.toml` Secrets, Invite-Bundles in `fs-node`

```rust
let (pub_key, priv_key) = generate_age_keypair();
let ct = AgeEncryptor::from_public_key(&pub_key)?.encrypt(plaintext)?;
let pt = AgeDecryptor::from_private_key(&priv_key)?.decrypt(&ct)?;
```

### HMAC-SHA256 (Feature `hmac`)

- Shared-Key Message Authentication + Invite-Token-Signing
- Constant-time Verifikation (kein timing attack)
- Tag: 32 Bytes

```rust
let mac = HmacProvider::new(b"secret-key");
let tag = mac.sign_bytes(data);
mac.verify_bytes(data, &tag)?;
```

### Ed25519 (Feature `signing`)

- `FsSigningKey` / `FsVerifyingKey` — Ed25519 über SHA-256(data)
- `PackageSignature` — 64-Byte detached Signatur, hex-codiert
- Anwendung: Paket-Signierung im Store, chain-of-trust

```rust
let sk = FsSigningKey::generate();
let vk = sk.verifying_key();
let sig = sk.sign_package(data);
vk.verify_package(data, &sig)?;

// Keypair für store keygen:
let (sk_hex, vk_hex) = generate_keypair();
```

### mTLS (Feature `mtls`)

- `CaBundle::generate(cn, days)` — self-signed CA
- `ca.issue_server_cert(cn, san, days)` — Server-Zertifikat
- `ca.issue_client_cert(cn, days)` — Client-Zertifikat (mTLS)
- Output: PEM (rcgen 0.14)

### KeyGen (Feature `keygen`)

- `random_bytes(n)` — kryptographisch zufällig
- `random_secret(len)` — base64url-kodiert
- `random_hex(len)` — hex-kodiert
- `derive_key(password, salt, iter)` — PBKDF2-HMAC-SHA256, 32 Bytes

### JoinToken (Feature `tokens`)

- Format: `fsn1.<base64url(node_id|address|expires|nonce)>`
- `JoinToken::generate(node_id, address, ttl_secs)`
- `JoinToken::parse(token_str)` + `token.verify(expected_address)`
- `generate_recovery_token()` — 64-stelliger Hex-String

---

## Sicherheitshinweise

- Kein `unsafe`-Code
- `HmacProvider::verify_bytes` nutzt `hmac::Mac::verify_slice` (constant-time)
- age-Output ist immer ASCII-armored — keine Binär-Ciphertexts
- Ed25519 signiert über `SHA-256(data)`, nicht rohe Bytes
- Private Keys (`FsSigningKey`) niemals loggen oder serialisieren
- `AgePassphraseEncryptor` — Passphrase wird als `SecretString` gehalten

---

## Dependencies

| Crate | Feature | Zweck |
|---|---|---|
| `fs-error` | immer | Fehlertypen |
| `age` | `age` | age Encryption (X25519 + scrypt) |
| `hmac` + `sha2` | `hmac` | HMAC-SHA256 |
| `ed25519-dalek` + `sha2` | `signing` | Ed25519 + SHA-256 |
| `rcgen` + `time` | `mtls` | Zertifikatsgenerierung |
| `rand` + `pbkdf2` + `sha2` | `keygen` | Zufallsdaten + PBKDF2 |
| `rand` + `hex` | `tokens` | Token-Generierung |

---

## Repo

- Lokal: `/home/kal/Server/fs-libs/fs-crypto/`
- GitHub: `git@github.com:FreeSynergy/fs-libs.git` (Workspace-Member)
