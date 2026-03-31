# Event-Driven Services

[← Zurück zum Index](../INDEX.md) | [Message Bus](bus.md) | [Bus-API Namespaces](bus-api-namespaces.md)

---

## Grundprinzip

FreeSynergy-Services kommunizieren **nicht** über direkte Aufrufe, sondern über Events.
Ein Service publiziert ein Ereignis — alle Interessenten reagieren darauf. Kein Service
muss wissen, wer auf seine Events hört.

```
Kein direkter Aufruf:  service_a.notify(service_b, "new_package")  ✗
Richtig:               bus.publish("inventory::package::installed", event).await?  ✓
```

Dies entspricht dem **Observer Pattern** auf Bus-Ebene.

---

## Die vier Kern-Services

### fs-registry — Service-Registry

**Rolle:** Hält den globalen Zustand aller laufenden Services und ihrer Capabilities.

**Betriebsweise:** Eigenständiger gRPC-Server (läuft immer).

| Aktion | Mechanismus |
|---|---|
| Service startet | publiziert `registry::service::registered` |
| Service stoppt | publiziert `registry::service::stopped` |
| Capability hinzugefügt | publiziert `registry::capability::added` |
| Capability entfernt | publiziert `registry::capability::removed` |
| Andere fragen Registry | gRPC-Call: `lookup_capability("db.engine.*")` |

`fs-registry` selbst subscribed auf diese Events und aktualisiert seinen internen State.
Alle anderen Services fragen `fs-registry` via gRPC — nie direkt andere Services.

---

### fs-inventory — Paket-Inventar

**Rolle:** Hält fest, was auf diesem Node installiert ist.

**Betriebsweise:** Leichter gRPC-Server + Bus-Subscriber.

| Event (subscribed) | Reaktion |
|---|---|
| `inventory::package::installed` | Eintrag in lokale DB speichern |
| `inventory::package::removed` | Eintrag aus DB löschen |
| `inventory::package::updated` | Eintrag aktualisieren |

Wer publiziert diese Events? Der Store (`fs-store`) nach einer erfolgreichen
Installation — `fs-inventory` ist nur Konsument, nie Initiator.

**Abfragen:** gRPC — `list_installed()`, `get_package("kanidm")`, `is_installed("forgejo")`.

---

### fs-session — Session-Management

**Rolle:** Weiß, welcher User eingeloggt ist und welche Apps offen sind.

**Betriebsweise:** Leichter gRPC-Server + Bus-Subscriber.

| Event (subscribed) | Reaktion |
|---|---|
| `session::user::login` | Session anlegen, User-Kontext setzen |
| `session::user::logout` | Session beenden, Apps schließen |
| `session::app::opened` | App zur offenen-Apps-Liste hinzufügen |
| `session::app::closed` | App aus offenen-Apps-Liste entfernen |

Wer publiziert? `fs-auth` publiziert Login/Logout — `fs-desktop` publiziert App-Events.

**Abfragen:** gRPC — `current_user()`, `open_apps()`, `session_info()`.

---

### fs-info — System-Informationen

**Rolle:** Liefert aktuelle Hardware-Metriken (CPU, RAM, Disk, Netzwerk).

**Betriebsweise:** On-demand gRPC-Server — **kein Bus-Subscriber**.

Warum kein Event-Subscriber? System-Metriken ändern sich kontinuierlich — es gibt
kein sinnvolles "etwas ist passiert"-Event. Stattdessen: direkte gRPC-Abfrage.

`fs-info` **publiziert** jedoch bei Schwellwert-Überschreitungen:

| Bedingung | Event |
|---|---|
| RAM > 90% | `system::health::degraded` |
| Disk > 95% | `system::health::degraded` |
| CPU > 95% (dauerhaft) | `system::health::degraded` |
| Wieder normal | `system::health::restored` |

**Abfragen:** gRPC — `system_info()`, `cpu_usage()`, `memory_info()`, `disk_info()`.

---

## Architektur-Überblick

```
fs-auth          fs-store        fs-desktop
    │                │               │
    │ login/logout   │ installed/     │ app opened/
    │ events         │ removed events │ closed events
    └────────────────┴───────────────┘
                     │
                  fs-bus
                     │
        ┌────────────┼────────────┐
        │            │            │
   fs-registry  fs-inventory  fs-session
   (subscribed) (subscribed)  (subscribed)
        │
   (gRPC-Queries von allen Services)
```

---

## Event vs. gRPC-Query — Entscheidungsregel

| Situation | Mechanismus |
|---|---|
| Etwas ist passiert (Zustandsänderung) | Bus-Event publizieren |
| Ich brauche den aktuellen Stand | gRPC-Query |
| Regelmäßige Metriken abrufen | gRPC-Query (kein Polling via Events) |
| Ich will auf Änderungen reagieren | Bus-Event subscriben |

**Niemals:** Polling via Events (Bus ist kein Ticker). Für Metriken → gRPC on-demand.

---

## Startup-Reihenfolge

Services starten in dieser Reihenfolge:

```
1. fs-bus        — Bus muss zuerst laufen
2. fs-registry   — registriert sich selbst, wartet auf andere
3. fs-auth       — meldet sich bei Registry an
4. fs-inventory  — subscribed auf package-Events
5. fs-session    — subscribed auf user/app-Events
6. fs-info       — registriert sich, startet Alerting
7. alle anderen  — fragen Registry nach Capabilities
```

---

Weiter: [Message Bus](bus.md) | [Bus-API Namespaces](bus-api-namespaces.md) | [Registry](registry.md) | [Inventory](inventory.md) | [Session](session.md)
