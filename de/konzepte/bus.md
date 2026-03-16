# Message Bus

[← Zurück zum Index](../INDEX.md) | [Rollen](rollen.md) | [Rechte](rechte.md)

---

## Was der Bus macht

Der Bus ist die zentrale Kommunikationsschicht. Er verbindet alle Services, Bots, und Programme miteinander — ohne dass sie sich gegenseitig kennen müssen.

```
Service A sendet Event → Bus → Route → Service B, C, D empfangen
```

Kein Service weiß wer seine Events empfängt. Kein Empfänger weiß wer das Event gesendet hat (außer er schaut in die Metadaten).

## Produzenten (wer sendet)

Praktisch alles kann Events senden:
- Services (Kanidm, Forgejo, Outline, Vikunja, ...)
- Bots (Broadcast, Gatekeeper, ...)
- Benutzer-Aktionen (über Desktop)
- Timer/Cron
- Webhooks (extern)
- LLMs (Ollama, Claude)
- ERPs, CRMs, CI/CD, Monitoring — jedes Programm mit API

## Konsumenten (wer empfängt)

- Services (andere Services die auf Events reagieren)
- Bots (Nachrichten an Messenger weiterleiten)
- [Lenses](../programme/lenses/README.md) (Daten für Ansichten sammeln)
- [Search](../programme/search/README.md) (Index aktualisieren)
- [Tasks](tasks.md) (Automatisierungen auslösen)
- Desktop (Notifications anzeigen)
- Audit-Log (alles protokollieren)

## Routing

Events werden über Routing-Regeln weitergeleitet:
- Basierend auf Event-Typ
- Basierend auf Quelle
- Basierend auf Inhalt (Pattern-Matching)
- Transformation über Tera-Templates

## Rechte im Bus

Der Bus respektiert die [Rechte-Kaskade](rechte.md). Wenn ein Service nur `read` an die Föderation freigibt, können keine `write`-Events von der Föderation an diesen Service geroutet werden.

## Föderaler Bus

Innerhalb eines Projekts: Direkter Bus (WebSocket/In-Process).
Zwischen Projekten: Föderaler Bus (über API, gefiltert nach Rechten).
Zwischen Föderationen: Über den Auth-Broker der Föderation.

---

**Hinweis:** Dieses Dokument ist eine Vorbereitung. Die Details des Bus-Protokolls, Event-Formate, und die genaue Interaktion mit der Föderation müssen noch besprochen werden.

Weiter: [Tasks](tasks.md) | [Föderation](foederation.md)
