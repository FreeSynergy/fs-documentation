# Embed

| Feld | Wert |
|------|------|
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `app`, `widget`, `iframe` |
| **States** | `geladen`, `fehler` |
| **Gestures** | `tap`, `drag` (nur mit `interactive`) |
| **Animations** | `fade-in` |
| **Related** | `map-view`, `whiteboard`, `dashboard`, `base` |
| **Status** | documented |

!!! info "Standardisierung"
    Die bisherigen Komponenten `app-embed`, `widget-embed` und `iframe-embed` wurden zum Attribut
    `source` von `embed`: `app`, `widget`, `iframe`.

## Beschreibung

Ein **Embed** bindet fremden Inhalt in eine FreeSynergy-Fläche ein: ein anderes FreeSynergy-Programm,
ein Widget oder eine externe Seite. Der Inhalt gehört nicht zur Anwendung; er wird in seiner
eigenen Fläche gezeigt und über eine klar benannte Schnittstelle angesprochen.

## Zweck

- Ein FreeSynergy-Programm in ein anderes einbetten (z. B. einen Kalender in ein Dashboard)
- Ein Widget (Wetter, Uhr, Zähler) auf einer Seite oder einem Dashboard platzieren
- Eine externe Seite oder einen externen Player einbetten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **app** | ein anderes FreeSynergy-Programm im Fenster |
| **widget** | kleines Programm mit eigener Konfiguration |
| **iframe** | externe Seite über `src` |

## Funktionen

- Einheitliche Größe über `size` und `ratio`; das responsive Verhalten lässt sich abschalten
- Nachrichtenaustausch mit dem eingebetteten Inhalt (`postMessage`) mit Prüfung des Ursprungs
- Lade- und Fehlerzustände sind Teil der Komponente, nicht des eingebetteten Inhalts
- Sandbox und Berechtigungen wirken nur mit `source = iframe`

## Abgrenzung

- **Nicht verwechseln mit** `app-embed`, `widget-embed` und `iframe-embed`: Diese drei
  früheren eigenständigen Komponenten sind jetzt Werte von `source` innerhalb von `embed`.

- **Nicht verwechseln mit** [map-view](../../../widgets/special/map-view/) und [whiteboard](../whiteboard/):
  Das sind eigene Komponenten mit eigener Datenstruktur, keine Einbettung.

- **Nicht verwechseln mit** [iframe](https://developer.mozilla.org/docs/Web/HTML/Element/iframe):
  `embed` ist die Fläche einschließlich Zuständen und Berechtigungen.

## Best Practices

- Externe Inhalte immer getrennt behandeln, über die Modi `media-src` und `scripts-src`;
  der Standard ist keine Skriptausführung.

- `origin` immer setzen, wenn `postMessage` aktiv ist.
- Bei eingebetteten Programmen: kein doppeltes Menü. Das einbettende Programm blendet
  seine eigenen Kopfzeilen aus, wenn `source = app` gilt.

- Ein Embed ist nie der einzige Weg zum Inhalt – biete auch einen Link nach außen an.

## Siehe auch

- [Dashboard](../dashboard/) — Embeds als Bausteine
- [Basiskomponente](../../../primitives/basics/base.md)
