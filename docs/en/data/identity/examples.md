# Identity (Web of Trust) – examples

The AS2 fields (`Relationship`, `subject`, `relationship`, `object`, `publicKey`) are ✅ vocabulary-verified. The additions (`claim_type`, `method`, `attestedAt`) are **our own decision (open for discussion)** and are meant as an extension to the envelope.

## 1. Attestation after a personal meeting (QR scan) — `Create` on `Relationship`

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "actor": "https://<instance>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "object": {
    "type": "Relationship",
    "id": "https://<instance>/identity/01HTZS3B7D9M2P5V8K4R6T1W0Q",
    "subject": "https://<instance>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
    "relationship": "fs:person_key",
    "object": "https://other.example/profile/01HTZS6H8L3C7N9X2B5D8F4K1M",
    "fs:attestedAt": "2026-11-01T18:30:00Z",
    "fs:method": "qr-in-person",
    "fs:keyRef": "did:key:z6Mk...example..."
  }
}
```

> `fs:` prefix = our extension, until the WoT spec / RLTP supplies field names. The `did:key` form comes from Anton's stack (✅ reviewed; field meaning ⚠️ not yet evidenced field by field).

## 2. Key on the actor (AS2 `publicKey`, ✅)

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

(The key value itself follows the signature mechanism that is still to be evidenced — which is why `publicKeyPem` is missing here.)

## 3. Trust question as an API, not as a field (rule: no score in storage)

```json
{
  "query": {
    "from": "https://<instance>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
    "about": "https://other.example/profile/01HTZS6H8L3C7N9X2B5D8F4K1M",
    "claim": "person_key"
  },
  "answer": {
    "paths": 3,
    "strongestChain": ["<instance>/profile/01HTZK5C8R...", "partner.example/profile/01HTZS9..."],
    "note": "Computed — not stored."
  }
}
```

## 4. Differentiation: what would be **wrong** here

❌ A field `trustworthy: true` on the profile — violates rule 1: trust is a **statement of another actor**, not an attribute of the person.
