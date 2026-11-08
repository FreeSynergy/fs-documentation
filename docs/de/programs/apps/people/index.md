# Kontakte und CRM-Verwaltung

## Kurz gesagt

People hält die Menschen in deinem Leben: Freunde, Familie, Kollegen, Kunden und Gruppen davon. Jede Person ist eine Karte, und eine Karte kann mehrere Rollen tragen. Es beantwortet die Frage: Wer ist diese Person?

**Befehl:** `fs-people`, ein Befehl je Programm mit Unterbefehlen ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); Programme werden umgestellt, wenn sie ohnehin angefasst werden, deshalb ist noch nicht jedes so weit).

## Was hier anders ist

- Eine Karte folgt dem offenen Standard JSContact (RFC 9553). Alles, was das Programm nicht versteht, wird behalten, nicht weggeworfen.
- Du kannst Kontakte als vCard übernehmen und wieder herausnehmen; der Originaltext wird je Karte aufbewahrt.
- Karten, die als sensibel markiert sind, bleiben aus Exporten heraus, außer du gibst sie ausdrücklich frei. Rollen werden getrennt von der Karte gehalten, damit ein Export sie nicht verrät.
- Ist ein Teilnehmer eine KI, sagt die Karte das. Die Markierung schränkt nichts ein; sie zeigt nur, mit wem du es zu tun hast.
- People arbeitet allein. Andere FreeSynergy-Programme können auf eine Person über ihre ID verweisen, statt eine eigene Kopie zu führen.

## Wo es heute steht

Neueste Version: `v0.0.2`. Du kannst Karten anlegen, bearbeiten, löschen, auflisten und durchsuchen, vCard importieren und exportieren sowie Gruppen, mehrere Rollen je Person und Beziehungen führen. Das Programm kann vorschlagen, dass zwei Karten dieselbe Person sind; zusammengeführt wird erst, wenn du es bestätigst. Ein kleiner Server und ein erstes, vorläufiges Fenster gibt es.

Noch nicht da: Gruppen, Beziehungen und Rollen verwalten oder die sensible Markierung im Fenster setzen, Rückgängig und Live-Aktualisierungen, Anmeldung (die handelnde Person ist ein Platzhalter), CardDAV und Synchronisierung zwischen Geräten. Die Schnittstelle ist ein Entwurf ohne zweiten Nutzer bisher und kann sich deshalb noch ändern.

## Geplante Facetten

Facetten sind Teile eines Programms, die wie eigene Apps wirken ([ADR 0061](../../../decisions/0061-facetten.md)). Jede bekommt einen eigenen Befehl, eine Verbindung zu `fs-people` ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md)).

Vorgeschlagen, noch nicht gebaut:

- Kontakte: dein Adressbuch.
- Nutzer: Personen, die das System benutzen.
- KIs: Teilnehmer, die KI sind.
- Partner: Interessenten, Kunden und Lieferanten.
- Team: die Menschen, mit denen du arbeitest.
- Mitglieder: Mitglieder einer Gruppe oder eines Vereins.

## Überblick

Dieser Bereich enthält Dokumentation zu verschiedenen Kontakt- und CRM-Systemen.

## Verfügbare Systeme

- **civicrm** - Verwaltung von Mitgliedern und Kontakten
- **suitecrm** - Open-Source-CRM
- **odoo** - Software für die Betriebsführung (CRM-Modul)
- **frappe** - Modernes ERP mit CRM
- **metronic** - CRM-System
- **pipedrive** - Verwaltung der Verkaufspipeline
- **lessonly** - Plattform für Kundendaten
- **salesforce** - CRM-Plattform
- **hubspot** - CRM-Plattform
- **zoho-crm** - CRM-Software
- **insightly** - CRM und Projektmanagement
- **pabbly-crm** - CRM-Software
- **capsule** - CRM für kleine Unternehmen
- **sugarcrm** - CRM-Plattform
- **roistat** - Marketing-Analyse und CRM

## Was ist CRM?

CRM (Customer Relationship Management) ist ein Konzept für die systematische Pflege von Kundenbeziehungen. CRM-Systeme umfassen:

- Verwaltung von Kontaktdaten
- Erfassung von Kontakten und Kommunikation
- Verwaltung der Verkaufspipeline
- Verfolgung von Verkaufschancen (Opportunitys)
- Kundenanalyse und Segmentierung
- Automatisierung von Marketing- und Vertriebsprozessen

## Anwendungsbereiche

- **Vertrieb**: Lead-Gewinnung und Verwaltung von Chancen
- **Kundenservice**: Kundenbetreuung und Support
- **Marketing**: Kampagnen und Kundensegmente
- **E-Commerce**: Kundenverwaltung für Online-Shops
- **Dienstleistungen**: Verwaltung der Kunden von Dienstleistern

## Vorteile von CRM-Systemen

- **Nähe zum Kunden**: Alle Kundeninformationen an einem Ort
- **Vertriebsförderung**: Verkaufschancen erkennen
- **Kundenbindung**: Bessere Betreuung der Kunden
- **Auswertung**: Kundenanalysen und Berichte
- **Automatisierung**: Prozesse automatisieren
- **Integration**: Verbindung mit anderen Werkzeugen

## Auswahlkriterien

Bei der Wahl eines CRM-Systems solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen werden gebraucht?
- **Skalierbarkeit**: Wie viele Kunden und Kontakte?
- **Bedienbarkeit**: Wie benutzerfreundlich ist es?
- **Integration**: Wie gut passt das System zur bestehenden Infrastruktur?
- **Kosten**: Kostenlos oder kostenpflichtig?
- **Mobiler Zugriff**: Gibt es mobile Apps?

## Verwandte Kategorien

- [Marketing](../marketing/) - Marketing-Werkzeuge und Analysen
- [Helpdesk](../helpdesk/) - Support- und Ticketsysteme
- [Projektmanagement](../../suites/projectmanagement/) - Projektmanagement

## Schnellstart

1. **CRM auswählen**: Wähle ein System anhand der Anforderungen
2. **Installation/Konto**: System installieren oder Konto anlegen
3. **Konfiguration**: System anpassen und einrichten
4. **Daten importieren**: Bestehende Kunden und Kontakte importieren
5. **Workflow festlegen**: Vertriebs- und Marketingprozesse festlegen

## Weitere Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen CRM-Systeme.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysierte Programme (4), nach Funktion, nichts kopiert (ADR 0012/0013):

- [GNOME Contacts](frontends/gnome-contacts/index.md) — GNOME Contacts ist die schlanke Kontakt-App für GNOME: Kontakte anlegen, verknüpfen und mit Evolution-Data-Server-Quellen synchronisieren (lokale Adressbücher, CalDAV/CardDAV-Konten, Google, LDAP).
- [KAddressBook](frontends/kaddressbook/index.md) — KAddressBook ist die Kontaktverwaltung von KDE PIM: auf vCard aufgebaut, verwaltet über Akonadi-Ressourcen (lokale Ordner, IMAP-Kontakte, CardDAV, LDAP).
- [Monica](frontends/monica/index.md) — Monica ist ein selbst gehostetes persönliches CRM: Menschen mit all ihren Beziehungen, Aktivitäten, Geschenken, Aufgaben und Notizen erfassen – als Web-App (Laravel/Vue) mit einer REST-API.
- [Nextcloud Contacts](frontends/nextcloud-contacts/index.md) — Nextcloud Contacts ist die Kontakt-App der Nextcloud-Suite: Adressbücher im Browser, über CardDAV mit allen Geräten synchronisiert, mit Benutzerkonten, Kreisen/Gruppen und dem Personenbereich o…

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
