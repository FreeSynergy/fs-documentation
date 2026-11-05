# draw.io - API documentation

## Overview

draw.io has **no public REST API** for diagrams. The documented interfaces are: the XML file format, the **postMessage protocol of the iframe embedding**, **URL parameters**, the **JavaScript plugin API** and the **command line of the desktop version**. Cloud storages (Google Drive, OneDrive, Dropbox) are attached through their own external APIs.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST API | — | ❌ Not available |
| postMessage (iframe embedding) | Load, save, export from a third-party UI | Publicly documented |
| URL parameters | Control the UI, load a file (`url=`, `embed=1`, …) | Publicly documented (FAQ list) |
| JS plugins | Extend the editor at runtime | Documented (examples in the repo) |
| CLI `drawio` (desktop) | Batch export PNG/SVG/PDF | Documented |
| File format `.drawio` | Diagram exchange | Publicly documented |
| Webhooks | — | ❌ Not available |

## Authentication

- **The app itself**: no user accounts, no tokens — draw.io cannot authenticate on its own
- **Cloud storages**: OAuth 2.0 for Google Drive, Microsoft OneDrive and Dropbox when connecting; productive installations need their own client IDs (Configure area)
- **Embedded instance**: the host application takes care of login and file permissions, draw.io receives content via postMessage
- **Self-hosted**: the standard installation is unprotected; set up access protection yourself via reverse proxy/SSO

## Embedding protocol (postMessage)

The host page and the draw.io iframe exchange JSON messages (`proto=json`). The actions and events are documented as follows (details and extra fields version-dependent):

| Direction | Message (action/event) | Description |
|-----------|------------------------|-------------|
| Host → draw.io | `init` | Handshake after loading |
| Host → draw.io | `load` | Load the diagram XML into the editor |
| Host → draw.io | `save` | Request the currently edited diagram |
| Host → draw.io | `export` | Request an export (PNG, SVG, PDF …) |
| draw.io → Host | `load` | Editor is ready, possibly contains the loaded XML |
| draw.io → Host | `save` | Updated diagram XML |
| draw.io → Host | `export` | Exported image (usually base64-encoded) |
| draw.io → Host | `exit` | The user wants to close the editor |

### Example: the host page receives a diagram

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
      localStorage.setItem('diagram', msg.xml);
    }
  });
</script>
```

### Common URL parameters

| Parameter | Effect |
|-----------|--------|
| `embed=1` | Embedding mode (own header off) |
| `proto=json` | postMessage in JSON format |
| `chrome=0` | Sidebar and menus off |
| `noSaveBtn=1`, `noExitBtn=1` | Hide buttons |
| `libraries=1` | Show/hide libraries |
| `dark=1` | Dark interface (version-dependent) |
| `url=<address>` | Open a diagram from a URL |
| `ui=…` | Interface variant (e.g. reduced) |

The complete list is in the official FAQ "Known URL parameters" (www.drawio.com).

## File format (XML)

```xml
<mxfile host="embed.draw.io">
  <diagram id="page-1" name="Flow">
    <mxGraphModel dx="800" dy="600" grid="1" page="1">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="2" value="Request" style="rounded=1;fillColor=#dae8fc;"
                vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="3" value="" style="edgeStyle=orthogonalEdgeStyle;"
                edge="1" parent="1" source="2" target="4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="4" value="Response" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="240" y="40" width="120" height="60" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## CLI examples (desktop version)

```bash
# PNG export without a GUI
drawio -x -f png -o flow.png flow.drawio

# all pages as SVG, embedded in the PNG (editable diagram)
drawio -x -e -f png -o flow.drawio.png flow.drawio

# start a self-hosted instance and check reachability
docker run -d --name drawio -p 8080:8080 jgraph/drawio
curl -I http://localhost:8080/
```

The flag names (`-x`, `-f`, `-o`, `-p`, `-b`, `-s`) match the desktop documentation; details are version-dependent.

### Export request to the embedded editor

```json
{ "action": "export", "format": "svg" }
```

The editor answers with an `export` message; the image content arrives as text or as a base64-encoded data stream depending on the format.

## Plugin scaffold (JavaScript)

Own plugins are simple scripts that extend the running editor (for self-hosted instances; location and activation are version-dependent):

```javascript
// Scaffold following the example plugins in the source
function init(uiEditor) {
  const graph = uiEditor.getGraph();
  // create your own menu items, actions or automations here
}
```

## Rate limits

- draw.io itself knows **no API quotas** (static delivery)
- The limits of the attached storages apply (Google/Microsoft/Dropbox APIs)

## Webhooks

❌ Not available. Changes to `.drawio` files can only be observed on the storage system (Drive push, Git hooks, folder watching).

## SDKs and client libraries

- **Officially**: no SDK packages; mxGraph is the underlying open-source drawing library
- **`drawio` desktop CLI**: the official batch export (included in the Electron version)
- **Community**: Python libraries for writing `.drawio` files (e.g. drawpyo), third-party Docker/CLI export tools (check quality and currency)

## See also

- [description.md](description.md)
- [menus.md](menus.md)
- [features.md](features.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
