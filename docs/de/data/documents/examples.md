# Dokumente – Beispiele

## Markierung auf einer Spanne: eigene Erklärung ersetzt das Original (leiser gestellt, ADR 0033)

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

Wird sie rückgängig gemacht (`Undo` auf der Annotation), erscheint der Originalsatz wieder.

## Markierung auf einem Punkt: Variable (Serienbrief)

Ein Punkt-Anker (Position ohne Länge) mit `fs:name` = `recipient.name` und `fs:type` = `contact`
fügt den Wert dort ein; derselbe Text kann für viele Empfänger ausgefüllt werden.

> Der Motivationsbegriff `fs:marking` ist ein Arbeitsname — das finale Vokabular ist Teil der Markierungs-Spec.
