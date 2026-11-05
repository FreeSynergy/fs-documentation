# Ant Media Server - Keyboard shortcuts

## Overview

The web panel of the Ant Media Server has **no documented shortcuts**. It follows the usual web conventions. Operation runs through mouse, forms and REST calls.

## Command line and service

| Command | Purpose |
|---------|---------|
| `antmedia-service start` | start the server (installation under `/usr/local/antmedia`) |
| `antmedia-service stop` | stop |
| `antmedia-service restart` | restart (the settings are reloaded) |
| `antmedia-service status` | process status |
| `systemctl start antmedia` | on systems with a systemd unit |
| `tail -f logs/error.log` | watch the live log |

The exact script/unit name is **installation-dependent** (image, package manager, Docker).

## Web panel (`http://host:5080`)

| Key | Purpose |
|-----|---------|
| `Tab` / `Shift+Tab` | move between form fields |
| `Enter` | confirm dialogs, trigger the search |
| `Esc` | close modals (URL dialog, token dialog) |
| `Ctrl+F` | filter in long stream/VoD lists |

## REST calls as the "quick commands"

| Task | Invocation |
|------|------------|
| List streams | `curl -s localhost:5080/live/rest/v2/broadcasts/list/0/10` |
| Stop a stream | `curl -s -X POST localhost:5080/live/rest/v2/broadcasts/<id>/stop` |
| Server info (management API) | `curl -s localhost:5080/rest/v2/…` (details per the Swagger docs) |

## Mac variants

| Windows/Linux | Mac | Note |
|---------------|-----|------|
| `Ctrl+F` | `Cmd+F` | browser search |
| `Esc` | `Esc` | close modals |
| `antmedia-service …` | — | the panel is platform-independent |

## Summary

- In short: **no shortcuts** in the panel; server control through service commands, automation through REST v2
- For a FreeSynergy skin interface AMS prescribes no keys — your own hotkeys are freely choosable
- Recurring routines (create a stream, start a recording) belong in scripts against the REST API, not in keyboard combinations
