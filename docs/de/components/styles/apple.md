# Stil: Apple

**Status: Messblatt, Entwurf (2026-11-10).** Der Apple-Stil wird 1:1 aus Apples eigenen Apps nachgebaut (ADR 0066,
Nachtrag vom 2026-11-09). Dieses Blatt sammelt die Maße aus Apples öffentlichen Richtlinien, mit der Quelle für jeden
Wert. Werte, die in den öffentlichen Richtlinien nicht stehen, sind mit **nicht veröffentlicht** markiert. Sie müssen
aus Screenshots von Apples Apps gemessen werden und werden nie aus diesem Blatt als "Apple-Werte" in ein Repository
kopiert.

Quellen, durchgehend verwendet:

- **HIG Typography**: https://developer.apple.com/design/human-interface-guidelines/typography.md
- **HIG Layout**: https://developer.apple.com/design/human-interface-guidelines/layout.md
- **HIG Lists and tables**: https://developer.apple.com/design/human-interface-guidelines/lists-and-tables.md
- **HIG Materials**: https://developer.apple.com/design/human-interface-guidelines/materials.md
- **HIG Color**: https://developer.apple.com/design/human-interface-guidelines/color.md
- **HIG Accessibility**: https://developer.apple.com/design/human-interface-guidelines/accessibility.md
- **Apple Contacts user guide (Mac)**: https://support.apple.com/guide/contacts/adrb003645bb/mac

Die HIG-Seiten wurden am 2026-11-10 in ihrer Markdown-Form gelesen. Apples Seiten können sich ändern; vor einem Release
prüfen.

## 1. Schriftgrößen und Zeilenhöhen

### macOS-Textstile (Punkt, HIG Typography, "macOS built-in text styles")

| Textstil | Gewicht | Größe (pt) | Zeilenhöhe (pt) | Hervorhebungsgewicht |
|----------|---------|------------|-----------------|----------------------|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

Quelle: HIG Typography, Tabelle unter "macOS built-in text styles".

### Standard-Dynamic-Type-Größen, iOS und iPadOS (Punkt, zur Referenz)

| Textstil | Größe (pt) | Zeilenhöhe (pt) |
|----------|------------|-----------------|
| Large Title | 34 | 41 |
| Body | 17 | 22 |
| Caption 2 | 11 | 13 |

Quelle: HIG Typography, iOS-Dynamic-Type-Tabelle, Standardzeile (Large). Nur für die iPhone-Variante des Simple-Stils
verwenden, nicht für den Desktop-Stil.

### Empfohlene Größen und Mindestwerte

| Plattform | Standard-Textgröße | Mindest-Textgröße |
|-----------|--------------------|-------------------|
| macOS | 13 pt | 10 pt |
| iOS, iPadOS | 17 pt | 11 pt |

Quelle: HIG Typography, "Ensuring legibility", und HIG Accessibility, Tabelle "Vision".

Vergrößerung: Menschen die Option geben, den Text um mindestens 200 % zu vergrößern (HIG Accessibility, "Support larger
text sizes").

### Schriftfamilie

- **SF Pro** ist die Systemschrift von macOS und iOS (aus dem Gedächtnis; in den gelesenen Seiten nicht bestätigt).
- **Lizenz**: Apples Schriftlizenz deckt nur die Entwicklung für Apple-Plattformen ab. SF darf deshalb nicht in unseren
  Paketen ausgeliefert werden (aus dem Gedächtnis; auf Apples Entwicklerseite prüfen). Wir nutzen eine offene Schrift
  (Abschnitt 9).

## 2. Abstände, Raster und Layout

- **Raster (8-Punkt)**: in den gelesenen HIG-Seiten **nicht gefunden**. Für den Apple-Stil kein 8-Punkt-Raster annehmen,
  bis gemessen.
- **Innenabstand um Bedienelemente** (HIG Accessibility, "Offer sufficiently sized controls"): etwa **12 pt** um Elemente
  mit Rahmen (Schaltflächen, Felder), etwa **24 pt** um Elemente ohne Rahmen, gemessen bis zur sichtbaren Kante.
- **Steuerelementgröße** (HIG Accessibility, Tabelle "Offer sufficiently sized controls"): macOS-Standard **28 × 28 pt**,
  Minimum **20 × 20 pt**. Für den Desktop-Stil den Standard verwenden.
- **Ränder, Fenster-Abstände, Breiten von Seitenleiste und Listen**: in den gelesenen Seiten **nicht veröffentlicht**
  (HIG Layout gibt nur qualitative Regeln: Safe Areas, Layout-Hilfslinien, "Steuerelemente nicht am unteren Fensterrand
  platzieren" auf macOS).

## 3. Listen und Zeilen

- **Zeilenhöhe, Trennlinien-Einzug, Symbolgröße, Zeilenabstand**: auf der HIG-Seite Lists and tables **nicht
  veröffentlicht** (sie gibt nur Regeln: zeilenbasiertes Format für Text, alternierende Zeilenfarben in mehrspaltigen
  Tabellen auf macOS, Klick auf eine Spaltenüberschrift zum Sortieren, veränderbare Spaltenbreiten, Gliederungsansichten
  für Hierarchie).
- Aus Apples eigenen Apps messen (Kontakte, Mail, Finder) und die Werte mit dem Dateinamen des Screenshots in dieses
  Blatt schreiben.
- **Alternierende Zeilenhintergründe**: macOS nutzt die Systemfarbe "Alternating content background colors" (HIG Color,
  macOS-Tabelle). Kein Wert.

## 4. Radien

- **Eckradien von Fenstern, Sheets und Steuerelementen**: in den gelesenen HIG-Seiten **nicht veröffentlicht**. Die
  Liquid-Glass-Formen werden als konzentrisch beschrieben, im Text wurde aber kein Radiuswert gefunden. Aus Screenshots
  messen.

## 5. Materialien (Liquid Glass und Standardmaterialien)

Quelle: HIG Materials.

- **Liquid Glass** bildet die funktionale Schicht über dem Inhalt: Navigation, Werkzeugleisten, Seitenleisten. Nicht in
  der Inhaltsschicht verwenden.
- **Varianten**: *regular* (unscharf und mit angepasster Helligkeit; Standard für die meisten Systemkomponenten,
  Seitenleisten, Warnungen, Popover) und *clear* (stark transluzent; für Komponenten über Fotos und Videos).
- **Abdunkelungsschicht für klares Liquid Glass**: liegt der Inhalt darunter hell, eine **dunkle Abdunkelungsschicht mit
  35 % Deckkraft** ergänzen. Über dunklem Hintergrund oder bei Steuerelementen für die Medienwiedergabe nicht nötig.
- **Standardmaterialien** (Inhaltsschicht, macOS): die Standardmaterialien der Plattform mit Unschärfe und Vibrancy. Die HIG
  nennt keine Zahlen für Unschärferadius oder Deckkraft. Das dünne Material lenkt die Aufmerksamkeit auf interaktive
  Elemente, das reguläre trennt Seitenleisten und gruppierte Tabellen, das dicke hält dunkle Elemente deutlich.
- **Farbe in Liquid Glass**: Farbe sparsam einsetzen, nur für den Hintergrund primärer Aktionen (HIG Color, Liquid Glass
  colour).

## 6. Farben

Quelle: HIG Color, "Specifications / System colors" (die Werte sind Apples Referenzwerte; die HIG sagt, sie können sich
zwischen Releases ändern, deshalb nicht im Code festschreiben, sondern nur in diesem Blatt für das Erscheinungsbild).

| Systemfarbe | Standard hell (RGB) | Standard dunkel (RGB) |
|-------------|---------------------|-----------------------|
| Blue | 0, 136, 255 | 0, 145, 255 |
| Red | 255, 56, 60 | 255, 66, 69 |
| Green | 52, 199, 89 | 48, 209, 88 |
| Orange | 255, 141, 40 | 255, 146, 48 |
| Yellow | 255, 204, 0 | 255, 214, 0 |
| Gray (iOS systemGray) | 142, 142, 147 | 142, 142, 147 |

- **Semantische Farben** (HIG Color, macOS-Tabelle): label, secondary label, tertiary label, separator, control background,
  window background, selected content background, keyboard focus indicator colour, control accent. Wir verwenden die
  semantischen Namen, nicht die Werte.
- **Kontrast** (HIG Accessibility, WCAG AA als Richtwert): Text bis 17 pt braucht **4,5 : 1**; ab 18 pt oder bei jedem
  fetten Text genügen **3 : 1**. In hellem und dunklem Erscheinungsbild prüfen.

## 7. Fokus

- Apple nennt die **Farbe des Tastaturfokus-Indikators** (HIG Color, macOS-Tabelle). Die gelesenen HIG-Seiten geben
  **keine Breite und keinen Versatz** für den Fokusring. Aus einem fokussierten Steuerelement in der App messen und den
  Wert hier festhalten.
- Tastaturbedienung muss mit Vollständiger Tastaturzugriff funktionieren (HIG Accessibility, "Speech").

## 8. Kontakte unter macOS (Layout, für People)

Quelle: Apple Contacts user guide (siehe Link oben), nur Layout; Maße sind **nicht veröffentlicht**.

- Das Fenster hat drei Teile: eine **Seitenleiste** mit Listen und Smart Lists (umschalten über Darstellung > Listen
  einblenden / Listen ausblenden; den Trenner ziehen; ganz nach links ziehen, um sie zu verbergen), eine **Kontaktliste**
  in der Mitte und die **Karte** des ausgewählten Kontakts rechts.
- Doppelklick auf einen Kontakt oder Karte > In separatem Fenster öffnen öffnet die Karte in einem eigenen Fenster.
- Die Sortierung nach Namen ist eine Einstellung. Ältere Anleitungen nennen Listen "Gruppen".

Maße, die aus Screenshots von Kontakte ergänzt werden (Standardgröße des Fensters, Breite der Seitenleiste, Zeilenhöhe der
Listen, Breite der Karte): **nicht veröffentlicht**.

## 9. Offene Schriften mit ähnlichen Maßen

Keine offene Schrift ist eine Kopie von SF; die Maße oben werden mit unseren eigenen Metriken nachgebildet. Kandidaten
(Lizenz geprüft, wie angegeben):

| Schrift | Lizenz | Hinweis |
|---------|--------|---------|
| Inter | SIL Open Font License 1.1 (geprüft 2026-11-10 in https://github.com/rsms/inter, "Copyright (c) 2016 The Inter Project Authors") | Neutrale Grotesk, großes x-Höhe, in der Anwendung nahe an SF. |
| Noto Sans | SIL Open Font License 1.1 (geprüft 2026-11-10 in https://github.com/notofonts/noto-fonts, "Copyright 2018 The Noto Project Authors") | Breite Sprachabdeckung. |

Für den Apple-Stil zuerst **Inter** verwenden; sie passt am besten zu den Textstilen oben. Den Lizenztext im
Schriftpaket vor jedem Release prüfen.

## 10. Screenshots

- Noch keine heruntergeladen. Die HIG-Bilder sind unter den geratenen Pfaden nicht erreichbar (404), und in diesem Durchgang
  wurde kein offizieller Screenshot von Kontakte gefunden. Nächster Schritt: von Apples eigenen Pressseiten oder der
  App-Store-Seite nehmen, unter `/srv/FreeSynergy/.scratch/reference/apple/<programm>/` mit einer `SOURCES.txt` ablegen,
  nie in einem Repository.
