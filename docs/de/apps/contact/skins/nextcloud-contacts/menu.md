# Nextcloud Contacts - Menüpunkte

## Hauptnavigation (Nextcloud-Kopfzeile)

- App-Icon „Kontakte“ links in der App-Leiste (Reihenfolge adminverwaltet)
- Obere Leiste: Suche, Benutzer-Menü, Admin-Einstellungen (⚙ → „Kontakte-Verwaltung“ je nach Version)

## Linke Spalte

| Menüpunkt | Beschreibung |
|-----------|--------------|
| Alle Kontakte | übergreifende Kontaktliste des Nutzers |
| Gelöschte Kontakte | Papierkorb mit Wiederherstellung |
| Freigegebene Adressbücher | von anderen geteilte Bücher |
| Adressbücher (eigene) | „Persönlich“, „Geburts- & Jahrestage“, weitere eigene |
| + Neues Adressbuch | neues CardDAV-Adressbuch anlegen |

## Kontakt-Detail

- Bearbeiten / Fertig
- Felder hinzufügen (Telefon, E-Mail, Adresse, Organisation, Geburtstag, Notizen, Social-Media)
- Favorit (Stern)
- Aktionen-Menü: **Anrufen** (Talk/SIP), **Nachrichten** (Talk), **E-Mail schreiben** (Mail-App), **Als Karte speichern** (vCard-Datei), **Löschen**

## Freigabe-Menü (pro Adressbuch)

- Teilen mit Benutzern/Gruppen/Kreisen — Rechte: Lesen, Lesen/Schreiben, Editor
- Öffentliches Link-Sharing (Adressbuch-Link, Lesezugriff)
- CardDAV-URL des Buches anzeigen (für externe Clients)

## Import/Export-Menü

- `.vcf`-Datei(en) per Drag & Drop oder Datei-Dialog importieren (Duplikaterkennung)
- Kontakte markieren → „Kontakte herunterladen“ (`.vcf`)

## Menüs nach Rolle

| Rolle | Menü |
|-------|------|
| Normaler Nutzer | eigene Bücher, empfangene Freigaben |
| Gruppen-Admin | Freigaben für die eigene Gruppe verwalten |
| Nextcloud-Admin | „Einstellungen → Kontakte“: Kreise erlauben, Systemadressbuch (gelbes Buch), Zertifikats-/ColdStore-Optionen |
