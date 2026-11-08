# Kontakt- und CRM-Verwaltung

## Kurz gesagt

People hält die Menschen in deinem Leben fest: Freunde, Familie, Kolleginnen und Kollegen, Kundschaft und Gruppen davon. Jede Person ist eine Karte, und eine Karte kann mehrere Rollen tragen. Es beantwortet die Frage: Wer ist das?

## Was hier anders ist

- Eine Karte folgt dem offenen Standard JSContact (RFC 9553). Alles, was das Programm nicht versteht, wird behalten und nicht weggeworfen.
- Du kannst Kontakte als vCard einlesen und wieder ausgeben; der Originaltext wird pro Karte aufbewahrt.
- Als sensibel markierte Karten bleiben aus Exporten heraus, außer du gibst sie namentlich frei. Rollen sind von der Karte getrennt gehalten, sodass ein Export sie nicht verrät.
- Ist ein Beteiligter eine KI, sagt die Karte das. Die Markierung schränkt nichts ein; sie zeigt dir nur, mit wem du es zu tun hast.
- People arbeitet allein. Andere FreeSynergy-Programme können auf eine Person über ihre ID verweisen, statt eigene Kopien zu halten.

## Wo es heute steht

Neuester Tag: `v0.6.0`. Du kannst Karten anlegen, bearbeiten, löschen, auflisten und durchsuchen, vCard importieren und exportieren sowie Gruppen, mehrere Rollen pro Person und Beziehungen pflegen. Das Programm kann vorschlagen, dass zwei Karten dieselbe Person sind; zusammengeführt wird erst, wenn du es bestätigst. Ein kleiner Server und ein erstes, vorläufiges Fenster sind vorhanden.

Noch nicht vorhanden: Gruppen, Beziehungen und Rollen oder die Markierung als sensibel im Fenster verwalten, Rückgängig und Live-Aktualisierung, Anmeldung (die handelnde Person ist ein Platzhalter), CardDAV und Synchronisation zwischen Geräten. Die Oberfläche ist ein Entwurf ohne zweite Nutzerin oder zweiten Nutzer und kann sich daher noch ändern.

## Geplante Facetten

Vorgeschlagen, nicht gebaut:

- Contacts: dein Adressbuch.
- Users: Menschen, die das System nutzen.
- AIs: Beteiligte, die KI sind.
- Partners: Leads, Kundschaft und Lieferanten.
- Team: die Menschen, mit denen du arbeitest.
- Members: Mitglieder einer Gruppe oder eines Vereins.

## Übersicht

Dieser Bereich enthält Dokumentation für verschiedene Kontakt- und CRM-Systeme.

## Verfügbare Systeme

- **civicrm** - Constituent Relationship Management
- **suitecrm** - Open-Source-CRM
- **odoo** - Software für Unternehmensverwaltung (CRM-Modul)
- **frappe** - modernes ERP mit CRM
- **metronic** - CRM-System
- **pipedrive** - Verwaltung der Vertriebspipeline
- **lessonly** - Kundendatenplattform
- **salesforce** - CRM-Plattform
- **hubspot** - CRM-Plattform
- **zoho-crm** - CRM-Software
- **insightly** - CRM und Projektmanagement
- **pabbly-crm** - CRM-Software
- **capsule** - CRM für Kleinunternehmen
- **sugarcrm** - CRM-Plattform
- **roistat** - Marketing-Analytik und CRM

## Was ist CRM?

CRM (Customer Relationship Management) ist ein Konzept zur systematischen Verwaltung von Kundenbeziehungen. CRM-Systeme umfassen:

- Kontaktdaten verwalten
- Interaktionen und Kommunikation verfolgen
- Vertriebspipeline verwalten
- Verkaufschancen (Opportunities) verfolgen
- Kundenanalyse und Segmentierung
- Automatisierung von Marketing- und Vertriebsprozessen

## Anwendungsbereiche

- **Vertrieb**: Lead-Generierung und Verwaltung von Verkaufschancen
- **Kundenservice**: Kundenbetreuung und Support
- **Marketing**: Kampagnen und Kundensegmente
- **E-Commerce**: Kundenverwaltung für Online-Shops
- **Dienstleistung**: Kundenverwaltung für Dienstleister

## Vorteile von CRM-Systemen

- **Kundennähe**: Alle Kundeninformationen an einem Ort
- **Verkaufsförderung**: Verkaufschancen erkennen
- **Kundenbindung**: Bessere Kundenbetreuung
- **Analyse**: Kundenanalysen und Berichte
- **Automatisierung**: Prozesse automatisieren
- **Integration**: Verbindung mit anderen Werkzeugen

## Auswahlkriterien

Bei der Wahl eines CRM-Systems solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen werden benötigt?
- **Skalierbarkeit**: Wie viele Kundschaft und Kontakte?
- **Benutzerfreundlichkeit**: Wie einfach ist die Bedienung?
- **Integration**: Wie gut passt das System in die bestehende Infrastruktur?
- **Kosten**: Kostenlos oder kostenpflichtig?
- **Mobiler Zugriff**: Gibt es mobile Apps?

## Verwandte Kategorien

- [Marketing](../marketing/) - Marketing-Werkzeuge und Analytik
- [Helpdesk](../helpdesk/) - Support- und Ticketsysteme
- [Projektmanagement](../../suites/projectmanagement/) - Projektmanagement

## Schnellstart

1. **CRM auswählen**: Ein System nach deinen Anforderungen wählen
2. **Installation/Konto**: System installieren oder ein Konto anlegen
3. **Konfiguration**: System anpassen und einrichten
4. **Daten importieren**: Bestehende Kundschaft und Kontakte importieren
5. **Workflow festlegen**: Vertriebs- und Marketingprozesse definieren

## Mehr Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen CRM-Systeme.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysierte Programme (4), nach Funktion, nichts kopiert (ADR 0012/0013):

- [GNOME Contacts](frontends/gnome-contacts/index.md) — GNOME Contacts ist die schlanke Kontakt-App für GNOME: Kontakte anlegen, verknüpfen und mit Evolution-Data-Server-Quellen (lokale Adressbücher, CalDAV/CardDAV-Konten, Google, LDAP) synchronisieren.
- [KAddressBook](frontends/kaddressbook/index.md) — KAddressBook ist die Kontaktverwaltung von KDE PIM: vCard-basiert, verwaltet über Akonadi-Ressourcen (lokale Ordner, IMAP-Contacts, CardDAV, LDAP).
- [Monica](frontends/monica/index.md) — Monica ist ein selbst gehostetes persönliches CRM: Personen mit all ihren Beziehungen, Aktivitäten, Geschenken, Aufgaben und Notizen festhalten — als Web-App (Laravel/Vue) mit REST-API.
- [Nextcloud Contacts](frontends/nextcloud-contacts/index.md) — Nextcloud Contacts ist die Kontakt-App der Nextcloud-Suite: Adressbücher im Browser, synchron über CardDAV mit allen Geräten, verknüpft mit Benutzerkonten, Kreisen/Gruppen und dem Startseiten-Perso…

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
