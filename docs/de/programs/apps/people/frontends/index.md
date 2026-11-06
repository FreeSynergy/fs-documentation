# Contact — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Contact` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [GNOME Contacts](gnome-contacts/index.md) | [latest](gnome-contacts/latest/description.md) | GNOME Contacts ist die schlanke Kontakt-App für GNOME: Kontakte anlegen, verknüpfen, mit Evolution-Data-Server-Quellen (Lokale Adressbücher, CalDAV/CardDAV-Konten, Google, LDAP) synchronisieren. |
| [KAddressBook](kaddressbook/index.md) | [latest](kaddressbook/latest/description.md) | KAddressBook ist die Kontaktverwaltung von KDE PIM: vCard-basiert, verwaltet über Akonadi-Ressourcen (lokale Ordner, IMAP-Contacts, CardDAV, LDAP). |
| [Monica](monica/index.md) | [latest](monica/latest/description.md) | Monica ist ein Self-Hosted Personal-CRM: Personen mit all ihren Beziehungen, Aktivitäten, Geschenken, Aufgaben und Notizen festhalten — als Web-App (Laravel/Vue) mit REST-API. |
| [Nextcloud Contacts](nextcloud-contacts/index.md) | [latest](nextcloud-contacts/latest/description.md) | Nextcloud Contacts ist die Kontakt-App der Nextcloud-Suite: Adressbücher im Browser, synchron über CardDAV mit allen Geräten, verknüpft mit Benutzerkonten, Kreisen/Gruppen und dem Startseiten-Perso… |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/people/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
