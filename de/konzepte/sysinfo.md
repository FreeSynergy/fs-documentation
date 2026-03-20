# System-Information (SysInfo)

[← Zurück zum Index](../INDEX.md) | [Pakete](pakete.md) | [Node-Plattformen](node-plattformen.md)

---

## Wozu SysInfo?

Damit der Store bei der Installation weiß was auf dem aktuellen System verfügbar ist — und damit Pakete deklarieren können, was sie voraussetzen.

Beispiele:
- Kanidm braucht PAM → PAM gibt es auf Linux und macOS, nicht auf Windows → Installation zeigt das PAM-Feature nur wenn PAM vorhanden ist
- Ein Dienst will als systemd-Service registriert werden → Häkchen nur anzeigen wenn systemd läuft
- Auf macOS gibt es launchd → Häkchen für launchd-Service
- Auf Windows gibt es Windows Services → Häkchen für Windows-Dienst
- "Git fehlt" → Store kann Init nicht fortsetzen, warnt den Nutzer

SysInfo ist kein Daemon der alles ständig pollt. Es ist ein **intelligenter, fauler Auskunftgeber** — Daten werden nur gelesen wenn sie gebraucht werden, und gecacht wenn sie sich selten ändern.

---

## Drei Schichten

### Schicht 1 — Statische Daten (einmalig lesen, langzeitig cachen)

Daten die sich nur ändern wenn das System geändert wird. Werden beim ersten Bedarf gelesen und in `~/.config/fsn/sysinfo.toml` gecacht (Invalidierung: manuell oder nach 24h).

```
OS + Typ           → Linux, macOS, Windows
OS-Version         → Fedora 43, Ubuntu 24.04, macOS 14.x, Windows 11
Architektur        → x86_64, aarch64, arm7
Verfügbare Features:
  systemd          → ja/nein
  PAM              → ja (Linux/macOS) / nein (Windows)
  launchd          → ja (macOS) / nein
  Windows Services → ja (Windows) / nein
  Podman           → ja/nein + Version
  Docker           → ja/nein + Version
  Podman Quadlet   → ja/nein (benötigt systemd)
  Git              → ja/nein + Version
  SSH (ed25519)    → ja/nein
```

### Schicht 2 — Dynamische Daten (nur auf Anfrage lesen)

Daten die sich ständig ändern. Werden NUR gelesen wenn ein Widget, eine Installation oder ein CLI-Befehl danach fragt. Keine Hintergrund-Schleife.

```
Festplatten:       belegt / frei pro Partition
RAM:               belegt / frei
CPU-Temperatur:    aktuell (wenn verfügbar)
SMART-Status:      pro Laufwerk (wenn verfügbar)
Batterie:          Ladezustand, Ladezeit (Laptops)
```

### Schicht 3 — Alerting (konfigurierbar in Settings)

Schwellenwerte die der Nutzer in den Einstellungen festlegen kann. SysInfo überprüft diese periodisch (konfigurierbares Intervall, Standard: alle 5 Minuten) und sendet bei Überschreitung ein Event auf den **Message Bus**.

```
Thresholds (Beispiele):
  Festplatte > 90% voll          → sysinfo.alert.disk.full
  CPU-Temperatur > 80°C          → sysinfo.alert.cpu.hot
  SMART-Fehler erkannt           → sysinfo.alert.disk.smart
  RAM > 95% belegt               → sysinfo.alert.memory.full
```

**Die Benachrichtigung geht über den Bus** — Desktop empfängt sie und zeigt eine Notification. Widget empfängt sie und aktualisiert sich. Nie direkt, immer über Rollen.

---

## Platform-Feature-Tags in Paketen

Pakete deklarieren Platform-Anforderungen als Tags im Manifest:

```toml
[package]
tags = ["iam", "oidc", "pam", "requires:pam", "requires:systemd", "platform:linux"]
```

**Standard-Tags für Platform-Features:**

| Tag | Bedeutung |
|---|---|
| `platform:linux` | Nur Linux unterstützt |
| `platform:macos` | Nur macOS unterstützt |
| `platform:windows` | Nur Windows unterstützt |
| `platform:linux+macos` | Linux und macOS, kein Windows |
| `requires:systemd` | Systemd muss laufen |
| `requires:pam` | PAM muss verfügbar sein |
| `requires:podman` | Podman muss installiert sein |
| `requires:git` | Git muss installiert sein |

**Was der Store damit macht:**

1. SysInfo liefert: "Wir sind auf Windows, kein PAM, kein systemd"
2. Paket hat Tag `requires:pam`
3. Store: Feature wird ausgegraut + Info-Text: "PAM nicht verfügbar auf diesem System"
4. Paket hat Tag `platform:linux`
5. Store: Paket wird mit Badge ⚠️ angezeigt: "Nur auf Linux"

Die Pakete werden trotzdem angezeigt — der Nutzer soll sehen was möglich wäre. Nur die Installation wird blockiert oder eingeschränkt.

---

## Wo SysInfo lebt

**Crate:** `fsn-sysinfo` in `FreeSynergy.Lib` (Core)

SysInfo ist eine **shared Library**, kein eigenes Programm. Sie wird von mehreren Programmen genutzt:
- **Store** — bei der Installation (Feature-Check)
- **Node** — für den Alerting-Loop
- **Desktop** — für Widgets (Disk, RAM, Temperatur)
- **Init** — für den ersten Überblick (Git vorhanden? Podman vorhanden?)

---

## CLI

```bash
# Statische Daten anzeigen
fsn sysinfo

# Dynamische Daten (aktuell)
fsn sysinfo --live

# Cache leeren (erzwingt Neu-Lesen der statischen Daten)
fsn sysinfo --refresh

# Nur ein bestimmtes Feature prüfen
fsn sysinfo --check pam
fsn sysinfo --check systemd
fsn sysinfo --check git
```

---

## Alerting konfigurieren

In Settings → System → Benachrichtigungen:

| Einstellung | Typ | Standard |
|---|---|---|
| Festplatte voll (Schwelle %) | Zahl | 90 |
| RAM voll (Schwelle %) | Zahl | 95 |
| CPU-Temperatur (°C) | Zahl | 80 |
| SMART-Fehler sofort melden | Boolean | ja |
| Prüf-Intervall (Minuten) | Zahl | 5 |

---

Weiter: [Pakete](pakete.md) | [Node-Plattformen](node-plattformen.md) | [Message Bus](bus.md)
