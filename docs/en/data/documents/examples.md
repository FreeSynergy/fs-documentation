# Documents – examples

## Own explanation beside a help text (original muted)

```json
{
  "@context": ["http://www.w3.org/ns/anno.jsonld", {"fs": "https://freesynergy.net/ns#"}],
  "type": "Annotation",
  "id": "https://<instance>/documents/018ebf91-ace0-7c11-9a20-5b2f0d3e4a71",
  "motivation": "fs:superseding",
  "body": {
    "type": "TextualBody",
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
