# nginx-rtmp-module - Keyboard shortcuts

## Overview

The module has **no interface and no shortcuts**. It is operated through the nginx command line and `nginx.conf`. The status page (`/stat`) is a normal HTML/XML page without its own keys.

## nginx command line

| Command | Purpose |
|---------|---------|
| `nginx -t` | check the configuration (syntax and paths) |
| `nginx -s reload` | reload the configuration without downtime |
| `nginx -s stop` | terminate immediately |
| `nginx -s quit` | terminate in an orderly way |
| `nginx -v` / `nginx -V` | version / build options (the module is visible) |
| `nginx -c /path/nginx.conf` | use a different configuration file |

## Service management

| Command | Purpose |
|---------|---------|
| `systemctl start nginx` | start |
| `systemctl reload nginx` | apply a configuration change |
| `journalctl -u nginx -f` | log stream (the RTMP events too) |

## Status page (`http://host/stat`)

| Key | Purpose |
|-----|---------|
| `F5` / `Ctrl+R` | reload the status |
| `Ctrl+F` | search in the stream list |

## Mac variants

| Windows/Linux | Mac | Note |
|---------------|-----|------|
| `Ctrl+R` | `Cmd+R` | browser reload |
| `systemctl …` | `brew services restart nginx` | no interface of its own |

## Summary

- In short: **no shortcuts** — everything runs through `nginx.conf`, `nginx -t` and `nginx -s reload`
- For a FreeSynergy skin interface the original prescribes no keys; your own hotkeys (e.g. "check the configuration", "reload") can be defined freely
- Automation replaces the keyboard: hooks (`on_publish`, `on_record_done`) and `exec` commands
