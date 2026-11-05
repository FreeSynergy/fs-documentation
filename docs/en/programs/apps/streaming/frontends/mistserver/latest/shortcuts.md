# MistServer - Keyboard shortcuts

## Overview

MistServer is a service with a web interface — there are **no documented shortcuts**. The interface follows the usual browser keyboard habits (Tab/Enter), its own keys do not exist.

## Command line and service

| Invocation | Purpose |
|------------|---------|
| `MistServer` | starts the controller and the configured connectors |
| `MistServer -h` | help for the start and API parameters (the port can be changed via a parameter) |
| `systemctl start mistserver` | start the service |
| `systemctl restart mistserver` | apply changes |
| `journalctl -u mistserver -f` | log stream |

## Browser interface (`http://host:4242`)

| Key | Purpose |
|-----|---------|
| `Tab` / `Shift+Tab` | move between fields in forms |
| `Enter` | confirm forms |
| `Ctrl+R` | reload the interface (refresh the status) |
| Right-click | the context menu of a stream (open, delete, create) |

## API calls as the "quick commands"

| Task | Invocation |
|------|------------|
| Read the configuration | `curl -s 'http://localhost:4242/api?command={"config":{}}'` |
| Active streams | `curl -s 'http://localhost:4242/api?command={"active_streams":[]}'` |
| Statistics | `curl -s 'http://localhost:4242/api?command={"stats_streams":["clients"]}'` |
| System data | `curl -s 'http://localhost:4242/api?command={"capabilities":{}}'` |

## Mac variants

| Windows/Linux | Mac | Note |
|---------------|-----|------|
| `Ctrl+R` | `Cmd+R` | browser reload |
| `systemctl …` | `launchctl …` | MistServer runs on macOS as a process/service |

## Summary

- In short: **no real shortcuts**; interaction runs through tables, context menus and JSON commands
- For a FreeSynergy skin interface no keys of the original have to be copied — your own key layout can be defined freely and then added here
- In practice automation replaces every "keyboard combination": streams, pushes and protocols are set through the API
