# Programme

**Ein Motor pro Thema. So viele Gesichter, wie es Menschen gibt.**

Jede App, die du in FreeSynergy siehst, steht auf einem starken Motor, der sein Thema in- und auswendig kennt: Menschen, Nachrichten, Aufgaben, Dateien, Termine. Darauf wählst du, wie sie aussieht und wie viel sie zeigt. Darunter sprechen alle Engines dieselben offenen Schnittstellen, sodass deine Kontakte, dein Kalender und deine Nachrichten zusammenarbeiten, ohne dass du etwas einrichten musst. Du musst nie lernen, wie sie gebaut ist. Wenn du es aber wissen willst, hier ist es.

## Wie es gebaut ist

```
  Suites        Groupware · Projektmanagement · CRM · ERP · Helpdesk · Democracy
                (mehrere Programme, für einen Zweck zusammengestellt)
                        │ nutzt
  ┌─────────────────────┴──────────────────────────────────────────────┐
  │ Programm fs-people                       Programm fs-messenger     │  ← besitzt die Daten und einen offenen Standard
  │   Facetten Contacts · Users · AIs · …      Facetten Mail · Chat    │  ← sehen aus wie eigene Apps
  │     Frontends  einfach · klassisch · voll …  Frontends  …          │  ← wie es aussieht; jederzeit wechselbar
  │     Admin-Frontend (alle Einstellungen)      Admin-Frontend        │  ← das Sicherheitsnetz
  └─────────────────────┬──────────────────────────────────────────────┘
                        │ gebaut aus
  Components    Kalenderraster · Dateiverwaltung · Diagramme · Chat …
```

FreeSynergy sortiert alles nach **Zweck**, nicht danach, wie ein Werkzeug aussieht. Für Menschen ist alles einfach eine **App**. Hinter den Apps stecken einige wenige Arten von Bausteinen, und der Unterschied zwischen ihnen ist, was FreeSynergy für eine Person einfach und zugleich für ein Unternehmen vollständig macht. (ADR 0021, 0049, 0061)

## Die Arten

| Art | Was es ist | Hat eigene Daten? | Beispiel |
|-----|------------|-------------------|----------|
| **Programm** | Der Motor für ein Thema. Er besitzt die Daten und die Regeln sowie einen offenen Standard. | Ja | `fs-people`, `fs-messenger`, `fs-tasks` |
| **Facette** | Ein Teil eines Programms, der wie eine eigene App aussieht: eigener Name, eigenes Logo, eigener Menüeintrag, ein fester Filter auf die Daten des Programms. Das Programm legt seine Facetten fest. | Nein | Contacts, Users, AIs und Partners in `fs-people`; Mail und Chat in `fs-messenger` |
| **Frontend** | Eine Sicht auf ein Programm oder eine Facette: sehr einfach, klassisch, vertraut oder vollständig. Mehrere pro Programm und pro Facette; du kannst wechseln. | Nein | Eine einfache Kontaktliste; ein vollständiger Kontaktmanager |
| **Admin-Frontend** | Das Frontend mit *allen* Einstellungen. Jedes Programm und jede Facette hat eins. | Nein | "Contacts – Einstellungen" |
| **Component, Workbench** | Ein Stück Bildschirm, das etwas zeigt, ohne zu wissen, was die Daten bedeuten. Frontends werden aus ihnen gebaut. | Nein | Ein Kalenderraster, ein Dateimanager |
| **Suite** | Mehrere Programme, für einen Zweck zusammengestellt. | Nein (nutzt die der Programme) | Groupware, Projektmanagement, CRM |

Eine Facette ist das Gegenteil einer Suite: Eine Suite bringt mehrere Programme zusammen; eine Facette zeigt einen Teil eines einzigen Programms.

## Warum wir diese Unterschiede machen

**Menschen suchen, was sie brauchen, nicht, wie etwas gebaut ist.** Jemand will seine Kontakte, nicht „Personendatensätze mit der Rolle Kontakt“. Jemand will E-Mail und muss nicht wissen, dass dieselbe Engine auch Chats aus Matrix trägt. Facetten geben jedem Bedürfnis eine eigene App, mit einem Namen, der sagt, was sie ist.

**Ein Motor hält alles zusammen.** Weil Contacts und Users beide `fs-people` sind, sind eine Person, die du kennst, und das Konto, mit dem sie sich anmeldet, derselbe Datensatz. Weil Mail und Chat beide `fs-messenger` sind, kann eine Unterhaltung von einem zum anderen wandern. Getrennte Programme würden die Daten kopieren und auseinanderlaufen lassen.

**Frontends lassen jeden wählen.** Der Motor kann weit mehr, als irgendein Bildschirm zeigt. Die eine Person will drei Knöpfe, die andere will jedes Detail, eine dritte will etwas, das sich anfühlt wie das Programm, das sie schon kennt. Alle arbeiten mit denselben Daten und können jederzeit wechseln.

**Das Admin-Frontend ist das Sicherheitsnetz.** Ein einfaches Frontend blendet Einstellungen bewusst aus. Wenn etwas versehentlich abgeschaltet wurde, hat das Admin-Frontend alle Einstellungen, sodass du oder jemand, der dir hilft, es immer wieder richten kannst. Deshalb muss jedes Programm und jede Facette eins haben. In Desktop-Menüs sind Admin-Frontends unter *Einstellungen* gruppiert, damit das Hauptmenü kurz bleibt.

## Im Store

[FreeSynergy.Store](platform/store.md) listet jede Facette als App mit eigenem Logo. Eine App zu installieren, installiert das Programm dahinter; eine zweite Facette desselben Programms fügt nur ihren Menüeintrag und ihre Frontends hinzu.

## Geplante Facetten

| Programm | Facetten (vorgeschlagen) |
|---------|-------------------|
| `fs-people` | Contacts, Users, AIs, Partners (Leads, Kunden, Lieferanten), Team, Mitglieder |
| `fs-messenger` | Mail, Chat, evtl. Forum |
| `fs-files` | Gallery, Music, Videos, Documents |
| `fs-tasks` | To-dos, Tickets |
| `fs-calendar` | Calendar, Booking (mit `fs-resources`) |

## Kategorien

| Kategorie | Inhalt | Analysierte Programme |
|----------|---------|-------------------|
| [Wiki](apps/wiki/) | Wiki und Wissenssysteme | vollständig (7 Programme) |
| [Messenger](apps/messenger/) | Chat, E-Mail, soziale Netzwerke | vollständig (7 Programme) |
| [Desktop](platform/desktop/) | Desktop-Programme, Dashboards, Startseiten | vollständig (12 Programme) |
| [Whiteboards](apps/whiteboard/) | Kollaborative Whiteboards | vollständig (6 Programme) |
| [Helpdesk](apps/helpdesk/) | Tickets und Support | vollständig (8 Programme) |
| [Projektmanagement](suites/projectmanagement/) | Aufgaben, Boards, Projekte | vollständig (8 Programme) |
| [Kontakte](apps/people/) | Kontaktverwaltung | vollständig (4 Programme) |
| [CRM](suites/crm/) | Kundenbeziehungen | vollständig (6 Programme) |
| [Kalender](apps/calendar/) | Termine und Planung | vollständig (6 Programme) |
| [Maps](apps/maps/) | Karten und Geodaten | vollständig (7 Programme) |
| [ERP](suites/erp/) | Ressourcenplanung | vollständig (6 Programme) |
| [Workflows](suites/workflows/) | Automatisierung und Integration | vollständig (6 Programme) |
| [Demokratie](suites/democracy/) | Beteiligungsplattformen | vollständig (6 Programme) |
| [Marketing](apps/marketing/) | Marketing und Analytics | vollständig (6 Programme) |
| [Marktplätze](suites/marketplace/) | Marktplatz-Software und fremde Marktplätze | vollständig (6 Programme) |
| [Foto-Galerien](apps/gallery/) | Bild- und Videosammlungen | vollständig (8 Programme) |
| [Streaming](apps/streaming/) | Encoder, Medienserver, Multistreaming | vollständig (10 Programme) |


Wie die bekannten Programme jeder Kategorie analysiert werden (nur Funktionen, nichts kopiert, ADR 0012, 0013), steht im Frontends-Index jeder Kategorie, zum Beispiel [Wiki](apps/wiki/frontends/index.md).

## Querverweise auf Systembereiche

| Bereich | Bezug zu Programmen |
|---------|---------------------|
| [Komponenten](../components/) | UI-Elemente, die in den Oberflächen verwendet werden |
| [Gesten](../interactions/gestures/) | Interaktionen in Touch-Oberflächen |
| [Animationen](../interactions/animations/) | Übergänge und Rückmeldungen in den Oberflächen |
| [Standardisierte Daten](../data/) | Felder, Modelle und das API-Muster aller Programme |


## Die Entscheidungen hinter dieser Seite, in einfachen Worten

- **Facetten** ([ADR 0061](../decisions/0061-facetten.md)). Menschen suchen „Kontakte“, nicht „Personendatensätze“. Darum kann ein Programm Teile von sich als eigene Apps zeigen, mit eigenem Namen und Icon. Du installierst Contacts, und das Programm `fs-people` kommt mit. Jedes Programm und jede Facette hat außerdem ein **Admin-Frontend** mit allen Einstellungen, als Sicherheitsnetz.
- **Ein Befehl** ([ADR 0063](../decisions/0063-ein-programm-ein-befehl.md)). Jedes Programm ist ein Befehl mit dem Namen des Programms, `fs-tasks`, `fs-people`, und hat Unterbefehle wie `git`. Ohne Argumente öffnet er das Fenster. Eine Facette hat einen eigenen Befehl, der ein Link auf ihr Programm ist, zum Beispiel `fs-contacts`.
- **Pakete liegen in Git** ([ADR 0062](../decisions/0062-paket-repos-in-git.md)). Programme hängen nicht an einer einzigen Webseite. Ein Katalog listet sie, jede Version ist ein Git-Tag, alles ist signiert, und jeder, der Git betreiben kann, kann es spiegeln. Du vertraust den Signaturen, nicht dem Ort.
- **Versionsnummern** ([ADR 0064](../decisions/0064-versionen-ab-0-0-1.md)). Alles beginnt bei `0.0.1` und zählt an der letzten Stelle hoch. `0.1.0` gibt es, wenn ein Mensch ein Programm benutzen kann und es den Handtest des Besitzers besteht, `1.0.0`, wenn zwei unabhängige Nutzer seine Schnittstelle verwenden. Eine hohe Zahl soll nicht mehr versprechen, als wir zeigen können.
- **Überall dasselbe Fenster** ([ADR 0065](../decisions/0065-standard-fensterhuelle.md), im Grundsatz angenommen, die Einzelheiten sind noch ein Vorschlag). Jedes Fenster hat dieselben Grundlagen: ein Standard-Menü mit festen Tastenkürzeln, ein „Über“ mit der Version einen Klick entfernt, Hilfe auf F1 (aus dem Wiki, wenn es installiert ist, sonst aus dieser Dokumentation), Meldungen, die zu ihrem Anlass gehören und nie in der falschen Ansicht hängen bleiben, Fehler, die nie still sind, und einen Neustart nach einem Update.

Die Entscheidungen sind auf Deutsch geschrieben; [alle Entscheidungen](../decisions/index.md).
