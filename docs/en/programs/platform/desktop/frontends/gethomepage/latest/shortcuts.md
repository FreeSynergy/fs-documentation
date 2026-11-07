# gethomepage (Library) - Commands instead of shortcuts

## Overview

For a library layer without an interface there are **no keyboard shortcuts**. Instead, this file is the reference for **build, dev, test and container commands** as well as for the environment variables that control the behavior of the clients. All commands run in the repository `gethomepage/homepage` (Node.js ≥ current LTS; the package manager is **pnpm** – a `preinstall` hook enforces this).

---

## Keyboard shortcuts (quick check)

The layer runs in the terminal and in the Node process, therefore there are **no keyboard shortcuts**; the usable keys are those of the terminal in use.

| Shortcut | Function |
|----------|----------|
| `Ctrl+C` | cancel the running dev server or test run |
| `q` (in Vitest watch mode) | end test watching |
| `a` (in Vitest watch mode) | run all tests again |
| `Ctrl+Shift+P` | ❌ Not available – no command palette of an interface |
| `F5` | ❌ Not available – no display window of this layer |

---

## Setup (one-time)

| Command | Function |
|---------|----------|
| `corepack enable` | provide pnpm via Node.js |
| `pnpm install` | install dependencies |
| `pnpm install --frozen-lockfile` | exactly the versions of the lockfile (CI) |
| `cp -r src/skeleton config` | create example configuration (locally) |
| `node -v` | check Node version |
| `pnpm -v` | check pnpm version |

**Note**: `npm install` aborts, because `preinstall: npx only-allow pnpm` prevents other package managers.

---

## Development

| Command | Function |
|---------|----------|
| `pnpm dev` | Next.js dev server on port 3000, reload on code change |
| `pnpm dev -p 3001` | dev server on another port |
| `pnpm start` | production server after `pnpm build` |
| `pnpm build` | production build (`next build --webpack`) |
| `pnpm telemetry disable` | disable Next.js telemetry |
| `PORT=4000 pnpm start` | set port for the running server |
| `HOMEPAGE_ALLOWED_HOSTS=localhost:3000 pnpm dev` | satisfy the host check locally |

---

## Tests and quality

| Command | Function |
|---------|----------|
| `pnpm test` | run all tests (Vitest) |
| `pnpm test:watch` | run tests again on changes |
| `pnpm test:coverage` | tests with coverage report |
| `pnpm vitest run src/utils/proxy` | only tests of one area |
| `pnpm vitest run -t "pihole"` | only tests with a matching name |
| `pnpm lint` | ESLint over the whole source tree |
| `npx prettier --write src/widgets/<service>` | format file |
| `npx eslint src/pages/api/services/proxy.js` | check one file |

**Test location**: tests lie alongside the source (`widget.test.js`, `proxy.test.js`, `component.test.jsx`) – new modules need matching test files.

---

## Containers and deployment

| Command | Function |
|---------|----------|
| `docker build -t homepage:dev .` | build local image |
| `docker run -p 3000:3000 -v $PWD/config:/app/config homepage:dev` | start with local config |
| `docker run -p 3000:3000 -v /var/run/docker.sock:/var/run/docker.sock:ro …` | enable Docker detection |
| `docker compose up -d` | start with compose file |
| `docker compose logs -f homepage` | watch handler and config log |
| `docker exec -it homepage sh` | enter the container |
| `docker logs homepage 2>&1 \| grep servicesProxy` | view only proxy decisions |
| `kubectl apply -f k8s.yaml` | deployment in the cluster (template in the repository) |

---

## Configuration check (runs via the application)

| Command / endpoint | Function |
|--------------------|----------|
| `curl -s localhost:3000/api/validate` | YAML errors with file and line |
| `curl -s localhost:3000/api/hash` | hashes of the config files (change detection) |
| `curl -s localhost:3000/api/revalidate` | discard dashboard cache |
| `curl -s localhost:3000/api/healthcheck` | returns `up` |
| `curl -s "localhost:3000/api/services/proxy?group=…&service=…&index=0"` | test client call directly |
| `curl -s "localhost:3000/api/siteMonitor?groupName=…&serviceName=…"` | test reachability of a tile |

---

## Documentation work

| Command | Function |
|---------|----------|
| `pip install -r requirements.txt` | dependencies of the project documentation (mkdocs) |
| `mkdocs serve` | local documentation preview |
| `mkdocs build` | build documentation |
| `pnpm i18n` / Crowdin file `crowdin.yml` | synchronize translations (project standard) |

---

## Environment variables of the layer

| Variable | Function |
|----------|----------|
| `HOMEPAGE_ALLOWED_HOSTS` | permitted `Host` headers, otherwise `400` |
| `HOMEPAGE_VAR_*` | value substitution in config files |
| `HOMEPAGE_FILE_*` | file content as substitution |
| `HOMEPAGE_AUTH_ENABLED` | enable session check for the routes |
| `NEXTAUTH_SECRET` / `HOMEPAGE_AUTH_SECRET` | signature of the session |
| `NEXTAUTH_URL` / `HOMEPAGE_EXTERNAL_URL` | cookie properties (Secure) |
| `HOMEPAGE_MCP_ENABLED` / `HOMEPAGE_MCP_TOKEN` | MCP endpoint and token |
| `PUID` / `PGID` | user/group in the container |
| `PORT` | port of the server |

---

## Maintenance after an update

| Step | Command |
|---------|---------|
| Read changes | check the release notes of the repository |
| Replace image | `docker compose pull && docker compose up -d` |
| Check config | `curl -s localhost:3000/api/validate` |
| Check clients | check the log for new `Unknown proxy service type` messages |
| Tests locally | `pnpm test` after own fork |

---

## Mac variants

The commands are platform-independent; on macOS only paths and socket differ:

| Command | Function |
|---------|----------|
| `brew install node pnpm` | install the toolchain |
| `-v /var/run/docker.sock:/var/run/docker.sock:ro` | Docker socket (Docker Desktop) |
| `open http://localhost:3000` | open the page in the browser |
| `pbcopy < config/services.yaml` | copy the config to the clipboard |


---

## Working on the fork (Git)

| Command | Function |
|---------|----------|
| `git switch -c feature/<service>` | create a new branch for a service module |
| `git add src/widgets/<service>` | stage new files |
| `git commit -m "feat(widgets): connect <service>"` | comment the change with convention |
| `git rebase origin/main` | keep the fork up to date |
| `git push -u origin feature/<service>` | upload the branch to the pull request |
| `pnpm test && pnpm lint` | mandatory check before submitting |

---

## Summary

Instead of shortcuts, this layer offers a clear command set:

- **`pnpm install` / `pnpm dev` / `pnpm build` / `pnpm test`** for the development cycle
- **`docker build` / `docker compose logs`** for operation and troubleshooting
- **`/api/validate`, `/api/hash`, `/api/revalidate`** for configuration control
- **Environment variables** instead of controls for the behavior
