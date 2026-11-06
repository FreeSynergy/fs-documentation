# draw.io - Funktionen

## Übersicht

draw.io folgt dem klassischen Zeichenprogramm-Aufbau: Menüleiste, Formbibliothek links, Formatierungs-Panel rechts, Leinwand mit Seiten unten. Die Funktionen gliedern sich in Zeichenwerkzeuge, Formbibliotheken, Objektmodell, Zusammenarbeit, Dateien/Export und Einbettung.

---

## 1. Bearbeiten und Leinwand

- **Seiten**: mehrere Seiten je Datei, Tabs unten, eigene Hintergrundfarben (Extras > Seiten)
- **Raster und Führungen**: magnetisches Einrasten, orangefarbene Ausrichtungs-Linien, Seitenränder
- **Verbindungspunkte**: Formen zeigen Ein-/Ausgänge beim Überfahren; Kanten stehen orthogonal oder kurvenbasiert
- **Kantenhüpfchen** (Line jumps): überschneidende Linien machen sichtbare Bögen
- **Gruppierung und Container**: Formen können andere Formen enthalten (Gruppen, Swimlanes, Frames)
- **Stil-Editor**: jeder Formstil ist eine lesbare Stil-Zeichenkette (`rounded=1;fillColor=#dae8fc;...`)

## 2. Formbibliotheken

- **Standardordner**: General, Arrows, Basic, BPMN, Flowchart, UML, Network, Mockup, ER
- **Cloud- und Anbieter-Sets**: AWS, Azure, GCP, Kubernetes, Cisco, Citrix, F5, NetApp, OpenStack, VMware
- **Umschalten** über „Weitere Formen“ unten links; Bibliotheken einklappbar
- **Eigene Formen**: aus SVG/PNG erstellen und in der persönlichen Seitenleiste speichern
- **Formsuche**: Suchfeld links oben findet Formen über alle aktiven Bibliotheken

## 3. Objektmodell (mxCell)

- Ein Diagramm besteht aus Zellen: `vertex` (Formen), `edge` (Kanten) und Zell-Texten
- Kanten referenzieren `source` und `target` und hängen sich beim Verschieben mit
- Parent-Beziehungen bilden Gruppen und Container (`parent`-Attribut)
- Stil als String, Geometrie als Rechteck (`x`, `y`, `width`, `height`) im XML
- **Daten-Anhänge**: Zellen können benutzerdefinierte Attribute tragen (Bearbeiten > Daten bearbeiten) — nützlich für Auswertung und Generated Diagrams

## 4. Echtzeit-Synchronisation und Zusammenarbeit

- **Realtime Sync** (Extras-Menü): alle Bearbeitungsschritte einer Cloud-Datei werden gemeinsam gesehen (versionsabhängig)
- **Versionen** (Datei > Versionen): Historie des Cloud-Speichers, Vergleich und Wiederherstellung
- Berechtigungen kommen vom Speicher (Google Drive, OneDrive, GitHub): Wer die Datei ändern darf, darf sie ändern
- Kein Ende-zu-Ende-Schutz: Inhalt liegt lesbar beim Speicheranbieter, sofern nicht verschlüsselt

## 5. Dateien und Export

- **Format**: `.drawio` bzw. `.xml` (wahlweise komprimiert), `.drawio.png`/`.drawio.svg` mit eingebettetem Diagramm
- **Export**: PNG, JPEG, SVG, PDF, HTML, XML, VSDX (Import und Export für Microsoft Visio-Dateien)
- **Auto-Save** auf Cloud-Speicher aktivierbar
- **Drucken** inklusive Seitenumbruch-Vorschau; „Umblatten“ großer Diagramme

## 6. Einbettung und Plugins

- **iframe-Einbettung**: `https://embed.draw.io/?embed=1&proto=json` mit dokumentiertem postMessage-Austausch (laden, speichern, exportieren)
- **URL-Parameter**: Oberfläche reduzieren (`chrome=0`), Theme, Bibliotheken, Dark Mode — Liste in den offiziellen FAQs
- **JS-Plugins**: eigene Skripte, die den Editor zur Laufzeit erweitern (Repository-Beispiele enthalten)
- **Integrationen**: Confluence- und Jira-Apps von draw.io, GitHub-/GitLab-Bearbeitung per Link

## Konfiguration

- **Zusätzliche Konfiguration**: JSON-Objekte für Storage-Keys, erlaubte Dienste und UI-Optionen (Configure-Seite der selbst gehosteten Instanz, `configure.js` für die Desktop-/Web-App)
- **Storage-Client-Keys**: eigener Google-/Microsoft-/Dropbox-OAuth-Client für produktive Umgebungen
- **Erscheinungsbild**: Theme hell/dunkel (versionsabhängig), Sprache über Extras
- **Desktop-Version**: Dateiverknüpfungen und Auto-Update über die Electron-Einstellungen

### Daten und Automatisierung

- Zell-Attribute als Datenanhänge (Bearbeiten > Daten bearbeiten)
- **CSV-/XML-Import**: Diagramme aus Tabellen erzeugen (Extras-Menü, versionsabhängig)
- Batch-Export über die Desktop-CLI für CI-Pipelines
- Stil-Vorgaben für Organisationen über Konfigurationsdateien

---

## Vergleich mit den Nachbarn

| Kriterium | draw.io | Excalidraw | tldraw |
|-----------|---------|------------|--------|
| Stil | technisch-exakt | handgezeichnet | clean, flott |
| Format | XML (`.drawio`) | JSON (`.excalidraw`) | Snapshot-JSON |
| Formbibliotheken | sehr groß, Cloud-Sets | klein + Bibliotheken | Grundformen, erweiterbar per SDK |
| Kollaboration | Realtime-Sync (Cloud) | E2E-verschlüsselte Räume | Sync-Server/Cloud (SDK) |
| Öffentliche API | ❌ (Einbettung/CLI) | ❌ (Datei/SDK) | ❌ (SDK/Sync) |
| Rolle | Standard-Diagramme | Skizzen | Baustein für eigene Apps |

---

## Was draw.io NICHT kann

- **Keine Moderation**: keine Abstimmungen, Timer, Kommentare im Board (das bietet Miro)
- **Keine öffentliche REST-API**: Diagramme werden über Dateien, Einbettung und Plugins gesteuert (siehe [api.md](api.md))
- **Keine Webhooks**: Änderungen lösen keine externen Signale aus
- **Kein Skizzen-Stil**: Zeichenfläche ist technisch, nicht handschriftlich (dafür Excalidraw)
- **Kein Rechte-Management in der App**: Rollen stammen aus dem Cloud-Speicher
- **Kein Ende-zu-Ende-Schutz**: Dateien liegen lesbar beim Speicheranbieter
- **Keine echte Mehrzeichenfläche**: draw.io ist Seiten-, kein Whiteboard-Denken (wenig Freihand, keine Notizzettel-Kultur)

## Module und Integrationen

- **Google Drive / OneDrive / Dropbox / GitHub / GitLab / Trello**: direkte Speicher- und Öffnen-Dialoge
- **draw.io für Confluence und Jira**: Diagramme als Attachments direkt in Atlassian-Seiten
- **GitHub-Actions-Workflows** (Community): automatischer PNG/SVG-Export aus Repositories
- **Community-CLI-Werkzeuge**: Batch-Export und Konvertierung (Details in [api.md](api.md))

## Erweiterungen und Plugins

- **Plugin-API (JavaScript)**: Menüs, Aktionen und Automatisierung zur Laufzeit; Beispiele im Quellcode-Ordner `plugins/`
- **Eigene Form-Sets** als `.shape`-Dateien definieren
- **Styles und Themes** über Konfigurationsdateien vorgeben (Organisations-Vorgaben)
