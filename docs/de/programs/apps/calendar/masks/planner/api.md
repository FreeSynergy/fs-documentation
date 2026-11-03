# GNOME Planner - API Dokumentation

**Versionsstand: 0.14.92 (16.12.2023)** — Quelltext-Beta-Release, gepflegt (Übersetzungs-Updates bis April 2026), in Debian stable (trixie, 0.14.92-1.1) und Arch extra (0.14.92-4) verpackt.

## Status-Prüfung (Lohnt das Dokumentieren?)

- **Noch entwickelt/genutzt?** Ja: Release 0.14.91 (2022) und 0.14.92 (2023) nach langer Pause; Repo `gitlab.gnome.org/World/planner` aktiv (letzte Commits April 2026, überwiegend Übersetzungen); Distributionspakete aktuell. → Dokumentieren statt Löschen.
- **Einzigartige Features** (auch falls die Entwicklung einschlief): projektinterne Arbeitskalender pro Ressource, benutzerdefinierte Eigenschaften (custom properties) auf Projekt-/Aufgaben-/Ressourcenebene, optionale PostgreSQL-Ablage von Projekten über ein Plugin — das bietet kein anderer Kalender-Skin dieser Serie.

## Übersicht

Planner ist ein reiner Desktop-Planer **ohne Server und ohne Live-API**. Die programmatische Schnittstelle ist die Datei: das XML-Format `*.planner` (MIME `application/x-planner`) und — intern — die Bibliothek **libplanner** (Klassenpräfix `Mrp*`). Seit 0.14.91 ist libplanner **privat**: sie wird nicht mehr installiert, ein Out-of-Tree-Plugin-/Programmierzugriff gibt es offiziell nicht mehr (Issue #238).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| `*.planner` / `*.mrproject` (XML) | Projekt speichern/laden, Konvertierung | offiziell, DTD im Quelltext (`data/dtd/mrproject-0.6.dtd`) |
| libplanner (`Mrp*`, C/GObject) | Planungsobjekte, CPM-Berechnung, Storage-Module | **privat** seit 0.14.91 (nicht installiert, keine stabile ABI) |
| SQL-Plugin (libgda → PostgreSQL) | „Open from Database…“ / „Save to Database“ | offiziell, aber experimentell (Meson-Option `database-gda`) |
| HTML-Export (libxslt) | Berichte als HTML | offiziell |
| REST/GraphQL/WebSocket | — | ❌ nicht vorhanden |
| Webhooks | — | ❌ nicht vorhanden |

## Das Dateiformat `*.planner`

- **Endungen/MIME:** `*.planner` (Standard beim Speichern) und `*.mrproject`; MIME-Typ `application/x-planner`, Unterart von `application/xml`; Magic-Marker `mrproject-version` (siehe `data/mime/app.drey.Planner.xml.in`). Die frühere Endung `.ppx` kommt im Quelltext von 0.14.92 nirgends mehr vor.
- **Schema:** DTD `data/dtd/mrproject-0.6.dtd`; Root-Element `<project mrproject-version="2" …>` (die 0.11-Altformate werden über `libplanner/mrp-old-xml.c` gelesen; der Export ins 0.11-Format wurde in 0.14.92 entfernt, Bug #248).

Ausschnitt (gekürzt) aus `examples/sample-1.planner` des Quelltext-Tarballs:

```xml
<?xml version="1.0"?>
<project name="Sample 1" company="Planner Community" manager="Richard Hult"
         phase="Implementation" project-start="20040701T000000Z"
         mrproject-version="2" calendar="1">
  <phases>
    <phase name="Design"/>
    <phase name="Implementation"/>
  </phases>
  <calendars>
    <day-types>
      <day-type id="0" name="Working" description="A default working day"/>
      <day-type id="1" name="Nonworking" description="A default non working day"/>
    </day-types>
    <calendar id="1" name="Default">
      <default-week mon="0" tue="0" wed="0" thu="0" fri="0" sat="1" sun="1"/>
      <overridden-day-types>
        <overridden-day-type id="0">
          <interval start="0800" end="1200"/>
          <interval start="1300" end="1700"/>
        </overridden-day-type>
      </overridden-day-types>
      <days/>
    </calendar>
  </calendars>
  <tasks>
    <task id="3" name="Report" work="0" start="20040708T104000Z"
          end="20040708T104000Z" percent-complete="0" priority="0"
          type="milestone" scheduling="fixed-work">
      <predecessors>
        <predecessor id="1" predecessor-id="2" type="FS"/>
      </predecessors>
    </task>
  </tasks>
  <resource-groups/>
  <resources>
    <resource id="1" name="Alvaro del Castillo" short-name="ACS" type="1"
              units="0" email="" note="" std-rate="0">
      <properties>
        <property name="cost" value=""/>
      </properties>
    </resource>
  </resources>
  <allocations>
    <allocation task-id="2" resource-id="1" units="75"/>
    <allocation task-id="15" resource-id="1" units="100"/>
  </allocations>
</project>
```

**Kernelemente der DTD (0.6):**

| Element | Wichtigste Attribute | Hinweise |
|---------|----------------------|----------|
| `project` | `mrproject-version="2"`, `name`, `project-start`, `company`, `manager`, `phase`, `calendar` | Reihenfolge der Kinder: `properties*`, `phases?`, `calendars?`, `tasks?`, `resource-groups?`, `resources?`, `allocations?` |
| `task` | `id`, `name`, `start`, `end`, `work`, `duration`, `percent-complete`, `priority`, `type=normal\|milestone`, `scheduling=fixed-work\|fixed-duration`, `note` | Unteraufgaben sind verschachtelte `task`-Elemente; eigene Kopfzeilen („summary“) werden implizit aus Kindern berechnet |
| `predecessor` | `predecessor-id`, `type=FS\|FF\|SS\|SF`, `lag` | Verweist per Task-`id` |
| `constraint` | `type`, `time` | Implementiert: ASAP (Standard), SNET („start not earlier than“), MSO („must start on“); ALAP und FNLT sind in `mrp-types.h` als *unimplemented* markiert |
| `property` / `properties` | `name`, `type=date\|duration\|float\|int\|text\|text-list\|cost`, `owner=project\|task\|resource`, `value` | Benutzerdefinierte Spalten; DTD-kommentar weist auf die Doppelrolle Deklaration/Wert hin |
| `calendar` | `id`, `name`; Kinder `default-week`, `overridden-day-types`, `days`, verschachtelte `calendar` | Arbeits-/Nichtarbeitstage mit Tagesintervallen (`interval start/end` = Uhrzeit HHMM); untergeordnete Kalender erben vom Basiskalender |
| `resource` | `id`, `name`, `short-name`, `email`, `type=1\|2` (Arbeit\|Material), `group`, `units`, `std-rate`, `ovt-rate`, `calendar` | eigener Kalender pro Ressource möglich |
| `allocation` | `task-id`, `resource-id`, `units` | Zuordnung Ressource↔Aufgabe in Prozent |

**Zeiteinheiten:** `start`/`end`/`project-start` als `YYYYMMDDTHHMMSSZ`; interne Zeit `mrptime` ist eine 64-Bit-Sekundenzahl seit Unix-Epoche (`libplanner/mrp-time.h`, mit 0.14.91 Y2038-fest); `work` steht in **Sekunden** (Beispiel oben: `work="115200"` = 32 h).

## Authentifizierung

Keine — lokale Dateien; Zugriffsrechte über Dateisystem/Shares. Nur das SQL-Plugin fragt bei „Save to Database“ Server, Datenbankname, Benutzer und Passwort ab.

## Import/Export als „API“

| Richtung | Format | Weg / Schalter |
|----------|--------|----------------|
| Import | MS Project **XML** (ab MSP 2002, „Save As… XML“) | `Datei → Importieren → MS Project XML…`; XSLT `data/stylesheets/msp2planner.xsl`; experimentell; Kalender, Gruppen und benutzerdefinierte Felder werden **nicht** importiert |
| Import | Kontakte/Ressourcen aus Evolution Data Server oder LDAP | `Datei → Importieren → EDS…` (Plugin, Meson-Option `eds`, standardmäßig deaktiviert) |
| Import/Export | PostgreSQL-Datenbank | `Datei → Importieren → Open from Database…` / `Datei → Exportieren → Save to Database…` (libgda; Schema `data/sql/database.sql`) |
| Export | HTML (Gantt-Bild, Aufgabenliste, Ressourcentabelle) | `Datei → Exportieren → HTML…` (XSLT unter `data/stylesheets/`) |
| Export | PDF | GTK-Druckdialog „In Datei drucken“; Druckdialog wählt Ansichten per Häkchen |
| Export | Planner-0.11-Altformat | ❌ in 0.14.92 entfernt (Bug #248) |

## Beispiel: Auswertung per Skript

```python
import xml.etree.ElementTree as ET

t = ET.parse("projekt.planner")
root = t.getroot()

def walk(tasks):
    for task in tasks:
        work_h = int(task.get("work") or 0) / 3600.0   # Sekunden -> Stunden
        print(f"{task.get('name')}: {work_h:.1f} h "
              f"({task.get('start')} .. {task.get('end')})")
        walk(task.findall("task"))

walk(root.find("tasks"))
```

## Rate Limits

Entfällt (keine Netzwerk-API). Das SQL-Plugin unterliegt nur den Grenzen der PostgreSQL-Verbindung.

## SDKs und Bibliotheken

- **libplanner** (C/GObject, Klassen `MrpProject`, `MrpTask`, `MrpResource`, `MrpCalendar`, `MrpRelation`, `MrpAssignment`, Storage-Module …): nur noch **intern** gebaut; Referenz-/Doku-Objekte existieren nur mit Meson-Option `gtk_doc=true` als *private* API-Referenz.
- **Python-Bindings:** nicht vorhanden; `tests/python/task-test.py` ist ein Alttest gegen das historische `mrproject`-PyGTK-Modul und läuft mit aktuellen Versionen nicht.
- **Konverter:** `.planner` ist normales XML → eigene Skripte mit XSLT/DOM; das SQL-Schema (`data/sql/`) ist ein zweiter strukturierter Zugang.

## Skin-Hinweis

Ein Planner-Skin in FreeSynergy bildet die vier Ansichten (Gantt, Aufgaben, Ressourcen, Ressourcennutzung) nach und liest/schreibt `*.planner`-XML; Zeit-/Aufwandsfelder auf das Standardmodell mappen ([Felder](../../../../../data/felder.md), [Task-/Projekt-Modell](../../../../../data/modelle.md); siehe auch [data/projects](../../../../../data/projects/)).
