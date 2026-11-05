# Wowza Streaming Engine - Menu items

## Overview

All operation runs through the **Wowza Streaming Engine Manager** (`http://<host>:8088`, HTTPS `:8090`). The manager is a lean web app: the server menu on the left, detail pages on the right. The configuration underneath sits in XML files; manager pages are mostly direct masks over them.

## Server menu (left area)

| Menu item | Description |
|-----------|-------------|
| Login | username/password (accounts in `managernames.properties`) |
| Applications | list of all applications of a virtual host; choosing one opens the application page |
| Add Application | assistant: name + type (e.g. Live, Live and VOD, VOD) |
| Streaming Publishers | active feeders; block/release publishers (publisher control) |
| Connections | active viewer/player connections with IP, stream, duration |
| Restart | restart the server or an individual application |
| Log Viewer | live excerpt from `wowzastreamingengine_error.log` |
| Server name/logout | at the top: instance name, licence status, sign out |

## Per application (tabs on the application page)

| Tab | Description |
|-----|-------------|
| Playback Options | ready-made playback URLs (HLS, DASH, Smooth, RTMP, CMAF) for copying |
| Properties | form-based editing of the `Application.xml` (recording, DVR, timing …) |
| Security | configure hash-key/token checks for play and publish |
| Stream Targets | forward the input to external RTMP targets (name + URL/key) |
| Restart Application | restart only this application |

## Context menus

- ❌ no right-click context menus — all actions are buttons/links in tables (⚠ the manager is deliberately simple)
- stream/connection rows directly contain their actions (e.g. blocking for publishers)

## Menus by user role

| Role | visible |
|------|---------|
| Manager account (admin) | all menus |
| further accounts | the same functional scope as the admin account; finely granular roles ❌ |
| REST API user | no menu — the same accounts as the manager, access only to the API |

## Note

The exact menu/tab names vary slightly with the engine version (4.x); the installed version is authoritative.
