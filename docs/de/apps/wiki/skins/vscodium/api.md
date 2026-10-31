# Vscodium - API Dokumentation

## Übersicht
Vscodium ist eine Open-Source Version von Visual Studio Code. Die API ist hauptsächlich über die VS Code Extension API verfügbar, die es ermöglicht, Editor-Funktionen, Code-Intelligenz und UI-Elemente zu erweitern.

## Authentifizierung
Vscodium selbst hat keine Authentifizierungs-API, da es lokal ausgeführt wird. Extension APIs verwenden:
- **Keine Authentifizierung**: Lokale Extensions haben vollen Zugriff
- **OAuth2**: Für Cloud-basierte Extensions (GitHub, Azure DevOps, etc.)

## Endpunkte (Extension API)

### Extension API (TypeScript)
Vscodium expose die VS Code Extension API über das `vscode` Modul:

#### Commands
```typescript
vscode.commands.registerCommand('extension.commandName', callback)
vscode.commands.executeCommand('extension.commandName')
```

#### Editor
```typescript
vscode.window.activeTextEditor
vscode.window.createTextEditorDecorationType(options)
vscode.workspace.openTextDocument(uri)
```

#### Workspace
```typescript
vscode.workspace.workspaceFolders
vscode.workspace.onDidChangeWorkspaceFolders
vscode.workspace.onDidSaveTextDocument
```

#### UI
```typescript
vscode.window.showInformationMessage(message, ...actions)
vscode.window.showQuickPick(items, options)
vscode.window.createStatusBarItem()
```

#### Language Server
```typescript
vscode.languages.registerCompletionItemProvider(selector, provider)
vscode.languages.registerDefinitionProvider(selector, provider)
vscode.languages.registerHoverProvider(selector, provider)
```

#### Terminal
```typescript
vscode.window.createTerminal(options)
vscode.window.activeTerminal
```

### Debugging API
```typescript
vscode.debug.startDebugging(workspaceFolder, config)
vscode.debug.onDidStartDebugSession
vscode.debug.onDidTerminateDebugSession
```

### Settings API
```typescript
vscode.workspace.getConfiguration()
vscode.workspace.updateWorkspaceFolders()
```

### Tasks
```typescript
vscode.tasks.registerTaskProvider(type, provider)
vscode.tasks.executeTask(task)
```

## Beispiele

### Basic Extension
```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    // Command registrieren
    let disposable = vscode.commands.registerCommand('helloWorld.hello', async () => {
        vscode.window.showInformationMessage('Hallo von Vscodium!');
    });

    context.subscriptions.push(disposable);

    // Completion Provider
    let provider = vscode.languages.registerCompletionItemProvider('typescript', {
        provideCompletionItems(document, position) {
            return [
                new vscode.CompletionItem('vscode', vscode.CompletionItemKind.Keyword),
                new vscode.CompletionItem('api', vscode.CompletionItemKind.Text)
            ];
        }
    });

    context.subscriptions.push(provider);
}

export function deactivate() {}
```

### Status Bar Item
```typescript
const statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
statusBarItem.text = '$(info) Vscodium API';
statusBarItem.tooltip = 'Status Info';
statusBarItem.show();

// Update
statusBarItem.text = '$(check) Bereit';
```

### Quick Pick
```typescript
const selection = await vscode.window.showQuickPick(
    ['Option 1', 'Option 2', 'Option 3'],
    { placeHolder: 'Wähle eine Option' }
);
```

### Webview
```typescript
const panel = vscode.window.createWebviewPanel(
    'myView',
    'Meine Ansicht',
    vscode.ViewColumn.One,
    { enableScripts: true, retainContextWhenHidden: true }
);

panel.webview.html = `
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Vscodium Webview</h1>
        <button id="btn">Klick mich</button>
        <script>
            const vscode = acquireVsCodeApi();
            document.getElementById('btn').addEventListener('click', () => {
                vscode.postMessage({ command: 'click' });
            });
        </script>
    </body>
    </html>
`;
```

### Terminal
```typescript
const terminal = vscode.window.createTerminal({
    name: 'Mein Terminal',
    shellPath: '/bin/bash'
});
terminal.show();
terminal.sendText('npm start');
```

## Rate Limits
- Keine Rate Limits für lokalen Einsatz
- Extension APIs haben keine eingebaute Begrenzung

## Webhooks
Vscodium hat kein eingebautes Webhook-System. Extensions können:
- File system events hören: `vscode.workspace.onDidCreateFiles`
- Terminal output überwachen
- HTTP Server in Extensions starten

## SDKs und Client-Bibliotheken
- **TypeScript/JavaScript**: `@types/vscode` (Type Definitions)
- **Python**: `vscode-python` (Python Extension API)
- **.NET**: `OmniSharp` (Language Server Protocol)

Installieren:
```bash
# Type Definitions
npm install --save-dev @types/vscode

# Extension Scaffold
npm install -g yo generator-code
yo code
```

## API References
- **Extension API**: https://code.visualstudio.com/api
- **Language Server Protocol**: https://microsoft.github.io/language-server-protocol/
- **Webview UI**: https://code.visualstudio.com/api/extension-guides/webview

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
