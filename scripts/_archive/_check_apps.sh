#!/bin/sh
# Inventar: prüft pro App/Skin, ob die 7 erwarteten Dateien vorhanden sind
APPS_DIR="/srv/FreeSynergy/fs-documentation/docs/de/apps"
REQUIRED="api.md description.md features.md index.md menu.md shortcuts.md structure.md"

for app in "$APPS_DIR"/*/; do
  app=${app%/}; app=${app##*/}
  [ -d "$app" ] 2>/dev/null
  echo "== APP: $app =="
  # App-Root
  if [ -d "$APPS_DIR/$app/skins" ]; then
    for skin in "$APPS_DIR/$app/skins"/*/; do
      skin=${skin%/}; name=${skin##*/}
      missing=""
      for f in $REQUIRED; do
        [ -f "$skin/$f" ] || missing="$missing $f"
      done
      if [ -n "$missing" ]; then
        echo "  INCOMPLETE skin $name -> missing:$missing"
      fi
    done
    # skins/index.md
    [ -f "$APPS_DIR/$app/skins/index.md" ] || echo "  MISSING skins/index.md"
    [ -f "$APPS_DIR/$app/index.md" ] || echo "  MISSING app index.md"
  else
    echo "  NO skins dir"
  fi
done
