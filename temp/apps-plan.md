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
- [~] programs/apps/calendar/skins/index.md

### calendar / davical
- [x] programs/apps/calendar/skins/davical/api.md
- [x] programs/apps/calendar/skins/davical/description.md
- [x] programs/apps/calendar/skins/davical/features.md
- [x] programs/apps/calendar/skins/davical/index.md
- [x] programs/apps/calendar/skins/davical/menu.md
- [x] programs/apps/calendar/skins/davical/shortcuts.md
- [x] programs/apps/calendar/skins/davical/structure.md

### calendar / google-calendar
- [x] programs/apps/calendar/skins/google-calendar/api.md
- [x] programs/apps/calendar/skins/google-calendar/description.md
- [x] programs/apps/calendar/skins/google-calendar/features.md
- [x] programs/apps/calendar/skins/google-calendar/index.md
- [x] programs/apps/calendar/skins/google-calendar/menu.md
- [x] programs/apps/calendar/skins/google-calendar/shortcuts.md
- [x] programs/apps/calendar/skins/google-calendar/structure.md

### calendar / merkuro
- [x] programs/apps/calendar/skins/merkuro/api.md
- [x] programs/apps/calendar/skins/merkuro/description.md
- [x] programs/apps/calendar/skins/merkuro/features.md
- [x] programs/apps/calendar/skins/merkuro/index.md
- [x] programs/apps/calendar/skins/merkuro/menu.md
- [x] programs/apps/calendar/skins/merkuro/shortcuts.md
- [x] programs/apps/calendar/skins/merkuro/structure.md

### calendar / nextcloud-calendar
- [x] programs/apps/calendar/skins/nextcloud-calendar/api.md
- [x] programs/apps/calendar/skins/nextcloud-calendar/description.md
- [x] programs/apps/calendar/skins/nextcloud-calendar/features.md
- [x] programs/apps/calendar/skins/nextcloud-calendar/index.md
- [x] programs/apps/calendar/skins/nextcloud-calendar/menu.md
- [x] programs/apps/calendar/skins/nextcloud-calendar/shortcuts.md
- [x] programs/apps/calendar/skins/nextcloud-calendar/structure.md

### calendar / outlook-calendar
- [x] programs/apps/calendar/skins/outlook-calendar/api.md
- [x] programs/apps/calendar/skins/outlook-calendar/description.md
- [x] programs/apps/calendar/skins/outlook-calendar/features.md
- [x] programs/apps/calendar/skins/outlook-calendar/index.md
- [x] programs/apps/calendar/skins/outlook-calendar/menu.md
- [x] programs/apps/calendar/skins/outlook-calendar/shortcuts.md
- [x] programs/apps/calendar/skins/outlook-calendar/structure.md

### calendar / planner
- [x] programs/apps/calendar/skins/planner/api.md
- [x] programs/apps/calendar/skins/planner/description.md
- [x] programs/apps/calendar/skins/planner/features.md
- [x] programs/apps/calendar/skins/planner/index.md
- [x] programs/apps/calendar/skins/planner/menu.md
- [x] programs/apps/calendar/skins/planner/shortcuts.md
- [x] programs/apps/calendar/skins/planner/structure.md

## contact

- [ ] Pflichtmenge einfrieren → `programs/apps/contact/requirements.md`

- [~] programs/apps/contact/index.md
- [~] programs/apps/contact/skins/index.md

### contact / gnome-contacts
- [~] programs/apps/contact/skins/gnome-contacts/api.md
- [~] programs/apps/contact/skins/gnome-contacts/description.md
- [~] programs/apps/contact/skins/gnome-contacts/features.md
- [~] programs/apps/contact/skins/gnome-contacts/index.md
- [~] programs/apps/contact/skins/gnome-contacts/menu.md
- [~] programs/apps/contact/skins/gnome-contacts/shortcuts.md
- [~] programs/apps/contact/skins/gnome-contacts/structure.md

### contact / kaddressbook
- [~] programs/apps/contact/skins/kaddressbook/api.md
- [~] programs/apps/contact/skins/kaddressbook/description.md
- [~] programs/apps/contact/skins/kaddressbook/features.md
- [~] programs/apps/contact/skins/kaddressbook/index.md
- [~] programs/apps/contact/skins/kaddressbook/menu.md
- [~] programs/apps/contact/skins/kaddressbook/shortcuts.md
- [~] programs/apps/contact/skins/kaddressbook/structure.md

### contact / monica
- [~] programs/apps/contact/skins/monica/api.md
- [~] programs/apps/contact/skins/monica/description.md
- [~] programs/apps/contact/skins/monica/features.md
- [~] programs/apps/contact/skins/monica/index.md
- [~] programs/apps/contact/skins/monica/menu.md
- [~] programs/apps/contact/skins/monica/shortcuts.md
- [~] programs/apps/contact/skins/monica/structure.md

### contact / nextcloud-contacts
- [~] programs/apps/contact/skins/nextcloud-contacts/api.md
- [~] programs/apps/contact/skins/nextcloud-contacts/description.md
- [~] programs/apps/contact/skins/nextcloud-contacts/features.md
- [~] programs/apps/contact/skins/nextcloud-contacts/index.md
- [~] programs/apps/contact/skins/nextcloud-contacts/menu.md
- [~] programs/apps/contact/skins/nextcloud-contacts/shortcuts.md
- [~] programs/apps/contact/skins/nextcloud-contacts/structure.md

## crm

- [ ] Pflichtmenge einfrieren → `programs/suites/crm/requirements.md`

- [~] programs/suites/crm/index.md
- [~] programs/suites/crm/skins/index.md

### crm / civicrm
- [~] programs/suites/crm/skins/civicrm/api.md
- [~] programs/suites/crm/skins/civicrm/description.md
- [~] programs/suites/crm/skins/civicrm/features.md
- [~] programs/suites/crm/skins/civicrm/index.md
- [~] programs/suites/crm/skins/civicrm/menu.md
- [~] programs/suites/crm/skins/civicrm/shortcuts.md
- [~] programs/suites/crm/skins/civicrm/structure.md

### crm / espocrm
- [~] programs/suites/crm/skins/espocrm/api.md
- [~] programs/suites/crm/skins/espocrm/description.md
- [~] programs/suites/crm/skins/espocrm/features.md
- [~] programs/suites/crm/skins/espocrm/index.md
- [~] programs/suites/crm/skins/espocrm/menu.md
- [~] programs/suites/crm/skins/espocrm/shortcuts.md
- [~] programs/suites/crm/skins/espocrm/structure.md

### crm / hubspot
- [~] programs/suites/crm/skins/hubspot/api.md
- [~] programs/suites/crm/skins/hubspot/description.md
- [~] programs/suites/crm/skins/hubspot/features.md
- [~] programs/suites/crm/skins/hubspot/index.md
- [~] programs/suites/crm/skins/hubspot/menu.md
- [~] programs/suites/crm/skins/hubspot/shortcuts.md
- [~] programs/suites/crm/skins/hubspot/structure.md

### crm / pipedrive
- [~] programs/suites/crm/skins/pipedrive/api.md
- [~] programs/suites/crm/skins/pipedrive/description.md
- [~] programs/suites/crm/skins/pipedrive/features.md
- [~] programs/suites/crm/skins/pipedrive/index.md
- [~] programs/suites/crm/skins/pipedrive/menu.md
- [~] programs/suites/crm/skins/pipedrive/shortcuts.md
- [~] programs/suites/crm/skins/pipedrive/structure.md

### crm / salesforce
- [~] programs/suites/crm/skins/salesforce/api.md
- [~] programs/suites/crm/skins/salesforce/description.md
- [~] programs/suites/crm/skins/salesforce/features.md
- [~] programs/suites/crm/skins/salesforce/index.md
- [~] programs/suites/crm/skins/salesforce/menu.md
- [~] programs/suites/crm/skins/salesforce/shortcuts.md
- [~] programs/suites/crm/skins/salesforce/structure.md

### crm / suitecrm
- [~] programs/suites/crm/skins/suitecrm/api.md
- [~] programs/suites/crm/skins/suitecrm/description.md
- [~] programs/suites/crm/skins/suitecrm/features.md
- [~] programs/suites/crm/skins/suitecrm/index.md
- [~] programs/suites/crm/skins/suitecrm/menu.md
- [~] programs/suites/crm/skins/suitecrm/shortcuts.md
- [~] programs/suites/crm/skins/suitecrm/structure.md

## democracy

- [ ] Pflichtmenge einfrieren → `programs/suites/democracy/requirements.md`

- [~] programs/suites/democracy/index.md
- [~] programs/suites/democracy/skins/index.md

### democracy / adhocracy4
- [~] programs/suites/democracy/skins/adhocracy4/api.md
- [~] programs/suites/democracy/skins/adhocracy4/description.md
- [~] programs/suites/democracy/skins/adhocracy4/features.md
- [~] programs/suites/democracy/skins/adhocracy4/index.md
- [~] programs/suites/democracy/skins/adhocracy4/menu.md
- [~] programs/suites/democracy/skins/adhocracy4/shortcuts.md
- [~] programs/suites/democracy/skins/adhocracy4/structure.md

### democracy / circo
- [~] programs/suites/democracy/skins/circo/api.md
- [~] programs/suites/democracy/skins/circo/description.md
- [~] programs/suites/democracy/skins/circo/features.md
- [~] programs/suites/democracy/skins/circo/index.md
- [~] programs/suites/democracy/skins/circo/menu.md
- [~] programs/suites/democracy/skins/circo/shortcuts.md
- [~] programs/suites/democracy/skins/circo/structure.md

### democracy / consul
- [~] programs/suites/democracy/skins/consul/api.md
- [~] programs/suites/democracy/skins/consul/description.md
- [~] programs/suites/democracy/skins/consul/features.md
- [~] programs/suites/democracy/skins/consul/index.md
- [~] programs/suites/democracy/skins/consul/menu.md
- [~] programs/suites/democracy/skins/consul/shortcuts.md
- [~] programs/suites/democracy/skins/consul/structure.md

### democracy / decidim
- [~] programs/suites/democracy/skins/decidim/api.md
- [~] programs/suites/democracy/skins/decidim/description.md
- [~] programs/suites/democracy/skins/decidim/features.md
- [~] programs/suites/democracy/skins/decidim/index.md
- [~] programs/suites/democracy/skins/decidim/menu.md
- [~] programs/suites/democracy/skins/decidim/shortcuts.md
- [~] programs/suites/democracy/skins/decidim/structure.md

### democracy / liquid-feedback
- [~] programs/suites/democracy/skins/liquid-feedback/api.md
- [~] programs/suites/democracy/skins/liquid-feedback/description.md
- [~] programs/suites/democracy/skins/liquid-feedback/features.md
- [~] programs/suites/democracy/skins/liquid-feedback/index.md
- [~] programs/suites/democracy/skins/liquid-feedback/menu.md
- [~] programs/suites/democracy/skins/liquid-feedback/shortcuts.md
- [~] programs/suites/democracy/skins/liquid-feedback/structure.md

### democracy / polis
- [~] programs/suites/democracy/skins/polis/api.md
- [~] programs/suites/democracy/skins/polis/description.md
- [~] programs/suites/democracy/skins/polis/features.md
- [~] programs/suites/democracy/skins/polis/index.md
- [~] programs/suites/democracy/skins/polis/menu.md
- [~] programs/suites/democracy/skins/polis/shortcuts.md
- [~] programs/suites/democracy/skins/polis/structure.md

## desktop

- [ ] Pflichtmenge einfrieren → `programs/platform/desktop/requirements.md`

- [~] programs/platform/desktop/index.md
- [~] programs/platform/desktop/skins/index.md

### desktop / dashy
- [~] programs/platform/desktop/skins/dashy/api.md
- [~] programs/platform/desktop/skins/dashy/description.md
- [~] programs/platform/desktop/skins/dashy/features.md
- [~] programs/platform/desktop/skins/dashy/index.md
- [~] programs/platform/desktop/skins/dashy/menu.md
- [~] programs/platform/desktop/skins/dashy/shortcuts.md
- [~] programs/platform/desktop/skins/dashy/structure.md

### desktop / gethomepage
- [~] programs/platform/desktop/skins/gethomepage/api.md
- [~] programs/platform/desktop/skins/gethomepage/description.md
- [~] programs/platform/desktop/skins/gethomepage/features.md
- [~] programs/platform/desktop/skins/gethomepage/index.md
- [~] programs/platform/desktop/skins/gethomepage/menu.md
- [~] programs/platform/desktop/skins/gethomepage/shortcuts.md
- [~] programs/platform/desktop/skins/gethomepage/structure.md

### desktop / heimdall
- [~] programs/platform/desktop/skins/heimdall/api.md
- [~] programs/platform/desktop/skins/heimdall/description.md
- [~] programs/platform/desktop/skins/heimdall/features.md
- [~] programs/platform/desktop/skins/heimdall/index.md
- [~] programs/platform/desktop/skins/heimdall/menu.md
- [~] programs/platform/desktop/skins/heimdall/shortcuts.md
- [~] programs/platform/desktop/skins/heimdall/structure.md

### desktop / homarr
- [~] programs/platform/desktop/skins/homarr/api.md
- [~] programs/platform/desktop/skins/homarr/description.md
- [~] programs/platform/desktop/skins/homarr/features.md
- [~] programs/platform/desktop/skins/homarr/index.md
- [~] programs/platform/desktop/skins/homarr/menu.md
- [~] programs/platform/desktop/skins/homarr/shortcuts.md
- [~] programs/platform/desktop/skins/homarr/structure.md

### desktop / homepage
- [~] programs/platform/desktop/skins/homepage/api.md
- [~] programs/platform/desktop/skins/homepage/description.md
- [~] programs/platform/desktop/skins/homepage/features.md
- [~] programs/platform/desktop/skins/homepage/index.md
- [~] programs/platform/desktop/skins/homepage/menu.md
- [~] programs/platform/desktop/skins/homepage/shortcuts.md
- [~] programs/platform/desktop/skins/homepage/structure.md

### desktop / homer
- [~] programs/platform/desktop/skins/homer/api.md
- [~] programs/platform/desktop/skins/homer/description.md
- [~] programs/platform/desktop/skins/homer/features.md
- [~] programs/platform/desktop/skins/homer/index.md
- [~] programs/platform/desktop/skins/homer/menu.md
- [~] programs/platform/desktop/skins/homer/shortcuts.md
- [~] programs/platform/desktop/skins/homer/structure.md

### desktop / launchboard
- [~] programs/platform/desktop/skins/launchboard/api.md
- [~] programs/platform/desktop/skins/launchboard/description.md
- [~] programs/platform/desktop/skins/launchboard/features.md
- [~] programs/platform/desktop/skins/launchboard/index.md
- [~] programs/platform/desktop/skins/launchboard/menu.md
- [~] programs/platform/desktop/skins/launchboard/shortcuts.md
- [~] programs/platform/desktop/skins/launchboard/structure.md

### desktop / opnsense
- [~] programs/platform/desktop/skins/opnsense/api.md
- [~] programs/platform/desktop/skins/opnsense/description.md
- [~] programs/platform/desktop/skins/opnsense/features.md
- [~] programs/platform/desktop/skins/opnsense/index.md
- [~] programs/platform/desktop/skins/opnsense/menu.md
- [~] programs/platform/desktop/skins/opnsense/shortcuts.md
- [~] programs/platform/desktop/skins/opnsense/structure.md

### desktop / proxmox
- [~] programs/platform/desktop/skins/proxmox/api.md
- [~] programs/platform/desktop/skins/proxmox/description.md
- [~] programs/platform/desktop/skins/proxmox/features.md
- [~] programs/platform/desktop/skins/proxmox/index.md
- [~] programs/platform/desktop/skins/proxmox/menu.md
- [~] programs/platform/desktop/skins/proxmox/shortcuts.md
- [~] programs/platform/desktop/skins/proxmox/structure.md

### desktop / synology-dsm
- [~] programs/platform/desktop/skins/synology-dsm/api.md
- [~] programs/platform/desktop/skins/synology-dsm/description.md
- [~] programs/platform/desktop/skins/synology-dsm/features.md
- [~] programs/platform/desktop/skins/synology-dsm/index.md
- [~] programs/platform/desktop/skins/synology-dsm/menu.md
- [~] programs/platform/desktop/skins/synology-dsm/shortcuts.md
- [~] programs/platform/desktop/skins/synology-dsm/structure.md

### desktop / truenas
- [~] programs/platform/desktop/skins/truenas/api.md
- [~] programs/platform/desktop/skins/truenas/description.md
- [~] programs/platform/desktop/skins/truenas/features.md
- [~] programs/platform/desktop/skins/truenas/index.md
- [~] programs/platform/desktop/skins/truenas/menu.md
- [~] programs/platform/desktop/skins/truenas/shortcuts.md
- [~] programs/platform/desktop/skins/truenas/structure.md

### desktop / unraid
- [~] programs/platform/desktop/skins/unraid/api.md
- [~] programs/platform/desktop/skins/unraid/description.md
- [~] programs/platform/desktop/skins/unraid/features.md
- [~] programs/platform/desktop/skins/unraid/index.md
- [~] programs/platform/desktop/skins/unraid/menu.md
- [~] programs/platform/desktop/skins/unraid/shortcuts.md
- [~] programs/platform/desktop/skins/unraid/structure.md

## erp

- [ ] Pflichtmenge einfrieren → `programs/suites/erp/requirements.md`

- [~] programs/suites/erp/index.md
- [~] programs/suites/erp/skins/index.md

### erp / axelor
- [~] programs/suites/erp/skins/axelor/api.md
- [~] programs/suites/erp/skins/axelor/description.md
- [~] programs/suites/erp/skins/axelor/features.md
- [~] programs/suites/erp/skins/axelor/index.md
- [~] programs/suites/erp/skins/axelor/menu.md
- [~] programs/suites/erp/skins/axelor/shortcuts.md
- [~] programs/suites/erp/skins/axelor/structure.md

### erp / dolibarr
- [~] programs/suites/erp/skins/dolibarr/api.md
- [~] programs/suites/erp/skins/dolibarr/description.md
- [~] programs/suites/erp/skins/dolibarr/features.md
- [~] programs/suites/erp/skins/dolibarr/index.md
- [~] programs/suites/erp/skins/dolibarr/menu.md
- [~] programs/suites/erp/skins/dolibarr/shortcuts.md
- [~] programs/suites/erp/skins/dolibarr/structure.md

### erp / erpnext
- [~] programs/suites/erp/skins/erpnext/api.md
- [~] programs/suites/erp/skins/erpnext/description.md
- [~] programs/suites/erp/skins/erpnext/features.md
- [~] programs/suites/erp/skins/erpnext/index.md
- [~] programs/suites/erp/skins/erpnext/menu.md
- [~] programs/suites/erp/skins/erpnext/shortcuts.md
- [~] programs/suites/erp/skins/erpnext/structure.md

### erp / odoo
- [~] programs/suites/erp/skins/odoo/api.md
- [~] programs/suites/erp/skins/odoo/description.md
- [~] programs/suites/erp/skins/odoo/features.md
- [~] programs/suites/erp/skins/odoo/index.md
- [~] programs/suites/erp/skins/odoo/menu.md
- [~] programs/suites/erp/skins/odoo/shortcuts.md
- [~] programs/suites/erp/skins/odoo/structure.md

### erp / sage
- [~] programs/suites/erp/skins/sage/api.md
- [~] programs/suites/erp/skins/sage/description.md
- [~] programs/suites/erp/skins/sage/features.md
- [~] programs/suites/erp/skins/sage/index.md
- [~] programs/suites/erp/skins/sage/menu.md
- [~] programs/suites/erp/skins/sage/shortcuts.md
- [~] programs/suites/erp/skins/sage/structure.md

### erp / tryton
- [~] programs/suites/erp/skins/tryton/api.md
- [~] programs/suites/erp/skins/tryton/description.md
- [~] programs/suites/erp/skins/tryton/features.md
- [~] programs/suites/erp/skins/tryton/index.md
- [~] programs/suites/erp/skins/tryton/menu.md
- [~] programs/suites/erp/skins/tryton/shortcuts.md
- [~] programs/suites/erp/skins/tryton/structure.md

## gallery

- [ ] Pflichtmenge einfrieren → `programs/apps/gallery/requirements.md`

- [~] programs/apps/gallery/index.md
- [~] programs/apps/gallery/skins/index.md

### gallery / coppermine
- [~] programs/apps/gallery/skins/coppermine/api.md
- [~] programs/apps/gallery/skins/coppermine/description.md
- [~] programs/apps/gallery/skins/coppermine/features.md
- [~] programs/apps/gallery/skins/coppermine/index.md
- [~] programs/apps/gallery/skins/coppermine/menu.md
- [~] programs/apps/gallery/skins/coppermine/shortcuts.md
- [~] programs/apps/gallery/skins/coppermine/structure.md

### gallery / damselfly
- [~] programs/apps/gallery/skins/damselfly/api.md
- [~] programs/apps/gallery/skins/damselfly/description.md
- [~] programs/apps/gallery/skins/damselfly/features.md
- [~] programs/apps/gallery/skins/damselfly/index.md
- [~] programs/apps/gallery/skins/damselfly/menu.md
- [~] programs/apps/gallery/skins/damselfly/shortcuts.md
- [~] programs/apps/gallery/skins/damselfly/structure.md

### gallery / immich
- [~] programs/apps/gallery/skins/immich/api.md
- [~] programs/apps/gallery/skins/immich/description.md
- [~] programs/apps/gallery/skins/immich/features.md
- [~] programs/apps/gallery/skins/immich/index.md
- [~] programs/apps/gallery/skins/immich/menu.md
- [~] programs/apps/gallery/skins/immich/shortcuts.md
- [~] programs/apps/gallery/skins/immich/structure.md

### gallery / librephotos
- [~] programs/apps/gallery/skins/librephotos/api.md
- [~] programs/apps/gallery/skins/librephotos/description.md
- [~] programs/apps/gallery/skins/librephotos/features.md
- [~] programs/apps/gallery/skins/librephotos/index.md
- [~] programs/apps/gallery/skins/librephotos/menu.md
- [~] programs/apps/gallery/skins/librephotos/shortcuts.md
- [~] programs/apps/gallery/skins/librephotos/structure.md

### gallery / lychee
- [~] programs/apps/gallery/skins/lychee/api.md
- [~] programs/apps/gallery/skins/lychee/description.md
- [~] programs/apps/gallery/skins/lychee/features.md
- [~] programs/apps/gallery/skins/lychee/index.md
- [~] programs/apps/gallery/skins/lychee/menu.md
- [~] programs/apps/gallery/skins/lychee/shortcuts.md
- [~] programs/apps/gallery/skins/lychee/structure.md

### gallery / nextcloud-photos
- [~] programs/apps/gallery/skins/nextcloud-photos/api.md
- [~] programs/apps/gallery/skins/nextcloud-photos/description.md
- [~] programs/apps/gallery/skins/nextcloud-photos/features.md
- [~] programs/apps/gallery/skins/nextcloud-photos/index.md
- [~] programs/apps/gallery/skins/nextcloud-photos/menu.md
- [~] programs/apps/gallery/skins/nextcloud-photos/shortcuts.md
- [~] programs/apps/gallery/skins/nextcloud-photos/structure.md

### gallery / photoprism
- [~] programs/apps/gallery/skins/photoprism/api.md
- [~] programs/apps/gallery/skins/photoprism/description.md
- [~] programs/apps/gallery/skins/photoprism/features.md
- [~] programs/apps/gallery/skins/photoprism/index.md
- [~] programs/apps/gallery/skins/photoprism/menu.md
- [~] programs/apps/gallery/skins/photoprism/shortcuts.md
- [~] programs/apps/gallery/skins/photoprism/structure.md

### gallery / piwigo
- [~] programs/apps/gallery/skins/piwigo/api.md
- [~] programs/apps/gallery/skins/piwigo/description.md
- [~] programs/apps/gallery/skins/piwigo/features.md
- [~] programs/apps/gallery/skins/piwigo/index.md
- [~] programs/apps/gallery/skins/piwigo/menu.md
- [~] programs/apps/gallery/skins/piwigo/shortcuts.md
- [~] programs/apps/gallery/skins/piwigo/structure.md

## helpdesk

- [ ] Pflichtmenge einfrieren → `programs/apps/helpdesk/requirements.md`

- [~] programs/apps/helpdesk/index.md
- [~] programs/apps/helpdesk/skins/index.md

### helpdesk / freshdesk
- [~] programs/apps/helpdesk/skins/freshdesk/api.md
- [~] programs/apps/helpdesk/skins/freshdesk/description.md
- [~] programs/apps/helpdesk/skins/freshdesk/features.md
- [~] programs/apps/helpdesk/skins/freshdesk/index.md
- [~] programs/apps/helpdesk/skins/freshdesk/menu.md
- [~] programs/apps/helpdesk/skins/freshdesk/shortcuts.md
- [~] programs/apps/helpdesk/skins/freshdesk/structure.md

### helpdesk / glpi
- [~] programs/apps/helpdesk/skins/glpi/api.md
- [~] programs/apps/helpdesk/skins/glpi/description.md
- [~] programs/apps/helpdesk/skins/glpi/features.md
- [~] programs/apps/helpdesk/skins/glpi/index.md
- [~] programs/apps/helpdesk/skins/glpi/menu.md
- [~] programs/apps/helpdesk/skins/glpi/shortcuts.md
- [~] programs/apps/helpdesk/skins/glpi/structure.md

### helpdesk / helodesk
- [~] programs/apps/helpdesk/skins/helodesk/api.md
- [~] programs/apps/helpdesk/skins/helodesk/description.md
- [~] programs/apps/helpdesk/skins/helodesk/features.md
- [~] programs/apps/helpdesk/skins/helodesk/index.md
- [~] programs/apps/helpdesk/skins/helodesk/menu.md
- [~] programs/apps/helpdesk/skins/helodesk/shortcuts.md
- [~] programs/apps/helpdesk/skins/helodesk/structure.md

### helpdesk / helpscout
- [~] programs/apps/helpdesk/skins/helpscout/api.md
- [~] programs/apps/helpdesk/skins/helpscout/description.md
- [~] programs/apps/helpdesk/skins/helpscout/features.md
- [~] programs/apps/helpdesk/skins/helpscout/index.md
- [~] programs/apps/helpdesk/skins/helpscout/menu.md
- [~] programs/apps/helpdesk/skins/helpscout/shortcuts.md
- [~] programs/apps/helpdesk/skins/helpscout/structure.md

### helpdesk / osticket
- [~] programs/apps/helpdesk/skins/osticket/api.md
- [~] programs/apps/helpdesk/skins/osticket/description.md
- [~] programs/apps/helpdesk/skins/osticket/features.md
- [~] programs/apps/helpdesk/skins/osticket/index.md
- [~] programs/apps/helpdesk/skins/osticket/menu.md
- [~] programs/apps/helpdesk/skins/osticket/shortcuts.md
- [~] programs/apps/helpdesk/skins/osticket/structure.md

### helpdesk / request-tracker
- [~] programs/apps/helpdesk/skins/request-tracker/api.md
- [~] programs/apps/helpdesk/skins/request-tracker/description.md
- [~] programs/apps/helpdesk/skins/request-tracker/features.md
- [~] programs/apps/helpdesk/skins/request-tracker/index.md
- [~] programs/apps/helpdesk/skins/request-tracker/menu.md
- [~] programs/apps/helpdesk/skins/request-tracker/shortcuts.md
- [~] programs/apps/helpdesk/skins/request-tracker/structure.md

### helpdesk / zammad
- [~] programs/apps/helpdesk/skins/zammad/api.md
- [~] programs/apps/helpdesk/skins/zammad/description.md
- [~] programs/apps/helpdesk/skins/zammad/features.md
- [~] programs/apps/helpdesk/skins/zammad/index.md
- [~] programs/apps/helpdesk/skins/zammad/menu.md
- [~] programs/apps/helpdesk/skins/zammad/shortcuts.md
- [~] programs/apps/helpdesk/skins/zammad/structure.md

### helpdesk / zendesk
- [~] programs/apps/helpdesk/skins/zendesk/api.md
- [~] programs/apps/helpdesk/skins/zendesk/description.md
- [~] programs/apps/helpdesk/skins/zendesk/features.md
- [~] programs/apps/helpdesk/skins/zendesk/index.md
- [~] programs/apps/helpdesk/skins/zendesk/menu.md
- [~] programs/apps/helpdesk/skins/zendesk/shortcuts.md
- [~] programs/apps/helpdesk/skins/zendesk/structure.md

## maps

- [ ] Pflichtmenge einfrieren → `programs/apps/maps/requirements.md`

- [~] programs/apps/maps/index.md
- [~] programs/apps/maps/skins/index.md
- [~] programs/apps/maps/standpunkte.md

### maps / leaflet
- [~] programs/apps/maps/skins/leaflet/api.md
- [~] programs/apps/maps/skins/leaflet/description.md
- [~] programs/apps/maps/skins/leaflet/features.md
- [~] programs/apps/maps/skins/leaflet/index.md
- [~] programs/apps/maps/skins/leaflet/menu.md
- [~] programs/apps/maps/skins/leaflet/shortcuts.md
- [~] programs/apps/maps/skins/leaflet/structure.md

### maps / maplibre
- [~] programs/apps/maps/skins/maplibre/api.md
- [~] programs/apps/maps/skins/maplibre/description.md
- [~] programs/apps/maps/skins/maplibre/features.md
- [~] programs/apps/maps/skins/maplibre/index.md
- [~] programs/apps/maps/skins/maplibre/menu.md
- [~] programs/apps/maps/skins/maplibre/shortcuts.md
- [~] programs/apps/maps/skins/maplibre/structure.md

### maps / openstreetmap
- [~] programs/apps/maps/skins/openstreetmap/api.md
- [~] programs/apps/maps/skins/openstreetmap/description.md
- [~] programs/apps/maps/skins/openstreetmap/features.md
- [~] programs/apps/maps/skins/openstreetmap/index.md
- [~] programs/apps/maps/skins/openstreetmap/menu.md
- [~] programs/apps/maps/skins/openstreetmap/shortcuts.md
- [~] programs/apps/maps/skins/openstreetmap/structure.md

### maps / organic-maps
- [~] programs/apps/maps/skins/organic-maps/api.md
- [~] programs/apps/maps/skins/organic-maps/description.md
- [~] programs/apps/maps/skins/organic-maps/features.md
- [~] programs/apps/maps/skins/organic-maps/index.md
- [~] programs/apps/maps/skins/organic-maps/menu.md
- [~] programs/apps/maps/skins/organic-maps/shortcuts.md
- [~] programs/apps/maps/skins/organic-maps/structure.md

### maps / osmand
- [~] programs/apps/maps/skins/osmand/api.md
- [~] programs/apps/maps/skins/osmand/description.md
- [~] programs/apps/maps/skins/osmand/features.md
- [~] programs/apps/maps/skins/osmand/index.md
- [~] programs/apps/maps/skins/osmand/menu.md
- [~] programs/apps/maps/skins/osmand/shortcuts.md
- [~] programs/apps/maps/skins/osmand/structure.md

### maps / qgis
- [~] programs/apps/maps/skins/qgis/api.md
- [~] programs/apps/maps/skins/qgis/description.md
- [~] programs/apps/maps/skins/qgis/features.md
- [~] programs/apps/maps/skins/qgis/index.md
- [~] programs/apps/maps/skins/qgis/menu.md
- [~] programs/apps/maps/skins/qgis/shortcuts.md
- [~] programs/apps/maps/skins/qgis/structure.md

### maps / umap
- [~] programs/apps/maps/skins/umap/api.md
- [~] programs/apps/maps/skins/umap/description.md
- [~] programs/apps/maps/skins/umap/features.md
- [~] programs/apps/maps/skins/umap/index.md
- [~] programs/apps/maps/skins/umap/menu.md
- [~] programs/apps/maps/skins/umap/shortcuts.md
- [~] programs/apps/maps/skins/umap/structure.md

## marketing

- [ ] Pflichtmenge einfrieren → `programs/apps/marketing/requirements.md`

- [~] programs/apps/marketing/index.md
- [~] programs/apps/marketing/skins/index.md

### marketing / google-analytics
- [~] programs/apps/marketing/skins/google-analytics/api.md
- [~] programs/apps/marketing/skins/google-analytics/description.md
- [~] programs/apps/marketing/skins/google-analytics/features.md
- [~] programs/apps/marketing/skins/google-analytics/index.md
- [~] programs/apps/marketing/skins/google-analytics/menu.md
- [~] programs/apps/marketing/skins/google-analytics/shortcuts.md
- [~] programs/apps/marketing/skins/google-analytics/structure.md

### marketing / hotjar
- [~] programs/apps/marketing/skins/hotjar/api.md
- [~] programs/apps/marketing/skins/hotjar/description.md
- [~] programs/apps/marketing/skins/hotjar/features.md
- [~] programs/apps/marketing/skins/hotjar/index.md
- [~] programs/apps/marketing/skins/hotjar/menu.md
- [~] programs/apps/marketing/skins/hotjar/shortcuts.md
- [~] programs/apps/marketing/skins/hotjar/structure.md

### marketing / mailchimp
- [~] programs/apps/marketing/skins/mailchimp/api.md
- [~] programs/apps/marketing/skins/mailchimp/description.md
- [~] programs/apps/marketing/skins/mailchimp/features.md
- [~] programs/apps/marketing/skins/mailchimp/index.md
- [~] programs/apps/marketing/skins/mailchimp/menu.md
- [~] programs/apps/marketing/skins/mailchimp/shortcuts.md
- [~] programs/apps/marketing/skins/mailchimp/structure.md

### marketing / matomo
- [~] programs/apps/marketing/skins/matomo/api.md
- [~] programs/apps/marketing/skins/matomo/description.md
- [~] programs/apps/marketing/skins/matomo/features.md
- [~] programs/apps/marketing/skins/matomo/index.md
- [~] programs/apps/marketing/skins/matomo/menu.md
- [~] programs/apps/marketing/skins/matomo/shortcuts.md
- [~] programs/apps/marketing/skins/matomo/structure.md

### marketing / mautic
- [~] programs/apps/marketing/skins/mautic/api.md
- [~] programs/apps/marketing/skins/mautic/description.md
- [~] programs/apps/marketing/skins/mautic/features.md
- [~] programs/apps/marketing/skins/mautic/index.md
- [~] programs/apps/marketing/skins/mautic/menu.md
- [~] programs/apps/marketing/skins/mautic/shortcuts.md
- [~] programs/apps/marketing/skins/mautic/structure.md

### marketing / plausible
- [~] programs/apps/marketing/skins/plausible/api.md
- [~] programs/apps/marketing/skins/plausible/description.md
- [~] programs/apps/marketing/skins/plausible/features.md
- [~] programs/apps/marketing/skins/plausible/index.md
- [~] programs/apps/marketing/skins/plausible/menu.md
- [~] programs/apps/marketing/skins/plausible/shortcuts.md
- [~] programs/apps/marketing/skins/plausible/structure.md

## marketplace

- [ ] Pflichtmenge einfrieren → `programs/suites/marketplace/requirements.md`

- [~] programs/suites/marketplace/index.md
- [~] programs/suites/marketplace/skins/index.md

### marketplace / arcemall
- [~] programs/suites/marketplace/skins/arcemall/api.md
- [~] programs/suites/marketplace/skins/arcemall/description.md
- [~] programs/suites/marketplace/skins/arcemall/features.md
- [~] programs/suites/marketplace/skins/arcemall/index.md
- [~] programs/suites/marketplace/skins/arcemall/menu.md
- [~] programs/suites/marketplace/skins/arcemall/shortcuts.md
- [~] programs/suites/marketplace/skins/arcemall/structure.md

### marketplace / cs-cart-multivendor
- [~] programs/suites/marketplace/skins/cs-cart-multivendor/api.md
- [~] programs/suites/marketplace/skins/cs-cart-multivendor/description.md
- [~] programs/suites/marketplace/skins/cs-cart-multivendor/features.md
- [~] programs/suites/marketplace/skins/cs-cart-multivendor/index.md
- [~] programs/suites/marketplace/skins/cs-cart-multivendor/menu.md
- [~] programs/suites/marketplace/skins/cs-cart-multivendor/shortcuts.md
- [~] programs/suites/marketplace/skins/cs-cart-multivendor/structure.md

### marketplace / ebay
- [~] programs/suites/marketplace/skins/ebay/api.md
- [~] programs/suites/marketplace/skins/ebay/description.md
- [~] programs/suites/marketplace/skins/ebay/features.md
- [~] programs/suites/marketplace/skins/ebay/index.md
- [~] programs/suites/marketplace/skins/ebay/menu.md
- [~] programs/suites/marketplace/skins/ebay/shortcuts.md
- [~] programs/suites/marketplace/skins/ebay/structure.md

### marketplace / etsy
- [~] programs/suites/marketplace/skins/etsy/api.md
- [~] programs/suites/marketplace/skins/etsy/description.md
- [~] programs/suites/marketplace/skins/etsy/features.md
- [~] programs/suites/marketplace/skins/etsy/index.md
- [~] programs/suites/marketplace/skins/etsy/menu.md
- [~] programs/suites/marketplace/skins/etsy/shortcuts.md
- [~] programs/suites/marketplace/skins/etsy/structure.md

### marketplace / kleinanzeigen
- [~] programs/suites/marketplace/skins/kleinanzeigen/api.md
- [~] programs/suites/marketplace/skins/kleinanzeigen/description.md
- [~] programs/suites/marketplace/skins/kleinanzeigen/features.md
- [~] programs/suites/marketplace/skins/kleinanzeigen/index.md
- [~] programs/suites/marketplace/skins/kleinanzeigen/menu.md
- [~] programs/suites/marketplace/skins/kleinanzeigen/shortcuts.md
- [~] programs/suites/marketplace/skins/kleinanzeigen/structure.md

### marketplace / sharetribe
- [~] programs/suites/marketplace/skins/sharetribe/api.md
- [~] programs/suites/marketplace/skins/sharetribe/description.md
- [~] programs/suites/marketplace/skins/sharetribe/features.md
- [~] programs/suites/marketplace/skins/sharetribe/index.md
- [~] programs/suites/marketplace/skins/sharetribe/menu.md
- [~] programs/suites/marketplace/skins/sharetribe/shortcuts.md
- [~] programs/suites/marketplace/skins/sharetribe/structure.md

## messenger

- [ ] Pflichtmenge einfrieren → `programs/apps/messenger/requirements.md`

- [~] programs/apps/messenger/index.md
- [~] programs/apps/messenger/skins/index.md

### messenger / discord
- [~] programs/apps/messenger/skins/discord/api.md
- [~] programs/apps/messenger/skins/discord/description.md
- [~] programs/apps/messenger/skins/discord/features.md
- [~] programs/apps/messenger/skins/discord/index.md
- [~] programs/apps/messenger/skins/discord/menu.md
- [~] programs/apps/messenger/skins/discord/shortcuts.md
- [~] programs/apps/messenger/skins/discord/structure.md

### messenger / element
- [~] programs/apps/messenger/skins/element/api.md
- [~] programs/apps/messenger/skins/element/description.md
- [~] programs/apps/messenger/skins/element/features.md
- [~] programs/apps/messenger/skins/element/index.md
- [~] programs/apps/messenger/skins/element/menu.md
- [~] programs/apps/messenger/skins/element/shortcuts.md
- [~] programs/apps/messenger/skins/element/structure.md

### messenger / kontact
- [~] programs/apps/messenger/skins/kontact/api.md
- [~] programs/apps/messenger/skins/kontact/description.md
- [~] programs/apps/messenger/skins/kontact/features.md
- [~] programs/apps/messenger/skins/kontact/index.md
- [~] programs/apps/messenger/skins/kontact/menu.md
- [~] programs/apps/messenger/skins/kontact/shortcuts.md
- [~] programs/apps/messenger/skins/kontact/structure.md

### messenger / mastodon
- [~] programs/apps/messenger/skins/mastodon/api.md
- [~] programs/apps/messenger/skins/mastodon/description.md
- [~] programs/apps/messenger/skins/mastodon/features.md
- [~] programs/apps/messenger/skins/mastodon/index.md
- [~] programs/apps/messenger/skins/mastodon/menu.md
- [~] programs/apps/messenger/skins/mastodon/shortcuts.md
- [~] programs/apps/messenger/skins/mastodon/structure.md

### messenger / outlook
- [~] programs/apps/messenger/skins/outlook/api.md
- [~] programs/apps/messenger/skins/outlook/description.md
- [~] programs/apps/messenger/skins/outlook/features.md
- [~] programs/apps/messenger/skins/outlook/index.md
- [~] programs/apps/messenger/skins/outlook/menu.md
- [~] programs/apps/messenger/skins/outlook/shortcuts.md
- [~] programs/apps/messenger/skins/outlook/structure.md

### messenger / telegram
- [~] programs/apps/messenger/skins/telegram/api.md
- [~] programs/apps/messenger/skins/telegram/description.md
- [~] programs/apps/messenger/skins/telegram/features.md
- [~] programs/apps/messenger/skins/telegram/index.md
- [~] programs/apps/messenger/skins/telegram/menu.md
- [~] programs/apps/messenger/skins/telegram/shortcuts.md
- [~] programs/apps/messenger/skins/telegram/structure.md

### messenger / thunderbird
- [~] programs/apps/messenger/skins/thunderbird/api.md
- [~] programs/apps/messenger/skins/thunderbird/description.md
- [~] programs/apps/messenger/skins/thunderbird/features.md
- [~] programs/apps/messenger/skins/thunderbird/index.md
- [~] programs/apps/messenger/skins/thunderbird/menu.md
- [~] programs/apps/messenger/skins/thunderbird/shortcuts.md
- [~] programs/apps/messenger/skins/thunderbird/structure.md

## projectmanagement

- [ ] Pflichtmenge einfrieren → `programs/apps/projectmanagement/requirements.md`

- [~] programs/apps/projectmanagement/index.md
- [~] programs/apps/projectmanagement/skins/index.md

### projectmanagement / asana
- [~] programs/apps/projectmanagement/skins/asana/api.md
- [~] programs/apps/projectmanagement/skins/asana/description.md
- [~] programs/apps/projectmanagement/skins/asana/features.md
- [~] programs/apps/projectmanagement/skins/asana/index.md
- [~] programs/apps/projectmanagement/skins/asana/menu.md
- [~] programs/apps/projectmanagement/skins/asana/shortcuts.md
- [~] programs/apps/projectmanagement/skins/asana/structure.md

### projectmanagement / jira
- [~] programs/apps/projectmanagement/skins/jira/api.md
- [~] programs/apps/projectmanagement/skins/jira/description.md
- [~] programs/apps/projectmanagement/skins/jira/features.md
- [~] programs/apps/projectmanagement/skins/jira/index.md
- [~] programs/apps/projectmanagement/skins/jira/menu.md
- [~] programs/apps/projectmanagement/skins/jira/shortcuts.md
- [~] programs/apps/projectmanagement/skins/jira/structure.md

### projectmanagement / openproject
- [~] programs/apps/projectmanagement/skins/openproject/api.md
- [~] programs/apps/projectmanagement/skins/openproject/description.md
- [~] programs/apps/projectmanagement/skins/openproject/features.md
- [~] programs/apps/projectmanagement/skins/openproject/index.md
- [~] programs/apps/projectmanagement/skins/openproject/menu.md
- [~] programs/apps/projectmanagement/skins/openproject/shortcuts.md
- [~] programs/apps/projectmanagement/skins/openproject/structure.md

### projectmanagement / planka
- [~] programs/apps/projectmanagement/skins/planka/api.md
- [~] programs/apps/projectmanagement/skins/planka/description.md
- [~] programs/apps/projectmanagement/skins/planka/features.md
- [~] programs/apps/projectmanagement/skins/planka/index.md
- [~] programs/apps/projectmanagement/skins/planka/menu.md
- [~] programs/apps/projectmanagement/skins/planka/shortcuts.md
- [~] programs/apps/projectmanagement/skins/planka/structure.md

### projectmanagement / redmine
- [~] programs/apps/projectmanagement/skins/redmine/api.md
- [~] programs/apps/projectmanagement/skins/redmine/description.md
- [~] programs/apps/projectmanagement/skins/redmine/features.md
- [~] programs/apps/projectmanagement/skins/redmine/index.md
- [~] programs/apps/projectmanagement/skins/redmine/menu.md
- [~] programs/apps/projectmanagement/skins/redmine/shortcuts.md
- [~] programs/apps/projectmanagement/skins/redmine/structure.md

### projectmanagement / taiga
- [~] programs/apps/projectmanagement/skins/taiga/api.md
- [~] programs/apps/projectmanagement/skins/taiga/description.md
- [~] programs/apps/projectmanagement/skins/taiga/features.md
- [~] programs/apps/projectmanagement/skins/taiga/index.md
- [~] programs/apps/projectmanagement/skins/taiga/menu.md
- [~] programs/apps/projectmanagement/skins/taiga/shortcuts.md
- [~] programs/apps/projectmanagement/skins/taiga/structure.md

### projectmanagement / trello
- [~] programs/apps/projectmanagement/skins/trello/api.md
- [~] programs/apps/projectmanagement/skins/trello/description.md
- [~] programs/apps/projectmanagement/skins/trello/features.md
- [~] programs/apps/projectmanagement/skins/trello/index.md
- [~] programs/apps/projectmanagement/skins/trello/menu.md
- [~] programs/apps/projectmanagement/skins/trello/shortcuts.md
- [~] programs/apps/projectmanagement/skins/trello/structure.md

### projectmanagement / wekan
- [~] programs/apps/projectmanagement/skins/wekan/api.md
- [~] programs/apps/projectmanagement/skins/wekan/description.md
- [~] programs/apps/projectmanagement/skins/wekan/features.md
- [~] programs/apps/projectmanagement/skins/wekan/index.md
- [~] programs/apps/projectmanagement/skins/wekan/menu.md
- [~] programs/apps/projectmanagement/skins/wekan/shortcuts.md
- [~] programs/apps/projectmanagement/skins/wekan/structure.md

## streaming

- [ ] Pflichtmenge einfrieren → `programs/apps/streaming/requirements.md`

- [~] programs/apps/streaming/index.md
- [~] programs/apps/streaming/skins/index.md

### streaming / ant-media-server
- [~] programs/apps/streaming/skins/ant-media-server/api.md
- [~] programs/apps/streaming/skins/ant-media-server/description.md
- [~] programs/apps/streaming/skins/ant-media-server/features.md
- [~] programs/apps/streaming/skins/ant-media-server/index.md
- [~] programs/apps/streaming/skins/ant-media-server/menu.md
- [~] programs/apps/streaming/skins/ant-media-server/shortcuts.md
- [~] programs/apps/streaming/skins/ant-media-server/structure.md

### streaming / ffmpeg
- [~] programs/apps/streaming/skins/ffmpeg/api.md
- [~] programs/apps/streaming/skins/ffmpeg/description.md
- [~] programs/apps/streaming/skins/ffmpeg/features.md
- [~] programs/apps/streaming/skins/ffmpeg/index.md
- [~] programs/apps/streaming/skins/ffmpeg/menu.md
- [~] programs/apps/streaming/skins/ffmpeg/shortcuts.md
- [~] programs/apps/streaming/skins/ffmpeg/structure.md

### streaming / gstreamer
- [~] programs/apps/streaming/skins/gstreamer/api.md
- [~] programs/apps/streaming/skins/gstreamer/description.md
- [~] programs/apps/streaming/skins/gstreamer/features.md
- [~] programs/apps/streaming/skins/gstreamer/index.md
- [~] programs/apps/streaming/skins/gstreamer/menu.md
- [~] programs/apps/streaming/skins/gstreamer/shortcuts.md
- [~] programs/apps/streaming/skins/gstreamer/structure.md

### streaming / mediamtx
- [~] programs/apps/streaming/skins/mediamtx/api.md
- [~] programs/apps/streaming/skins/mediamtx/description.md
- [~] programs/apps/streaming/skins/mediamtx/features.md
- [~] programs/apps/streaming/skins/mediamtx/index.md
- [~] programs/apps/streaming/skins/mediamtx/menu.md
- [~] programs/apps/streaming/skins/mediamtx/shortcuts.md
- [~] programs/apps/streaming/skins/mediamtx/structure.md

### streaming / mistserver
- [~] programs/apps/streaming/skins/mistserver/api.md
- [~] programs/apps/streaming/skins/mistserver/description.md
- [~] programs/apps/streaming/skins/mistserver/features.md
- [~] programs/apps/streaming/skins/mistserver/index.md
- [~] programs/apps/streaming/skins/mistserver/menu.md
- [~] programs/apps/streaming/skins/mistserver/shortcuts.md
- [~] programs/apps/streaming/skins/mistserver/structure.md

### streaming / nginx-rtmp-module
- [~] programs/apps/streaming/skins/nginx-rtmp-module/api.md
- [~] programs/apps/streaming/skins/nginx-rtmp-module/description.md
- [~] programs/apps/streaming/skins/nginx-rtmp-module/features.md
- [~] programs/apps/streaming/skins/nginx-rtmp-module/index.md
- [~] programs/apps/streaming/skins/nginx-rtmp-module/menu.md
- [~] programs/apps/streaming/skins/nginx-rtmp-module/shortcuts.md
- [~] programs/apps/streaming/skins/nginx-rtmp-module/structure.md

### streaming / obs-studio
- [~] programs/apps/streaming/skins/obs-studio/api.md
- [~] programs/apps/streaming/skins/obs-studio/description.md
- [~] programs/apps/streaming/skins/obs-studio/features.md
- [~] programs/apps/streaming/skins/obs-studio/index.md
- [~] programs/apps/streaming/skins/obs-studio/menu.md
- [~] programs/apps/streaming/skins/obs-studio/shortcuts.md
- [~] programs/apps/streaming/skins/obs-studio/structure.md

### streaming / restream
- [~] programs/apps/streaming/skins/restream/api.md
- [~] programs/apps/streaming/skins/restream/description.md
- [~] programs/apps/streaming/skins/restream/features.md
- [~] programs/apps/streaming/skins/restream/index.md
- [~] programs/apps/streaming/skins/restream/menu.md
- [~] programs/apps/streaming/skins/restream/shortcuts.md
- [~] programs/apps/streaming/skins/restream/structure.md

### streaming / restreamer
- [~] programs/apps/streaming/skins/restreamer/api.md
- [~] programs/apps/streaming/skins/restreamer/description.md
- [~] programs/apps/streaming/skins/restreamer/features.md
- [~] programs/apps/streaming/skins/restreamer/index.md
- [~] programs/apps/streaming/skins/restreamer/menu.md
- [~] programs/apps/streaming/skins/restreamer/shortcuts.md
- [~] programs/apps/streaming/skins/restreamer/structure.md

### streaming / wowza
- [~] programs/apps/streaming/skins/wowza/api.md
- [~] programs/apps/streaming/skins/wowza/description.md
- [~] programs/apps/streaming/skins/wowza/features.md
- [~] programs/apps/streaming/skins/wowza/index.md
- [~] programs/apps/streaming/skins/wowza/menu.md
- [~] programs/apps/streaming/skins/wowza/shortcuts.md
- [~] programs/apps/streaming/skins/wowza/structure.md

## whiteboards

- [ ] Pflichtmenge einfrieren → `programs/apps/whiteboards/requirements.md`

- [~] programs/apps/whiteboards/index.md
- [~] programs/apps/whiteboards/skins/index.md

### whiteboards / drawio
- [~] programs/apps/whiteboards/skins/drawio/api.md
- [~] programs/apps/whiteboards/skins/drawio/description.md
- [~] programs/apps/whiteboards/skins/drawio/features.md
- [~] programs/apps/whiteboards/skins/drawio/index.md
- [~] programs/apps/whiteboards/skins/drawio/menu.md
- [~] programs/apps/whiteboards/skins/drawio/shortcuts.md
- [~] programs/apps/whiteboards/skins/drawio/structure.md

### whiteboards / excalidraw
- [~] programs/apps/whiteboards/skins/excalidraw/api.md
- [~] programs/apps/whiteboards/skins/excalidraw/description.md
- [~] programs/apps/whiteboards/skins/excalidraw/features.md
- [~] programs/apps/whiteboards/skins/excalidraw/index.md
- [~] programs/apps/whiteboards/skins/excalidraw/menu.md
- [~] programs/apps/whiteboards/skins/excalidraw/shortcuts.md
- [~] programs/apps/whiteboards/skins/excalidraw/structure.md

### whiteboards / miro
- [~] programs/apps/whiteboards/skins/miro/api.md
- [~] programs/apps/whiteboards/skins/miro/description.md
- [~] programs/apps/whiteboards/skins/miro/features.md
- [~] programs/apps/whiteboards/skins/miro/index.md
- [~] programs/apps/whiteboards/skins/miro/menu.md
- [~] programs/apps/whiteboards/skins/miro/shortcuts.md
- [~] programs/apps/whiteboards/skins/miro/structure.md

### whiteboards / mural
- [~] programs/apps/whiteboards/skins/mural/api.md
- [~] programs/apps/whiteboards/skins/mural/description.md
- [~] programs/apps/whiteboards/skins/mural/features.md
- [~] programs/apps/whiteboards/skins/mural/index.md
- [~] programs/apps/whiteboards/skins/mural/menu.md
- [~] programs/apps/whiteboards/skins/mural/shortcuts.md
- [~] programs/apps/whiteboards/skins/mural/structure.md

### whiteboards / openboard
- [~] programs/apps/whiteboards/skins/openboard/api.md
- [~] programs/apps/whiteboards/skins/openboard/description.md
- [~] programs/apps/whiteboards/skins/openboard/features.md
- [~] programs/apps/whiteboards/skins/openboard/index.md
- [~] programs/apps/whiteboards/skins/openboard/menu.md
- [~] programs/apps/whiteboards/skins/openboard/shortcuts.md
- [~] programs/apps/whiteboards/skins/openboard/structure.md

### whiteboards / tldraw
- [~] programs/apps/whiteboards/skins/tldraw/api.md
- [~] programs/apps/whiteboards/skins/tldraw/description.md
- [~] programs/apps/whiteboards/skins/tldraw/features.md
- [~] programs/apps/whiteboards/skins/tldraw/index.md
- [~] programs/apps/whiteboards/skins/tldraw/menu.md
- [~] programs/apps/whiteboards/skins/tldraw/shortcuts.md
- [~] programs/apps/whiteboards/skins/tldraw/structure.md

## wiki

- [ ] Pflichtmenge einfrieren → `programs/apps/wiki/requirements.md`

- [~] programs/apps/wiki/index.md
- [~] programs/apps/wiki/skins/index.md

### wiki / confluence
- [~] programs/apps/wiki/skins/confluence/api.md
- [~] programs/apps/wiki/skins/confluence/description.md
- [~] programs/apps/wiki/skins/confluence/features.md
- [~] programs/apps/wiki/skins/confluence/index.md
- [~] programs/apps/wiki/skins/confluence/menu.md
- [~] programs/apps/wiki/skins/confluence/shortcuts.md
- [~] programs/apps/wiki/skins/confluence/structure.md

### wiki / mediawiki
- [~] programs/apps/wiki/skins/mediawiki/api.md
- [~] programs/apps/wiki/skins/mediawiki/description.md
- [~] programs/apps/wiki/skins/mediawiki/features.md
- [~] programs/apps/wiki/skins/mediawiki/index.md
- [~] programs/apps/wiki/skins/mediawiki/menu.md
- [~] programs/apps/wiki/skins/mediawiki/shortcuts.md
- [~] programs/apps/wiki/skins/mediawiki/structure.md

### wiki / notion
- [~] programs/apps/wiki/skins/notion/api.md
- [~] programs/apps/wiki/skins/notion/description.md
- [~] programs/apps/wiki/skins/notion/features.md
- [~] programs/apps/wiki/skins/notion/index.md
- [~] programs/apps/wiki/skins/notion/menu.md
- [~] programs/apps/wiki/skins/notion/shortcuts.md
- [~] programs/apps/wiki/skins/notion/structure.md

### wiki / tango.io
- [~] programs/apps/wiki/skins/tango.io/api.md
- [~] programs/apps/wiki/skins/tango.io/description.md
- [~] programs/apps/wiki/skins/tango.io/features.md
- [~] programs/apps/wiki/skins/tango.io/index.md
- [~] programs/apps/wiki/skins/tango.io/menu.md
- [~] programs/apps/wiki/skins/tango.io/shortcuts.md
- [~] programs/apps/wiki/skins/tango.io/structure.md

### wiki / vscodium
- [~] programs/apps/wiki/skins/vscodium/api.md
- [~] programs/apps/wiki/skins/vscodium/description.md
- [~] programs/apps/wiki/skins/vscodium/features.md
- [~] programs/apps/wiki/skins/vscodium/index.md
- [~] programs/apps/wiki/skins/vscodium/menu.md
- [~] programs/apps/wiki/skins/vscodium/shortcuts.md
- [~] programs/apps/wiki/skins/vscodium/structure.md

### wiki / wikijs
- [~] programs/apps/wiki/skins/wikijs/api.md
- [~] programs/apps/wiki/skins/wikijs/description.md
- [~] programs/apps/wiki/skins/wikijs/features.md
- [~] programs/apps/wiki/skins/wikijs/index.md
- [~] programs/apps/wiki/skins/wikijs/menu.md
- [~] programs/apps/wiki/skins/wikijs/shortcuts.md
- [~] programs/apps/wiki/skins/wikijs/structure.md

### wiki / xwiki
- [~] programs/apps/wiki/skins/xwiki/api.md
- [~] programs/apps/wiki/skins/xwiki/description.md
- [~] programs/apps/wiki/skins/xwiki/features.md
- [~] programs/apps/wiki/skins/xwiki/index.md
- [~] programs/apps/wiki/skins/xwiki/menu.md
- [~] programs/apps/wiki/skins/xwiki/shortcuts.md
- [~] programs/apps/wiki/skins/xwiki/structure.md

## workflows

- [ ] Pflichtmenge einfrieren → `programs/suites/workflows/requirements.md`

- [~] programs/suites/workflows/index.md
- [~] programs/suites/workflows/skins/index.md

### workflows / apache-airflow
- [~] programs/suites/workflows/skins/apache-airflow/api.md
- [~] programs/suites/workflows/skins/apache-airflow/description.md
- [~] programs/suites/workflows/skins/apache-airflow/features.md
- [~] programs/suites/workflows/skins/apache-airflow/index.md
- [~] programs/suites/workflows/skins/apache-airflow/menu.md
- [~] programs/suites/workflows/skins/apache-airflow/shortcuts.md
- [~] programs/suites/workflows/skins/apache-airflow/structure.md

### workflows / make
- [~] programs/suites/workflows/skins/make/api.md
- [~] programs/suites/workflows/skins/make/description.md
- [~] programs/suites/workflows/skins/make/features.md
- [~] programs/suites/workflows/skins/make/index.md
- [~] programs/suites/workflows/skins/make/menu.md
- [~] programs/suites/workflows/skins/make/shortcuts.md
- [~] programs/suites/workflows/skins/make/structure.md

### workflows / n8n
- [~] programs/suites/workflows/skins/n8n/api.md
- [~] programs/suites/workflows/skins/n8n/description.md
- [~] programs/suites/workflows/skins/n8n/features.md
- [~] programs/suites/workflows/skins/n8n/index.md
- [~] programs/suites/workflows/skins/n8n/menu.md
- [~] programs/suites/workflows/skins/n8n/shortcuts.md
- [~] programs/suites/workflows/skins/n8n/structure.md

### workflows / node-red
- [~] programs/suites/workflows/skins/node-red/api.md
- [~] programs/suites/workflows/skins/node-red/description.md
- [~] programs/suites/workflows/skins/node-red/features.md
- [~] programs/suites/workflows/skins/node-red/index.md
- [~] programs/suites/workflows/skins/node-red/menu.md
- [~] programs/suites/workflows/skins/node-red/shortcuts.md
- [~] programs/suites/workflows/skins/node-red/structure.md

### workflows / prefect
- [~] programs/suites/workflows/skins/prefect/api.md
- [~] programs/suites/workflows/skins/prefect/description.md
- [~] programs/suites/workflows/skins/prefect/features.md
- [~] programs/suites/workflows/skins/prefect/index.md
- [~] programs/suites/workflows/skins/prefect/menu.md
- [~] programs/suites/workflows/skins/prefect/shortcuts.md
- [~] programs/suites/workflows/skins/prefect/structure.md

### workflows / zapier
- [~] programs/suites/workflows/skins/zapier/api.md
- [~] programs/suites/workflows/skins/zapier/description.md
- [~] programs/suites/workflows/skins/zapier/features.md
- [~] programs/suites/workflows/skins/zapier/index.md
- [~] programs/suites/workflows/skins/zapier/menu.md
- [~] programs/suites/workflows/skins/zapier/shortcuts.md
- [~] programs/suites/workflows/skins/zapier/structure.md

---
*Insgesamt 869 Dateien (davon 833 Skin-Dateien in 119 Programmen).*
