# Restreamer - Keyboard shortcuts

## Overview

The Restreamer's web UI has **no documented shortcuts**. It follows the usual web
conventions; operation runs over forms and buttons. Automation and maintenance happen via
the command line inside the container.

## Web UI

| Key | Function |
|-----|----------|
| `Tab` / `Shift+Tab` | switch form fields |
| `Enter` | submit forms |
| `Esc` | abort confirmation prompts/dialogs |
| `Ctrl+C` on marked URL/snippet fields | copy the push URL, play URL or embed code |

## Container and CLI

| Command | Function |
|---------|----------|
| `docker restart restreamer` | apply the settings again |
| `docker exec -it restreamer sh` | open a shell in the container |
| `docker exec restreamer /opt/restreamer/bin/restreamer-cli help` | show the CLI commands |
| `docker exec restreamer tail -f /opt/restreamer/var/log/nginx/access.log` | watch accesses live |

The exact CLI syntax is **version-dependent** — the authoritative source is
`restreamer-cli help` in the respective image.

## The RTMP counterpart (OBS as an example)

The Restreamer itself is controlled from the encoder: in OBS one target is enough
(`rtmp://host:1935/live/stream?key=<pushKey>`); for OBS's own hotkeys see
[obs-studio/shortcuts.md](../../obs-studio/latest/shortcuts.md).

## Mac variants

| Windows/Linux | Mac | Note |
|---------------|-----|------|
| `Ctrl+C` | `Cmd+C` | copy the snippet fields |
| `Esc` | `Esc` | abort dialogs |
| `docker …` | `docker …` | the commands are platform-independent |

## Summary

- In short: **no shortcuts** in the web UI; control via forms, maintenance via Docker/`restreamer-cli`
- Recurring procedures (rotate the push key, maintain the target lists) belong in CLI/hook scripts, not in key combinations
- For a FreeSynergy frontend UI the Restreamer prescribes no keys — your own hotkeys are free to choose
