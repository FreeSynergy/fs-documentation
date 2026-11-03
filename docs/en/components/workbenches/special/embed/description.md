# Embed

| Field | Value |
| ------ | ------ |
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `app`, `widget`, `iframe` |
| **States** | `geladen`, `fehler` |
| **Gestures** | `tap`, `drag` (nur bei `interactive`) |
| **Animations** | `fade-in` |
| **Related** | `map-view`, `whiteboard`, `dashboard`, `base` |
| **State** | documented |

!!! info "Standardisierung"
    Die früheren Komponenten `app-embed`, `widget-embed` und `iframe-embed` sind in `embed` mit dem Attribut `source` aufgegangen: `app`, `widget`, `iframe`.

## Description

Ein **Embed** bindet fremden Inhalt in eine FreeSynergy-Oberfläche ein: ein anderes
FreeSynergy-Programm, ein Widget oder eine externe Seite. Der Inhalt gehört nicht zur
Anwendung; er wird in einer eigenen Fläche dargestellt und über eine klar benannte
Schnittstelle angesprochen.

## Purpose

- Ein FreeSynergy-Programm in ein anderes einbetten (z. B. Kalender in einem Dashboard)
- Ein Widget (Wetter, Uhr, Zähler) in eine Seite oder ein Dashboard setzen
- Eine externe Seite oder einen externen Player einbetten

## Variants

| Variant | Description |
| ---------- | -------------- |
| **app** | ein anderes FreeSynergy-Programm im Fenster |
| **widget** | kleines Programm mit eigener Konfiguration |
| **iframe** | externe Seite über `src` |

## Features

- Einheitliche Größe über `size` und `ratio`, responsives Verhalten abschaltbar
- Nachrichenaustausch mit dem eingebetteten Inhalt (`postMessage`) mit Origin-Prüfung
- Lade- und Fehlerzustand sind Teil der Komponente, nicht des eingebetteten Inhalts
- Sandbox und Berechtigungen nur bei `source = iframe` wirksam

## Distinction

- **Nicht verwechseln mit** `app-embed`, `widget-embed` und `iframe-embed`: diese drei
  früheren Eigenkomponenten sind als `source`-Werte in `embed` aufgegangen.

- **Nicht verwechseln mit** [map-view](../../../widgets/special/map-view/) und [whiteboard](../whiteboard/):
  das sind eigene Komponenten mit eigener Datenstruktur, keine Einbettung.

- **Nicht verwechseln mit** [iframe](https://developer.mozilla.org/docs/Web/HTML/Element/iframe):
  `embed` ist die Oberfläche inklusive Zuständen und Berechtigungen.

## Best Practices

- Externe Inhalte immer in den Modi `media-src` und `scripts-src` getrennt betrachten;
  Standard ist keine Skriptausführung.

- `origin` stets setzen, wenn `postMessage` aktiv ist.
- Für eingebettete Programme gilt: kein Doppelmenü. Das einbettende Programm
  versteckt eigene Kopfzeilen, wenn `source = app`.

- Ein Embed ist nie die einzige Möglichkeit, den Inhalt zu erreichen — Verweis
  nach außen mit anbieten.

## See also

- [Dashboard](../dashboard/) — Embeds als Bausteine
- [Base component](../../../primitives/basics/base.md)
