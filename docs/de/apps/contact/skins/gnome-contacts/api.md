# GNOME Contacts - API Dokumentation

## Übersicht

GNOME Contacts selbst hat **keine API** — die programmatische Ebene ist der **Evolution Data Server (EDS)** mit seiner D-Bus-/libebook-Schnittstelle sowie die Protokolle der angebundenen Quellen (CardDAV, LDAP, Google Contacts API). vCard-Dateien sind der neutrale Austauschweg.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| libebook / EDS D-Bus (`EBookClient`) | Kontakte lesen/schreiben | offiziell (C/Vala; GObject-Introspection für Python/JS) |
| CardDAV/LDAP/Google-Kontakte der Quellen | Synchronisation | Standard-Protokolle |
| `.vcf`-Dateien | Import/Export | offiziell |
| REST | — | ❌ Nicht vorhanden |

## Authentifizierung

EDS lokal ohne Auth; Quellen im GNOME-Online-Account-Dialog (OAuth2 Google, Basic CardDAV, simple bind LDAP), Schlüssel im GNOME Keyring.

## libebook-Beispiel (C, gekürzt)

```c
EBookClient *client;
e_book_client_connect_by_source(registry, source, &client, NULL);

ECVCard vcv; e_vcard_from_file("andrea.vcf", &vcv, NULL);
e_book_client_create_contact(client, E_CONTACT(&vcv), &uid, NULL);
```

- Quellen = `ESource`-Einträge; jede Quelle ist ein Adressbuch
- `e_book_client_get_view()` mit RFC-2426-Suchfilter (`"fn=Andrea"`)

## Python/JS via GObject-Introspection

```python
gi.require_version('EBookClient', '1.2')
from gi.repository import EBookClient
```

## Austauschweg für Skripte

`⋮ → Exportieren…` erzeugt einen `.vcf`-Stapel → beliebig weiterverarbeiten; Rückimport über `⋮ → Importieren…`.

## Rate Limits

Ausschließlich die der Quellen-Server (Google-Quotas, Nextcloud-Throttling).

## Skin-Hinweis

Ein GNOME-Contacts-Skin spiegelt die Karte/Felder-Maske; Datenmodel-Brücke über EDS oder `.vcf` → [Contact-Modell](../../../../data/modelle.md).
