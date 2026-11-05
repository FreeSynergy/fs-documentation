# Wowza Streaming Engine - Keyboard shortcuts

## Overview

The Wowza Streaming Engine Manager has **no documented shortcuts**. It follows the usual web conventions; server control runs through service commands, automation through the REST API.

## Web manager (`http://host:8088`)

| Key | Purpose |
|-----|---------|
| `Tab` / `Shift+Tab` | move between form fields |
| `Enter` | confirm dialogs (restart, save properties) |
| `Esc` | cancel confirmation dialogs |
| `Ctrl+F` | filter in long application/connection lists |

## Service and console

| Command | Purpose |
|---------|---------|
| `systemctl start wowza` / `stop` / `restart` | the engine as a service (Linux) |
| `<Install>/bin/WowzaStreamingEngine start` | start without systemd |
| Windows: services console → "Wowza Streaming Engine" | service control on Windows |
| `tail -f <Install>/logs/wowzastreamingengine_access.log` | watch the live log |

The exact script/unit name is **installation-dependent** (package, Docker image).

## REST calls as the "quick commands"

| Task | Invocation |
|------|------------|
| List the applications | `curl -u user:pass http://localhost:8087/v2/instances` |
| Restart an application | `curl -u user:pass -X POST http://localhost:8087/v2/instances/_definst_/applications/myapp/restart` |
| Show the connections | `curl -u user:pass http://localhost:8087/v2/connections` |

## Mac variants

| Windows/Linux | Mac | Note |
|---------------|-----|------|
| `Ctrl+F` | `Cmd+F` | browser search in the manager |
| `Esc` | `Esc` | cancel dialogs |
| service commands | — | the engine does not run on macOS; the manager is reachable platform-independently |

## Summary

- In short: **no shortcuts** in the manager; server control through service commands, automation through REST v2
- For a FreeSynergy skin interface Wowza prescribes no keys — your own hotkeys are freely choosable
- Recurring routines (create an application, restart, maintain restream targets) belong in scripts against the REST API, not in keyboard combinations
