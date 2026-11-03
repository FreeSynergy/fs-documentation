# Homer - Funktionen

## Übersicht

Homer besteht aus einer statischen Seite und einer YAML-Beschreibung. Alles, was Homer kann, ergibt sich aus dieser Datei: Struktur, Beschriftung, Suchbarkeit, Aussehen. Es gibt keine Serverlogik, keine Anmeldung und keine Aktionen gegen Dienste.

---

## 1. Kacheln (Dienste)

- **Grunddaten**: `name`, `url`, `icon`
- **Zielrahmen**: `target` steuert, ob der Link im gleichen Tab, neuem Tab oder Fenster öffnet
- **Icon-Quellen**: mitgelieferte Icon-Sets, eigene Dateien im Ordner `assets/icons/`, URL zu einem Bild
- **Suchwörter**: `keywords` ergänzen Begriffe, über die eine Kachel gefunden wird
- **Kleine Markierung**: `tag` hängt eine Beschriftung an die Kachel (Farbgebung je nach Version/CSS)
- **Kein Resize, kein Drag & Drop**: Größe und Reihenfolge entstehen aus der Datei und dem Browserfenster

## 2. Gruppen und Spalten

- **Gruppen** (`apps`) fassen Kacheln zusammen, zum Beispiel „Medien“, „Netzwerk“, „Werkzeuge“
- **Gruppen-Header**: Name, optionales Logo/Bild, optionales Symbol (`class` für Icon-Klassen)
- **Spaltenanzahl** global einstellbar; auf kleinen Bildschirmen bricht die Seite automatisch um
- **Reihenfolge** der Gruppen und Kacheln entspricht der Reihenfolge in der Datei

## 3. Suche

- **Aktivierbar** über `search: true`
- **Client-seitiger Filter**: tippen reduziert die sichtbaren Kacheln sofort
- **Getrennt durch** Name und `keywords`; Groß-/Kleinschreibung ist egal
- **Kein Suchindex** auf einem Server, keine Rechtschreibkorrektur über die einfache Übereinstimmung hinaus

## 4. Kopf- und Fußbereich

- **Titel und Untertitel** (`title`, `subtitle`), eigener Dokumenttitel im Browser-Tab
- **Logo** links, eigenes Favicon
- **Icon-Links** rechts oben (`links`): eigene Symbole mit Name, Icon, URL und Zielrahmen — typischerweise für Git, Statusseite oder Admin-Werkzeuge
- **Fußzeile** (`footer`) als Text, zum Beispiel Versionsstand oder Hinweis
- **Kopfzeile ausblendbar** (`header`), wenn die Seite als neue Tab-Seite genutzt wird

## 5. Aussehen

- **Helles und dunkles Schema** (`theme`, optional automatischer Wechsel)
- **Eigenes Stylesheet** über `stylesheet`, dadurch Farben, Abstände und Schrift vollständig anpassbar
- **CSS-Variablen** im Theme überschreiben, ohne die mitgelieferten Dateien zu verändern
- **Meldungen** für Lade-, Fehler- und Offline-Zustand (`message`) sind konfigurierbar

## 6. Konfiguration

- **Hauptdatei**: `assets/config.yml` (im Container als Volume eingebunden)
- **Alternativdateien**: `?config=<name>` in der URL lädt eine andere Datei derselben Installation (neuere Versionen)
- **Download-Knopf**: die eigene Konfiguration kann aus der Seite heruntergeladen werden (`download-config`)
- **Icons** liegen bei unter `assets/icons/`
- **Vorlagen**: das offizielle Image legt bei fehlender Konfiguration eine Vorlage an; Umgebungsvariablen können Platzhalter füllen (versionsabhängig)
- **Änderungen wirken** nach dem Neuladen der Seite, ohne Neustart eines Dienstes

## 7. Erweiterte Anzeige-Typen (versionsabhängig)

Neuere Versionen können Kacheln mit mehr als einem Link füllen:

- **RSS**: Überschriften eines Feeds in der Kachel
- **Text / HTML**: kurzer, fest konfigurierter Inhalt
- **JSON-Werte**: ein Feld aus einem HTTP-Endpunkt anzeigen

Die zugehörigen Feldnamen haben sich im Projekt mehrfach geändert. Vor der Nutzung sollte die mitgelieferte Beispieldatei der verwendeten Version geprüft werden.

## 8. Betrieb und Updates

- **Auslieferung**: Container-Image, statischer Ordner oder CDN
- **Update**: neues Image ziehen oder Dateien austauschen, Seite neu laden
- **Backup**: `config.yml`, Icon-Ordner und eigene CSS-Dateien genügen
- **Mehrere Umgebungen**: identische Dateien für Test und Produktiv, getrennt durch Ordner oder Repositories

## 9. Was Homer NICHT kann

- **Keine Live-Statusanzeigen** im eigentlichen Sinn (keine Ampeln, keine Erreichbarkeitsprüfung)
- **Keine Aktionen**: kein Start, Stopp oder Neustart von Containern und Diensten
- **Keine Benutzerverwaltung, keine Rollen, keine Anmeldung**
- **Keine individualisierte Ansicht** pro Person: alle sehen dieselbe Datei
- **Kein API, keine Webhooks, keine Automatisierung** über HTTP
- **Kein Drag & Drop** und keine Layout-Verwaltung in der Oberfläche
- **Keine Passwortherausforderung für die Config**: `assets/config.yml` ist ohne vorgeschalteten Schutz öffentlich lesbar
- **Keine Historie, keine Diagramme, keine Benachrichtigungen**

## 10. Erweiterungen und Integrationswege

- **Versionsverwaltung als Erweiterung**: Config in Git, Änderungen über Pull Requests, Ausrollen per CI/CD
- **Mehrfachkonfiguration**: unterschiedliche Dateien für Teams, Geräte oder Rollen (`?config=`)
- **Eigenes CSS** statt Theme-System: ein Stylesheet reicht für ein vollständiges Erscheinungsbild
- **Eigene Auswertung im Browser**: Der Quellcode ist eine kleine Vue-Anwendung; ein Fork erlaubt eigene Anzeige-Typen
- **Externe Datenquellen**: Wenn Werte in der Kachel nötig sind, liefert ein eigener Endpunkt die Daten und ein Anzeige-Typ (versionsabhängig) zeigt sie an
- **Kombination mit Proxy-Portalen**: Homer verlinkt auf ein Portal mit Single-Sign-On, der Schutz bleibt beim Proxy

---

## Vergleich der Dashboard-Typen

| Funktion | Homer | Homarr | Heimdall | Dashy |
|----------|-------|--------|----------|-------|
| Backend | Nein | Ja | Ja | Optional |
| Konfiguration | `config.yml` | Oberfläche | Oberfläche + `.env` | `conf.yml`/`conf.json` |
| Anmeldung | Nein (Proxy) | Ja | Ja | Ja |
| Statusanzeigen | Eingeschränkt | Ja | Ja | Ja |
| Größe/Lessbarkeit der Config | Sehr hoch | Nicht vorhanden | Nicht vorhanden | Mittel bis hoch |

---

## Siehe auch

- [menu.md](menu.md) - Seitenbereiche und Betriebsrollen
- [structure.md](structure.md) - Spalten, Gruppen und Kacheln
- [api.md](api.md) - `config.yml` als Schnittstelle
- [shortcuts.md](shortcuts.md) - Tastatur und Browser-Tasten
