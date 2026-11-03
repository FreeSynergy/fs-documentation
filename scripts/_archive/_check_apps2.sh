#!/bin/sh
# Liste alle Dateien in apps mit Zeilenanzahl, sortiert nach Größe (kleinste zuerst)
APPS_DIR="/srv/FreeSynergy/fs-documentation/docs/de/apps"
find "$APPS_DIR" -name '*.md' -type f -printf '%s %p\n' | sort -n | head -40
echo "--- total files:"
find "$APPS_DIR" -name '*.md' -type f | wc -l
