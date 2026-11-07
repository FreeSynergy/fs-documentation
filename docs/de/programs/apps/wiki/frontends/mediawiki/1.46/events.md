# MediaWiki 1.46 — Ereignisse nach außen

Version: 1.46.2. Quellen je Zeile wie angegeben.

MediaWiki-Kern hat kein allgemeines Webhook-System. Vorhandene Möglichkeiten:

| Mechanismus | Umfang | Status | Quelle |
|-------------|--------|--------|--------|
| Feed der letzten Änderungen (RSS/Atom) | Kern | Modul `action=feedrecentchanges` existiert; Parameter nicht gelesen | `includes/Api/ApiFeedRecentChanges.php`; Feed-Konfigurationsschlüssel `Feed`, `FeedLimit` (50), `FeedCacheTimeout` (60), `FeedDiffCutoff` (32768) in `includes/config-schema.php` |
| RCFeeds (Push von Einträgen der letzten Änderungen an ein Feed-Backend) | Kern, Konfiguration durch den Systemadministrator | Konfigurationsschlüssel `RCFeeds` existiert in `includes/config-schema.php`; Backend-Liste nicht gelesen | config-schema.php |
| EventStreams (SSE) | Von Wikimedia betriebener öffentlicher Dienst, nicht MediaWiki-Kern | öffentlicher Stream `https://stream.wikimedia.org/v2/stream/recentchange` | https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams (Zusammenfassung) |
| EventBus | MediaWiki-Erweiterung, die die von EventStreams genutzten Ereignisse erzeugt | Erweiterung; nicht gelesen | (Die Seite EventStreams nennt, dass Änderungen über EventBus aus MediaWiki kommen) |
| Echo | Erweiterung: Benachrichtigungen im Wiki, Web- und E-Mail-Benachrichtigungen, Push-Einstellungen | Benachrichtigungen, keine Webhooks | https://www.mediawiki.org/wiki/Extension:Echo |

## EventStreams (nicht Kern)

Quelle: https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams (über die Zusammenfassung gelesen).

- Transport: Server-Sent Events (SSE). `Accept: application/json` liefert zeilengetrenntes JSON.
- Streams: `recentchange`, `revision-create`; mehrere Streams können mit Kommas kombiniert werden.
- Öffentlicher Endpunkt: `https://stream.wikimedia.org/v2/stream/recentchange`. Ein interner Endpunkt existiert nur für Wikimedia.
- Verbindungs-Timeout auf dem Server: 15 Minuten. Clients verbinden sich neu und setzen mit `Last-Event-ID` fort.
- Keine Filterung auf dem Server. Ereignisse mit `meta.domain === 'canary'` verwerfen.
- Vorgesehen für kleine externe Werkzeuge. Keine numerische Ratenbegrenzung veröffentlicht.
- Unser Frontend ist nicht von EventStreams abhängig. Ein selbst gehostetes Wiki bräuchte einen eigenen Ereignis-Erzeuger.

## Letzte Änderungen in der Oberfläche

- Die Seite der letzten Änderungen (`Special:RecentChanges`) und die Beobachtungsliste verwenden dasselbe Datenmodell. Quelle: https://www.mediawiki.org/wiki/API:RecentChanges und https://www.mediawiki.org/wiki/API:Watchlist.
- Polling ist der übliche Weg, mit dem ein Frontend die Liste aktualisiert. Der Konfigurationsschlüssel `StructuredChangeFiltersLiveUpdatePollingRate` = 3 in `includes/config-schema.php` scheint ein Abfrageintervall für die Filteroberfläche von Special:RecentChanges festzulegen (Lesart anhand des Namens, nicht durch eine Dokumentationsseite bestätigt). Es ist eine Polling-Einstellung, kein Push-Kanal.

## Nicht geprüft

- Ob ein Kern-Hook bei jeder Bearbeitung eine HTTP-Anfrage an eine konfigurierte URL senden kann. Im Kern nicht gefunden; kein Webhook-Codepfad gelesen.
- Format der Nutzlast der Einträge von `action=feedrecentchanges`.
