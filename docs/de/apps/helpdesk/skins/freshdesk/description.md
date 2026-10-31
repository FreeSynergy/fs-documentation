# Freshdesk - Beschreibung

## Was das Programm macht

Freshdesk macht Support als Abo: Mailboxen werden zu Ticketquellen, Agenten arbeiten eine Aufgabenliste ab, Regeln erledigen Routine. Der Rest ist wie Zendesk, aber in günstigeren Tiers und mit stärker integrierten Freshworks-Schwestern (Freshchat, Freshcaller, Freddy).

## Vorteile

- **günstiger Einstieg**, solide Gratis-/Omni-Tiers
- **weniger Konfigurationsballast** als Zendesk — schnell produktiv
- **API + Webhooks** für Automatisierung ohne App-Zwang

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Zendesk** | größeres Ökosystem, tiefere Customization; Freshdesk ist schlanker im Standard |
| **Zammad** | Datenhoheit + freier Code statt SaaS-Abo |
| **Help Scout** | Mailbox-/Teampostfach-Philosophie ohne klassische Ticketmaske |

## Technische Details

- **Modell**: SaaS (Multi-Region), Subdomain `firma.freshdesk.com`
- **Authentifizierung**: E-Mail/Passwort, SSO SAML; API-Key pro Account/Agent; OAuth2 (Developer Platform)
- **Pläne**: Free → Growth → Pro → Enterprise; Omnichannel-Bündel
- **Data-Residency**: EU/US/IN/AU je Kontoauswahl (Planabhängigkeit prüfen)

## Für wen geeignet

- KMU und wachsende Teams, die ohne Admin-Team starten
- FreeSynergy-Szenarien, die SaaS-Ticket-APIs (REST v2) als Skin-Vorbild brauchen
