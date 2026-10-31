# gethomepage (Bibliothek) - Kommandos statt Shortcuts

## Übersicht

Für eine Bibliotheksschicht ohne Oberfläche gibt es **keine Tastatur-Shortcuts**. Stattdessen ist diese Datei das Nachschlagewerk für **Build-, Dev-, Test- und Container-Kommandos** sowie für die Umgebungsvariablen, die das Verhalten der Clients steuern. Alle Kommandos laufen im Repository `gethomepage/homepage` (Node.js ≥ aktuelle LTS, Paketmanager ist **pnpm** – ein `preinstall`-Hook erzwingt das).

---

## Tastenkürzel (Kurzprüfung)

Die Schicht läuft im Terminal und im Node-Prozess, deshalb gibt es **keine Tastatur-Shortcuts**; die mögliche Tastatur ist die des eingesetzten Terminals.

| Shortcut | Funktion |
|----------|----------|
| `Ctrl+C` | laufenden Dev-Server oder Testlauf abbrechen |
| `q` (im Watch-Modus von Vitest) | Testbeobachtung beenden |
| `a` (im Watch-Modus von Vitest) | alle Tests erneut ausführen |
| `Strg+Shift+P` | ❌ Nicht vorhanden – keine Befehlspalette einer Oberfläche |
| `F5` | ❌ Nicht vorhanden – kein Anzeigefenster dieser Schicht |

---

## Einrichtung (einmalig)

| Kommando | Funktion |
|----------|----------|
| `corepack enable` | pnpm über Node.js bereitstellen |
| `pnpm install` | Abhängigkeiten installieren |
| `pnpm install --frozen-lockfile` | exakt die Versionen des Lockfiles (CI) |
| `cp -r src/skeleton config` | Beispielkonfiguration anlegen (lokal) |
| `node -v` | Node-Version prüfen |
| `pnpm -v` | pnpm-Version prüfen |

**Hinweis**: `npm install` bricht ab, weil `preinstall: npx only-allow pnpm` andere Paketmanager verhindert.

---

## Entwicklung

| Kommando | Funktion |
|----------|----------|
| `pnpm dev` | Next.js-Dev-Server auf Port 3000, Reload bei Codeänderung |
| `pnpm dev -p 3001` | Dev-Server auf anderer Port |
| `pnpm start` | Produktiver Server nach `pnpm build` |
| `pnpm build` | Produktionsbuild (`next build --webpack`) |
| `pnpm telemetry disable` | Next.js-Telemetrie abschalten |
| `PORT=4000 pnpm start` | Port für den laufenden Server setzen |
| `HOMEPAGE_ALLOWED_HOSTS=localhost:3000 pnpm dev` | Host-Prüfung lokal erfüllen |

---

## Tests und Qualität

| Kommando | Funktion |
|----------|----------|
| `pnpm test` | alle Tests (Vitest) ausführen |
| `pnpm test:watch` | Tests bei Änderungen erneut ausführen |
| `pnpm test:coverage` | Tests mit Abdeckungsbericht |
| `pnpm vitest run src/utils/proxy` | nur Tests eines Bereichs |
| `pnpm vitest run -t "pihole"` | nur Tests mit passendem Namen |
| `pnpm lint` | ESLint über den ganzen Quellbaum |
| `npx prettier --write src/widgets/<dienst>` | Datei formatieren |
| `npx eslint src/pages/api/services/proxy.js` | eine Datei prüfen |

**Testablage**: Tests liegen neben der Quelle (`widget.test.js`, `proxy.test.js`, `component.test.jsx`) – neue Module brauchen passende Testdateien.

---

## Container und Deployment

| Kommando | Funktion |
|----------|----------|
| `docker build -t homepage:dev .` | lokales Image bauen |
| `docker run -p 3000:3000 -v $PWD/config:/app/config homepage:dev` | mit lokaler Config starten |
| `docker run -p 3000:3000 -v /var/run/docker.sock:/var/run/docker.sock:ro …` | Docker-Erkennung aktivieren |
| `docker compose up -d` | mit Compose-Datei starten |
| `docker compose logs -f homepage` | Handler- und Config-Log beobachten |
| `docker exec -it homepage sh` | in den Container wechseln |
| `docker logs homepage 2>&1 \| grep servicesProxy` | nur Proxy-Entscheidungen ansehen |
| `kubectl apply -f k8s.yaml` | Deployment im Cluster (Vorlage im Repository) |

---

## Konfigurationsprüfung (läuft über die Anwendung)

| Kommando / Endpunkt | Funktion |
|--------------------|----------|
| `curl -s localhost:3000/api/validate` | YAML-Fehler mit Datei und Zeile |
| `curl -s localhost:3000/api/hash` | Hashes der Config-Dateien (Änderungserkennung) |
| `curl -s localhost:3000/api/revalidate` | Dashboard-Cache verwerfen |
| `curl -s localhost:3000/api/healthcheck` | Liefert `up` |
| `curl -s "localhost:3000/api/services/proxy?group=…&service=…&index=0"` | Client-Aufruf direkt testen |
| `curl -s "localhost:3000/api/siteMonitor?groupName=…&serviceName=…"` | Erreichbarkeit einer Kachel testen |

---

## Dokumentationsarbeiten

| Kommando | Funktion |
|----------|----------|
| `pip install -r requirements.txt` | Abhängigkeiten der Projektdoku (mkdocs) |
| `mkdocs serve` | Doku lokal Vorschau |
| `mkdocs build` | Doku bauen |
| `pnpm i18n` / Crowdin-Datei `crowdin.yml` | Übersetzungen synchronisieren (Projektstandard) |

---

## Umgebungsvariablen der Schicht

| Variable | Funktion |
|----------|----------|
| `HOMEPAGE_ALLOWED_HOSTS` | erlaubte `Host`-Header, sonst `400` |
| `HOMEPAGE_VAR_*` | Wert-Ersetzung in Config-Dateien |
| `HOMEPAGE_FILE_*` | Dateiinhalt als Ersetzung |
| `HOMEPAGE_AUTH_ENABLED` | Sitzungsprüfung für die Routen aktivieren |
| `NEXTAUTH_SECRET` / `HOMEPAGE_AUTH_SECRET` | Signatur der Sitzung |
| `NEXTAUTH_URL` / `HOMEPAGE_EXTERNAL_URL` | Cookie-Eigenschaften (Secure) |
| `HOMEPAGE_MCP_ENABLED` / `HOMEPAGE_MCP_TOKEN` | MCP-Endpunkt und Token |
| `PUID` / `PGID` | Benutzer/Gruppe im Container |
| `PORT` | Port des Servers |

---

## Wartung nach einem Update

| Schritt | Kommando |
|---------|----------|
| Changes lesen | Release-Notes des Repository prüfen |
| Image tauschen | `docker compose pull && docker compose up -d` |
| Config prüfen | `curl -s localhost:3000/api/validate` |
| Clients prüfen | Log auf neue `Unknown proxy service type`-Meldungen kontrollieren |
| Tests lokal | `pnpm test` nach eigenem Fork |

---

## Mac-Varianten

Die Kommandos sind plattformunabhängig; unter macOS unterscheiden sich nur Pfade und Socket:

| Kommando | Funktion |
|----------|----------|
| `brew install node pnpm` | Werkzeugkette installieren |
| `-v /var/run/docker.sock:/var/run/docker.sock:ro` | Docker-Socket (Docker Desktop) |
| `open http://localhost:3000` | Seite im Browser öffnen |
| `pbcopy < config/services.yaml` | Config in die Zwischenablage |


---

## Arbeiten am Fork (Git)

| Kommando | Funktion |
|----------|----------|
| `git switch -c feature/<dienst>` | neuen Zweig für ein Dienst-Modul anlegen |
| `git add src/widgets/<dienst>` | neue Dateien vormerken |
| `git commit -m "feat(widgets): <dienst> anbinden"` | Änderung mit Konvention kommentieren |
| `git rebase origin/main` | Fork auf dem aktuellen Stand halten |
| `git push -u origin feature/<dienst>` | Zweig zum Pull Request hochladen |
| `pnpm test && pnpm lint` | Pflichtprüfung vor dem Einreichen |

---

## Zusammenfassung

Statt Shortcuts bietet diese Schicht ein klares Kommando-Set:

- **`pnpm install` / `pnpm dev` / `pnpm build` / `pnpm test`** für den Entwicklungszyklus
- **`docker build` / `docker compose logs`** für Betrieb und Fehlersuche
- **`/api/validate`, `/api/hash`, `/api/revalidate`** für Konfigurationskontrolle
- **Umgebungsvariablen** statt Bedienelementen für das Verhalten
