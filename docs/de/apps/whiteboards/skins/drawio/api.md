# draw.io - API Dokumentation

## Übersicht

draw.io hat **keine öffentliche REST-API** für Diagramme. Die dokumentierten Schnittstellen sind: das XML-Dateiformat, das **postMessage-Protokoll der iframe-Einbettung**, **URL-Parameter**, die **JavaScript-Plugin-API** und die **Kommandozeile der Desktop-Version**. Cloud-Speicher (Google Drive, OneDrive, Dropbox) werden über deren eigene, externe APIs angebunden.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST-API | — | ❌ Nicht vorhanden |
| postMessage (iframe-Einbettung) | Laden, Speichern, Exportieren aus fremdem UI | Öffentlich dokumentiert |
| URL-Parameter | UI steuern, Datei laden (`url=`, `embed=1`, …) | Öffentlich dokumentiert (FAQ-Liste) |
| JS-Plugins | Editor zur Laufzeit erweitern | Dokumentiert (Beispiele im Repo) |
| CLI `drawio` (Desktop) | Batch-Export PNG/SVG/PDF | Dokumentiert |
| Dateiformat `.drawio` | Diagramm-Austausch | Öffentlich dokumentiert |
| Webhooks | — | ❌ Nicht vorhanden |

## Authentifizierung

- **App selbst**: keine Nutzerkonten, keine Tokens — draw.io kann allein nicht authentifizieren
- **Cloud-Speicher**: OAuth 2.0 für Google Drive, Microsoft OneDrive, Dropbox beim Verbinden; produktive Installationen brauchen eigene Client-IDs (Configure-Bereich)
- **Eingebettete Instanz**: die Wirtsanwendung kümmert sich um Login und Dateirechte, draw.io erhält Inhalt per postMessage
- **Self-Hosted**: Standardinstallation ist ungeschützt; Zugangsschutz über Reverse Proxy/SSO selbst einrichten

## Einbettungs-Protokoll (postMessage)

Hostseite und draw.io-iframe tauschen JSON-Nachrichten (`proto=json`). Die actions und events sind wie folgt dokumentiert (Details und Zusatzfelder versionsabhängig):

| Richtung | Nachricht (action/event) | Beschreibung |
|----------|--------------------------|--------------|
| Host → draw.io | `init` | Handshake nach dem Laden |
| Host → draw.io | `load` | Diagramm-XML in den Editor laden |
| Host → draw.io | `save` | Aktuell bearbeitetes Diagramm anfordern |
| Host → draw.io | `export` | Export anfordern (PNG, SVG, PDF …) |
| draw.io → Host | `load` | Editor bereit, enthält ggf. geladenes XML |
| draw.io → Host | `save`  Aktualisiertes Diagramm-XML |
| draw.io → Host | `export` | Exportiertes Bild (meist base64-kodiert) |
| draw.io → Host | `exit` | Nutzer möchte den Editor schließen |

### Beispiel: Host-Seite empfängt ein Diagramm

```html
<iframe id="d" src="https://embed.draw.io/?embed=1&proto=json&spin=1"></iframe>
<script>
  const frame = document.getElementById('d');
  window.addEventListener('message', (evt) => {
    const msg = JSON.parse(evt.data);
    if (msg.action === 'load') {
      frame.contentWindow.postMessage(
        JSON.stringify({ action: 'load', xml: '<mxfile>...</mxfile>' }), '*');
    }
    if (msg.action === 'save') {
      localStorage.setItem('diagramm', msg.xml);
    }
  });
</script>
```

### Gängige URL-Parameter

| Parameter | Wirkung |
|-----------|---------|
| `embed=1` | Einbettungsmodus (eigene Kopfzeile aus) |
| `proto=json` | postMessage im JSON-Format |
| `chrome=0` | Seitenleiste und Menüs aus |
| `noSaveBtn=1`, `noExitBtn=1` | Buttons ausblenden |
| `libraries=1` | Bibliotheken ein-/ausblenden |
| `dark=1` | dunkle Oberfläche (versionsabhängig) |
| `url=<adresse>` | Diagramm von URL öffnen |
| `ui=…` | Oberflächenvariante (z. B. reduced) |

Die vollständige Liste führt die offizielle FAQ „Known URL parameters“ (www.drawio.com).

## Dateiformat (XML)

```xml
<mxfile host="embed.draw.io">
  <diagram id="seite-1" name="Ablauf">
    <mxGraphModel dx="800" dy="600" grid="1" page="1">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="2" value="Anfrage" style="rounded=1;fillColor=#dae8fc;"
                vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="3" value="" style="edgeStyle=orthogonalEdgeStyle;"
                edge="1" parent="1" source="2" target="4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="4" value="Antwort" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="240" y="40" width="120" height="60" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## CLI-Beispiele (Desktop-Version)

```bash
# PNG-Export ohne GUI
drawio -x -f png -o ablauf.png ablauf.drawio

# alle Seiten als SVG, eingebettet ins PNG (editierbares Diagramm)
drawio -x -e -f png -o ablauf.drawio.png ablauf.drawio

# Self-Hosted-Instanz starten und Erreichbarkeit prüfen
docker run -d --name drawio -p 8080:8080 jgraph/drawio
curl -I http://localhost:8080/
```

Die Flag-Namen (`-x`, `-f`, `-o`, `-p`, `-b`, `-s`) entsprechen der Desktop-Dokumentation; Details versionsabhängig.

### Export-Anfrage an den eingebetteten Editor

```json
{ "action": "export", "format": "svg" }
```

Der Editor antwortet mit einer `export`-Nachricht; der Bildinhalt kommt je nach Format als Text oder base64-kodierter Datenstrom an.

## Plugin-Gerüst (JavaScript)

Eigene Plugins sind einfache Skripte, die den laufenden Editor erweitern (für selbst gehostete Instanzen; Ablage und Aktivierung versionsabhängig):

```javascript
// Gerüst nach Vorbild der Beispiel-Plugins im Quellcode
function init(uiEditor) {
  const graph = uiEditor.getGraph();
  // eigene Menüpunkte, Aktionen oder Automatisierungen hier anlegen
}
```

## Rate Limits

- draw.io selbst kennt **keine API-Kontingente** (statische Auslieferung)
- Es gelten die Limits der angebundenen Speicher (Google-/Microsoft-/Dropbox-APIs)

## Webhooks

❌ Nicht vorhanden. Änderungen an `.drawio`-Dateien lassen sich nur am Speichersystem beobachten (Drive-Push, Git-Hooks, Ordner-Überwachung).

## SDKs und Client-Bibliotheken

- **Offiziell**: keine SDK-Pakete; mxGraph ist die zugrunde liegende, quelloffene Zeichenbibliothek
- **`drawio`-Desktop-CLI**: offizieller Batch-Export (in Electron-Version enthalten)
- **Community**: Python-Bibliotheken zum Schreiben von `.drawio`-Dateien (z. B. drawpyo), Docker-/CLI-Exportwerkzeuge von Dritten (Qualität und Stand prüfen)

## Siehe auch

- [description.md](description.md)
- [menu.md](menu.md)
- [features.md](features.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
