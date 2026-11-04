# Apps – Abarbeitungsplan

Checkliste aller Dateien unter `docs/de/programs/` (Pfade relativ zu `docs/de/`).

**Bedeutung der Markierung** (festgelegt 2026-11-03, `conventions/decisions/0006`):

| Zeichen | Heißt |
|---------|-------|
| `[x]` | **an Primärquellen verifiziert** — Quelltext-Tag, offizielle API-Referenz oder offizielle Hilfeseite; Fundstellen in `index.md` der Skin |
| `[~]` | Datei **vorhanden**, Inhalt **nicht** an Primärquellen verifiziert — kann veraltet oder mit einem anderen Produkt vermischt sein |
| `[ ]` | Datei fehlt |

Der Haken ist kein Zähler für geschriebene Dateien, sondern der Nachweis, dass nachgeprüft
wurde. `[~]` ist Restarbeit — aber geringere als `[ ]`.

**Abbruchkriterium pro Kategorie** (ADR 0006): **3–5 Masken** der Kategorie vollständig
verifizieren, dann die Schnittmenge dieser Masken als **Pflichtmenge** in
`programs/<ebene>/<kategorie>/requirements.md` **einfrieren** und die Zeile
„Pflichtmenge eingefroren“ abhaken. Die übrigen Masken der Kategorie sind **Stichprobe**:
nur abarbeiten, wenn sie eine Fähigkeit zeigen, die in `requirements.md` fehlt.
Die Dateien sind das Mittel, nicht das Ziel.

**Übersicht:** 17 Kategorien · 119 Programme (Skins) · 869 Markdown-Dateien —
davon `[x]` verifiziert 42, `[~]` vorhanden ohne Beleg 827, `[ ]` fehlt 0

- [~] programs/index.md

## calendar

- [x] Pflichtmenge einfrieren → `programs/apps/calendar/requirements.md`

- [~] programs/apps/calendar/index.md
- [~] programs/apps/calendar/masks/index.md

### calendar / davical
- [x] programs/apps/calendar/masks/davical/api.md
- [x] programs/apps/calendar/masks/davical/description.md
- [x] programs/apps/calendar/masks/davical/features.md
- [x] programs/apps/calendar/masks/davical/index.md
- [x] programs/apps/calendar/masks/davical/menu.md
- [x] programs/apps/calendar/masks/davical/shortcuts.md
- [x] programs/apps/calendar/masks/davical/structure.md

### calendar / google-calendar
- [x] programs/apps/calendar/masks/google-calendar/api.md
- [x] programs/apps/calendar/masks/google-calendar/description.md
- [x] programs/apps/calendar/masks/google-calendar/features.md
- [x] programs/apps/calendar/masks/google-calendar/index.md
- [x] programs/apps/calendar/masks/google-calendar/menu.md
- [x] programs/apps/calendar/masks/google-calendar/shortcuts.md
- [x] programs/apps/calendar/masks/google-calendar/structure.md

### calendar / merkuro
- [x] programs/apps/calendar/masks/merkuro/api.md
- [x] programs/apps/calendar/masks/merkuro/description.md
- [x] programs/apps/calendar/masks/merkuro/features.md
- [x] programs/apps/calendar/masks/merkuro/index.md
- [x] programs/apps/calendar/masks/merkuro/menu.md
- [x] programs/apps/calendar/masks/merkuro/shortcuts.md
- [x] programs/apps/calendar/masks/merkuro/structure.md

### calendar / nextcloud-calendar
- [x] programs/apps/calendar/masks/nextcloud-calendar/api.md
- [x] programs/apps/calendar/masks/nextcloud-calendar/description.md
- [x] programs/apps/calendar/masks/nextcloud-calendar/features.md
- [x] programs/apps/calendar/masks/nextcloud-calendar/index.md
- [x] programs/apps/calendar/masks/nextcloud-calendar/menu.md
- [x] programs/apps/calendar/masks/nextcloud-calendar/shortcuts.md
- [x] programs/apps/calendar/masks/nextcloud-calendar/structure.md

### calendar / outlook-calendar
- [x] programs/apps/calendar/masks/outlook-calendar/api.md
- [x] programs/apps/calendar/masks/outlook-calendar/description.md
- [x] programs/apps/calendar/masks/outlook-calendar/features.md
- [x] programs/apps/calendar/masks/outlook-calendar/index.md
- [x] programs/apps/calendar/masks/outlook-calendar/menu.md
- [x] programs/apps/calendar/masks/outlook-calendar/shortcuts.md
- [x] programs/apps/calendar/masks/outlook-calendar/structure.md

### calendar / planner
- [x] programs/apps/calendar/masks/planner/api.md
- [x] programs/apps/calendar/masks/planner/description.md
- [x] programs/apps/calendar/masks/planner/features.md
- [x] programs/apps/calendar/masks/planner/index.md
- [x] programs/apps/calendar/masks/planner/menu.md
- [x] programs/apps/calendar/masks/planner/shortcuts.md
- [x] programs/apps/calendar/masks/planner/structure.md

## contact

- [ ] Pflichtmenge einfrieren → `programs/apps/contact/requirements.md`

- [~] programs/apps/contact/index.md
- [~] programs/apps/contact/masks/index.md

### contact / gnome-contacts
- [~] programs/apps/contact/masks/gnome-contacts/api.md
- [~] programs/apps/contact/masks/gnome-contacts/description.md
- [~] programs/apps/contact/masks/gnome-contacts/features.md
- [~] programs/apps/contact/masks/gnome-contacts/index.md
- [~] programs/apps/contact/masks/gnome-contacts/menu.md
- [~] programs/apps/contact/masks/gnome-contacts/shortcuts.md
- [~] programs/apps/contact/masks/gnome-contacts/structure.md

### contact / kaddressbook
- [~] programs/apps/contact/masks/kaddressbook/api.md
- [~] programs/apps/contact/masks/kaddressbook/description.md
- [~] programs/apps/contact/masks/kaddressbook/features.md
- [~] programs/apps/contact/masks/kaddressbook/index.md
- [~] programs/apps/contact/masks/kaddressbook/menu.md
- [~] programs/apps/contact/masks/kaddressbook/shortcuts.md
- [~] programs/apps/contact/masks/kaddressbook/structure.md

### contact / monica
- [~] programs/apps/contact/masks/monica/api.md
- [~] programs/apps/contact/masks/monica/description.md
- [~] programs/apps/contact/masks/monica/features.md
- [~] programs/apps/contact/masks/monica/index.md
- [~] programs/apps/contact/masks/monica/menu.md
- [~] programs/apps/contact/masks/monica/shortcuts.md
- [~] programs/apps/contact/masks/monica/structure.md

### contact / nextcloud-contacts
- [~] programs/apps/contact/masks/nextcloud-contacts/api.md
- [~] programs/apps/contact/masks/nextcloud-contacts/description.md
- [~] programs/apps/contact/masks/nextcloud-contacts/features.md
- [~] programs/apps/contact/masks/nextcloud-contacts/index.md
- [~] programs/apps/contact/masks/nextcloud-contacts/menu.md
- [~] programs/apps/contact/masks/nextcloud-contacts/shortcuts.md
- [~] programs/apps/contact/masks/nextcloud-contacts/structure.md

## crm

- [ ] Pflichtmenge einfrieren → `programs/suites/crm/requirements.md`

- [~] programs/suites/crm/index.md
- [~] programs/suites/crm/masks/index.md

### crm / civicrm
- [~] programs/suites/crm/masks/civicrm/api.md
- [~] programs/suites/crm/masks/civicrm/description.md
- [~] programs/suites/crm/masks/civicrm/features.md
- [~] programs/suites/crm/masks/civicrm/index.md
- [~] programs/suites/crm/masks/civicrm/menu.md
- [~] programs/suites/crm/masks/civicrm/shortcuts.md
- [~] programs/suites/crm/masks/civicrm/structure.md

### crm / espocrm
- [~] programs/suites/crm/masks/espocrm/api.md
- [~] programs/suites/crm/masks/espocrm/description.md
- [~] programs/suites/crm/masks/espocrm/features.md
- [~] programs/suites/crm/masks/espocrm/index.md
- [~] programs/suites/crm/masks/espocrm/menu.md
- [~] programs/suites/crm/masks/espocrm/shortcuts.md
- [~] programs/suites/crm/masks/espocrm/structure.md

### crm / hubspot
- [~] programs/suites/crm/masks/hubspot/api.md
- [~] programs/suites/crm/masks/hubspot/description.md
- [~] programs/suites/crm/masks/hubspot/features.md
- [~] programs/suites/crm/masks/hubspot/index.md
- [~] programs/suites/crm/masks/hubspot/menu.md
- [~] programs/suites/crm/masks/hubspot/shortcuts.md
- [~] programs/suites/crm/masks/hubspot/structure.md

### crm / pipedrive
- [~] programs/suites/crm/masks/pipedrive/api.md
- [~] programs/suites/crm/masks/pipedrive/description.md
- [~] programs/suites/crm/masks/pipedrive/features.md
- [~] programs/suites/crm/masks/pipedrive/index.md
- [~] programs/suites/crm/masks/pipedrive/menu.md
- [~] programs/suites/crm/masks/pipedrive/shortcuts.md
- [~] programs/suites/crm/masks/pipedrive/structure.md

### crm / salesforce
- [~] programs/suites/crm/masks/salesforce/api.md
- [~] programs/suites/crm/masks/salesforce/description.md
- [~] programs/suites/crm/masks/salesforce/features.md
- [~] programs/suites/crm/masks/salesforce/index.md
- [~] programs/suites/crm/masks/salesforce/menu.md
- [~] programs/suites/crm/masks/salesforce/shortcuts.md
- [~] programs/suites/crm/masks/salesforce/structure.md

### crm / suitecrm
- [~] programs/suites/crm/masks/suitecrm/api.md
- [~] programs/suites/crm/masks/suitecrm/description.md
- [~] programs/suites/crm/masks/suitecrm/features.md
- [~] programs/suites/crm/masks/suitecrm/index.md
- [~] programs/suites/crm/masks/suitecrm/menu.md
- [~] programs/suites/crm/masks/suitecrm/shortcuts.md
- [~] programs/suites/crm/masks/suitecrm/structure.md

## democracy

- [ ] Pflichtmenge einfrieren → `programs/suites/democracy/requirements.md`

- [~] programs/suites/democracy/index.md
- [~] programs/suites/democracy/masks/index.md

### democracy / adhocracy4
- [~] programs/suites/democracy/masks/adhocracy4/api.md
- [~] programs/suites/democracy/masks/adhocracy4/description.md
- [~] programs/suites/democracy/masks/adhocracy4/features.md
- [~] programs/suites/democracy/masks/adhocracy4/index.md
- [~] programs/suites/democracy/masks/adhocracy4/menu.md
- [~] programs/suites/democracy/masks/adhocracy4/shortcuts.md
- [~] programs/suites/democracy/masks/adhocracy4/structure.md

### democracy / circo
- [~] programs/suites/democracy/masks/circo/api.md
- [~] programs/suites/democracy/masks/circo/description.md
- [~] programs/suites/democracy/masks/circo/features.md
- [~] programs/suites/democracy/masks/circo/index.md
- [~] programs/suites/democracy/masks/circo/menu.md
- [~] programs/suites/democracy/masks/circo/shortcuts.md
- [~] programs/suites/democracy/masks/circo/structure.md

### democracy / consul
- [~] programs/suites/democracy/masks/consul/api.md
- [~] programs/suites/democracy/masks/consul/description.md
- [~] programs/suites/democracy/masks/consul/features.md
- [~] programs/suites/democracy/masks/consul/index.md
- [~] programs/suites/democracy/masks/consul/menu.md
- [~] programs/suites/democracy/masks/consul/shortcuts.md
- [~] programs/suites/democracy/masks/consul/structure.md

### democracy / decidim
- [~] programs/suites/democracy/masks/decidim/api.md
- [~] programs/suites/democracy/masks/decidim/description.md
- [~] programs/suites/democracy/masks/decidim/features.md
- [~] programs/suites/democracy/masks/decidim/index.md
- [~] programs/suites/democracy/masks/decidim/menu.md
- [~] programs/suites/democracy/masks/decidim/shortcuts.md
- [~] programs/suites/democracy/masks/decidim/structure.md

### democracy / liquid-feedback
- [~] programs/suites/democracy/masks/liquid-feedback/api.md
- [~] programs/suites/democracy/masks/liquid-feedback/description.md
- [~] programs/suites/democracy/masks/liquid-feedback/features.md
- [~] programs/suites/democracy/masks/liquid-feedback/index.md
- [~] programs/suites/democracy/masks/liquid-feedback/menu.md
- [~] programs/suites/democracy/masks/liquid-feedback/shortcuts.md
- [~] programs/suites/democracy/masks/liquid-feedback/structure.md

### democracy / polis
- [~] programs/suites/democracy/masks/polis/api.md
- [~] programs/suites/democracy/masks/polis/description.md
- [~] programs/suites/democracy/masks/polis/features.md
- [~] programs/suites/democracy/masks/polis/index.md
- [~] programs/suites/democracy/masks/polis/menu.md
- [~] programs/suites/democracy/masks/polis/shortcuts.md
- [~] programs/suites/democracy/masks/polis/structure.md

## desktop

- [ ] Pflichtmenge einfrieren → `programs/platform/desktop/requirements.md`

- [~] programs/platform/desktop/index.md
- [~] programs/platform/desktop/masks/index.md

### desktop / dashy
- [~] programs/platform/desktop/masks/dashy/api.md
- [~] programs/platform/desktop/masks/dashy/description.md
- [~] programs/platform/desktop/masks/dashy/features.md
- [~] programs/platform/desktop/masks/dashy/index.md
- [~] programs/platform/desktop/masks/dashy/menu.md
- [~] programs/platform/desktop/masks/dashy/shortcuts.md
- [~] programs/platform/desktop/masks/dashy/structure.md

### desktop / gethomepage
- [~] programs/platform/desktop/masks/gethomepage/api.md
- [~] programs/platform/desktop/masks/gethomepage/description.md
- [~] programs/platform/desktop/masks/gethomepage/features.md
- [~] programs/platform/desktop/masks/gethomepage/index.md
- [~] programs/platform/desktop/masks/gethomepage/menu.md
- [~] programs/platform/desktop/masks/gethomepage/shortcuts.md
- [~] programs/platform/desktop/masks/gethomepage/structure.md

### desktop / heimdall
- [~] programs/platform/desktop/masks/heimdall/api.md
- [~] programs/platform/desktop/masks/heimdall/description.md
- [~] programs/platform/desktop/masks/heimdall/features.md
- [~] programs/platform/desktop/masks/heimdall/index.md
- [~] programs/platform/desktop/masks/heimdall/menu.md
- [~] programs/platform/desktop/masks/heimdall/shortcuts.md
- [~] programs/platform/desktop/masks/heimdall/structure.md

### desktop / homarr
- [~] programs/platform/desktop/masks/homarr/api.md
- [~] programs/platform/desktop/masks/homarr/description.md
- [~] programs/platform/desktop/masks/homarr/features.md
- [~] programs/platform/desktop/masks/homarr/index.md
- [~] programs/platform/desktop/masks/homarr/menu.md
- [~] programs/platform/desktop/masks/homarr/shortcuts.md
- [~] programs/platform/desktop/masks/homarr/structure.md

### desktop / homepage
- [~] programs/platform/desktop/masks/homepage/api.md
- [~] programs/platform/desktop/masks/homepage/description.md
- [~] programs/platform/desktop/masks/homepage/features.md
- [~] programs/platform/desktop/masks/homepage/index.md
- [~] programs/platform/desktop/masks/homepage/menu.md
- [~] programs/platform/desktop/masks/homepage/shortcuts.md
- [~] programs/platform/desktop/masks/homepage/structure.md

### desktop / homer
- [~] programs/platform/desktop/masks/homer/api.md
- [~] programs/platform/desktop/masks/homer/description.md
- [~] programs/platform/desktop/masks/homer/features.md
- [~] programs/platform/desktop/masks/homer/index.md
- [~] programs/platform/desktop/masks/homer/menu.md
- [~] programs/platform/desktop/masks/homer/shortcuts.md
- [~] programs/platform/desktop/masks/homer/structure.md

### desktop / launchboard
- [~] programs/platform/desktop/masks/launchboard/api.md
- [~] programs/platform/desktop/masks/launchboard/description.md
- [~] programs/platform/desktop/masks/launchboard/features.md
- [~] programs/platform/desktop/masks/launchboard/index.md
- [~] programs/platform/desktop/masks/launchboard/menu.md
- [~] programs/platform/desktop/masks/launchboard/shortcuts.md
- [~] programs/platform/desktop/masks/launchboard/structure.md

### desktop / opnsense
- [~] programs/platform/desktop/masks/opnsense/api.md
- [~] programs/platform/desktop/masks/opnsense/description.md
- [~] programs/platform/desktop/masks/opnsense/features.md
- [~] programs/platform/desktop/masks/opnsense/index.md
- [~] programs/platform/desktop/masks/opnsense/menu.md
- [~] programs/platform/desktop/masks/opnsense/shortcuts.md
- [~] programs/platform/desktop/masks/opnsense/structure.md

### desktop / proxmox
- [~] programs/platform/desktop/masks/proxmox/api.md
- [~] programs/platform/desktop/masks/proxmox/description.md
- [~] programs/platform/desktop/masks/proxmox/features.md
- [~] programs/platform/desktop/masks/proxmox/index.md
- [~] programs/platform/desktop/masks/proxmox/menu.md
- [~] programs/platform/desktop/masks/proxmox/shortcuts.md
- [~] programs/platform/desktop/masks/proxmox/structure.md

### desktop / synology-dsm
- [~] programs/platform/desktop/masks/synology-dsm/api.md
- [~] programs/platform/desktop/masks/synology-dsm/description.md
- [~] programs/platform/desktop/masks/synology-dsm/features.md
- [~] programs/platform/desktop/masks/synology-dsm/index.md
- [~] programs/platform/desktop/masks/synology-dsm/menu.md
- [~] programs/platform/desktop/masks/synology-dsm/shortcuts.md
- [~] programs/platform/desktop/masks/synology-dsm/structure.md

### desktop / truenas
- [~] programs/platform/desktop/masks/truenas/api.md
- [~] programs/platform/desktop/masks/truenas/description.md
- [~] programs/platform/desktop/masks/truenas/features.md
- [~] programs/platform/desktop/masks/truenas/index.md
- [~] programs/platform/desktop/masks/truenas/menu.md
- [~] programs/platform/desktop/masks/truenas/shortcuts.md
- [~] programs/platform/desktop/masks/truenas/structure.md

### desktop / unraid
- [~] programs/platform/desktop/masks/unraid/api.md
- [~] programs/platform/desktop/masks/unraid/description.md
- [~] programs/platform/desktop/masks/unraid/features.md
- [~] programs/platform/desktop/masks/unraid/index.md
- [~] programs/platform/desktop/masks/unraid/menu.md
- [~] programs/platform/desktop/masks/unraid/shortcuts.md
- [~] programs/platform/desktop/masks/unraid/structure.md

## erp

- [ ] Pflichtmenge einfrieren → `programs/suites/erp/requirements.md`

- [~] programs/suites/erp/index.md
- [~] programs/suites/erp/masks/index.md

### erp / axelor
- [~] programs/suites/erp/masks/axelor/api.md
- [~] programs/suites/erp/masks/axelor/description.md
- [~] programs/suites/erp/masks/axelor/features.md
- [~] programs/suites/erp/masks/axelor/index.md
- [~] programs/suites/erp/masks/axelor/menu.md
- [~] programs/suites/erp/masks/axelor/shortcuts.md
- [~] programs/suites/erp/masks/axelor/structure.md

### erp / dolibarr
- [~] programs/suites/erp/masks/dolibarr/api.md
- [~] programs/suites/erp/masks/dolibarr/description.md
- [~] programs/suites/erp/masks/dolibarr/features.md
- [~] programs/suites/erp/masks/dolibarr/index.md
- [~] programs/suites/erp/masks/dolibarr/menu.md
- [~] programs/suites/erp/masks/dolibarr/shortcuts.md
- [~] programs/suites/erp/masks/dolibarr/structure.md

### erp / erpnext
- [~] programs/suites/erp/masks/erpnext/api.md
- [~] programs/suites/erp/masks/erpnext/description.md
- [~] programs/suites/erp/masks/erpnext/features.md
- [~] programs/suites/erp/masks/erpnext/index.md
- [~] programs/suites/erp/masks/erpnext/menu.md
- [~] programs/suites/erp/masks/erpnext/shortcuts.md
- [~] programs/suites/erp/masks/erpnext/structure.md

### erp / odoo
- [~] programs/suites/erp/masks/odoo/api.md
- [~] programs/suites/erp/masks/odoo/description.md
- [~] programs/suites/erp/masks/odoo/features.md
- [~] programs/suites/erp/masks/odoo/index.md
- [~] programs/suites/erp/masks/odoo/menu.md
- [~] programs/suites/erp/masks/odoo/shortcuts.md
- [~] programs/suites/erp/masks/odoo/structure.md

### erp / sage
- [~] programs/suites/erp/masks/sage/api.md
- [~] programs/suites/erp/masks/sage/description.md
- [~] programs/suites/erp/masks/sage/features.md
- [~] programs/suites/erp/masks/sage/index.md
- [~] programs/suites/erp/masks/sage/menu.md
- [~] programs/suites/erp/masks/sage/shortcuts.md
- [~] programs/suites/erp/masks/sage/structure.md

### erp / tryton
- [~] programs/suites/erp/masks/tryton/api.md
- [~] programs/suites/erp/masks/tryton/description.md
- [~] programs/suites/erp/masks/tryton/features.md
- [~] programs/suites/erp/masks/tryton/index.md
- [~] programs/suites/erp/masks/tryton/menu.md
- [~] programs/suites/erp/masks/tryton/shortcuts.md
- [~] programs/suites/erp/masks/tryton/structure.md

## gallery

- [ ] Pflichtmenge einfrieren → `programs/apps/gallery/requirements.md`

- [~] programs/apps/gallery/index.md
- [~] programs/apps/gallery/masks/index.md

### gallery / coppermine
- [~] programs/apps/gallery/masks/coppermine/api.md
- [~] programs/apps/gallery/masks/coppermine/description.md
- [~] programs/apps/gallery/masks/coppermine/features.md
- [~] programs/apps/gallery/masks/coppermine/index.md
- [~] programs/apps/gallery/masks/coppermine/menu.md
- [~] programs/apps/gallery/masks/coppermine/shortcuts.md
- [~] programs/apps/gallery/masks/coppermine/structure.md

### gallery / damselfly
- [~] programs/apps/gallery/masks/damselfly/api.md
- [~] programs/apps/gallery/masks/damselfly/description.md
- [~] programs/apps/gallery/masks/damselfly/features.md
- [~] programs/apps/gallery/masks/damselfly/index.md
- [~] programs/apps/gallery/masks/damselfly/menu.md
- [~] programs/apps/gallery/masks/damselfly/shortcuts.md
- [~] programs/apps/gallery/masks/damselfly/structure.md

### gallery / immich
- [~] programs/apps/gallery/masks/immich/api.md
- [~] programs/apps/gallery/masks/immich/description.md
- [~] programs/apps/gallery/masks/immich/features.md
- [~] programs/apps/gallery/masks/immich/index.md
- [~] programs/apps/gallery/masks/immich/menu.md
- [~] programs/apps/gallery/masks/immich/shortcuts.md
- [~] programs/apps/gallery/masks/immich/structure.md

### gallery / librephotos
- [~] programs/apps/gallery/masks/librephotos/api.md
- [~] programs/apps/gallery/masks/librephotos/description.md
- [~] programs/apps/gallery/masks/librephotos/features.md
- [~] programs/apps/gallery/masks/librephotos/index.md
- [~] programs/apps/gallery/masks/librephotos/menu.md
- [~] programs/apps/gallery/masks/librephotos/shortcuts.md
- [~] programs/apps/gallery/masks/librephotos/structure.md

### gallery / lychee
- [~] programs/apps/gallery/masks/lychee/api.md
- [~] programs/apps/gallery/masks/lychee/description.md
- [~] programs/apps/gallery/masks/lychee/features.md
- [~] programs/apps/gallery/masks/lychee/index.md
- [~] programs/apps/gallery/masks/lychee/menu.md
- [~] programs/apps/gallery/masks/lychee/shortcuts.md
- [~] programs/apps/gallery/masks/lychee/structure.md

### gallery / nextcloud-photos
- [~] programs/apps/gallery/masks/nextcloud-photos/api.md
- [~] programs/apps/gallery/masks/nextcloud-photos/description.md
- [~] programs/apps/gallery/masks/nextcloud-photos/features.md
- [~] programs/apps/gallery/masks/nextcloud-photos/index.md
- [~] programs/apps/gallery/masks/nextcloud-photos/menu.md
- [~] programs/apps/gallery/masks/nextcloud-photos/shortcuts.md
- [~] programs/apps/gallery/masks/nextcloud-photos/structure.md

### gallery / photoprism
- [~] programs/apps/gallery/masks/photoprism/api.md
- [~] programs/apps/gallery/masks/photoprism/description.md
- [~] programs/apps/gallery/masks/photoprism/features.md
- [~] programs/apps/gallery/masks/photoprism/index.md
- [~] programs/apps/gallery/masks/photoprism/menu.md
- [~] programs/apps/gallery/masks/photoprism/shortcuts.md
- [~] programs/apps/gallery/masks/photoprism/structure.md

### gallery / piwigo
- [~] programs/apps/gallery/masks/piwigo/api.md
- [~] programs/apps/gallery/masks/piwigo/description.md
- [~] programs/apps/gallery/masks/piwigo/features.md
- [~] programs/apps/gallery/masks/piwigo/index.md
- [~] programs/apps/gallery/masks/piwigo/menu.md
- [~] programs/apps/gallery/masks/piwigo/shortcuts.md
- [~] programs/apps/gallery/masks/piwigo/structure.md

## helpdesk

- [ ] Pflichtmenge einfrieren → `programs/apps/helpdesk/requirements.md`

- [~] programs/apps/helpdesk/index.md
- [~] programs/apps/helpdesk/masks/index.md

### helpdesk / freshdesk
- [~] programs/apps/helpdesk/masks/freshdesk/api.md
- [~] programs/apps/helpdesk/masks/freshdesk/description.md
- [~] programs/apps/helpdesk/masks/freshdesk/features.md
- [~] programs/apps/helpdesk/masks/freshdesk/index.md
- [~] programs/apps/helpdesk/masks/freshdesk/menu.md
- [~] programs/apps/helpdesk/masks/freshdesk/shortcuts.md
- [~] programs/apps/helpdesk/masks/freshdesk/structure.md

### helpdesk / glpi
- [~] programs/apps/helpdesk/masks/glpi/api.md
- [~] programs/apps/helpdesk/masks/glpi/description.md
- [~] programs/apps/helpdesk/masks/glpi/features.md
- [~] programs/apps/helpdesk/masks/glpi/index.md
- [~] programs/apps/helpdesk/masks/glpi/menu.md
- [~] programs/apps/helpdesk/masks/glpi/shortcuts.md
- [~] programs/apps/helpdesk/masks/glpi/structure.md

### helpdesk / helodesk
- [~] programs/apps/helpdesk/masks/helodesk/api.md
- [~] programs/apps/helpdesk/masks/helodesk/description.md
- [~] programs/apps/helpdesk/masks/helodesk/features.md
- [~] programs/apps/helpdesk/masks/helodesk/index.md
- [~] programs/apps/helpdesk/masks/helodesk/menu.md
- [~] programs/apps/helpdesk/masks/helodesk/shortcuts.md
- [~] programs/apps/helpdesk/masks/helodesk/structure.md

### helpdesk / helpscout
- [~] programs/apps/helpdesk/masks/helpscout/api.md
- [~] programs/apps/helpdesk/masks/helpscout/description.md
- [~] programs/apps/helpdesk/masks/helpscout/features.md
- [~] programs/apps/helpdesk/masks/helpscout/index.md
- [~] programs/apps/helpdesk/masks/helpscout/menu.md
- [~] programs/apps/helpdesk/masks/helpscout/shortcuts.md
- [~] programs/apps/helpdesk/masks/helpscout/structure.md

### helpdesk / osticket
- [~] programs/apps/helpdesk/masks/osticket/api.md
- [~] programs/apps/helpdesk/masks/osticket/description.md
- [~] programs/apps/helpdesk/masks/osticket/features.md
- [~] programs/apps/helpdesk/masks/osticket/index.md
- [~] programs/apps/helpdesk/masks/osticket/menu.md
- [~] programs/apps/helpdesk/masks/osticket/shortcuts.md
- [~] programs/apps/helpdesk/masks/osticket/structure.md

### helpdesk / request-tracker
- [~] programs/apps/helpdesk/masks/request-tracker/api.md
- [~] programs/apps/helpdesk/masks/request-tracker/description.md
- [~] programs/apps/helpdesk/masks/request-tracker/features.md
- [~] programs/apps/helpdesk/masks/request-tracker/index.md
- [~] programs/apps/helpdesk/masks/request-tracker/menu.md
- [~] programs/apps/helpdesk/masks/request-tracker/shortcuts.md
- [~] programs/apps/helpdesk/masks/request-tracker/structure.md

### helpdesk / zammad
- [~] programs/apps/helpdesk/masks/zammad/api.md
- [~] programs/apps/helpdesk/masks/zammad/description.md
- [~] programs/apps/helpdesk/masks/zammad/features.md
- [~] programs/apps/helpdesk/masks/zammad/index.md
- [~] programs/apps/helpdesk/masks/zammad/menu.md
- [~] programs/apps/helpdesk/masks/zammad/shortcuts.md
- [~] programs/apps/helpdesk/masks/zammad/structure.md

### helpdesk / zendesk
- [~] programs/apps/helpdesk/masks/zendesk/api.md
- [~] programs/apps/helpdesk/masks/zendesk/description.md
- [~] programs/apps/helpdesk/masks/zendesk/features.md
- [~] programs/apps/helpdesk/masks/zendesk/index.md
- [~] programs/apps/helpdesk/masks/zendesk/menu.md
- [~] programs/apps/helpdesk/masks/zendesk/shortcuts.md
- [~] programs/apps/helpdesk/masks/zendesk/structure.md

## maps

- [ ] Pflichtmenge einfrieren → `programs/apps/maps/requirements.md`

- [~] programs/apps/maps/index.md
- [~] programs/apps/maps/masks/index.md
- [~] programs/apps/maps/standpunkte.md

### maps / leaflet
- [~] programs/apps/maps/masks/leaflet/api.md
- [~] programs/apps/maps/masks/leaflet/description.md
- [~] programs/apps/maps/masks/leaflet/features.md
- [~] programs/apps/maps/masks/leaflet/index.md
- [~] programs/apps/maps/masks/leaflet/menu.md
- [~] programs/apps/maps/masks/leaflet/shortcuts.md
- [~] programs/apps/maps/masks/leaflet/structure.md

### maps / maplibre
- [~] programs/apps/maps/masks/maplibre/api.md
- [~] programs/apps/maps/masks/maplibre/description.md
- [~] programs/apps/maps/masks/maplibre/features.md
- [~] programs/apps/maps/masks/maplibre/index.md
- [~] programs/apps/maps/masks/maplibre/menu.md
- [~] programs/apps/maps/masks/maplibre/shortcuts.md
- [~] programs/apps/maps/masks/maplibre/structure.md

### maps / openstreetmap
- [~] programs/apps/maps/masks/openstreetmap/api.md
- [~] programs/apps/maps/masks/openstreetmap/description.md
- [~] programs/apps/maps/masks/openstreetmap/features.md
- [~] programs/apps/maps/masks/openstreetmap/index.md
- [~] programs/apps/maps/masks/openstreetmap/menu.md
- [~] programs/apps/maps/masks/openstreetmap/shortcuts.md
- [~] programs/apps/maps/masks/openstreetmap/structure.md

### maps / organic-maps
- [~] programs/apps/maps/masks/organic-maps/api.md
- [~] programs/apps/maps/masks/organic-maps/description.md
- [~] programs/apps/maps/masks/organic-maps/features.md
- [~] programs/apps/maps/masks/organic-maps/index.md
- [~] programs/apps/maps/masks/organic-maps/menu.md
- [~] programs/apps/maps/masks/organic-maps/shortcuts.md
- [~] programs/apps/maps/masks/organic-maps/structure.md

### maps / osmand
- [~] programs/apps/maps/masks/osmand/api.md
- [~] programs/apps/maps/masks/osmand/description.md
- [~] programs/apps/maps/masks/osmand/features.md
- [~] programs/apps/maps/masks/osmand/index.md
- [~] programs/apps/maps/masks/osmand/menu.md
- [~] programs/apps/maps/masks/osmand/shortcuts.md
- [~] programs/apps/maps/masks/osmand/structure.md

### maps / qgis
- [~] programs/apps/maps/masks/qgis/api.md
- [~] programs/apps/maps/masks/qgis/description.md
- [~] programs/apps/maps/masks/qgis/features.md
- [~] programs/apps/maps/masks/qgis/index.md
- [~] programs/apps/maps/masks/qgis/menu.md
- [~] programs/apps/maps/masks/qgis/shortcuts.md
- [~] programs/apps/maps/masks/qgis/structure.md

### maps / umap
- [~] programs/apps/maps/masks/umap/api.md
- [~] programs/apps/maps/masks/umap/description.md
- [~] programs/apps/maps/masks/umap/features.md
- [~] programs/apps/maps/masks/umap/index.md
- [~] programs/apps/maps/masks/umap/menu.md
- [~] programs/apps/maps/masks/umap/shortcuts.md
- [~] programs/apps/maps/masks/umap/structure.md

## marketing

- [ ] Pflichtmenge einfrieren → `programs/apps/marketing/requirements.md`

- [~] programs/apps/marketing/index.md
- [~] programs/apps/marketing/masks/index.md

### marketing / google-analytics
- [~] programs/apps/marketing/masks/google-analytics/api.md
- [~] programs/apps/marketing/masks/google-analytics/description.md
- [~] programs/apps/marketing/masks/google-analytics/features.md
- [~] programs/apps/marketing/masks/google-analytics/index.md
- [~] programs/apps/marketing/masks/google-analytics/menu.md
- [~] programs/apps/marketing/masks/google-analytics/shortcuts.md
- [~] programs/apps/marketing/masks/google-analytics/structure.md

### marketing / hotjar
- [~] programs/apps/marketing/masks/hotjar/api.md
- [~] programs/apps/marketing/masks/hotjar/description.md
- [~] programs/apps/marketing/masks/hotjar/features.md
- [~] programs/apps/marketing/masks/hotjar/index.md
- [~] programs/apps/marketing/masks/hotjar/menu.md
- [~] programs/apps/marketing/masks/hotjar/shortcuts.md
- [~] programs/apps/marketing/masks/hotjar/structure.md

### marketing / mailchimp
- [~] programs/apps/marketing/masks/mailchimp/api.md
- [~] programs/apps/marketing/masks/mailchimp/description.md
- [~] programs/apps/marketing/masks/mailchimp/features.md
- [~] programs/apps/marketing/masks/mailchimp/index.md
- [~] programs/apps/marketing/masks/mailchimp/menu.md
- [~] programs/apps/marketing/masks/mailchimp/shortcuts.md
- [~] programs/apps/marketing/masks/mailchimp/structure.md

### marketing / matomo
- [~] programs/apps/marketing/masks/matomo/api.md
- [~] programs/apps/marketing/masks/matomo/description.md
- [~] programs/apps/marketing/masks/matomo/features.md
- [~] programs/apps/marketing/masks/matomo/index.md
- [~] programs/apps/marketing/masks/matomo/menu.md
- [~] programs/apps/marketing/masks/matomo/shortcuts.md
- [~] programs/apps/marketing/masks/matomo/structure.md

### marketing / mautic
- [~] programs/apps/marketing/masks/mautic/api.md
- [~] programs/apps/marketing/masks/mautic/description.md
- [~] programs/apps/marketing/masks/mautic/features.md
- [~] programs/apps/marketing/masks/mautic/index.md
- [~] programs/apps/marketing/masks/mautic/menu.md
- [~] programs/apps/marketing/masks/mautic/shortcuts.md
- [~] programs/apps/marketing/masks/mautic/structure.md

### marketing / plausible
- [~] programs/apps/marketing/masks/plausible/api.md
- [~] programs/apps/marketing/masks/plausible/description.md
- [~] programs/apps/marketing/masks/plausible/features.md
- [~] programs/apps/marketing/masks/plausible/index.md
- [~] programs/apps/marketing/masks/plausible/menu.md
- [~] programs/apps/marketing/masks/plausible/shortcuts.md
- [~] programs/apps/marketing/masks/plausible/structure.md

## marketplace

- [ ] Pflichtmenge einfrieren → `programs/suites/marketplace/requirements.md`

- [~] programs/suites/marketplace/index.md
- [~] programs/suites/marketplace/masks/index.md

### marketplace / arcemall
- [~] programs/suites/marketplace/masks/arcemall/api.md
- [~] programs/suites/marketplace/masks/arcemall/description.md
- [~] programs/suites/marketplace/masks/arcemall/features.md
- [~] programs/suites/marketplace/masks/arcemall/index.md
- [~] programs/suites/marketplace/masks/arcemall/menu.md
- [~] programs/suites/marketplace/masks/arcemall/shortcuts.md
- [~] programs/suites/marketplace/masks/arcemall/structure.md

### marketplace / cs-cart-multivendor
- [~] programs/suites/marketplace/masks/cs-cart-multivendor/api.md
- [~] programs/suites/marketplace/masks/cs-cart-multivendor/description.md
- [~] programs/suites/marketplace/masks/cs-cart-multivendor/features.md
- [~] programs/suites/marketplace/masks/cs-cart-multivendor/index.md
- [~] programs/suites/marketplace/masks/cs-cart-multivendor/menu.md
- [~] programs/suites/marketplace/masks/cs-cart-multivendor/shortcuts.md
- [~] programs/suites/marketplace/masks/cs-cart-multivendor/structure.md

### marketplace / ebay
- [~] programs/suites/marketplace/masks/ebay/api.md
- [~] programs/suites/marketplace/masks/ebay/description.md
- [~] programs/suites/marketplace/masks/ebay/features.md
- [~] programs/suites/marketplace/masks/ebay/index.md
- [~] programs/suites/marketplace/masks/ebay/menu.md
- [~] programs/suites/marketplace/masks/ebay/shortcuts.md
- [~] programs/suites/marketplace/masks/ebay/structure.md

### marketplace / etsy
- [~] programs/suites/marketplace/masks/etsy/api.md
- [~] programs/suites/marketplace/masks/etsy/description.md
- [~] programs/suites/marketplace/masks/etsy/features.md
- [~] programs/suites/marketplace/masks/etsy/index.md
- [~] programs/suites/marketplace/masks/etsy/menu.md
- [~] programs/suites/marketplace/masks/etsy/shortcuts.md
- [~] programs/suites/marketplace/masks/etsy/structure.md

### marketplace / kleinanzeigen
- [~] programs/suites/marketplace/masks/kleinanzeigen/api.md
- [~] programs/suites/marketplace/masks/kleinanzeigen/description.md
- [~] programs/suites/marketplace/masks/kleinanzeigen/features.md
- [~] programs/suites/marketplace/masks/kleinanzeigen/index.md
- [~] programs/suites/marketplace/masks/kleinanzeigen/menu.md
- [~] programs/suites/marketplace/masks/kleinanzeigen/shortcuts.md
- [~] programs/suites/marketplace/masks/kleinanzeigen/structure.md

### marketplace / sharetribe
- [~] programs/suites/marketplace/masks/sharetribe/api.md
- [~] programs/suites/marketplace/masks/sharetribe/description.md
- [~] programs/suites/marketplace/masks/sharetribe/features.md
- [~] programs/suites/marketplace/masks/sharetribe/index.md
- [~] programs/suites/marketplace/masks/sharetribe/menu.md
- [~] programs/suites/marketplace/masks/sharetribe/shortcuts.md
- [~] programs/suites/marketplace/masks/sharetribe/structure.md

## messenger

- [ ] Pflichtmenge einfrieren → `programs/apps/messenger/requirements.md`

- [~] programs/apps/messenger/index.md
- [~] programs/apps/messenger/masks/index.md

### messenger / discord
- [~] programs/apps/messenger/masks/discord/api.md
- [~] programs/apps/messenger/masks/discord/description.md
- [~] programs/apps/messenger/masks/discord/features.md
- [~] programs/apps/messenger/masks/discord/index.md
- [~] programs/apps/messenger/masks/discord/menu.md
- [~] programs/apps/messenger/masks/discord/shortcuts.md
- [~] programs/apps/messenger/masks/discord/structure.md

### messenger / element
- [~] programs/apps/messenger/masks/element/api.md
- [~] programs/apps/messenger/masks/element/description.md
- [~] programs/apps/messenger/masks/element/features.md
- [~] programs/apps/messenger/masks/element/index.md
- [~] programs/apps/messenger/masks/element/menu.md
- [~] programs/apps/messenger/masks/element/shortcuts.md
- [~] programs/apps/messenger/masks/element/structure.md

### messenger / kontact
- [~] programs/apps/messenger/masks/kontact/api.md
- [~] programs/apps/messenger/masks/kontact/description.md
- [~] programs/apps/messenger/masks/kontact/features.md
- [~] programs/apps/messenger/masks/kontact/index.md
- [~] programs/apps/messenger/masks/kontact/menu.md
- [~] programs/apps/messenger/masks/kontact/shortcuts.md
- [~] programs/apps/messenger/masks/kontact/structure.md

### messenger / mastodon
- [~] programs/apps/messenger/masks/mastodon/api.md
- [~] programs/apps/messenger/masks/mastodon/description.md
- [~] programs/apps/messenger/masks/mastodon/features.md
- [~] programs/apps/messenger/masks/mastodon/index.md
- [~] programs/apps/messenger/masks/mastodon/menu.md
- [~] programs/apps/messenger/masks/mastodon/shortcuts.md
- [~] programs/apps/messenger/masks/mastodon/structure.md

### messenger / outlook
- [~] programs/apps/messenger/masks/outlook/api.md
- [~] programs/apps/messenger/masks/outlook/description.md
- [~] programs/apps/messenger/masks/outlook/features.md
- [~] programs/apps/messenger/masks/outlook/index.md
- [~] programs/apps/messenger/masks/outlook/menu.md
- [~] programs/apps/messenger/masks/outlook/shortcuts.md
- [~] programs/apps/messenger/masks/outlook/structure.md

### messenger / telegram
- [~] programs/apps/messenger/masks/telegram/api.md
- [~] programs/apps/messenger/masks/telegram/description.md
- [~] programs/apps/messenger/masks/telegram/features.md
- [~] programs/apps/messenger/masks/telegram/index.md
- [~] programs/apps/messenger/masks/telegram/menu.md
- [~] programs/apps/messenger/masks/telegram/shortcuts.md
- [~] programs/apps/messenger/masks/telegram/structure.md

### messenger / thunderbird
- [~] programs/apps/messenger/masks/thunderbird/api.md
- [~] programs/apps/messenger/masks/thunderbird/description.md
- [~] programs/apps/messenger/masks/thunderbird/features.md
- [~] programs/apps/messenger/masks/thunderbird/index.md
- [~] programs/apps/messenger/masks/thunderbird/menu.md
- [~] programs/apps/messenger/masks/thunderbird/shortcuts.md
- [~] programs/apps/messenger/masks/thunderbird/structure.md

## projectmanagement

- [ ] Pflichtmenge einfrieren → `programs/apps/projectmanagement/requirements.md`

- [~] programs/apps/projectmanagement/index.md
- [~] programs/apps/projectmanagement/masks/index.md

### projectmanagement / asana
- [~] programs/apps/projectmanagement/masks/asana/api.md
- [~] programs/apps/projectmanagement/masks/asana/description.md
- [~] programs/apps/projectmanagement/masks/asana/features.md
- [~] programs/apps/projectmanagement/masks/asana/index.md
- [~] programs/apps/projectmanagement/masks/asana/menu.md
- [~] programs/apps/projectmanagement/masks/asana/shortcuts.md
- [~] programs/apps/projectmanagement/masks/asana/structure.md

### projectmanagement / jira
- [~] programs/apps/projectmanagement/masks/jira/api.md
- [~] programs/apps/projectmanagement/masks/jira/description.md
- [~] programs/apps/projectmanagement/masks/jira/features.md
- [~] programs/apps/projectmanagement/masks/jira/index.md
- [~] programs/apps/projectmanagement/masks/jira/menu.md
- [~] programs/apps/projectmanagement/masks/jira/shortcuts.md
- [~] programs/apps/projectmanagement/masks/jira/structure.md

### projectmanagement / openproject
- [~] programs/apps/projectmanagement/masks/openproject/api.md
- [~] programs/apps/projectmanagement/masks/openproject/description.md
- [~] programs/apps/projectmanagement/masks/openproject/features.md
- [~] programs/apps/projectmanagement/masks/openproject/index.md
- [~] programs/apps/projectmanagement/masks/openproject/menu.md
- [~] programs/apps/projectmanagement/masks/openproject/shortcuts.md
- [~] programs/apps/projectmanagement/masks/openproject/structure.md

### projectmanagement / planka
- [~] programs/apps/projectmanagement/masks/planka/api.md
- [~] programs/apps/projectmanagement/masks/planka/description.md
- [~] programs/apps/projectmanagement/masks/planka/features.md
- [~] programs/apps/projectmanagement/masks/planka/index.md
- [~] programs/apps/projectmanagement/masks/planka/menu.md
- [~] programs/apps/projectmanagement/masks/planka/shortcuts.md
- [~] programs/apps/projectmanagement/masks/planka/structure.md

### projectmanagement / redmine
- [~] programs/apps/projectmanagement/masks/redmine/api.md
- [~] programs/apps/projectmanagement/masks/redmine/description.md
- [~] programs/apps/projectmanagement/masks/redmine/features.md
- [~] programs/apps/projectmanagement/masks/redmine/index.md
- [~] programs/apps/projectmanagement/masks/redmine/menu.md
- [~] programs/apps/projectmanagement/masks/redmine/shortcuts.md
- [~] programs/apps/projectmanagement/masks/redmine/structure.md

### projectmanagement / taiga
- [~] programs/apps/projectmanagement/masks/taiga/api.md
- [~] programs/apps/projectmanagement/masks/taiga/description.md
- [~] programs/apps/projectmanagement/masks/taiga/features.md
- [~] programs/apps/projectmanagement/masks/taiga/index.md
- [~] programs/apps/projectmanagement/masks/taiga/menu.md
- [~] programs/apps/projectmanagement/masks/taiga/shortcuts.md
- [~] programs/apps/projectmanagement/masks/taiga/structure.md

### projectmanagement / trello
- [~] programs/apps/projectmanagement/masks/trello/api.md
- [~] programs/apps/projectmanagement/masks/trello/description.md
- [~] programs/apps/projectmanagement/masks/trello/features.md
- [~] programs/apps/projectmanagement/masks/trello/index.md
- [~] programs/apps/projectmanagement/masks/trello/menu.md
- [~] programs/apps/projectmanagement/masks/trello/shortcuts.md
- [~] programs/apps/projectmanagement/masks/trello/structure.md

### projectmanagement / wekan
- [~] programs/apps/projectmanagement/masks/wekan/api.md
- [~] programs/apps/projectmanagement/masks/wekan/description.md
- [~] programs/apps/projectmanagement/masks/wekan/features.md
- [~] programs/apps/projectmanagement/masks/wekan/index.md
- [~] programs/apps/projectmanagement/masks/wekan/menu.md
- [~] programs/apps/projectmanagement/masks/wekan/shortcuts.md
- [~] programs/apps/projectmanagement/masks/wekan/structure.md

## streaming

- [ ] Pflichtmenge einfrieren → `programs/apps/streaming/requirements.md`

- [~] programs/apps/streaming/index.md
- [~] programs/apps/streaming/masks/index.md

### streaming / ant-media-server
- [~] programs/apps/streaming/masks/ant-media-server/api.md
- [~] programs/apps/streaming/masks/ant-media-server/description.md
- [~] programs/apps/streaming/masks/ant-media-server/features.md
- [~] programs/apps/streaming/masks/ant-media-server/index.md
- [~] programs/apps/streaming/masks/ant-media-server/menu.md
- [~] programs/apps/streaming/masks/ant-media-server/shortcuts.md
- [~] programs/apps/streaming/masks/ant-media-server/structure.md

### streaming / ffmpeg
- [~] programs/apps/streaming/masks/ffmpeg/api.md
- [~] programs/apps/streaming/masks/ffmpeg/description.md
- [~] programs/apps/streaming/masks/ffmpeg/features.md
- [~] programs/apps/streaming/masks/ffmpeg/index.md
- [~] programs/apps/streaming/masks/ffmpeg/menu.md
- [~] programs/apps/streaming/masks/ffmpeg/shortcuts.md
- [~] programs/apps/streaming/masks/ffmpeg/structure.md

### streaming / gstreamer
- [~] programs/apps/streaming/masks/gstreamer/api.md
- [~] programs/apps/streaming/masks/gstreamer/description.md
- [~] programs/apps/streaming/masks/gstreamer/features.md
- [~] programs/apps/streaming/masks/gstreamer/index.md
- [~] programs/apps/streaming/masks/gstreamer/menu.md
- [~] programs/apps/streaming/masks/gstreamer/shortcuts.md
- [~] programs/apps/streaming/masks/gstreamer/structure.md

### streaming / mediamtx
- [~] programs/apps/streaming/masks/mediamtx/api.md
- [~] programs/apps/streaming/masks/mediamtx/description.md
- [~] programs/apps/streaming/masks/mediamtx/features.md
- [~] programs/apps/streaming/masks/mediamtx/index.md
- [~] programs/apps/streaming/masks/mediamtx/menu.md
- [~] programs/apps/streaming/masks/mediamtx/shortcuts.md
- [~] programs/apps/streaming/masks/mediamtx/structure.md

### streaming / mistserver
- [~] programs/apps/streaming/masks/mistserver/api.md
- [~] programs/apps/streaming/masks/mistserver/description.md
- [~] programs/apps/streaming/masks/mistserver/features.md
- [~] programs/apps/streaming/masks/mistserver/index.md
- [~] programs/apps/streaming/masks/mistserver/menu.md
- [~] programs/apps/streaming/masks/mistserver/shortcuts.md
- [~] programs/apps/streaming/masks/mistserver/structure.md

### streaming / nginx-rtmp-module
- [~] programs/apps/streaming/masks/nginx-rtmp-module/api.md
- [~] programs/apps/streaming/masks/nginx-rtmp-module/description.md
- [~] programs/apps/streaming/masks/nginx-rtmp-module/features.md
- [~] programs/apps/streaming/masks/nginx-rtmp-module/index.md
- [~] programs/apps/streaming/masks/nginx-rtmp-module/menu.md
- [~] programs/apps/streaming/masks/nginx-rtmp-module/shortcuts.md
- [~] programs/apps/streaming/masks/nginx-rtmp-module/structure.md

### streaming / obs-studio
- [~] programs/apps/streaming/masks/obs-studio/api.md
- [~] programs/apps/streaming/masks/obs-studio/description.md
- [~] programs/apps/streaming/masks/obs-studio/features.md
- [~] programs/apps/streaming/masks/obs-studio/index.md
- [~] programs/apps/streaming/masks/obs-studio/menu.md
- [~] programs/apps/streaming/masks/obs-studio/shortcuts.md
- [~] programs/apps/streaming/masks/obs-studio/structure.md

### streaming / restream
- [~] programs/apps/streaming/masks/restream/api.md
- [~] programs/apps/streaming/masks/restream/description.md
- [~] programs/apps/streaming/masks/restream/features.md
- [~] programs/apps/streaming/masks/restream/index.md
- [~] programs/apps/streaming/masks/restream/menu.md
- [~] programs/apps/streaming/masks/restream/shortcuts.md
- [~] programs/apps/streaming/masks/restream/structure.md

### streaming / restreamer
- [~] programs/apps/streaming/masks/restreamer/api.md
- [~] programs/apps/streaming/masks/restreamer/description.md
- [~] programs/apps/streaming/masks/restreamer/features.md
- [~] programs/apps/streaming/masks/restreamer/index.md
- [~] programs/apps/streaming/masks/restreamer/menu.md
- [~] programs/apps/streaming/masks/restreamer/shortcuts.md
- [~] programs/apps/streaming/masks/restreamer/structure.md

### streaming / wowza
- [~] programs/apps/streaming/masks/wowza/api.md
- [~] programs/apps/streaming/masks/wowza/description.md
- [~] programs/apps/streaming/masks/wowza/features.md
- [~] programs/apps/streaming/masks/wowza/index.md
- [~] programs/apps/streaming/masks/wowza/menu.md
- [~] programs/apps/streaming/masks/wowza/shortcuts.md
- [~] programs/apps/streaming/masks/wowza/structure.md

## whiteboards

- [ ] Pflichtmenge einfrieren → `programs/apps/whiteboards/requirements.md`

- [~] programs/apps/whiteboards/index.md
- [~] programs/apps/whiteboards/masks/index.md

### whiteboards / drawio
- [~] programs/apps/whiteboards/masks/drawio/api.md
- [~] programs/apps/whiteboards/masks/drawio/description.md
- [~] programs/apps/whiteboards/masks/drawio/features.md
- [~] programs/apps/whiteboards/masks/drawio/index.md
- [~] programs/apps/whiteboards/masks/drawio/menu.md
- [~] programs/apps/whiteboards/masks/drawio/shortcuts.md
- [~] programs/apps/whiteboards/masks/drawio/structure.md

### whiteboards / excalidraw
- [~] programs/apps/whiteboards/masks/excalidraw/api.md
- [~] programs/apps/whiteboards/masks/excalidraw/description.md
- [~] programs/apps/whiteboards/masks/excalidraw/features.md
- [~] programs/apps/whiteboards/masks/excalidraw/index.md
- [~] programs/apps/whiteboards/masks/excalidraw/menu.md
- [~] programs/apps/whiteboards/masks/excalidraw/shortcuts.md
- [~] programs/apps/whiteboards/masks/excalidraw/structure.md

### whiteboards / miro
- [~] programs/apps/whiteboards/masks/miro/api.md
- [~] programs/apps/whiteboards/masks/miro/description.md
- [~] programs/apps/whiteboards/masks/miro/features.md
- [~] programs/apps/whiteboards/masks/miro/index.md
- [~] programs/apps/whiteboards/masks/miro/menu.md
- [~] programs/apps/whiteboards/masks/miro/shortcuts.md
- [~] programs/apps/whiteboards/masks/miro/structure.md

### whiteboards / mural
- [~] programs/apps/whiteboards/masks/mural/api.md
- [~] programs/apps/whiteboards/masks/mural/description.md
- [~] programs/apps/whiteboards/masks/mural/features.md
- [~] programs/apps/whiteboards/masks/mural/index.md
- [~] programs/apps/whiteboards/masks/mural/menu.md
- [~] programs/apps/whiteboards/masks/mural/shortcuts.md
- [~] programs/apps/whiteboards/masks/mural/structure.md

### whiteboards / openboard
- [~] programs/apps/whiteboards/masks/openboard/api.md
- [~] programs/apps/whiteboards/masks/openboard/description.md
- [~] programs/apps/whiteboards/masks/openboard/features.md
- [~] programs/apps/whiteboards/masks/openboard/index.md
- [~] programs/apps/whiteboards/masks/openboard/menu.md
- [~] programs/apps/whiteboards/masks/openboard/shortcuts.md
- [~] programs/apps/whiteboards/masks/openboard/structure.md

### whiteboards / tldraw
- [~] programs/apps/whiteboards/masks/tldraw/api.md
- [~] programs/apps/whiteboards/masks/tldraw/description.md
- [~] programs/apps/whiteboards/masks/tldraw/features.md
- [~] programs/apps/whiteboards/masks/tldraw/index.md
- [~] programs/apps/whiteboards/masks/tldraw/menu.md
- [~] programs/apps/whiteboards/masks/tldraw/shortcuts.md
- [~] programs/apps/whiteboards/masks/tldraw/structure.md

## wiki

- [ ] Pflichtmenge einfrieren → `programs/apps/wiki/requirements.md`

- [~] programs/apps/wiki/index.md
- [~] programs/apps/wiki/masks/index.md

### wiki / confluence
- [~] programs/apps/wiki/masks/confluence/api.md
- [~] programs/apps/wiki/masks/confluence/description.md
- [~] programs/apps/wiki/masks/confluence/features.md
- [~] programs/apps/wiki/masks/confluence/index.md
- [~] programs/apps/wiki/masks/confluence/menu.md
- [~] programs/apps/wiki/masks/confluence/shortcuts.md
- [~] programs/apps/wiki/masks/confluence/structure.md

### wiki / mediawiki
- [~] programs/apps/wiki/masks/mediawiki/api.md
- [~] programs/apps/wiki/masks/mediawiki/description.md
- [~] programs/apps/wiki/masks/mediawiki/features.md
- [~] programs/apps/wiki/masks/mediawiki/index.md
- [~] programs/apps/wiki/masks/mediawiki/menu.md
- [~] programs/apps/wiki/masks/mediawiki/shortcuts.md
- [~] programs/apps/wiki/masks/mediawiki/structure.md

### wiki / notion
- [~] programs/apps/wiki/masks/notion/api.md
- [~] programs/apps/wiki/masks/notion/description.md
- [~] programs/apps/wiki/masks/notion/features.md
- [~] programs/apps/wiki/masks/notion/index.md
- [~] programs/apps/wiki/masks/notion/menu.md
- [~] programs/apps/wiki/masks/notion/shortcuts.md
- [~] programs/apps/wiki/masks/notion/structure.md

### wiki / tango.io
- [~] programs/apps/wiki/masks/tango.io/api.md
- [~] programs/apps/wiki/masks/tango.io/description.md
- [~] programs/apps/wiki/masks/tango.io/features.md
- [~] programs/apps/wiki/masks/tango.io/index.md
- [~] programs/apps/wiki/masks/tango.io/menu.md
- [~] programs/apps/wiki/masks/tango.io/shortcuts.md
- [~] programs/apps/wiki/masks/tango.io/structure.md

### wiki / vscodium
- [~] programs/apps/wiki/masks/vscodium/api.md
- [~] programs/apps/wiki/masks/vscodium/description.md
- [~] programs/apps/wiki/masks/vscodium/features.md
- [~] programs/apps/wiki/masks/vscodium/index.md
- [~] programs/apps/wiki/masks/vscodium/menu.md
- [~] programs/apps/wiki/masks/vscodium/shortcuts.md
- [~] programs/apps/wiki/masks/vscodium/structure.md

### wiki / wikijs
- [~] programs/apps/wiki/masks/wikijs/api.md
- [~] programs/apps/wiki/masks/wikijs/description.md
- [~] programs/apps/wiki/masks/wikijs/features.md
- [~] programs/apps/wiki/masks/wikijs/index.md
- [~] programs/apps/wiki/masks/wikijs/menu.md
- [~] programs/apps/wiki/masks/wikijs/shortcuts.md
- [~] programs/apps/wiki/masks/wikijs/structure.md

### wiki / xwiki
- [~] programs/apps/wiki/masks/xwiki/api.md
- [~] programs/apps/wiki/masks/xwiki/description.md
- [~] programs/apps/wiki/masks/xwiki/features.md
- [~] programs/apps/wiki/masks/xwiki/index.md
- [~] programs/apps/wiki/masks/xwiki/menu.md
- [~] programs/apps/wiki/masks/xwiki/shortcuts.md
- [~] programs/apps/wiki/masks/xwiki/structure.md

## workflows

- [ ] Pflichtmenge einfrieren → `programs/suites/workflows/requirements.md`

- [~] programs/suites/workflows/index.md
- [~] programs/suites/workflows/masks/index.md

### workflows / apache-airflow
- [~] programs/suites/workflows/masks/apache-airflow/api.md
- [~] programs/suites/workflows/masks/apache-airflow/description.md
- [~] programs/suites/workflows/masks/apache-airflow/features.md
- [~] programs/suites/workflows/masks/apache-airflow/index.md
- [~] programs/suites/workflows/masks/apache-airflow/menu.md
- [~] programs/suites/workflows/masks/apache-airflow/shortcuts.md
- [~] programs/suites/workflows/masks/apache-airflow/structure.md

### workflows / make
- [~] programs/suites/workflows/masks/make/api.md
- [~] programs/suites/workflows/masks/make/description.md
- [~] programs/suites/workflows/masks/make/features.md
- [~] programs/suites/workflows/masks/make/index.md
- [~] programs/suites/workflows/masks/make/menu.md
- [~] programs/suites/workflows/masks/make/shortcuts.md
- [~] programs/suites/workflows/masks/make/structure.md

### workflows / n8n
- [~] programs/suites/workflows/masks/n8n/api.md
- [~] programs/suites/workflows/masks/n8n/description.md
- [~] programs/suites/workflows/masks/n8n/features.md
- [~] programs/suites/workflows/masks/n8n/index.md
- [~] programs/suites/workflows/masks/n8n/menu.md
- [~] programs/suites/workflows/masks/n8n/shortcuts.md
- [~] programs/suites/workflows/masks/n8n/structure.md

### workflows / node-red
- [~] programs/suites/workflows/masks/node-red/api.md
- [~] programs/suites/workflows/masks/node-red/description.md
- [~] programs/suites/workflows/masks/node-red/features.md
- [~] programs/suites/workflows/masks/node-red/index.md
- [~] programs/suites/workflows/masks/node-red/menu.md
- [~] programs/suites/workflows/masks/node-red/shortcuts.md
- [~] programs/suites/workflows/masks/node-red/structure.md

### workflows / prefect
- [~] programs/suites/workflows/masks/prefect/api.md
- [~] programs/suites/workflows/masks/prefect/description.md
- [~] programs/suites/workflows/masks/prefect/features.md
- [~] programs/suites/workflows/masks/prefect/index.md
- [~] programs/suites/workflows/masks/prefect/menu.md
- [~] programs/suites/workflows/masks/prefect/shortcuts.md
- [~] programs/suites/workflows/masks/prefect/structure.md

### workflows / zapier
- [~] programs/suites/workflows/masks/zapier/api.md
- [~] programs/suites/workflows/masks/zapier/description.md
- [~] programs/suites/workflows/masks/zapier/features.md
- [~] programs/suites/workflows/masks/zapier/index.md
- [~] programs/suites/workflows/masks/zapier/menu.md
- [~] programs/suites/workflows/masks/zapier/shortcuts.md
- [~] programs/suites/workflows/masks/zapier/structure.md

---
*Insgesamt 869 Dateien (davon 833 Skin-Dateien in 119 Programmen).*
