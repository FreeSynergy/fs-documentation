# Proxmox VE - Struktur & UI/UX

## Übersicht

Proxmox VE zeigt nach dem Login ein Drei-Bereiche-Layout: links den Ressourcenbaum, rechts oben die Objekt-Kopfzeile mit Aktionsbuttons, darunter Reiter mit Tabellen und Formularen. Overlays (Dialoge, Konsolen) legen sich darüber; ein Task-Panel meldet Hintergrundaktionen.

## Fenster-Struktur

### Hauptansicht

```
┌──────────────────────────────────────────────────────────────────────┐
│ Kopf: Proxmox-Logo | Suchleiste | Theme | Benutzer-Menü | Abmelden   │
├────────────────────┬─────────────────────────────────────────────────┤
│ Ressourcenbaum     │ Objekt-Kopf: [pve1] [101 ubuntu-server]         │
│ ▼ Datacenter       │ Buttons: Start | Stop | Reboot | Migrate | ⋮    │
│   ▸ pve1           ├─────────────────────────────────────────────────┤
│     ▸ 101 ubuntu   │ Reiter: Summary Hardware Options Console …      │
│     ▸ 102 nginx    ├─────────────────────────────────────────────────┤
│   ▸ storage        │ Tabellen / Formulare / Diagramme des Reiters    │
│                    │ ┌────────────────────────────────────────────┐  │
│                    │ │ disk0   qc0  scsi0  32G  Local-LVM  [⋮]   │  │
│                    │ └────────────────────────────────────────────┘  │
├────────────────────┴─────────────────────────────────────────────────┤
│ Task-Panel (ausklappbar): laufende/backups/migrationen mit Status    │
└──────────────────────────────────────────────────────────────────────┘
```

### Dialog (Beispiel *Create VM*)

```
┌──────────────────────────────────────────────────────────┐
│  Create VM                                       [X]     │
├──────────────────────────────────────────────────────────┤
│  (General) (OS) (System) (Disks)                         │  ← Schrittleiste
│  Node [pve1 ▾]  VM ID [103 ]  Name [____________]       │
├──────────────────────────────────────────────────────────┤
│             [< Back]  [Next >]  [Create]                 │
└──────────────────────────────────────────────────────────┘
```

### Konsolenansicht

```
┌──────────────────────────────────────────────────────────┐
│  Console: xterm.js (VM 101)     [Menü ⚙: Tasten, Clipboard]│
├──────────────────────────────────────────────────────────┤
│                                                          │
│   terminal-/grafiknahe Konsole (noVNC oder xterm.js)     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfleiste | Oben | Suche, Theme-Umschalter, Benutzer-/Token-Menü |
| Ressourcenbaum | Links | Datacenter, Nodes, VMs, Container, Storage, Pools |
| Objektkopf | Rechts oben | Name, Status, Start/Stop/Reboot/Migrate/Console-Buttons |
| Reiter | Rechts mitte | Summary, Hardware, Options, Console, Backup, … |
| Tabellen | Im Reiter | Disks, Netze, Regeln, Jobs mit Aktionsmenüs (`⋮`) |
| Task-Panel | Unten | Hintergrund-Tasks (UPID) mit Fortschritt und Fehlerlink |
| Overlays | Mitte | Erstellungsassistenten, Edit-Dialoge, Konsole, Shell |

## UI/UX

### Design-Prinzipien

- **Ein Objekt im Fokus**: Baumauswahl steuert alles, keine Mehrfachfenster
- **Reiter pro Sachgebiet**: Hardware, Options, Sicherheit klar getrennt
- **Assistenten für Komplexes**: VM-/Storage-Anlage in Schritten mit Validierung
- **Actions nah am Objekt**: Buttons sitzen am Objektkopf, Zeilenaktionen im `⋮`-Menü

### Farbschema und Themes

- Hell/Dunkel/Auto über den Theme-Schalter der Kopfleiste (versionabhängig)
- Statusfarben: grün = running, grau = stopped, rot = Fehler; Konsolen haben eigene Farbgebung
- Eigene Logos/Themes für Unternehmen möglich (versionabhängig)

### Interaktionen

- **Suche oben**: filtert Baum nach VMID, Name, Tag, IP
- **Doppelklick**: öffnet Standardaktion (Console oder Reiter, objektabhängig)
- **Drag & Drop**: Boot-Reihenfolge ziehen; ansonsten selten
- **Rechter Klick**: vereinzelt Kontextaktionen im Baum (versionabhängig)
- **Live-Updates**: Diagramme und Statuswerte werden automatisch nachgezogen

### Responsive Design

- **Desktop**: volles Layout; Baum einklappbar für mehr Tabellenbreite
- **Tablet**: Baum überlays den Inhalt, Reiter als horizontal scrollbar
- **Mobil**: nutzbar, aber Tabellen und Konsolen bleiben klein — nicht primärer Zielmodus
- **Vollbild-Konsole**: Console-Reiter kann flächenfüllend maximiert werden (versionabhängig)

### Zugänglichkeit

- **Tastatur**: Reiter, Tabellen und Dialoge per `Tab`/`Enter` bedienbar; Konsolen fangen Tastatureingaben ab
- **Screenreader**: Tabellen haben Header-Zuordnung, aber dynamische Panels sind für Reader mittelgut (ExtJS-Historie, versionabhängig)
- **Fokusanzeige**: sichtbar, Dialoge fangen Fokus ein
- **Zoom**: Browser-Zoom ohne abgeschnittene Buttons, Tabellen scrollen dann horizontal

### Performance

- **API-getriebene Oberfläche**: jeder Reiter lädt bei Auswahl seine Daten; große Inventory-Listen werden paginiert
- **Konsolenstrom**: noVNC/xterm.js belastet Client und Netz, nicht die API
- **Task-Asynchronität**: lange Aktionen laufen als Tasks (UPID) weiter, UI blockiert nicht
- **Empfehlung**: In sehr großen Umgebungen Suche/Filter statt komplettem Baumausklappen nutzen

## Siehe auch

- [menu.md](menu.md) - Baumstruktur und Rollen im Detail
- [features.md](features.md) - Funktionsbereiche
- [shortcuts.md](shortcuts.md) - Tastatur und Konsolen-Tasten
- [api.md](api.md) - REST-API hinter jeder UI-Aktion
