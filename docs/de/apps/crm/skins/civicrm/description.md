# CiviCRM - Beschreibung

## Was das Programm macht

CiviCRM verwaltet die Beziehung zu „Mitgliedern“: wer hat gespendet, wer ist Mitglied bis wann, wer war bei welcher Veranstaltung, wer hat welche Petition unterschrieben. Es läuft als Modul innerhalb eines bestehenden CMS und teilt sich Benutzer und Rechte mit dessen Nutzerkonten.

## Vorteile

- **für Non-Profit gebaut**: Spenden/Mitgliedschaften/Events sind Erstklass-Objekte, nicht nachgerüstet
- **Datenhoheit**: quelloffen (AGPL), auf eigenem Server
- **CMS-Symbiose**: Formularseiten (Event-Registrierung, Spendenformulare) auf der eigenen Website
- **API v4** modern und Entity-getrieben — gut automatisierbar

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **SuiteCRM/EspoCRM** | Vertriebs-CRMs mit Leads/Pipeline/Deals; CiviCRM hat keine Sales-Pipeline |
| **Salesforce (Nonprofit Cloud)** | kommerziell, riesig; CiviCRM ist die Open-Source-Antwort auf dasselbe Problem |
| **Mailchimp** | nur Kampagnen/Publikumssegmente; CiviCRM ist Datenbank-first mit Mail als Kanal |

## Technische Details

- **Stack**: PHP, MySQL/MariaDB; läuft in Drupal/Joomla/WordPress (eigene Tabellen `civicrm_*`)
- **Frontend**: Angular-/jQuery-Mischmasch („Cividashboards“, SearchKit-Views), Formulare serverseitig
- **Authentifizierung**: CMS-Login + Civi-Permissions; API mit site_key/auth_key
- **Hosting**: Shared-Hosting-tauglich (Vorsicht Cron/Mailing), Docker-Images (Flow-Community)
- **Lizenz**: AGPL

## Für wen geeignet

- Vereine, Verbände, NGOs mit eigener Website und Spendenthematik
- FreeSynergy-Skins, die Kontakt + Beitrag + Event + Membership modellieren (Constituent-Modell)
