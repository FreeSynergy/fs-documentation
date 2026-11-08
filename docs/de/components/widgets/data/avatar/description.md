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
Ein Avatar ist ein visuelles Element für einen Nutzer. Es kann ein Foto, Initialen
oder ein Icon sein.

## Verwendungszweck

- Nutzerprofile in Listen und Chats zeigen
- Aktivitätsanzeige (wer hat was getan?)
- Nutzer in Kommentaren, Aufgaben usw. zuweisen

## Varianten

| Variante (`variant`) | Beschreibung |
|----------------------|--------------|
| **image** | Foto der Person, fällt bei einem Ladefehler auf die Initialen zurück |
| **initials** | ein oder zwei Buchstaben des Anzeigenamens |
| **icon** | Symbol für Gruppen, Rollen oder automatische Nutzer |
| **placeholder** | neutrale Silhouette, wenn nichts bekannt ist |

Die Form ist keine Variante, sondern wird über `shape` (`circular`, `square`,
`pill`) und `size` gesteuert.

## Features

- Rückfallkette: Foto → Initialen → Icon → Platzhalter
- Status-Badge (online, abwesend, beschäftigt) an einer festen Position
- Ein alternativer Name ist Pflicht, sonst ist der Avatar für Screenreader leer
- Nur anklickbar, wenn eine Kontaktkarte oder ein Profil folgt (`interactive`)

## Abgrenzung

- **Nicht verwechseln mit** [icon](../../../primitives/media/icon/): ein Icon steht für einen Befehl oder eine
  Sache, ein Avatar steht für eine Person.
- **Nicht verwechseln mit** [image](../../../primitives/media/image/): Bilder zeigen Inhalte, Avatare identifizieren.
- Das Status-Badge neben einem Avatar ist ein [badge](../../../primitives/feedback/badge/), kein Teil des Avatars.

## Best Practices

- Den Avatar immer mit einem Alternativtext (Name des Nutzers) versehen
- Auf Initialen zurückfallen, wenn kein Bild vorliegt
- Die Form innerhalb einer Anwendung einheitlich halten
- Hover-Effekt für die Interaktivität

## Status-Badges
Avatare können Status-Badges zeigen:

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Online** | grün | der Nutzer ist online |
| **Offline** | grau | der Nutzer ist offline |
| **Away** | orange | der Nutzer ist abwesend |
| **Busy** | rot | der Nutzer ist beschäftigt |
| **In-meeting** | blau | der Nutzer ist in einer Besprechung |

## Hover-Effekte

- **Zoom**: der Avatar wird leicht größer
- **Border**: der Rand leuchtet auf
- **Shadow**: der Schatten wird stärker

## Siehe auch

- [data – Übersicht](../index.md)
- [Basiskomponente](../../../primitives/basics/base.md)
