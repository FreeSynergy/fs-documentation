# Avatar

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `image`, `initials`, `icon`, `placeholder` |
| **Zustände** | `geladen`, `fehler` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `fade-in`, `lift` |
| **Verwandt** | `icon`, `image`, `badge`, `list-view` |
| **Status** | dokumentiert |

## Beschreibung
Ein Avatar ist ein visuelles Repräsentations-Element für einen Benutzer. Es kann aus einem Foto, Initialen oder einem Icon bestehen.

## Verwendungszweck

- Benutzerprofile in Listen und Chat anzeigen
- Aktivitätsanzeige (Wer hat was gemacht?)
- Nutzerzuordnung in Kommentaren, Aufgaben, etc.

## Varianten

| Variante (`variant`) | Beschreibung |
|----------------------|--------------|
| **image** | Foto der Person, bei Ladefehler Rückfall auf Initialen |
| **initials** | ein bis zwei Buchstaben des Anzeigenamens |
| **icon** | Symbol für Gruppen, Rollen oder automatische Nutzer |
| **placeholder** | neutrale Silhouette, wenn nichts bekannt ist |

Die Form ist keine Variante, sondern wird über `shape` (`circular`, `square`, `pill`) und
`size` gesteuert.

## Features

- Rückfallkette: Foto → Initialen → Icon → Platzhalter
- Statusbadge (online, abwesend, beschäftigt) an fester Position
- Alternativer Name ist Pflicht, sonst ist der Avatar für Screenreader leer
- Klickbar nur, wenn eine Kontaktkarte oder ein Profil folgt (`interactive`)

## Abgrenzung

- **Nicht verwechseln mit** [icon](../../media/icon/): ein Icon steht für einen Befehl oder eine
  Sache, ein Avatar stellt ein Subjekt dar.
- **Nicht verwechseln mit** [image](../../media/image/): Bilder zeigen Inhalt, Avatare identifizieren.
- Das Statusbadge neben dem Avatar ist ein [badge](../../feedback/badge/), nicht Teil des Avatars.

## Best Practices

- Avatar immer mit Alt-Text (Name des Benutzers)
- Fallback auf Initialen, wenn kein Bild vorhanden
- Konsistente Form innerhalb einer Anwendung
- Hover-Effekt für Interaktivität

## Status-Badges
Avatare können Status-Badges anzeigen:

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Online** | Grün | Benutzer ist online |
| **Offline** | Grau | Benutzer ist offline |
| **Away** | Orange | Benutzer ist abwesend |
| **Busy** | Rot | Benutzer ist beschäftigt |
| **In-Meeting** | Blau | Benutzer ist in Meeting |

## Hover-Effekte

- **Zoom**: Avatar vergrößert sich leicht
- **Border**: Rand leuchtet auf
- **Shadow**: Schatten wird stärker

## Siehe auch

- [data – Übersicht](../index.md)
- [Basiskomponente](../../basics/base/)
