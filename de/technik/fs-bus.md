# fs-bus

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

`fs-bus` ist der asynchrone Event-Bus für FreeSynergy.
Er bietet Topic-Routing, Retry mit Backoff, Subscriptions, Standing Orders,
konfigurierbare Routing-Regeln und optionales Bus-zu-Bus-Bridging.

---

## Architektur

```
Producer → BusMessage → MessageBus → Router → [TopicHandler, BusBridge, …]
                                   ↓
                         SubscriptionManager (role → topic filter)
                                   ↓
                         StandingOrdersEngine (persistent triggers)
                                   ↓
                         RoutingConfig (TOML rules → delivery + storage)
```

---

## Kern-Typen

| Typ / Trait              | Beschreibung                                            |
|--------------------------|---------------------------------------------------------|
| `MessageBus`             | Kern-Bus: publish, subscribe, routing                   |
| `BusMessage` / `Event`   | Nachrichten-Envelope mit Metadaten                      |
| `TopicHandler`-Trait     | Empfänger für bestimmte Topic-Muster                    |
| `Router` / `RoutingRule` | Topic-Routing-Regeln (TOML-konfigurierbar)              |
| `Subscription`           | Rollenbasierte Topic-Subscriptions                      |
| `StandingOrder`          | Persistente Trigger-Regeln                              |
| `EventBuffer`            | Gepufferter Versand mit Retry                           |
| `RetryPolicy`            | Strategy Pattern: exponential / fixed / none            |
| `Transform`-Trait        | Nachrichten-Transformation (Chain of Responsibility)    |
| `BusBridge` (feature)    | HTTP Bus-zu-Bus-Weiterleitung                           |
| `TeraTransform` (feature)| Tera-Template-basierte Transformation                   |

---

## Topic-Format

```
{domain}.{action}.{qualifier}

Beispiele:
  installer.package.installed   — Paket wurde installiert
  service.started               — Service wurde gestartet
  config.changed.fs-store       — Konfiguration von fs-store geändert
  auth.login                    — Nutzer eingeloggt
```

---

## Features (Cargo)

| Feature          | Aktiviert                              |
|------------------|----------------------------------------|
| `bridge`         | `BusBridge` für HTTP-Forwarding        |
| `tera-transform` | `TeraTransform` für Template-Transforms|

---

## Integration Tests

| Test          | Was wird geprüft                                              |
|---------------|---------------------------------------------------------------|
| `bus_wiring`  | Inventory + Registry reagieren auf Bus-Events                 |
| `e2e_install` | Komplette Install-Chain: Store → Bus → Inventory → Registry  |

---

## Repo

- Lokal: `/home/kal/Server/fs-bus/`
- GitHub: `git@github.com:FreeSynergy/fs-bus.git`

---

Weiter: [fs-config](fs-config.md) | [← Index](../INDEX.md)
