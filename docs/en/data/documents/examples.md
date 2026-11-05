# Documents – examples

## Mark on a range: own explanation replaces the original (muted, ADR 0033)

```json
{
  "@context": ["http://www.w3.org/ns/anno.jsonld", {"fs": "https://freesynergy.net/ns#"}],
  "type": "Annotation",
  "id": "https://<instance>/documents/018ebf91-ace0-7c11-9a20-5b2f0d3e4a71",
  "motivation": "fs:marking",
  "body": {
    "type": "TextualBody",
    "fs:name": "vault-hint",
    "fs:type": "explanation",
    "format": "text/markdown",
    "value": "In our club we always use the shared key in the vault — see screenshot."
  },
  "target": {
    "source": "https://<instance>/documents/018ebf91-ac10-7a02-8c11-1f2e3d4c5b6a",
    "selector": {"type": "TextQuoteSelector", "exact": "Import your key with the key manager."}
  }
}
```

Undoing it (`Undo` on the annotation) shows the original sentence again.

## Mark on a point: variable (mail merge)

A point anchor (position without length) with `fs:name` = `recipient.name` and `fs:type` = `contact`
inserts the value there; the same text can be filled for many recipients.

> The motivation term `fs:marking` is a working name — final vocabulary is part of the marking spec.
