# Kontaktdaten – Beispiele

Alle Feldnamen stammen aus der ✅ geprüften JSContact-Feldliste in [standards.md → Kontakte](../standards.md).

## 1. Person als JSContact-`Card` (kanonischer Speicher)

```json
{
  "@type": "Card",
  "version": 1,
  "uid": "01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "name": {
    "components": [
      { "kind": "given", "value": "Anna" },
      { "kind": "surname", "value": "Weber" }
    ],
    "isOrdered": true
  },
  "nicknames": ["awi"],
  "emails": [
    { "type": "home", "value": "anna@example.org" }
  ],
  "phones": [
    { "type": "cell", "value": "+49 30 123456" }
  ],
  "addresses": {
    "home": {
      "components": [
        { "kind": "locality", "value": "Berlin" },
        { "kind": "postcode", "value": "10115" },
        { "kind": "country", "value": "DE" }
      ]
    }
  },
  "keywords": ["Vorstand"],
  "notes": [
    { "type": "info", "value": "Bevorzugt E-Mail statt Telefon." }
  ]
}
```

## 2. Name mit Komponenten — warum kein `firstName`

Spanischer Name mit zwei Suffixen bleibt korrekt abbildbar:

```json
{
  "@type": "Name",
  "components": [
    { "kind": "given", "value": "María" },
    { "kind": "given2", "value": "José" },
    { "kind": "surname", "value": "García" },
    { "kind": "surname2", "value": "López" }
  ],
  "isOrdered": true
}
```

## 3. Verlustfreier Export als vCard 4.0 (RFC 6350, ✅)

```
BEGIN:VCARD
VERSION:4.0
UID:01HTZK5C8R4M6YQ2N9XGZ7TQ1A
FN:Anna Weber
N:Weber;Anna;;;
NICKNAME:awi
EMAIL;TYPE=home:anna@example.org
TEL;TYPE=cell:+4930123456
ADR;TYPE=home:;;10115 Berlin;Berlin;;DE
END:VCARD
```

## 4. Teiländerung über das JSContact-Patch-Muster (RFC 9553 + RFC 6902, ✅)

```json
{
  "@type": "PatchObject",
  "action": "replace",
  "path": "/phones/0/value",
  "value": "+49 170 999999"
}
```

## 5. `lifecycle` als Erweiterung (eigene Festlegung, zur Diskussion — ⚠️ `extensions`-Mechanismus noch belegen)

```json
{
  "extensions": {
    "fs": { "lifecycle": "customer" }
  }
}
```
