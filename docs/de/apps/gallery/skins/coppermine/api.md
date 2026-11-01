# Coppermine - API Dokumentation

## Übersicht

Coppermine besitzt **keine dokumentierte externe API**. Integrationen laufen über die serverseitige Plugin-Schnittstelle (`plugin_api`) und über das Thema/Template-System. Für automatisierten Zugriff bleibt nur der Weg über PHP-Code oder Datenbank.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| `plugin_api` (PHP-Hooks) | eigene Logik in Upload-/Anzeigeprozessen | offiziell, serverseitig |
| Theme/Template-API | Layout- und Blocksteuerung | offiziell |
| REST/JSON für externe Clients | — | ❌ |
| GraphQL / Webhooks | — | ❌ |

## Authentifizierung

- ausschließlich Coppermine-Sitzung (Cookie) oder Bridge-Login über ein CMS
- keine Token- oder API-Key-Mechanik vorhanden (❌)

## Plugin-Hooks (Auswahl)

| Hook | Zeitpunkt |
|------|-----------|
| `plugin_load` | beim Laden des Plugins |
| `page_start` / `page_end` | um die Seitenausgabe |
| `upload_pre_process` / `upload_post_process` | vor/nach dem Upload |
| `display_image` / `display_thumbnail` | bei der Auslieferung |
| `cpg_gallery_thumbnail` | beim Bau der Vorschaubilder |
| `admin_config_form` | Erweitern des Konfigurationsformulars |

Beispiel (eigener Hook, der Bildmetadaten nach extern meldet):

```php
function picture_sync(&$picture_data) {
    $payload = array(
        'pid'    => $picture_data['pid'],
        'title'  => $picture_data['pfilename'],
        'album'  => $picture_data['aid'],
        'url'    => cpg_get_full_image_url($picture_data),
    );
    file_get_contents('https://bridge.example/cpg', false,
        stream_context_create(array('http' => array(
            'method'  => 'POST',
            'header'  => "Content-Type: application/json\r\n",
            'content' => json_encode($payload),
        ))));
}
```

Registrierung im Plugin: `add_filter('upload_post_process', 'picture_sync');`

## Datenzugriff (nur intern)

| Tabelle | Inhalt |
|---------|--------|
| `cpg_pictures` | Bilder, Album (`aid`), Dateiname, Zähler |
| `cpg_albums` | Alben, Kategorie (`category`), Sichtbarkeitsrechte (`visibility`) |
| `cpg_categories` | Kategoriebaum |
| `cpg_comments` / `cpg_votes` | Kommentare und Bewertungen |
| `cpg_users` / `cpg_usergroups` | Benutzer und Rechtegruppen |

Direkte Datenbankzugriffe sind upgrade-anfällig und sollten über eine eigene Brücke gekapselt werden.

## SDKs und Client-Bibliotheken

- **offiziell**: keine
- **Community**: Skripte für FTP-Import, Bridge-Module für Joomla/WordPress

## Skin-Hinweis

Weil keine API existiert, bildet der FreeSynergy-Skin die Galerie über die eigene Datenhaltung ab; Migrationsfelder (`pid`, `aid`) entsprechen den Standardmodellen ([modelle.md](../../../../data/modelle.md)).
