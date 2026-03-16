# FreeSynergy — Dokumentation

**Sprache:** Deutsch  
**Stand:** März 2026  
**Repository:** https://github.com/FreeSynergy/Dokumentation

---

## Warum FreeSynergy?

Computer stellen Werkzeuge in den Vordergrund. Der Mensch muss wissen WELCHES Programm er öffnen muss, um an WELCHE Information zu kommen. Das ist rückwärts. Der Mensch braucht Informationen — und ob die aus einem Wiki, einer Datenbank, einer Karte oder einem Messenger kommen, ist irrelevant.

FreeSynergy dreht das um: **Die Information steht im Vordergrund, nicht das Werkzeug.** Programme arbeiten im Hintergrund zusammen. Der Mensch sieht nur das Ergebnis. Wenn er tiefer eintauchen will, klickt er sich zum Werkzeug durch — aber erst dann.

Dazu braucht es offene Standards, dezentrale Architektur und freiwillige Zusammenarbeit. Kein Zwang, kein Vendor-Lock-in, kein Zentralserver.

---

## Dokumentations-Übersicht

### Architektur
- [Gesamtübersicht](architektur/uebersicht.md) — Wie alles zusammenhängt
- [Rollen-System](konzepte/rollen.md) — Rollen statt Typen
- [Rechte-System](konzepte/rechte.md) — Rechte-Kaskade in Föderationen
- [Datenspeicherung](technik/datenspeicherung.md) — SQLite, Trennung, Interfaces

### Programme
- [Node](programme/node/README.md) — Der Projektverwalter
- [Conductor](programme/conductor/README.md) — Der Service-Orchestrierer
- [Desktop](programme/desktop/README.md) — Die Mensch-Maschine-Schnittstelle
- [Store](programme/store/README.md) — Das Wissen
- [Lenses](programme/lenses/README.md) — Der Informations-Betrachter
- [Search](programme/search/README.md) — Die Suche

### Konzepte
- [Rollen-System](konzepte/rollen.md) — Services deklarieren was sie können
- [Rechte-Kaskade](konzepte/rechte.md) — Rechte können nur abnehmen
- [Message Bus](konzepte/bus.md) — Kommunikation zwischen Services
- [Föderation](konzepte/foederation.md) — Zusammenarbeit zwischen Projekten
- [Pakete](konzepte/pakete.md) — Store-Paket-System
- [Tasks](konzepte/tasks.md) — Automatisierungs-Pipelines
- [Bots](konzepte/bots.md) — Bot-Framework
- [Themes](konzepte/themes.md) — Visuelles Design-System

### Technik
- [Datenspeicherung](technik/datenspeicherung.md) — SQLite-Architektur
- [Bibliotheken](technik/bibliotheken.md) — Welche Crates wofür
- [CSS-System](technik/css.md) — CSS-Variablen, Prefixing, Themes
- [UI-Objekt-System](technik/ui-objekte.md) — FsnObject: Fenster, Widgets, Modals
- [Installation](technik/installation.md) — Invite-System, Join-Prozess
- [Sicherheit](technik/sicherheit.md) — Encryption, Tokens, mTLS
- [i18n](technik/i18n.md) — Sprach-Snippets, RTL, Fallback

### TODO
- [Aktuelle TODO-Liste](todo/TODO.md) — Was gemacht werden muss
- [Bekannte Bugs](todo/BUGS.md) — Was kaputt ist
