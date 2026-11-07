# Confluence (Cloud, latest) · Themes

Quellen: S-Nummern verweisen auf [index.md](../../index.md).

## Was das Produkt bietet [S17]

- Theme pro Benutzer: Light oder Dark. Jeder Benutzer wählt selbst. Die Wahl ist getrennt vom Standard der Website.
- Standard der Website: Settings > Look and feel > Themes > Theme auswählen > Confirm (Administrator).
- Themes über die eingebaute Liste hinaus müssen zuerst aus dem Atlassian Marketplace installiert werden. [S17]
- Bereichs-Theme: Ein Bereich mit "Global look and feel" übernimmt das Theme der Website und dessen Anpassungen. Wie für einen einzelnen Bereich ein anderes Theme gesetzt wird: ungeprüft.
- Eigene Farben oder CSS in der Cloud: ungeprüft (S17 erwähnt "customizations", ohne sie aufzuzählen).

## Design-Tokens (Atlassian Design System)

Die eigenen Apps von Atlassian verwenden Design-Tokens. Diese sind veröffentlicht und beschreiben das System, das die Produkte von Atlassian nutzen. Für uns sind sie Referenzmaterial: Wir übernehmen die Struktur (Token-Namen, Skalen), nicht kopierte Werte oder Paletten. [S18][S19][S21]

| Bereich | Fakten | Quelle |
|---------|--------|--------|
| Farbe | Alle Farb-Tokens beginnen mit `color`, dann Eigenschaft (background, border, icon, text). Hell- und Dunkelthema: jeder Token ist pro Thema einem Wert zugeordnet. | [S18] |
| Farbe | 10 Akzentfarben, jede mit Token für Hintergrund, Text, Rahmen und Symbol. Akzent-Tokens sollten keine Bedeutung tragen (Information, Warnung, Erfolg). | [S18] |
| Farbe | Eingabe-Tokens: `color.border.input`, `color.background.input` | [S18] |
| Farbe | Atlassian gibt für seine Tokens WCAG-AA-Kontrast an | [S18] |
| Typografie | Schriftfamilien: Atlassian Sans (App-Schrift), Atlassian Mono (Code). Apps, die noch nicht im System sind, verwenden Systemschriften. | [S19] |
| Typografie | Einheiten: rem; 1 rem = 16 px | [S19] |
| Typografie | Tokens der Schriftskala: `font.heading.xxlarge` (2 rem / 32 px, Zeilenhöhe 36 px) bis `font.heading.xxsmall` (0,75 rem / 12 px); `font.body.large` (16 px / 24 px), `font.body` (14 px / 20 px), `font.body.small` (12 px / 16 px); `font.metric.*` für Kennzahlen; `font.code` (12 px / 20 px) | [S19] |
| Abstand | Basis-Token `space.100` = 8 px = 0,5 rem. Skala: `space.025` (2 px), `space.050` (4 px), `space.075` (6 px), `space.100` (8 px), `space.150` (12 px), `space.200` (16 px), `space.250` (20 px), `space.300` (24 px), `space.400` (32 px), `space.500` (40 px), `space.600` (48 px), `space.800` (64 px), `space.1000` (80 px) | [S21] |

## Was nachgebaut werden kann

| Element | Nachbauen? | Hinweis |
|---------|------------|---------|
| Helles und dunkles Thema mit einer Token-Schicht | Ja | Eigene Token-Namen und -Werte verwenden. |
| Schriftskala mit 14 px Fließtext und 16 px großem Fließtext | Ja | Die Struktur ist Standard; die Werte sind allgemein. |
| 8-px-Abstandsbasis | Ja | Nur die Struktur. |
| 10-Akzent-Palette | Nur als eigene Wahl | Keine Hex-Werte von Atlassian übernehmen. Unsere Markenpalette verwenden (der dataviz-Skill kann Platzhalter-Paletten liefern). |
| Genaue Farben, Layout-Tokens und CSS von Confluence | Nein | Hier nicht als kopierbare Ressource veröffentlicht; nicht geprüft. |

## Nicht geprüft

- Hex- oder RGB-Werte der eigenen Benutzeroberfläche von Confluence.
- Breiten der Seitenleiste und des Kopfbereichs von Confluence (frühere Fassung: 50 px und 30 px).
- Confluence-spezifische Schriftgrößen im Editor.
