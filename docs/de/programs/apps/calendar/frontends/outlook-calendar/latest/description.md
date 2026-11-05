# Outlook-Kalender – Beschreibung

*(Quellbasis: Microsoft Graph v1.0 Ressourcen-Doku, offizielle EWS-Deprecation-Seite, offizielle Tastaturkürzel-Seite von support.microsoft.com; Stand 2026-11-02 – Details und Fundstellen in [index.md](../index.md#quellen))*

## Was das Programm macht

**Outlook-Kalender** ist die Kalenderkomponente von Microsofts Outlook-Linie: dieselbe Kalenderfunktion erscheint in **Outlook on the web** (outlook.com privat bzw. outlook.office.com für Organisationen), im **neuen Outlook für Windows** (Web-Codebasis als Desktop-App), im **klassischen Outlook für Windows** (MAPI-Desktop-Client, Teil von Microsoft 365/Office), in **Outlook für Mac** und in **Outlook für iOS/Android**. Gespeichert werden Termine im Postfach des Backends **Exchange Online** (Microsoft 365); Zugriffsschicht für Automatisierung ist die **Microsoft-Graph-REST-API** (OAuth 2.0, OData/JSON).

Kernfunktionen: Termine und Wiederholungsserien, Einladungen mit RSVP (annehmen/vorläufig/ablehnen), Free/Busy-Abfragen und Terminfindung (`getSchedule`, `findMeetingTimes`), Erinnerungen, Dateianhänge, Kalenderfarben und -freigaben, Online-Besprechungen mit Teams, To-Do-Aufgaben, mehrere Kalender und Kalendergruppen je Postfach. Für Drittsysteme gibt es **echte Webhooks** über Graph change notifications – ein klarer Unterschied zu Nextcloud Calendar und DAViCal, die keine Push-Hooks bieten.

## Vorteile

- **Plattformweite Reichweite:** Ein Kalenderobjekt, das Desktop (Windows/Mac), Web und Mobile (eigene Outlook-Apps) mit demselben Backend bedient; in Unternehmen meist bereits durch Microsoft-365-Lizenzen vorhanden.
- **Terminfindung eingebaut:** Free/Busy über Nutzer/Ressourcen hinweg, Slot-Vorschläge (`findMeetingTimes`), Assistent für die Terminplanung im klassischen Client, Teilnehmer dürfen Gegenvorschläge machen (`allowNewTimeProposals`).
- **Organisationsfunktionen:** Freigaben mit Rechtestufen, Kalender veröffentlichen, Ressourcen (Räume/Ausstattung) alsbuchbare Objekte, Teams-Konferenz per Schalter.
- **Integrationslage:** Graph mit OAuth-Scopes, Webhooks, Delta-Queries und SDKs – deutlich reichhaltigere API als bei CalDAV-Servern üblich (dafür proprietär und an Microsoft-Identitäten gebunden).
- **Aktuell erzwungener Modernisierungsschub:** EWS wird in Exchange Online abgeschaltet (Okt 2026–Apr 2027); alle Integrationen landen zwangsläufig auf Graph.

## Abgrenzung zu vergleichbaren Produkten

| Produkt (in dieser Doku) | Unterschied |
|--------------------------|-------------|
| **Google Kalender** | Beide sind SaaS mit proprietärer API + Webhooks. Outlook liegt im Microsoft-Stack (Exchange/Teams/Entra), Google im Google-Stack (Gmail/Meet); Graph ist OData/JSON mit OAuth, Google nutzt Discovery/REST. Outlook punktet mit Ressourcen-/Raumbuchung im Unternehmenskontext, Google mit stärkerem Consumer-Ökosystem und Terminbuchungs-Seiten. |
| **Nextcloud Calendar** | Nextcloud: selbst gehoster Weboberfläche auf CalDAV mit offenen Standards, Datenhoheit, eigenen Buchung-/Proposal-Objekten, aber **keinen** Webhooks. Outlook: Cloud-Dienst, keine Datenhoheit, dafür Webhooks, Ressourcenverwaltung und tiefe Teams-Integration. |
| **DAViCal** | DAViCal ist nur CalDAV-/CardDAV-Backend ohne Oberfläche; Outlook-Kalender ist das Gegenteil: fertige Clients + proprietäres Backend, **ohne** CalDAV-Zugang für externe Clients. |
| **Merkuro** | Merkuro ist nativer KDE-Client, der u. a. **gegen** Groupware-Server (auch Exchange/kopfzeilenweise via kdepim-runtime-Ressource) arbeitet; Outlook-Kalender stellt selbst Server **und** Clients. |
| **GNOME Planner** (vorgesehen) | Planner ist schlanker Task-/Kalender-Client; Outlook-Kalender ist Unternehmens-Groupware. |

## Technische Details

- **Backend:** Exchange Online (Postfachspeicher mit Kalenderordner-Modell); Kalender-/Terminelemente sind Postfachobjekte, nicht ICS-Dateien. On-Premises-Variante: Exchange Server (eigene Lebenslinien).
- **API:** Microsoft Graph `v1.0`/`beta`; Ressourcen `calendar`, `event`, `calendarGroup`; Aktionen (accept/decline/cancel/instances), `delta`-Queries, `changeKey`-Konkurrenzschutz, `Prefer: IdType="ImmutableId"`. Webhooks über Subscriptions mit Lifecycle-Erneuerung.
- **Auth:** OAuth 2.0 (Entra ID bzw. Microsoft-Konto), keine Basic-Auth für Drittzugriffe; Admin-Einwilligung für mandantenweite Scopes.
- **Konnektoren-Historie:** EAS/MAPI/EWS als ältere Protokolle; EWS-Abschaltung Exchange Online aktiv, ältere Protokolle für kostenlose Outlook.com-Konten seit Anfang 2025 entfallen (Details nicht verifiziert).
- **Clients:** neues Outlook für Windows (ersetzt seit 2023 schrittweise Windows-Mail/-Kalender-Apps; kostenlose Konten seit Januar 2025 nicht mehr zurückstufbar – Sekundärquelle), klassisches Outlook für Windows bleibt für Enterprise im Sortiment; Outlook für Mac nutzt eigenes Store-Format ohne CalDAV.

## Für wen geeignet

- **Geeignet:** Organisationen und Einzelpersonen im Microsoft-365-Umfeld, die Termine, Ressourcenbuchung, Teams-Meetings und API-Automatisierung (Graph mit Webhooks) aus einer Hand wollen; IT, die OAuth/Entra-Identitäten ohnehinBetriebenBetrieb pflegt.
- **Weniger geeignet:** Selbsthosts mit Datenhoheits-Anspruch (dann Nextcloud Calendar/DAViCal), offene Standard-Clients (Thunderbird, DAVx⁵, Merkuro finden keinen CalDAV-Zugang zu Outlook-Konten), und Privatkonto-Nutzer, die third-party-Mailclients nutzen wollen (Protokollzugänge entzogen).
