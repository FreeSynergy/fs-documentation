# MediaMTX - Keyboard shortcuts

## Overview

MediaMTX runs as a daemon without an interactive console — there are **no keyboard shortcuts**. It is operated through the command line, service management, YAML and the HTTP API.

## Command line

| Invocation | Purpose |
|------------|---------|
| `mediamtx` | starts with `mediamtx.yml` in the current directory |
| `mediamtx /path/to/config.yml` | starts with a different configuration |
| `mediamtx --version` | version information |
| `Ctrl+C` (foreground) | orderly shutdown (the `runOnShutdown` hooks) |

## Service management

| Command | Purpose |
|---------|---------|
| `systemctl start mediamtx` | start |
| `systemctl restart mediamtx` | make a configuration change effective |
| `journalctl -u mediamtx -f` | log stream |
| `docker compose up -d` | container start (config as a volume) |

## API instead of shortcuts (the typical "quick commands")

| Task | Invocation |
|------|------------|
| Show paths | `curl -s localhost:9997/v3/paths/list` |
| Show connections | `curl -s localhost:9997/v3/connections/list` |
| Create a dynamic path | `curl -X POST localhost:9997/v3/config/paths/add/mypath -d '{"source":"publisher"}'` |
| Query metrics | `curl -s localhost:9998/metrics` |

## Mac variants

| Windows/Linux | Mac | Note |
|---------------|-----|------|
| `systemctl …` | `launchctl …` / brew services | MediaMTX has no interface of its own |
| `Ctrl+C` | `Cmd+C` | `Ctrl+C` also works in the terminal |

## Summary

- In short: **no shortcuts** — MediaMTX is controlled through the file, the ports and the API
- For a FreeSynergy skin interface no keys have to be prescribed; only the API calls and the port list matter
- Anyone who needs "hotkeys" defines them in their own interface and documents them there
