# Stil: SAP Fiori (Admin-Stil)

**Status: Messblatt, Entwurf (2026-11-10).** Das Admin-Frontend wird generiert und sieht aus wie SAP Fiori (ADR 0066;
Nachtrag 2026-11-09: "Admin-Stil = SAP Fiori, Maße aus den öffentlichen Fiori-Richtlinien"). Dieses Blatt gibt die Maße
mit ihrer Quelle an.

**Wichtig:** Die offiziellen SAP-Fiori-Webrichtlinien (sap.com/design-system und experience.sap.com) antworten auf
automatisierte Abrufe mit HTTP 403. Die Werte unten sind deshalb **nicht** von diesen Seiten gelesen. Sie stammen aus den
öffentlichen Theme-Tokens, die SAP in seinem Open-Source-Repository `SAP/fundamental-styles` veröffentlicht (Lizenz
Apache-2.0), Datei `docs/design-tokens.json`, Theme `sap_horizon` (das aktuelle Fiori-Theme). Die Token-Datei wurde am
2026-11-10 gelesen und trägt keine eigene Versionsnummer; vor jedem Release neu lesen. Werte in rem werden bei einer
Basisgröße von 16 px in px umgerechnet.

Quellen:

- **Design-Tokens (sap_horizon)**: https://github.com/SAP/fundamental-styles/blob/main/docs/design-tokens.json (Kopie der gelesenen Datei liegt in `.scratch`, nicht in einem Repository)
- **Theme-Quellen**: https://github.com/SAP/fundamental-styles/tree/main/packages/styles/src/theming
- **Fiori Design Guidelines, Content Density (Cozy and Compact)** (Seite existiert; nicht per automatisiertem Abruf erreichbar):
  https://www.sap.com/design-system/fiori-design-web/v1-120/foundations/visual/cozy-compact

## 1. Schrift

- Die Fiori-Schrift ist **72**, SAPs eigene Schrift (Tokens: `--sapFontFamily` = `"72", "72full", Arial, Helvetica, sans-serif`).
- **Wir verwenden 72 nicht.** Sie gehört SAP; ihre Lizenz erlaubt uns keine Auslieferung. Die offene Ersatzschrift steht in
  Abschnitt 6.

## 2. Schriftgrößen

Quelle: Kategorie `font` der Token-Datei.

| Token | Wert | px |
|-------|------|----|
| `--sapFontSmallSize` | .75rem | 12 |
| `--sapFontSize` (Standard, "medium") | .875rem | 14 |
| `--sapFontLargeSize` | 1rem | 16 |
| `--sapFontHeader6Size` | .875rem | 14 |
| `--sapFontHeader5Size` | 1rem | 16 |
| `--sapFontHeader4Size` | 1.25rem | 20 |
| `--sapFontHeader3Size` | 1.5rem | 24 |
| `--sapFontHeader2Size` | 2rem | 32 |
| `--sapFontHeader1Size` | 3rem | 48 |

Die Standardgröße von 14 px für Steuerelemente und Tabellenzellen verwenden. Die Größe "large" mit 16 px ist für
hervorgehobene Elemente gedacht; die Fiori-Richtlinien (Suchausschnitt der Seiten Content Density und Typography, nicht
vollständig gelesen) setzen dort Titel in Standard-Listenelemente.

## 3. Höhen, Radien, Rahmen

Quelle: Kategorie `element` der Token-Datei ("Element heights and borders").

| Token | Wert | px | Verwendung |
|-------|------|----|------------|
| `--sapElement_Height` | 2.25rem | 36 | Steuerelementhöhe (Standard) |
| `--sapElement_LineHeight` | 2.75rem | 44 | Cozy-Zeilenhöhe und Touch-Ziel |
| `--sapElement_Compact_Height` | 1.625rem | 26 | kompakte Steuerelementhöhe |
| `--sapElement_Compact_LineHeight` | 2rem | 32 | kompakte Zeilenhöhe und Zeilenhöhe in Listen |
| `--sapElement_Condensed_Height` | 1.375rem | 22 | verdichtete Höhe |
| `--sapElement_Condensed_LineHeight` | 1.5rem | 24 | verdichtete Zeilenhöhe |
| `--sapElement_BorderCornerRadius` | .75rem | 12 | Eckradius von Elementen |
| `--sapElement_BorderWidth` | .0625rem | 1 | Rahmen von Elementen |
| `--sapList_BorderWidth` | .0625rem | 1 | Rahmen von Listen |

Dichte (SAP-Richtlinien, Seite Content Density, wie im Suchausschnitt zusammengefasst): **Cozy** ist der Standard für die
meisten Steuerelemente und für Touch-Geräte; **Compact** behält die Schriftgröße bei und verkleinert Komponenten und
Abstände, für Maus und Tastatur. Cozy und Compact werden auf einer Seite nie gemischt. **Vorschlag (keine SAP-Regel):**
Das Admin-Frontend startet im **Compact**-Modus, weil es dichte Daten zeigt, Cozy als Einstellung. Das braucht die
Entscheidung des Eigentümers.

## 4. Abstände und Layout

Quelle: Kategorien `content_ui` und `shell` der Token-Datei.

| Token | Wert | px |
|-------|------|----|
| `--sapContent_Space_Tiny` | 0.5rem | 8 |
| `--sapContent_Space_S` / `_Small` | 1rem | 16 |
| `--sapContent_Space_M` / `_Medium` | 2rem | 32 |
| `--sapContent_Space_L` / `_Large` | 2rem / 3rem | 32 / 48 |
| `--sapContent_Space_XL` | 3rem | 48 |
| `--sapContent_Gap` | 1rem | 16 |
| `--sapContent_Margin_S` / `_Tiny` | 0 0 1rem | 0 0 16 |
| `--sapContent_Margin_M` / `_Small` | 1rem | 16 |
| `--sapContent_Margin_Medium` / `_L` | 1rem 2rem | 16 32 |
| `--sapContent_Margin_Large` / `_XL` | 1rem 3rem | 16 48 |
| `--sapContent_Padding_S` | 0 | 0 |
| `--sapContent_Padding_M` / `_L` | 2rem | 32 |
| `--sapContent_Padding_XL` | 3rem | 48 |
| `--sapShell_Gap_S` | .5rem | 8 |
| `--sapShell_Gap_M` / `_L` / `_XL` | 1rem | 16 |
| `--sapShell_GroupGap_S` | 2rem | 32 |
| `--sapShell_GroupGap_M` / `_L` / `_XL` | 3rem | 48 |

Der Rhythmus ist 8 px im kleinsten Schritt, dann 16, 32 und 48 px. Die Grundeinheit von 4 px erscheint nur beim
Symbol-Innenabstand (nicht in diesen Tokens).

## 5. Farben und Fokus

Quelle: Kategorien `list`, `field`, `content_ui`, `text`.

- **Fokus**: `--sapContent_FocusColor` = `#0032a5`, `--sapContent_FocusStyle` = solid, `--sapContent_FocusWidth` =
  .125rem (**2 px**). Rahmen des fokussierten Feldes: `--sapField_Focus_BorderColor` = `#0032a5`, Hintergrund `#fff`.
- **Listen**: Hintergrund `--sapList_Background` `#fff`; alternierende Zeilen `--sapList_AlternatingBackground` `#f5f6f7`;
  Rahmen `--sapList_BorderColor` `#e5e5e5`, Breite 1 px; aktive Zeile `--sapList_Active_Background` `#dee2e5`, Text
  `#131e29`; Rahmen der Gruppenüberschrift `#a8b2bd`.
- Kontrast: Text gegen die Hintergründe von Listen und Feldern prüfen, im hellen Theme und im Theme mit hohem Kontrast (die
  Tokens haben `_hc`-Varianten).

## 6. Offene Schrift mit ähnlichen Maßen

| Schrift | Lizenz | Hinweis |
|---------|--------|---------|
| Noto Sans | SIL Open Font License 1.1 (geprüft 2026-11-10 in https://github.com/notofonts/noto-fonts) | Neutrale humanistische Grotesk mit großer x-Höhe; Textbreite mit 72 bei 14 px zu vergleichen. |
| Inter | SIL Open Font License 1.1 (geprüft 2026-11-10 in https://github.com/rsms/inter) | Für Oberflächentext bei 12 bis 16 px entworfen. |

Für den Admin-Stil zuerst **Inter** verwenden; Noto Sans als Ersatz, wo ein Schriftsystem fehlt. Die Maße mit dem
Metriktest vor dem Tag prüfen (Textbreite langer Beschriftungen in Tabellenzellen).

## 7. Screenshots

- Noch keine heruntergeladen. Die Richtlinien-Seiten blockieren automatisierte Zugriffe (403), und die gefundenen
  SAP-Beispielseiten enthalten keinen stabilen Bildpfad. Nächster Schritt: offizielle Screenshots aus der SAP-Dokumentation
  oder der SAP-Fiori-Launchpad-Demo nehmen, falls deren Bedingungen es erlauben, und unter
  `/srv/FreeSynergy/.scratch/reference/fiori/<programm>/` mit `SOURCES.txt` ablegen.
