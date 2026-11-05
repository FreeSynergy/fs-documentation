#!/bin/sh
# For each EN component doc, count how many lines are identical to the DE source
# (excluding code fences and lines with no letters). High count = barely translated.
cd /srv/FreeSynergy/fs-documentation || exit 1
tmpd=temp/.tmpcmp; mkdir -p "$tmpd"
for de in $(find docs/de/components -name "*.md" | sort); do
  en=$(echo "$de" | sed 's|^docs/de/|docs/en/|')
  [ -f "$en" ] || continue
  sed -e '/```/,/```/d' -e '/^[[:space:]]*[|┌└├─│]/d' "$de" | grep -E '[A-Za-zÄÖÜäöüß]' | sort > "$tmpd/de"
  sed -e '/```/,/```/d' -e '/^[[:space:]]*[|┌└├─││]/d' "$en" | grep -E '[A-Za-zÄÖÜäöüß]' | sort > "$tmpd/en"
  same=$(comm -12 "$tmpd/de" "$tmpd/en" | grep -ciE 'und|oder|nicht|mit |von |für | ist | sind | wird| werden| kann| sich| auch| Beschreibung|Eigenschaften|Verwendung|Aussehen|Beispiele|Grundlayout|Varianten|Größen|Zustände|Farben|Siehe auch|Verhalten|Darstellung|Barrierefreiheit|Geerbt|Hauptattribute|Anwendung|Szenarien|Volle|Fläche|Bedienung|Funktion|Optionen|Zustand|Farbe|Größe|Zeile|Benutzer|Anzeige|Auswahl|Bereich|Knopf|Inhalt|Platzhalter|Einordnung|überwiegend|jeweils|sondern|wird|des |dem |den |denen|wobei|damit|dadurch|einzelne|mehrere' | grep -c .)
  if [ "$same" -gt 0 ]; then printf "%4s  %s\n" "$same" "$en"; fi
done | sort -rn
