# LaunchBoard - Beschreibung

## Übersicht

LaunchBoard richtet sich an Nutzer und kleine Teams, die ein hübsches Homelab-Dashboard **ohne YAML und ohne Quellcode** bauen wollen. Der Lieferumfang ist identisch, egal ob die Instanz beim Anbieter läuft oder im eigenen Docker-Container: Board-Editor, Widget-Bibliothek, Integrationsverwaltung und Benutzerverwaltung mit Single-Sign-On.

## Was LaunchBoard macht

LaunchBoard verwaltet **Boards** (Benutzerführungsoberflächen aus Kacheln) in einer mitgelieferten Datenbank. Im **Drag-&-Drop-Editor** entstehen Layouts aus App-Kacheln, Statusanzeigen, Diagrammen und Textblöcken; eine Widget-Bibliothek liefert vorgefertigte Bausteine. **Integrationen** hinterlegen URL und Schlüssel eines Dienstes; Widgets zeigen anschließend Live-Werte an und lösen bei unterstützten Diensten Aktionen aus (Container neu starten, Download pausieren). Der Zugang ist dreistufig: lokale Konten, OAuth2/OIDC gegen einen bestehenden Identity-Provider (Authentik, Keycloak, Entra ID, Google) oder eine geschützte Cloud-URL des Anbieters. Rollen bestimmen, wer Boards bauen darf und wer nur ansieht. Betrieb, Updates und bei der Cloud-Variante auch TLS übernimmt der Anbieter.

## Vorteile

- **Kein Config-Datei-Chaos**: alles per Maus, Boards und Widgets in der Datenbank
- **Schnell schön**: professionelle Vorlagen, Themes und Icon-Bibliotheken ab Werk
- **Single-Sign-On inklusive**: OAuth2/OIDC ist Kernfunktion, nicht Nachrüstung
- **Zwei Betriebswege**: Cloud-Abo für Minimalbetrieb, Container für Datenhoheit
- **Teamtauglich**: Rollen, Freigaben und geteilte Boards
- **Kommerzieller Support**: Updates, Support-Tickets, dokumentierte Roadmap
- **Aktionen möglich**: einige Integrationen erlauben Eingriffe in Container und Medien-Stacks

## Abgrenzung zu anderen Systemen

### LaunchBoard vs. Homarr
- **Beide** konfigurieren per Maus und speichern in einer Datenbank
- **Homarr** ist quelloffen und kostenlos, **LaunchBoard** proprietär mit Abo-Modell
- **Homarr** hat eine öffentliche tRPC-Referenz, **LaunchBoard** keine frei einsehbare API-Doku
- **LaunchBoard** punktet bei Vorlagen und SSO, **Homarr** bei Integrationstiefe im Homelab

### LaunchBoard vs. Heimdall
- **Heimdall** (Laravel, quelloffen) setzt auf App-Kacheln mit optionalen Statistiken, **LaunchBoard** auf einen vollen Widget-Editor
- **Heimdall** ohne nennenswerte Rechteverwaltung, **LaunchBoard** mit Rollen und Freigaben
- **Heimdall** kostenlos und selbst gehostet, **LaunchBoard** kostenpflichtig, optional als Cloud-Dienst

### LaunchBoard vs. Homer
- **Homer** ist eine statische, YAML-konfigurierte Seite ohne Login; **LaunchBoard** ist eine Anwendung mit Datenbank, Editor und Anmeldung
- **Homer** kostenlos und ohne Aktionen, **LaunchBoard** interaktiv mit Integrationen
- **Homer** passt zu minimalen Ansprüchen, **LaunchBoard** für Komfort und Teamnutzung

### LaunchBoard vs. Dashy
- **Dashy** konfiguriert `conf.yml` (optional mit UI-Editor) und ist quelloffen, **LaunchBoard** ausschließlich grafisch
- **Dashy** mit sehr weitreichendem Theme-System und eigener Widget-Syntax, **LaunchBoard** mit kuratierten Widgets und Themes
- **Dashy** ohne Support, **LaunchBoard** mit kommerziellem Support und Lizenzbedingungen je Tarif

## Technische Details

- **Backend**: proprietäre Server-Anwendung (nicht im Quelltext veröffentlicht); mitgelieferte relationale Datenbank im Container, bei der Cloud-Variante verwaltet durch den Anbieter
- **Database**: vorhanden – Boards, Widgets, Integrationen, Nutzer und Rollen werden persistiert; genaues Datenbanksystem laut Anbieterdoku im Kundenportal (**nicht öffentlich dokumentiert**)
- **Frontend**: moderne Web-Client-Oberfläche mit Drag-&-Drop-Editor, responsive Darstellung, eigener Theme-Engine
- **Authentication**: lokale Konten mit Passwort, **OAuth2/OIDC** (Authentik, Keycloak, Entra ID, Google, Generic OIDC), optional Header-Auth hinter einem Reverse Proxy; Rollen (Administrator, Editor, Betrachter)
- **Hosting**: Cloud-Abo (Subdomain des Anbieters, TLS und Updates inklusive) **oder** eigener Container (Docker/Compose, Port per Umgebungsvariable, HTTPS über Reverse Proxy); Lizenz/Subscription pro Instanz

## Für wen ist LaunchBoard geeignet?

- **Familien und kleine Teams**, die ein gepflegtes Dashboard mit SSO und getrennten Rechten brauchen
- **Nutzer ohne Lust auf YAML**, die Boards per Maus bauen und Vorlagen verwenden wollen
- **Betriebe, die Support erwarten** und dafür eine Lizenz akzeptieren
- **Weniger geeignet** für quelloffene Umgebungen, für Umgebungen ohne Datenbank und für alle, die ihre Dashboard-Definition in Git versionieren wollen (dann Homepage oder Homer)
