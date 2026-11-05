# Monica - Beschreibung

## Was das Programm macht

Monica sammelt alles um eine Person: Wer ist sie, wie sind wir verbunden, was haben wir unternommen, was habe ich ihr geschenkt, was habe ich vor, sie anzurufen. Es ist ein persönliches Beziehungs-Tagebuch mit CRM-Struktur — selbst gehostet, mit Web-UI und API.

## Vorteile

- **Behalt, was wichtig ist**: Beziehungen, Aktivitäten, Geschenke, Schulden an einem Ort
- **DSGVO-freundlich**: eigene Instanz, Export als JSON/vCard
- **API-first genug**: REST + Webhooks für Automatisierung (n8n & Co.)
- **Leichtgewichtig**: PHP/MySQL, Docker-Image, kleiner Ressourcenbedarf

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Nextcloud Contacts** | Adressbuch ohne Historie; Monica ergänzt die Geschichte (Aktivitäten, Geschenke, Beziehungen). |
| **Trekk** | ähnliches Personal-CRM, jünger, Go-Stack; Monica ist breiter integriert (Importe, Webhooks). |
| **SuiteCRM/Pipedrive** | Business-CRM mit Leads/Deals — falsches Werkzeug für Familie/Freunde. |

## Technische Details

- **Backend**: PHP (Laravel), MySQL/MariaDB; Queue Worker für Erinnerungen
- **Frontend**: Vue 2-Komponenten + Blade-Views (API-getrieben, SSR-Anteile)
- **Authentifizierung**: Session + E-Mail-Verifizierung; API-Token; 2FA (TOTP) unterstützt
- **Hosting**: Docker (web + worker + cron), Monica-CLOUD als Managed-Variante
- **Lizenz**: BSL (Business Source License) — Quelltext offen, kommerzielle Hostings eingeschränkt

## Für wen geeignet

- Menschen mit weitem Beziehungsnetz, die Nachfass-Angst haben („wann habe ich Tante Last gepflegt?“)
- FreeSynergy-Kontakt-Szenarien mit/activity-log-Model: Mapping auf Contact + Event + Task
