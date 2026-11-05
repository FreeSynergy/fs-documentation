# Merkuro – Beschreibung

*(Quellbasis: Merkuro 26.08.2, Release Service Okt 2026 – Fundstellen in [index.md](../index.md#quellen))*

## Namensgeschichte

**Kalendar** (Start 2021, KDE Gear seit 22.12) wurde zur Veröffentlichung von **KDE Gear 23.08 (August 2023) in Merkuro umbenannt**, weil die Anwendung über Kalender/Tasks hinaus zur Groupware-Suite wuchs. Heute existieren vier Programme: `merkuro-calendar`, `merkuro-contact`, `merkuro-mail` und `merkurolauncher`. Diese Sektion dokumentiert den Nachfolger von Kalendar: **Merkuro Calendar** (`org.kde.merkuro.calendar`).

## Was das Programm macht

Merkuro Calendar ist die **moderne Kalender-App der KDE-Desktop-Umgebung**: Termine, wiederkehrende Ereignisse und Aufgaben (VTodos) in Monats-, Wochen-, Arbeitswochen-, 3-Tage-, Tages-, Terminplan- und Aufgabenansicht. Die Daten hält nicht die App selbst, sondern der KDE-PIM-Dienst **Akonadi**, der lokale Kalender und Online-Kalender (**Nextcloud, Google Calendar, Outlook, CalDAV und viele mehr** (via Ressourcen aus `kdepim-runtime`)) synchronisiert. Damit ist Merkuro der native Desktop-/Mobile-Gegenentwurf zu Webkalendern.

Die UI ist **konvergent** (Kirigami/QML, Qt 6): auf dem Desktop mit einklappbarer Seitenleiste (`MainDrawer`) und Menüleiste (abschaltbar), auf Mobilgeräten (Plasma Mobile) mit Wisch-Gesten und Bottom-Toolbar.

## Vorteile

- **Nahtlos in KDE/Plasma:** Akonadi-Konten, KDE-Frameworks (Rahmen, Benachrichtigungen, I18n), mit dem Kontakte-/Mail-Zwilling der Suite kombinierbar; Single-Instance über D-Bus.
- **Offline-fähig:** lokale Akonadi-Kalender ohne Netzwerk; Online-Kalender werden im Hintergrund gespiegelt.
- **Konvergent:** dieselbe App auf Desktop und Telefon – für Webkalender wie Nextcloud Calendar ein Alleinstellungsmerkmal in dieser Doku-Serie.
- **Feiertage nach Region, Aufgaben mit Sortierung (Fälligkeit/Alphabet/Priorität), Erinnerungen, ICS-Import per Doppelklick, Undo/Redo, freie Ansichtskonfiguration** (wischbare Raster, Wochennummern, Belegtheits-/FreeBusy-Einstellungen) – alles per `kalendarrc` konfigurierbar.
- **Aktuell und aktiv gepflegt:** Releases im Monatstakt (26.08.2 Okt 2026), Maintainer des KDE-PIM-Teams.

## Abgrenzung zu vergleichbaren Produkten

| Produkt (in dieser Doku) | Unterschied |
|--------------------------|-------------|
| **Nextcloud Calendar** | Web-Oberfläche auf einem Nextcloud-Server; Merkuro ist ein nativer Client, der u. a. *mit* Nextcloud-Serversn (via CalDAV) zusammenarbeitet, aber weder Server noch Browser braucht. |
| **Davical** | reiner CalDAV-Server (Backend); Merkuro ist Client. Kombination Davical + Merkuro (CalDAV-Ressource) ist möglich. |
| **Google Kalender** | SaaS-Dienst; Merkuro ist ein Client dafür (über Google-Ressource in kdepim-runtime), aber quelloffen und selbstbestimmt mit Akonadi als Datenhaltung. |
| **KOrganizer** (nicht eigene Sektion) | der klassische, funktionsbreite KDE-Kalender (in Kontact integriert, Widgets-Toolkit); Merkuro ist der bewusst schlankere, QML-basierte Nachfolgebau, der auch mobil funktioniert. |

## Technische Details

- **Stack:** C++/Qt 6 (≥ 6.9), QML-UI mit Kirigami, KDE Frameworks ≥ 6.25; KDE-PIM-Bibliotheken 6.8.2 (`Akonadi`, `AkonadiCalendar`, `AkonadiContact`, `KCalCore` …) plus KDE-Rahmen wie `KF6::Holidays` (Feiertagskalender), `KF6::Contacts`, `KF6::DBusAddons`.
- **Modell-Schicht:** Qt-Modelle auf Akonadi (`IncidenceWrapper`, `RemindersModel`, `HourlyIncidenceModel`, Sammlungs-Modelle); die Views sind reine QML-Delegates.
- **D-Bus-Identität:** `KDBusService::Unique` (Desktop-Name `org.kde.merkuro.calendar`), Objekt `/Calendar`, Interface `org.kde.calendar.Calendar` mit `showIncidenceByUid` (Details in [api.md](api.md)).
- **Dateitypen:** `text/calendar` (`.ics`) als MimeType, Import über Positionsargumente.
- **Konfiguration:** KConfig `kalendarrc` (Gruppen General/Views/TaskView/Editor), Konten in Akonadi.
- **Lizenz:** GPL‑3; Repo `invent.kde.org/pim/merkuro`, AppStream `org.kde.merkuro.calendar` (addon zu `org.kde.merkuro`).

## Für wen geeignet

- **Geeignet:** KDE-/Plasma-Nutzer, die Kalender + Aufgaben nativ (auch auf Plasma Mobile) verwalten wollen; Kombination aus lokalen und Online-Kalendern (Nextcloud/Google/CalDAV) ohne Web-UI; wer Akonadi-basierte Wiederverwendung (Kontakte, Mail-Suite) schätzt.
- **Weniger geeignet:** Nicht-KDE-Umgebungen (Akonadi ist schwergewichtige Abhängigkeit), reine Server-/Headless-Szenarien (dafür Davical/Nextcloud), Teams, die gemeinsame Buchung/Teilverwaltung im Browser brauchen (Domäne der Webkalender), und alle, die API-Hooks erwarten – die App bietet keine (siehe api.md).
