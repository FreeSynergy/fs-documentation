# Adapter-Pattern

[← Zurück zum Index](../INDEX.md) | [Message Bus](bus.md) | [Rollen](rollen.md) | [Repository-Übersicht](../architektur/repositories.md)

---

## Das Problem (früher: Bridge)

FreeSynergy muss mit Diensten von Drittanbietern reden: kanidm für IAM, Stalwart für Mail, Forgejo für Git. Diese Dienste haben alle eigene APIs. Früher gab es dafür einen generischen "Bridge-Executor" der APIs dynamisch gemappt hat.

**Problem mit Bridge:** Dynamisches Mapping ist schwer zu testen, nicht typsicher, und erzeugt eine extra Komplexitätsschicht die niemand wirklich versteht.

---

## Die Lösung: Adapter-Pattern

Jede Rolle die FreeSynergy braucht bekommt einen **Standard-Trait**. Wer diesen Dienst bereitstellt, schreibt einen Adapter der diesen Trait implementiert.

```rust
// Standard-Trait — von FreeSynergy definiert
trait AuthService {
    async fn authenticate(&self, token: &str) -> Result<Claims>;
    async fn check_permission(&self, user: &str, action: &str) -> Result<bool>;
}

// Adapter für kanidm — implementiert den Standard-Trait
struct KanidmAdapter {
    base_url: String,
    client:   reqwest::Client,
}

impl AuthService for KanidmAdapter {
    async fn authenticate(&self, token: &str) -> Result<Claims> {
        // kanidm-spezifische HTTP-Calls
    }
    async fn check_permission(&self, user: &str, action: &str) -> Result<bool> {
        // kanidm-spezifische HTTP-Calls
    }
}
```

---

## Wie es zusammenspielt

```
Program braucht IAM
  → fragt fs-registry: "Wer bietet 'iam' an?"
  → Registry antwortet: "KanidmAdapter auf http://kanidm:8443"
  → Program ruft AuthService-Trait-Methode auf
  → KanidmAdapter übersetzt in kanidm-API
  → Ergebnis zurück
```

Kein generischer Dispatcher. Kein dynamisches Mapping. Typsicher.

---

## Wann ein Adapter, wann eigener Code?

| Situation | Lösung |
|---|---|
| Drittanbieter-Dienst der eine FS-Rolle erfüllt | Adapter schreiben |
| Eigener FS-Dienst | Trait direkt implementieren |
| Mehrere Dienste für dieselbe Rolle | Je ein Adapter, alle registrieren sich |
| Testen ohne echten Dienst | Mock-Adapter |

---

## Verbindung zur Registry

Adapters registrieren sich in `fs-registry` beim Start:

```rust
// Beim Start von kanidm-Adapter
registry.register(ServiceEntry::new(
    "kanidm",               // service_id
    "iam",                  // capability
    "http://kanidm:8443",   // endpoint
)).await?;
```

Beim Shutdown:
```rust
registry.deregister("kanidm").await?;
```

Programme fragen die Registry, nicht die Adapter direkt.

---

## Kein Bridge-Executor mehr

`fs-bridge` und `fs-bridge-sdk` sind entfernt (März 2026).

Der Bus routet direkt zu wer auch immer in der Registry für die benötigte
Capability registriert ist. Die Implementierung liegt im Adapter, nicht in
einer generischen Middleware.
