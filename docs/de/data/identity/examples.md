# Identität (Web of Trust) – Beispiele

Die AS2-Felder (`Relationship`, `subject`, `relationship`, `object`, `publicKey`) sind ✅ im Vokabular geprüft. Die Ergänzungen (`claim_type`, `method`, `attestedAt`) sind **unsere eigene Entscheidung (zur Diskussion offen)** und sollen als Erweiterung des Umschlags gelten.

## 1. Bestätigung nach einem persönlichen Treffen (QR-Scan) — `Create` auf `Relationship`

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "actor": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
  "object": {
    "type": "Relationship",
    "id": "https://<instance>/identity/018ebf91-aced-7d05-a2ed-13260da0f017",
    "subject": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
    "relationship": "fs:person_key",
    "object": "https://other.example/profile/01HTZS6H8L3C7N9X2B5D8F4K1M",
    "fs:attestedAt": "2026-11-01T18:30:00Z",
    "fs:method": "qr-in-person",
    "fs:keyRef": "did:key:z6Mk...example..."
  }
}
```

> Das Präfix `fs:` ist unsere Erweiterung, bis die WoT-Spezifikation / RLTP Feldnamen liefert. Die Form `did:key` stammt aus Antons Stack (✅ geprüft; die Bedeutung der Felder ist ⚠️ noch nicht Feld für Feld belegt).

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

(Der Schlüsselwert selbst folgt dem Signaturverfahren, das noch zu belegen ist — deshalb fehlt hier `publicKeyPem`.)

## 3. Vertrauensfrage als API, nicht als Feld (Regel: kein Wert im Speicher)

```json
{
  "query": {
    "from": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
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

## 4. Abgrenzung: was hier **falsch** wäre

❌ Ein Feld `trustworthy: true` am Profil — verletzt Regel 1: Vertrauen ist eine **Aussage eines anderen Akteurs**, kein Attribut der Person.
