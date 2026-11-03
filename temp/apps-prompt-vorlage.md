# Vorlage: App-Sektion abarbeiten (in neuem Thread einfügen)

Diesen Block kopieren, `KATEGORIE / APP` ersetzen und dem Agenten sagen:

---

Abarbeite die Sektion `### KATEGORIE / APP` aus `docs/de/apps/plan.md`
(z. B. `calendar / google-calendar`).

**Arbeitsweise – streng dateiweise, nie mehrere Dateien sammeln:**
1. Zu einer Datei recherchieren (aktuellste Version des Produkts).
2. Diese eine Datei vollständig schreiben/überschreiben.
3. Erst danach die Zeile dieser Datei in `docs/de/apps/plan.md` von `[ ]` auf `[x]` setzen.
4. Weiter zur nächsten Datei der Sektion (Reihenfolge wie im Plan).

**Rechercheregeln:**
- Nur Primärquellen: offizielles Quelltext-Repo (Tag des neuesten Release herunterladen und lokal lesen), offizielle API-Referenz, offizielle Hilfeseiten.
- Vorhandenen Dateiinhalt nicht vertrauen – er kann veraltete Fabrikation oder Produktvermischung enthalten (Beispiel davical: war mit Baïkal vermischt). Alles einzeln verifizieren.
- Nicht erfundene Features; Unklares als „nicht verifiziert“ kennzeichnen.

**Dateiregeln:**
- `api.md`: NUR die exakte API der neusten Version (Basis-URL, Ressourcen/Endpunkte, Methoden, Auth/Scopes, Limits, Push/Webhooks, SDKs, Versionsstand). Prüfe zuerst, ob das Produkt noch entwickelt und genutzt wird; wenn nicht: prüfe, ob es ein einzigartiges Feature hat, das andere nicht haben – fehlt beides, dem Nutzer zum Löschen vorschlagen statt schreiben.
- `description.md`: Was das Programm macht, Vorteile, Abgrenzung zu vergleichbaren Produkten (inkl. der in dieser Doku-Serie schon dokumentierten), technische Details, Für-wen-geeignet.
- `features.md`: verifizierte Funktionsliste plus Abschnitt „Was X NICHT bietet“.
- `index.md`: Kurzüberblick, Dateistruktur-Links und zwingend ein Abschnitt **Quellen**: jede Informationsquelle mit URL/Fundstelle und Versionsstand, damit die Recherche später wiederholbar ist.
- `menu.md`: echte Menü-/Navigationsstruktur – aus Quelltext (z. B. Menu-Definitionen) oder offiziellen Hilfeseiten, nicht erdacht.
- `shortcuts.md`: ehrlich prüfen (Code/Hilfeseite); gibt es keine eigenen Shortcuts, das ausdrücklich sagen und stattdessen Direct-URLs/CLI-Workflows listen; Shortcuts fremder Clients nur klar als client-seitig gekennzeichnet.
- `structure.md`: Request-/Programmablauf, Verzeichnis-/Modulstruktur, Konfiguration, Datenmodell, Deployments.

**Zum Abschluss:** `git add` für alle geänderten Dateien inkl. `docs/de/apps/plan.md`,
Commit mit Message `docs(de/apps): KATEGORIE/APP auf verifizierter Quellenbasis`, dann `git push origin main`.

---

## Beispiel-Aufruf

> Abarbeite die Sektion `### calendar / google-calendar` aus `docs/de/apps/plan.md` nach der Vorlage in `docs/de/apps/PROMPT-VORLAGE.md`.
