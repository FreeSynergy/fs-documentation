# Confluence (Cloud, latest) · Ereignisse (Webhooks)

Quellen: S-Nummern verweisen auf [index.md](../index.md).

Es gibt zwei Systeme. Forge ist das aktuelle. Connect-Webhooks sind veraltet, und Atlassian sagt, dass neue Erweiterbarkeit nur noch über Forge bereitgestellt wird. [S11]

## 1. Forge-Ereignisse (aktuell) [S10]

Ereignisnamen haben die Form `avi:confluence:<action>:<object>`. Die Nutzlasten bestehen meist aus vollständigen Objekten (nicht aus IDs). Benutzer werden über `accountId` identifiziert.

| Objekt | Ereignisse |
|--------|------------|
| Seite / Live-Dokument / Blogbeitrag | `created:page`, `updated:page`, `liked:page`, `viewed:page`, `archived:page`, `unarchived:page`, `moved:page`, `copied:page`, `children_reordered:page`, `permissions_updated:page`, `trashed:page`, `restored:page`, `deleted:page`; Live-Dokumente: `initialized:page`, `started:page`, `snapshotted:page`, `published:page`; Blogbeiträge: `created:blogpost`, `updated:blogpost`, `liked:blogpost`, `viewed:blogpost`, `permissions_updated:blogpost`, `trashed:blogpost`, `restored:blogpost`, `deleted:blogpost` |
| Whiteboard | `created:whiteboard`, `moved:whiteboard`, `copied:whiteboard`, `permissions_updated:whiteboard` |
| Datenbank | `created:database`, `moved:database`, `copied:database`, `permissions_updated:database` |
| Ordner | `created:folder`, `moved:folder`, `copied:folder`, `permissions_updated:folder` |
| Smart Link im Baum | `created:embed`, `moved:embed`, `copied:embed` |
| Inline-Aufgabe | `created:task`, `updated:task`, `removed:task` (Nutzlast enthält bei Aktualisierung `oldTask`) |
| Kommentar | `created:comment`, `updated:comment`, `liked:comment`, `deleted:comment` |
| Bereich | `created:space:V2`, `updated:space:V2`, `permissions_updated:space:V2`, `deleted:space:V2` |
| Anhang | `created:attachment`, `updated:attachment`, `viewed:attachment`, `archived:attachment`, `unarchived:attachment`, `trashed:attachment`, `restored:attachment`, `deleted:attachment` |
| Benutzerdefinierter Inhalt | `created:custom_content`, `updated:custom_content`, `permissions_updated:custom_content`, `trashed:custom_content`, `restored:custom_content`, `deleted:custom_content` |
| Label | `created:label`, `added:label`, `removed:label`, `deleted:label` |
| Benutzer | `created:user`, `deleted:user` |
| Gruppe | `created:group`, `deleted:group` |
| Relation | `created:relation`, `deleted:relation` |
| Suche | `performed:search` (Abfrage, accountType, Anzahl der Ergebnisse; kein Inhalt) |

Hinweise [S10]:
- Ereignisse für gelöschte und in den Papierkorb verschobene Inhalte sowie Ereignisse zu Berechtigungen von Bereichen benötigen `write:confluence-content` oder `write:confluence-space`.
- Kaskadierende Löschungen erzeugen nicht für jedes untergeordnete Element ein eigenes Ereignis.
- Bei Confluence-Ereignissen wird keine Beta- oder Abkündigungskennzeichnung angezeigt. Das Suffix `:V2` bei Bereichsereignissen wird nicht erklärt.

Ungeprüft: wie ein Nicht-Forge-Frontend (zum Beispiel unser eigener Server) Forge-Ereignisse empfangen würde. Forge-Ereignisse laufen innerhalb von Forge-Apps auf der Plattform von Atlassian. Eine Möglichkeit, sie an eine externe URL weiterzuleiten, wurde auf den gelesenen Seiten nicht gefunden.

## 2. Connect-Webhooks (veraltet) [S11]

Sie werden im App-Deskriptor `atlassian-connect.json` unter `modules.webhooks` deklariert. Jeder Eintrag hat `event` (erforderlich), `url` (erforderlich, relativ zur baseUrl des Add-ons), `excludeBody` (Standard false), `filter` (optional), `conditions` (nur `addon_is_licensed`), `propertyKeys` (nur Jira). [S11]

In S11 aufgeführte Confluence-Ereignisnamen (exakt):

```
attachment_archived attachment_created attachment_removed attachment_restored
attachment_trashed attachment_unarchived attachment_updated attachment_viewed
blog_created blog_moved blog_removed blog_restored blog_trashed blog_updated blog_viewed
blueprint_page_created comment_removed
connect_addon_disabled connect_addon_enabled
content_created content_removed content_restored content_trashed content_updated content_permissions_updated
group_created group_removed
label_added label_created label_deleted label_removed
page_archived page_children_reordered page_created page_initialized page_copied page_moved
page_removed page_restored page_trashed page_unarchived page_updated page_started
page_snapshotted page_published page_viewed
relation_created relation_deleted search_performed
space_created space_logo_updated space_permissions_updated space_removed space_updated
theme_enabled user_reactivated user_removed
```

## 3. Frühere Fassung (entfernt)

Die frühere, `events.md`-entsprechende Fassung listete `page.created`, `page.updated`, `page.deleted`, `comment.created`, `space.created` und den Endpunkt `POST /rest/webhooks/1.0/webhook`. Keines davon erscheint auf den gelesenen Cloud-Seiten. Entfernt. Der Pfad `/rest/webhooks/1.0/` gehört zu Data Center (Detail ungeprüft).

## 4. Hinweise zur Zustellung [S9]

- Ankündigung vom 2026-10-16: neue IP-Bereiche von Atlassian gelten ab 2027-01-01. Anfragen von Atlassian, einschließlich Webhooks, verwenden diese Bereiche. Erlaubnislisten müssen vor diesem Datum aktualisiert werden.
- 2026-09-25: Der Connect-Lebenszyklus-Hook `uninstalled` wird beim Upgrade auf eine reine Forge-Version nicht mehr ausgelöst.

## Relevanz für uns

Ein Kanal für Live-Aktualisierungen kann nur Forge-Ereignisse nutzen, wenn unsere Integration als Forge-App läuft oder die REST-API abfragt. Abfragen unterliegen dem Punktekontingent in [api.md](api.md).
