# OPNsense - Struktur & UI/UX

## Übersicht

OPNsense zeigt nach dem Login das Dashboard; darüber liegt die horizontale Menüleiste. Jede Seite ist eine „Page“ aus Formular-Panel oder Grid-Tabelle, bei Firewall-Seiten zusätzlich mit Apply-Leiste. Overlays (Edit-Dialoge, Statusmeldungen) erscheinen zentriert bzw. als Toast rechts oben. Der Zustand „ungespeicherte/unausgeführte Änderungen“ ist immer sichtbar.

## Fenster-Struktur

### Firewall-Regelseite (Beispiel)

```
┌──────────────────────────────────────────────────────────────────────┐
│ 🏠 | Interfaces | Firewall | VPN | Services | System      [Admin ▾]  │
├──────────┬───────────────────────────────────────────────────────────┤
│ Firewall │ Firewall: Rules: LAN     [+ Add] [⚙ Columns] [Apply]     │
│ ▸ Rules  │ ┌───────────────────────────────────────────────────────┐ │
│ ▸ NAT    │ │ ⋮ # │Proto│Source     │Dest      │Port │Desc │[⋮]    │ │
│ ▸ Aliases│ │   1 │ TCP │ lan_net   │ wan      │ 443 │ https│ ⋮    │ │
│ ▸ Settin.│ │   2 │ ANY │ alias_geo │ lan_srv  │ *   │ lab  │ ⋮    │ │
│          │ ├───────────────────────────────────────────────────────┤ │
│          │ │ search [_________]   rows 25  « 1 2 3 »               │ │
│          │ └───────────────────────────────────────────────────────┘ │
└──────────┴───────────────────────────────────────────────────────────┘
```

### Edit-Dialog (Regel/Alias)

```
┌──────────────────────────────────────────┐
│  Edit: Firewall Rule             [X]     │
├──────────────────────────────────────────┤
│  (General) (Advanced) (Description)      │ ← Abschnitts-Accordion
│  Action [Pass ▾]  Protocol [TCP ▾]       │
│  Source [network|alias]  [________]      │
├──────────────────────────────────────────┤
│           [Cancel]        [Save]         │
└──────────────────────────────────────────┘
```

### Apply-Zustand

```
┌────────────────────────────────────────────────────────┐
│ ⚠ Changes have been made that require apply.  [Apply]  │
└────────────────────────────────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Top-Menü | Oben | Dashboard, Interfaces, Firewall, VPN, Services, System |
| Submenu/links | Unter Menü | Unterpunkte des gewählten Top-Menüs (plugin-erweiterbar) |
| Page-Kopf | Inhalt oben | Titel, Add-Buttons, Spaltenmenü, Apply-Button (Firewall) |
| Grid | Inhalt mitte | Tabellen mit Suche, Paginierung, `⋮`-Zeilenmenüs |
| Formular-Panels | Inhalt | Akkordeons („General“, „Advanced“) mit Save/Revert |
| Toasts | rechts oben | Erfolg/Fehler/Aktionsergebnisse |
| Benutzer-Menü | rechts oben | Abmelden, Theme, Session-Info |

## UI/UX

### Design-Prinzipien

- **Save ≠ Apply**: Editieren und Aktivieren sind bewusst getrennt (Regelwerk-Integrität)
- **Grids für Masse**: Regeln/Aliases/Logs als durchsuchbare Tabellen, nie als Listenwand
- **Akkordeon-Formulare**: selten genutzte Optionen unter „Advanced“ versteckt
- **Konsistente Controller-Muster**: gleiche Dialogstruktur über fast alle Seiten (MVC-Framework)

### Farbschema und Themes

- Hell/Dunkel per Theme-Auswahl (Benutzermenü, versionabhängig); System- und Plugin-Seiten folgen teils eigenen Themes
- Status: grün = aktiv/erlaubt, rot = blockiert/Fehler, orange = Warnung/ausstehender Apply
- Deko minimal — Info-Dichte vor Farbe

### Interaktionen

- **Regel-Reihenfolge**: Drag & Drop auf Pfeil-Griffen, Reihenfolge = Abarbeitung
- **Grid-Suche**: live gegen Server (`searchPhrase`), Paginierung serverseitig
- **Kopieren/Versetzen**: Duplizieren von Regeln/Aliases über `⋮`-Menüs
- **Toasts und Progress**: längere Aktionen (Apply, Feeds) zeigen Statusmeldungen
- **Autocomplete**: Interface-/Alias-Auswahllisten in Regel-Dialogen
- **Type-ahead-Selects**: Auswahlfelder filtern beim Tippen (große Alias-/Zertifikatslisten)
- **Login-Seite**: Formular mit optionaler 2FA-Abfrage; Fehler erscheinen inline

### Responsive Design

- **Desktop**: Vollayout; Submenu links dauerhaft
- **Schmale Fenster**: Menü kollabiert in Hamburger, Grids scrollen horizontal
- **Mobil**: Kernseiten bedienbar, dichte Regel-Grids bleiben ein Kompromiss (versionabhängig)
- **Kein Offline-Modus**: ohne UI-Zugang bleibt Konsole/CLI

### Zugänglichkeit

- **Tastatur**: Formulare/Dialoge per `Tab`/`Enter`, Accordion-Header fokussierbar; Grid-Zeilenmenüs per `Tab` erreichbar
- **Screenreader**: Dialoge mit Überschrift/ARIA; Grid-Header verknüpft, aber dynamische Teile je nach Version mittelmäßig
- **Fokusanzeige**: sichtbar; Dialoge fangen Fokus ein
- **Sprache**: UI in vielen Sprachen (DE-Übersetzung fast vollständig, versionabhängig)

### Performance

- **Serverseitige Grids**: große Regelwerke bleiben flink, jede Suche ist ein API-ähnlicher Request
- **Dashboard-Polling**: Widgets laden in Intervallen; zu viele Widgets verlängern Ladezeit
- **Apply-Phasen**: pf-Regelladen kann bei riesigen Alias-Feeds spürbar dauern — Toast zeigt Fortschritt
- **Empfehlung**: Feed-Aliases mit „wide“/Duplikat-Bereinigung pflegen, Log-Grids zeitlich filtern

## Siehe auch

- [menu.md](menu.md) - Menüpfade und Rollen
- [features.md](features.md) - Funktionsbereiche
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
- [api.md](api.md) - MVC-API hinter jeder Seite
