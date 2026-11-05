# VSCodium - API Documentation

## Overview
VSCodium is an open-source version of Visual Studio Code. Its API is mainly
available through the VS Code extension API, which makes it possible to extend
the editor functions, the code intelligence and the UI elements.

## Authentication
VSCodium itself has no authentication API, because it runs locally. The
extension APIs use:
- **No authentication**: local extensions have full access
- **OAuth2**: for cloud-based extensions (GitHub, Azure DevOps, etc.)

## Endpoints (extension API)

### Extension API (TypeScript)
VSCodium exposes the VS Code extension API through the `vscode` module:

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

#### Language server
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

## Examples

### Basic extension
```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    // Register the command
    let disposable = vscode.commands.registerCommand('helloWorld.hello', async () => {
        vscode.window.showInformationMessage('Hello from VSCodium!');
    });

    context.subscriptions.push(disposable);

    // Completion provider
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

### Status bar item
```typescript
const statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
statusBarItem.text = '$(info) VSCodium API';
statusBarItem.tooltip = 'Status info';
statusBarItem.show();

// Update
statusBarItem.text = '$(check) Ready';
```

### Quick pick
```typescript
const selection = await vscode.window.showQuickPick(
    ['Option 1', 'Option 2', 'Option 3'],
    { placeHolder: 'Choose an option' }
);
```

### Webview
```typescript
const panel = vscode.window.createWebviewPanel(
    'myView',
    'My view',
    vscode.ViewColumn.One,
    { enableScripts: true, retainContextWhenHidden: true }
);

panel.webview.html = `
    <!DOCTYPE html>
    <html>
    <body>
        <h1>VSCodium webview</h1>
        <button id="btn">Click me</button>
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
    name: 'My terminal',
    shellPath: '/bin/bash'
});
terminal.show();
terminal.sendText('npm start');
```

## Rate limits
- No rate limits for local use
- The extension APIs have no built-in limit

## Webhooks
VSCodium has no built-in webhook system. Extensions can:
- listen to file system events: `vscode.workspace.onDidCreateFiles`
- watch the terminal output
- start an HTTP server inside an extension

## SDKs and client libraries
- **TypeScript/JavaScript**: `@types/vscode` (type definitions)
- **Python**: `vscode-python` (Python extension API)
- **.NET**: `OmniSharp` (Language Server Protocol)

Install:
```bash
# Type definitions
npm install --save-dev @types/vscode

# Extension scaffold
npm install -g yo generator-code
yo code
```

## API references
- **Extension API**: https://code.visualstudio.com/api
- **Language Server Protocol**: https://microsoft.github.io/language-server-protocol/
- **Webview UI**: https://code.visualstudio.com/api/extension-guides/webview

## See also
- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
