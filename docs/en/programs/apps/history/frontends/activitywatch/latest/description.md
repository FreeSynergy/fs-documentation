# ActivityWatch latest — Description

## Overview
An open-source suite that tracks computer use automatically and keeps the data under your control.

## What it does
- Watchers observe: keyboard/mouse activity (away after 3 minutes by default), active window title and application, browser tab (title, URL, audible, incognito).
- A local server stores events in buckets.
- A web interface and tray icon show and filter the data; categories with rules.
- Export, pausing, filtering.

## Who it suits
People who want an automatic, private record of how their time went.

## Differentiation
### ActivityWatch vs. Day One
Automatic and technical versus written and personal. Exist.io pulls data from many services and finds correlations; ActivityWatch stays on the machine.

## Technical details
Local server, default port 5600, listening on localhost only. Two server implementations exist (Python and Rust). Window watcher: Windows, macOS, Linux (X11 only). Browser extension: Chrome, Edge, Firefox. Licence name: Open.
