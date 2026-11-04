# Vorlage: Programm-Sektion abarbeiten (in neuem Thread einfügen)

Diesen Block kopieren, `KATEGORIE / PROGRAMM` ersetzen und dem Agenten sagen.

---

Abarbeite die Sektion `### KATEGORIE / PROGRAMM` aus `temp/apps-plan.md`
(z. B. `calendar / google-calendar`).

**Warum überhaupt (ADRs 0006, 0007):** die Maske ist die **Anforderungsgewinnung**. Beim Lesen
einer Masken-Doku entstehen zwei Listen: welche Funktionen unser Programm bieten muss, welche
Daten es dafür braucht. Eine Kategorie ist **fertig**, wenn 3–5 Masken verifiziert und die
Schnittmenge (Pflichtmenge) in `programs/<ebene>/<kategorie>/requirements.md` eingetragen ist.
Weitere Masken nur abarbeiten, wenn sie eine **neue Fähigkeit** zeigen.

**Arbeitsweise – streng dateiweise, nie mehrere Dateien sammeln:**
1. Zu einer Datei recherchieren (aktuellste Version des Produkts).
2. Diese eine Datei vollständig schreiben/überschreiben.
3. Erst danach die Zeile dieser Datei in `temp/apps-plan.md` von `[~]`/`[ ]` auf `[x]` setzen.
   Der Haken heißt **an Primärquellen verifiziert** — nicht „Datei existiert“.
4. Weiter zur nächsten Datei der Sektion (Reihenfolge wie im Plan).
5. Nach **3–5 verifizierten Programmen** der Kategorie: Pflichtmenge in
   `programs/<ebene>/<kategorie>/requirements.md` eintragen und die Freeze-Zeile im Plan abhaken.

**Rechercheregeln:**
- Nur Primärquellen: offizielles Quelltext-Repo (Tag des neuesten Release herunterladen und
  lokal lesen), offizielle API-Referenz, offizielle Hilfeseiten.
- Vorhandenen Dateiinhalt **nicht** vertrauen — er kann veraltete Fabrikation oder
  Produktvermischung enthalten (Beispiel davical: war mit Baïkal vermischt). Alles einzeln
  verifizieren.
- Nicht erfundene Features; Unklares als „nicht verifiziert“ kennzeichnen.
- Zusätzlich festhalten, **worin sich dieses Programm von Standards entfernt** — das ist ein
  eigenes Ergebnis (Beispiel: Google Kalender arbeitet praktisch ohne Standardprotokoll,
  OOXML statt ODF).

**Dateiregeln** (Sieben pro Maske unter `docs/<sprache>/programs/<ebene>/<kategorie>/masks/<programm>/`):
- `api.md`: NUR die exakte API der neusten Version (Basis-URL, Ressourcen/Endpunkte, Methoden,
  Auth/Scopes, Limits, Push/Webhooks, SDKs, Versionsstand). Prüfe zuerst, ob das Produkt noch
  entwickelt und genutzt wird; wenn nicht: hat es ein einzigartiges Feature, das andere nicht
  haben? Fehlt beides, dem Nutzer zum Löschen vorschlagen statt schreiben.
- `description.md`: Was das Programm macht, Vorteile, Abgrenzung zu vergleichbaren Produkten
  (inkl. der in dieser Serie schon dokumentierten), technische Details, Für-wen-geeignet.
- `features.md`: verifizierte Funktionsliste plus Abschnitt „Was X NICHT bietet“.
- `index.md`: Kurzüberblick, Dateistruktur-Links und zwingend ein Abschnitt **Quellen**: jede
  Informationsquelle mit URL/Fundstelle und Versionsstand, damit die Recherche wiederholbar ist.
- `menu.md`: echte Menü-/Navigationsstruktur – aus Quelltext (z. B. Menu-Definitionen) oder
  offiziellen Hilfeseiten, nicht erdacht.
- `shortcuts.md`: ehrlich prüfen (Code/Hilfeseite); gibt es keine eigenen Shortcuts, das
  ausdrücklich sagen und stattdessen Direct-URLs/CLI-Workflows listen; Shortcuts fremder Clients
  nur als client-seitig gekennzeichnet.
- `structure.md`: Request-/Programmablauf, Verzeichnis-/Modulstruktur, Konfiguration,
  Datenmodell, Deployments.

**Sprache (ADR 0008):** **Englisch zuerst** — `docs/en/…` ist die Fassung, die nach außen geht.
`docs/de/…` parallel pflegen, beide möglichst gleich halten (Textverkehr bleibt deutsch).

**Zum Abschluss:** `git add` für alle geänderten Dateien inkl. `temp/apps-plan.md`,
Commit mit Message `docs(programs): KATEGORIE/PROGRAMM verified against primary sources`,
dann `git push origin main`.

---

## Beispiel-Aufruf

> Abarbeite die Sektion `### calendar / google-calendar` aus `temp/apps-plan.md` nach der
> Vorlage in `temp/apps-prompt-vorlage.md`.
