# Umami – Beschreibung

## Was das Programm macht
Betreiber von Websites fügen ein Skript hinzu und lesen Besucherzahlen und Verhalten in einem Dashboard. Eigene Ereignisse erfassen Aktionen über Seitenaufrufe hinaus.

## Vorteile
- Keine Cookies, kein seitenübergreifendes Tracking, keine automatische Erhebung personenbezogener Daten (Dokumentation).
- MIT-Lizenz, selbst hostbar.
- Berichte über Seitenzahlen hinaus: Trichter, Bindung, Nutzerpfade.

## Abgrenzung
| System | Unterschied |
|--------|-------------|
| Plausible | Eine einfache Ansicht; Umami bietet mehr Berichtsarten für Produktanalyse. |
| Matomo | Größerer Funktionsumfang (Heatmaps und mehr); Umami ist schlanker. |

## Technische Details
Node.js mit Next.js und TypeScript; Prisma; PostgreSQL 12.14 oder neuer; Docker, Compose, Podman (README ✅). Optionale Zwei-Faktor-Authentifizierung.
