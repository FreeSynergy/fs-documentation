# Container Manager — Der Container-App-Verwalter

> **Hinweis:** Früher als zwei getrennte Programme bekannt (Container Manager + Builder). Jetzt vereint in einem Programm mit den Bereichen: Installed, Install New, Build & Publish, Logs.

[← Zurück zum Index](../../INDEX.md) | [Node](../node/README.md) | [Store](../store/README.md) | [Manager](../../konzepte/manager.md)

---

## Was der Container Manager macht

Der Container Manager nimmt eine YAML-Datei (Docker-Compose, Podman, oder eigenes Format) und verwandelt sie in einen laufenden, konfigurierten Service.

## Eigenständigkeit

Der Container Manager läuft **komplett alleine** — ohne Node, ohne Store, ohne Internet. Man gibt ihm eine YAML-Datei und er:
1. Parst sie
2. Analysiert sie
3. Generiert Quadlet-Dateien
4. Startet den Service

Wenn der Store verfügbar ist, nutzt er ihn für bessere Analyse (siehe unten). Aber er BRAUCHT ihn nicht.

## Der Analyse-Prozess

### Schritt 1: YAML parsen

```
Eingabe: docker-compose.yml oder Podman-YAML
  → Services extrahieren
  → Subcontainer/Subservices erkennen (gehören alle zum selben Paket)
  → Volumes, Networks, Ports extrahieren
  → Environment-Variablen extrahieren
```

### Schritt 2: Validierung (Dry-Run)

| Prüfung | Ergebnis |
|---|---|
| YAML-Syntax korrekt? | ✅ OK / ❌ Fehler mit Zeilennummer |
| Healthcheck vorhanden? | ✅ Vorhanden / ⚠️ Warnung: kein Healthcheck |
| Netzwerke korrekt? | ✅ OK / ⚠️ Netzwerk angelegt aber nicht benutzt |
| Port-Konflikte? | ✅ OK / ❌ Port 8443 schon von Service X belegt |
| Image erreichbar? | ✅ OK / ⚠️ Konnte Image nicht prüfen (offline) |

### Schritt 3: Variablen-Analyse

Jede Environment-Variable wird analysiert. Der Container Manager erkennt Typen anhand von **Schlüsselwörtern im Variablennamen**:

| Muster im Namen | Erkannter Basis-Typ | Erkannte Rolle |
|---|---|---|
| `*_HOST`, `*_HOSTNAME` | `hostname` | Abhängig vom Kontext |
| `*_URL`, `*_URI`, `*_ENDPOINT` | `url` | Abhängig vom Kontext |
| `*_PORT` | `port` | Abhängig vom Kontext |
| `*_PASSWORD`, `*_PASS`, `*_SECRET` | `secret` | Abhängig vom Kontext |
| `*_KEY`, `*_TOKEN`, `*_API_KEY` | `secret` | Abhängig vom Kontext |
| `*_USER`, `*_USERNAME` | `string` | Abhängig vom Kontext |
| `*_EMAIL`, `*_MAIL_FROM` | `email` | - |
| `*_DB`, `*_DATABASE` | `connection-string` | `database` |

**Rollen-Erkennung über Kontext-Wörter:**

| Wörter im Namen | Erkannte Ober-Rolle | Mögliche Unter-Rollen |
|---|---|---|
| `POSTGRES`, `PG`, `PGSQL` | `database` | `database.postgres` |
| `MYSQL`, `MARIADB` | `database` | `database.mysql` / `database.mariadb` |
| `MONGO`, `MONGODB` | `database` | `database.mongodb` |
| `REDIS` | `cache` | `cache.redis` |
| `DRAGONFLY` | `cache` | `cache.dragonfly` |
| `MEMCACHE`, `MEMCACHED` | `cache` | `cache.memcached` |
| `VALKEY` | `cache` | `cache.valkey` |
| `KEYDB` | `cache` | `cache.keydb` |
| `SMTP`, `MAIL` | `smtp` | `smtp.sender` / `smtp.receiver` |
| `OAUTH`, `OIDC`, `AUTH`, `SSO` | `iam` | `iam.oidc-provider` |
| `LDAP` | `iam` | `iam.ldap` |
| `S3`, `MINIO`, `STORAGE` | `storage` | `storage.s3` |

**Wichtig:** Die Erkennung ist eine **Wahrscheinlichkeits-Einschätzung**, keine Garantie. Der Container Manager gibt Konfidenz an:

```
SMTP_HOST → hostname, Rolle: smtp.host (Konfidenz: 95%)
DB_URL → connection-string, Rolle: database (Konfidenz: 80%, Unterrolle unklar)
CACHE_BACKEND → string, Rolle: cache (Konfidenz: 60%, könnte auch was anderes sein)
```

### Schritt 4: YAML → Quadlet + Config

Aus der analysierten YAML werden generiert:
- **Quadlet `.container`-Datei** (für systemd/Podman)
- **Config-Templates** (Tera-Dateien für service-spezifische Konfiguration)
- **manifest.toml** (Paket-Manifest mit allen Metadaten)

### Schritt 5: Store-Integration (optional)

Wenn der Store erreichbar ist:
1. Container Manager fragt: "Gibt es `kanidm/server` im Store?"
2. Store antwortet: "Ja, hier sind bekannte Variablen, Rollen, Beschreibungen, Icon"
3. Container Manager **ergänzt** seine Analyse — überschreibt NICHTS, füllt nur Lücken
4. Bei Konflikten: Fragt den Benutzer

### Schritt 6: Speicherung + Inventory-Eintrag

Nach erfolgreichem Deploy:
- Quadlet-Dateien + Config-Templates: `services/{paketname}/`
- **Inventory-Eintrag schreiben** (via `fsn-inventory`):
  - `InstalledResource` (id, resource_type, version, status: Active)
  - `ServiceInstance` (name, roles_provided, port, network)
- Status-Updates bei start/stop/error → `Inventory::update_status()`

Der Paketname = Hauptservice-Name aus der YAML.

**Das Inventory ist danach die einzige Wahrheit.** Das UI zeigt nur, was im Inventory steht. Kein anderes System darf eine eigene Liste führen.

## Interfaces

| Interface | Beispiel |
|---|---|
| CLI | `fsn container-app analyze compose.yml` |
| CLI | `fsn container-app install compose.yml` |
| CLI | `fsn container-app status kanidm` |
| CLI | `fsn container-app start kanidm` / `stop` / `restart` |
| API | `POST /api/container-app/analyze` mit YAML-Body |
| UI | Container Manager-View im [Desktop](../desktop/README.md) |

## Podman: KEIN Socket

Der Container Manager nutzt **keinen Podman-Socket**. Container werden ausschließlich verwaltet über:
- **Quadlet-Dateien** (`.container` → systemd-Generator)
- **systemctl** (start, stop, status, restart)
- **journalctl** (Logs)

## Build & Publish (früher: Builder)

Der Builder ist jetzt direkt im Container Manager integriert.
Im Bereich "Build & Publish" kannst du:
1. Eine docker-compose.yml einfügen
2. Analysieren lassen (Variablen, Rollen, Healthchecks)
3. Direkt in den Store veröffentlichen

Das separate Builder-Programm gibt es nicht mehr.

## Architektur

| Modul | Zweck |
|---|---|
| `app.rs` | `ContainerApp` — Dioxus Root-Komponente, Sidebar + Detail-Ansicht |
| `status.rs` | `UnitActiveStateDisplay` — Extension-Trait für Status-Anzeige |

## Repo

`git@github.com:FreeSynergy/fs-container-app.git`

## Bibliotheken

| Crate | Zweck |
|---|---|
| `fs-container` | Container-Abstraktion (Bollard/Docker API) |
| `fs-components` | Wiederverwendbare UI-Komponenten |
| `fs-i18n` | Lokalisierte Texte |
| `fs-error` | Fehlerbehandlung |

## Beziehung Store / Inventory / Container Manager

```
Store (Was gibt es?)
  → Container Manager (Wie wird es installiert/betrieben?)
    → Inventory (Was ist installiert + Status?)
      → UI (Zeigt nur Inventory-Inhalte)
```

- Store: Liefert Metadaten, Rollen, Variablen, Compose-YAML
- Container Manager: Analysiert, deployt, konfiguriert, überwacht
- Inventory: Empfängt den fertigen Zustand — wird vom Container Manager geschrieben
- UI: Zeigt ausschließlich Inventory-Inhalte. Grüner Punkt = läuft, Ausgegraut = gestoppt, Roter Punkt = Fehler

---

Weiter: [Store](../store/README.md) | [Inventory](../../konzepte/inventory.md) | [Rollen](../../konzepte/rollen.md)
