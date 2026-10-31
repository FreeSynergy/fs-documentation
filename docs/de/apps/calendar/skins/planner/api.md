# GNOME Planner - API Dokumentation

## Übersicht

Planner ist ein reiner Desktop-Planer **ohne Server und ohne Live-API**. Die programmatische Schnittstelle ist die Datei: das XML-Format `.ppx` und die C-Bibliothek **libplanner**, die Format-Lesen/-Schreiben und die Planungs-Berechnung (CPM, Early/Late, kritischer Pfad) kapselt. Für eine Skin-/FreeSynergy-Anbindung ist das Dateiformat der Einstiegspunkt.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| `.ppx` (XML-Datei) | Projekt speichern/laden, Konvertierung | offiziell (Formatdokumentation im Quelltext, Schema unvollständig) |
| libplanner (C) | Planungsobjekte, `.ppx`-/`.mpp`-Reader | offiziell (Bibliothek) |
| HTML-/Print-Export | Berichte, PDF über Druckdialog | offiziell |
| REST/GraphQL/WebSocket | — | ❌ Nicht vorhanden |
| Webhooks | — | ❌ Nicht vorhanden |

## Authentifizierung

Keine — lokale Dateien. Zugriffsrechte über Dateisystem/Shares.

## Das `.ppx`-Format (Kernstruktur)

```xml
<project>
  <name>Migration</name>
  <start>2026-11-01T00:00:00</start>
  <calendar-days-per-week>5</calendar-days-per-week>
  <task>
    <name>Analyse</name>
    <type>normal</type>            <!-- normal | milestone | summary -->
    <start>2026-11-02T08:00:00</start>
    <finish>2026-11-09T17:00:00</finish>
    <work>160000</work>            <!-- Zehntelsekunden -->
    <complete>40</complete>        <!-- Prozent -->
    <priority>Medium</priority>
    <predecessor>
      <name>Grundlage</name>
      <type>finish_to_start</type> <!-- FS/SS/FF/SF -->
      <lag>0</lag>
    </predecessor>
    <resource name="anna" units="100"/>
  </task>
</project>
```

Wichtig: Dauern/Aufwand in Zehntelsekunden; Termine ohne Zeitzone (lokale Projektkalenderzeit).

## Import/Export als „API"

| Richtung | Format | Weg |
|----------|--------|-----|
| Import | `.mpp` (MS Project) | LibMSP-Reader in Planner/libplanner |
| Import | `.moe` (OpenProj) | eingeschränkt |
| Export | HTML | Menü Datei → Dokument drucken/HTML |
| Export | PDF | GTK-Druckdialog „Als PDF" |
| Konvertierung | `.ppx` ↔ JSON | eigenes Skript gegen libplanner oder XML-Parsing |

## Beispiel: Auswertung per Skript

```python
import xml.etree.ElementTree as ET
t = ET.parse("projekt.ppx")
for task in t.getroot().findall("task"):
    name = task.findtext("name")
    work = int(task.findtext("work") or 0) // 36000  # Zehntelsekunden -> Stunden
    print(f"{name}: {work} h")
```

## Rate Limits

Entfällt (keine Netzwerk-API).

## SDKs und Bibliotheken

- **libplanner** (C): Referenzimplementierung, GObject-API; Python-Bindings historisch (ungepflegt)
- **Konverter-Skripte** (Community): `.ppx` → GanttProject `.gan` / PMXML — Qualität individuell prüfen
- **LibMSP** (C++): `.mpp`-Leser, von Planner genutzt

## Skin-Hinweis

Ein Planner-Skin in FreeSynergy bildet Gantt/Baum-UI nach und tauscht `.ppx`-Dateien aus; Zeit-/Aufwandsfelder auf das Standardmodell mappen ([Felder](../../../../data/felder.md), [Task-Modell](../../../../data/modelle.md)).
