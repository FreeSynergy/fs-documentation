# Registry

[← Zurück zum Index](../INDEX.md) | [Session](session.md) | [Adapter-Pattern](adapter.md) | [Repository-Übersicht](../architektur/repositories.md)

---

## Was ist die Registry?

Die **Registry** beantwortet die Frage: *"Welche Dienste sind gerade auf diesem Node aktiv und erreichbar?"*

Sie ist das Verzeichnis aller laufenden Service-Capabilities. Der Bus und andere Programme schauen in die Registry wenn sie wissen müssen, wer eine bestimmte Aufgabe erledigen kann.

**Repository:** `FreeSynergy/fs-registry`

---

## Konzept: Capability

Eine **Capability** ist eine benannte Fähigkeit die ein Dienst anbietet:

| Capability | Bedeutung | Beispiel-Dienst |
|---|---|---|
| `iam` | Identity & Access Management | kanidm |
| `mail` | E-Mail senden/empfangen | Stalwart |
| `git` | Git-Repositories verwalten | Forgejo |
| `storage` | Objekt-Speicher | fs-node (S3) |
| `matrix` | Matrix-Messaging | tuwunel |

---

## Ablauf

```
1. Dienst startet → registriert sich:
   registry.register(ServiceEntry::new("kanidm", "iam", "http://kanidm:8443"))

2. Programm braucht IAM:
   let services = registry.by_capability("iam").await?;
   // → [ServiceEntry { service_id: "kanidm", endpoint: "http://kanidm:8443", status: Up }]

3. Programm nutzt den Adapter:
   let adapter = KanidmAdapter::new(&services[0].endpoint);
   adapter.authenticate(token).await?

4. Dienst stoppt → deregistriert sich:
   registry.deregister("kanidm").await?;
```

---

## Verbindung zum Adapter-Pattern

Registry und Adapter arbeiten zusammen:
- Die Registry weiß *wo* ein Dienst läuft (Endpoint)
- Der Adapter weiß *wie* man mit ihm redet (API)

Der Bus schaut in die Registry, wählt den passenden Eintrag, und übergibt an den Adapter.

Details: [Adapter-Pattern](adapter.md)

---

## Abgrenzung zu fs-inventory

| | Registry | Inventory |
|---|---|---|
| Frage | Wer läuft gerade? | Was ist installiert? |
| Daten | Laufende Dienste + Endpoints | Installierte Ressourcen + Versionen |
| Lebensdauer | Start bis Stop des Dienstes | Persistent auf dem Node |
| Schreibt wer? | Dienst selbst (on start/stop) | Package Manager |
