# Identität (Web of Trust) – Beispiele

AS2-Felder (`Relationship`, `subject`, `relationship`, `object`, `publicKey`) sind ✅ Vokabular-geprüft. Die Ergänzungen (`claim_type`, `method`, `attestedAt`) sind **eigene Festlegung (zur Diskussion)** und als Erweiterung zum Envelope gedacht.

## 1. Beglaubigung nach persönlichem Treffen (QR-Scan) — `Create` auf `Relationship`

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "actor": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "object": {
    "type": "Relationship",
    "id": "https://<instanz>/identity/01HTZS3B7D9M2P5V8K4R6T1W0Q",
    "subject": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
    "relationship": "fs:person_key",
    "object": "https://other.example/profile/01HTZS6H8L3C7N9X2B5D8F4K1M",
    "fs:attestedAt": "2026-11-01T18:30:00Z",
    "fs:method": "qr-in-person",
    "fs:keyRef": "did:key:z6Mk...beispiel..."
  }
}
```

> `fs:`-Präfix = unsere Erweiterung, bis die WoT Spec / RLTP Feldnamen liefert. `did:key`-Form aus Antons Stack (✅ gesichtet; Feldbedeutung ⚠️ noch nicht feldgenau belegt).

## 2. Schlüssel am Akteur (AS2 `publicKey`, ✅)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Person",
  "id": "https://other.example/profile/01HTZS6H8L3C7N9X2B5D8F4K1M",
  "preferredUsername": "ben",
  "publicKey": {
    "id": "https://other.example/profile/01HTZS6H8L3C7N9X2B5D8F4K1M#mainKey",
    "owner": "https://other.example/profile/01HTZS6H8L3C7N9X2B5D8F4K1M"
  }
}
```

(Der Schlüsselwert selbst folgt dem noch zu belegenden Signatur-Mechanismus — deshalb hier ohne `publicKeyPem`.)

## 3. Vertrauensfrage als API, nicht als Feld (Regel: kein Score im Speicher)

```json
{
  "query": {
    "from": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
    "about": "https://other.example/profile/01HTZS6H8L3C7N9X2B5D8F4K1M",
    "claim": "person_key"
  },
  "answer": {
    "paths": 3,
    "strongestChain": ["<instanz>/profile/01HTZK5C8R...", "partner.example/profile/01HTZS9..."],
    "note": "Berechnet — nicht gespeichert."
  }
}
```

## 4. Abgrenzung: Was hier **falsch** wäre

❌ Ein Feld `vertrauenswuerdig: true` am Profil — verstößt gegen Regel 1: Vertrauen ist eine **Aussage eines anderen Akteurs**, kein Attribut der Person.
