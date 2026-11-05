# Homer - Menüpunkte

## Übersicht

Homer hat **keine Menüs im klassischen Sinn**: Es gibt keine Navigation, keine Einstellungsseite und keine Verwaltungsoberfläche. Bedienelemente sind die Kopfzeile, die Icon-Links, das Suchfeld und die Kacheln selbst. Was als „Menü“ empfunden wird, entsteht durch die Konfigurationsdatei.

## Bedienelemente auf der Seite

### 1. Kopfzeile
- **Funktion**: Titel, Untertitel und Logo der Startseite
- **Details**:
  - `title` und `subtitle` als Text
  - `logo` links, `icon` als Favicon im Browser-Tab
  - `document-title` bestimmt den Tab-Titel
  - Kopfzeile über `header` ausblendbar (praktisch als neue Tab-Seite)

### 2. Icon-Links (rechts oben)
- **Funktion**: eigene, dauerhafte Verknüpfungen, zum Beispiel zu Git, Statusseite oder Administration
- **Details**:
  - Liste `links` mit `name`, `icon`, `url` und optionalem `target`
  - erscheinen als kleine Symbole mit Tooltip
  - Reihenfolge wie in der Datei
  - keine Aufklappmenüs, jeder Eintrag ist ein direkter Link

### 3. Suchfeld
- **Funktion**: Kacheln nach Name und Suchwörtern filtern
- **Details**:
  - nur sichtbar, wenn `search: true` gesetzt ist
  - filtert ohne Neuladen, Anzeige reduziert sich sofort
  - Löschen des Textes zeigt wieder alle Kacheln
  - kein Vorschlagsmenü, keine Trefferzähler

### 4. Gruppenüberschriften
- **Funktion**: fassen Kacheln thematisch zusammen
- **Details**:
  - `name` als Überschrift
  - optionales `logo` (Bild) und `class` (Symbol)
  - Überschriften werden nicht verlinkt und sind nicht aufklappbar

### 5. Kacheln (Dienste)
- **Funktion**: Link zu einem Dienst, erkennbar an Icon und Name
- **Details**:
  - Linksklick öffnet das in `target` eingestellte Ziel
  - Hover hebt die Kachel leicht hervor
  - `tag` zeigt eine kleine Markierung, `keywords` wirken nur in der Suche
  - **kein Kontextmenü von Homer**: der Rechtsklick zeigt das Browser-Menü (Link kopieren, neu öffnen)

### 6. Konfigurations-Werkzeug
- **Funktion**: die eigene Konfiguration herunterladen (`download-config`)
- **Details**:
  - kleiner Knopf/Link, abhängig von der Einstellung
  - lädt die aktuell geladene `config.yml` herunter
  - dient dem Sichern und Übertragen auf eine andere Installation
  - **Vorsicht**: die Datei enthält interne URLs; ohne Proxy-Schutz ist sie für alle lesbar

### 7. Fußzeile
- **Funktion**: Hinweis, Versionsstand oder Rechtliches
- **Details**:
  - Freitext über `footer`
  - keine Linksammlung, keine Aktionselemente

## Konfigurationsdatei als „Menüebene“

| Bereich | Datei-Abschnitt | Wirkung auf der Seite |
|---------|-----------------|------------------------|
| Kopfzeile | `title`, `subtitle`, `logo`, `header` | sichtbarer Kopfbereich |
| Icon-Links | `links` | Symbole rechts oben |
| Suche | `search` | Suchfeld an/aus |
| Struktur | `columns`, `apps` | Spaltenanzahl, Gruppen, Kacheln |
| Aussehen | `theme`, `stylesheet` | helles/dunkles Schema, eigenes CSS |
| Meldungen | `message` | Lade-, Fehler- und Offline-Hinweise |
| Export | `download-config` | Download-Knopf |

## Menüs nach Rolle

Homer kennt **keine Konten und keine Rollen**. Unterschiede entstehen ausschließlich im Betrieb:

### Betreiber (Schreibender Zugriff)
- darf `assets/config.yml`, `assets/icons/` und eigene CSS-Dateien ändern
- pflegt Änderungen in Git und rollt sie über das Deployment aus
- entscheidet über Icon-Links, Gruppenreihenfolge und Suchwörter
- **Kein Menü in Homer**: Änderungen geschehen in der Datei und im Deployment

### Angemeldeter Nutzer (über Reverse Proxy)
- sieht Homer nur, nachdem ein vorgeschalteter Schutz (Basic Auth, Authentik, Authelia) ihn akzeptiert hat
- Bedienung identisch zum Gast: Kacheln öffnen, suchen, eventuell Konfiguration herunterladen
- Rollenunterschiede sind ausschließlich Regeln des Proxies

### Read-only-Nutzer (Standardfall)
- sieht genau die ausgelieferte Datei
- kann nichts ändern, da keine Schreibmöglichkeit existiert
- sinnvolle Betriebsform: Download-Knopf deaktivieren, damit die Konfiguration nicht sichtbar wird

### Unterschiedliche Ansichten pro Person
- über mehrere Dateien: `?config=team-a.yml`, `?config=mobile.yml`
- der Proxy kann diese Parameter je Nutzergruppen setzen
- jede Datei erzeugt eine eigene, in sich geschlossene Startseite

## Sicherheitsrelevante Hinweise

- Ohne vorgeschalteten Proxy sind **Kacheln, interne URLs und die komplette Konfiguration öffentlich** lesbar
- `download-config` nicht aktivieren, wenn die Konfiguration nicht geteilt werden soll
- Geschützte Bereiche bleiben geschützt: Homer verlinkt nur, es übernimmt keine Anmeldung

## Shortcuts

Die nutzbaren Tasten (überwiegend Browser-Standard) stehen in [shortcuts.md](shortcuts.md).
