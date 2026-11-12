# Stil: Windows

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

**Status: Messblatt, Entwurf (2026-11-10).** Der Windows-Stil wird 1:1 nachgebaut, je Kategorie ein Windows-Programm,
möglichst eines ohne Linux-Gegenstück (ADR 0066, Nachtrag vom 2026-11-09). Kein Linux-Programm dient als Vorlage. Dieses
Blatt sammelt die Maße aus Microsofts öffentlichen Richtlinien mit der Quelle für jeden Wert. Werte, die in den öffentlichen
Richtlinien nicht stehen, sind mit **nicht veröffentlicht** markiert und müssen aus Screenshots gemessen werden.

Quellen, durchgehend verwendet:

- **Fluent 2, Spacing and proximity / Layout**: https://fluent2.microsoft.design/layout
- **Fluent 2, Shapes**: https://fluent2.microsoft.design/shapes
- **Fluent 2, Typography (Web-Skala)**: https://fluent2.microsoft.design/typography
- **Windows, Typography in Windows 11 (Schriftskala, Schriftregeln)**: https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography
- **Windows, Geometry in Windows 11 (Eckradien)**: https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/geometry
- **Windows, Acrylic material**: https://learn.microsoft.com/en-us/windows/apps/design/style/acrylic
- **Windows, Mica material**: https://learn.microsoft.com/en-us/windows/apps/design/style/mica
- **Windows, Keyboard accessibility**: https://learn.microsoft.com/en-us/windows/apps/design/accessibility/keyboard-accessibility

Fluent 2 und Windows 11 unterscheiden sich an einigen Stellen (unten vermerkt). Wo sie sich unterscheiden, verwenden wir
für den Desktop-Stil den Windows-11-Wert und notieren den Fluent-Wert daneben.

## 1. Schriftgrößen und Zeilenhöhen

### Windows-11-Schriftskala (effektive Pixel, epx; Seite Windows Typography)

| Stil | Gewicht | Größe / Zeilenhöhe |
|------|---------|--------------------|
| Caption | Regular | 12 / 16 |
| Body | Regular | 14 / 20 |
| Body strong | Semibold | 14 / 20 |
| Body large | Regular | 18 / 24 |
| Body large strong | Semibold | 18 / 24 |
| Subtitle | Semibold | 20 / 28 |
| Title | Semibold | 28 / 36 |
| Title large | Semibold | 40 / 52 |
| Display | Semibold | 68 / 92 |

Quelle: Seite Windows Typography, Tabelle "Type ramp". Fett und kursiv gehören nicht zur Skala; für Hervorhebung Semibold
verwenden.

### Fluent-2-Web-Skala (px; Seite Fluent 2 Typography)

| Stil | Gewicht | Größe / Zeilenhöhe |
|------|---------|--------------------|
| Caption 2 | Regular | 10 / 14 |
| Caption 1 | Regular | 12 / 16 |
| Body 1 | Regular | 14 / 20 |
| Subtitle 2 | Semibold | 16 / 22 |
| Subtitle 1 | Semibold | 20 / 26 |
| Title 3 | Semibold | 24 / 32 |
| Title 2 | Semibold | 28 / 36 |
| Title 1 | Semibold | 32 / 40 |
| Large Title | Semibold | 40 / 52 |
| Display | Semibold | 68 / 92 |

Quelle: Seite Fluent 2 Typography. Die Unterschiede zur Windows-Skala: Subtitle ist 20 / 26 im Web und 20 / 28 in
Windows 11; die Web-Skala hat Caption 2 mit 10 / 14 und Title 3 mit 24 / 32, die Windows nicht aufführt.

### Lesbarkeits-Mindestwerte (Windows 11)

- **14 px Semibold** oder **12 px Regular** ist der kleinste Text, den die Windows-Richtlinien erlauben (Seite Windows
  Typography, Tabelle "Best practices"). Kleinerer Text ist in manchen Sprachen unlesbar.
- Satzschreibweise für allen UI-Text. Auslassungspunkte für die meisten Kürzungen; Abschneiden nur in seltenen Fällen.
- 50 bis 60 Buchstaben je Zeile für Fließtext (Seite Windows Typography, "Character count").

### Schriftfamilie

- **Segoe UI Variable** ist die Systemschrift von Windows (Seite Windows Typography). Achsen: Gewicht 100 bis 700 und eine
  automatische optische Größe von 8 pt bis 36 pt.
- Wir liefern Segoe UI Variable nicht aus (Microsofts Schrift). Offene Ersatzschriften stehen in Abschnitt 9.

## 2. Abstände, Raster und Geometrie

- **Abstandsskala (Web, Seite Fluent 2 Layout)**: eine Grundeinheit von **4 px**. Tokens in px: 0, 2, 4, 6, 8, 10, 12, 16, 20,
  24, 28, 32, 36, 40, 48, 52, 56. Die Werte 2, 6 und 10 sind für Symbol-Innenabstände.
- **Mindestgröße für Touch-Ziele** (Seite Fluent 2 Layout, "Applying Fluent spacing"): 44 × 44 px für Web und iOS, 48 × 48
  für Android (die Seite nennt keinen eigenen Desktop-Wert).
- **Breakpoints** (Seite Fluent 2 Layout): klein 320–479 px, mittel 480–639, groß 640–1023, extra groß 1024–1365,
  xx-groß 1366–1919, xxx-groß 1920 und mehr.
- **Raster**: ein 12-Spalten-Raster ist die übliche Wahl; Rinnen und Ränder sind Vielfache der Grundeinheit und ändern sich
  je Breakpoint. **Kein konkreter Rand- oder Rinnenwert** auf der gelesenen Seite.
- **Eckradien** (Seite Windows Geometry, "Rounded corners"):

| Element | Radius |
|---------|--------|
| Oberste Container: App-Fenster, Flyouts, Dialoge | 8 px |
| Elemente auf der Seite: Schaltflächen, Listen-Hintergründe, Textfelder, Listenansichten | 4 px |
| Leistenelemente: Fortschrittsbalken, Bildlaufleisten, Schieberegler | 4 px |
| QuickInfo (Ausnahme) | 4 px |
| Eingerastete oder maximierte Fenster | 0 px |

  Globale Ressourcen: `ControlCornerRadius` (4 px) und `OverlayCornerRadius` (8 px).
- **Fluent-Eckentokens** (Seite Fluent 2 Shapes): 0, 2, 4, 8, 12 px und Kreis. Windows verwendet nur 4 und 8.
- **Strichstärken-Tokens** (Seite Fluent 2 Shapes, Web): 1, 2, 3, 4 px.

## 3. Listen und Zeilen

- **Zeilenhöhe, Trennlinie, Symbolgröße, Innenabstand von Listenelementen**: auf den gelesenen Seiten **nicht
  veröffentlicht**. Windows 11 nutzt Listenansichten mit 4 px Ecken (Abschnitt 2). Aus den Windows-Programmvorlagen
  messen (Abschnitt 8).

## 4. Materialien

### Mica (Microsoft Learn, Mica material)

- Undurchsichtiges, dynamisches Material für die **Basisschicht** langlebiger Fenster (Apps und Einstellungen). Es
  übernimmt das Hintergrundbild einmal und fällt auf eine Volltonfarbe zurück, wenn das Fenster inaktiv ist.
- Mica Alt ist eine Variante mit stärkerer Tönung für Titelleisten mit Registerkarten. Mica ist in der Titelleiste nur
  sichtbar, wenn die App in den Nicht-Client-Bereich hineinreicht.
- Inhaltsschichten liegen darüber mit dem schwach deckenden `LayerFillColorDefaultBrush` (Standardmuster oder Karten).
- Kein Hintergrundmaterial zweimal in einer Anwendung anwenden. Nicht auf ein einzelnes Element anwenden.
- Ersatzfarben: `SolidBackgroundFillColorBase` (Mica), `SolidBackgroundFillColorBaseAlt` (Mica Alt).
- **Keine numerischen Werte** für Unschärfe oder Deckkraft auf der gelesenen Seite.

### Acrylic (Microsoft Learn, Acrylic material)

- Transluzente Textur für **flüchtige Oberflächen** (Menüs, Flyouts, Popups: Hintergrund-Acrylic) und **unterstützende
  Bereiche** (In-App-Acrylic).
- Rezept (von der Seite): Hintergrund, Unschärfe, Ausschluss-Mischschicht (für Kontrast), Farbtönung, Rauschen.
- Nicht mehrere Acrylic-Flächen nebeneinander setzen (sichtbare Naht). Keinen akzentfarbenen Text auf Acrylic.
- Acrylic wird undurchsichtig, wenn Transparenz aus ist, im Energiesparmodus, auf schwacher Hardware oder wenn ein
  Hintergrundfenster inaktiv wird.
- **Keine numerischen Werte** für Unschärfe, Rauschen oder Tönung auf der gelesenen Seite.

Unser Desktop-Stil verwendet die flache Fluent-Oberfläche: undurchsichtige Schichten, eine Mica-ähnliche Basis, wo es passt.
Acrylic nur für flüchtige Oberflächen; der Unschärfewert ist aus den Screenshots in Abschnitt 10 zu messen.

## 5. Farben

- Die Windows-Farben sind **Theme-Tokens** (zum Beispiel `SolidBackgroundFillColorBase`); die gelesenen öffentlichen Seiten
  geben die Tokennamen und das Verhalten in hell und dunkel, nicht die Hex-Werte. Werte sind auf den gelesenen Seiten
  nicht veröffentlicht.
- Lesbarkeit: Text muss auf Acrylic den Kontrast erreichen (Seite Acrylic). Auf transluzenten Flächen die Textfarben von
  Windows verwenden, keine eigenen Akzente.

## 6. Fokus

- **Visuelles Tastaturfokus-Merkmal** (Seite Keyboard accessibility): ein gestrichelter Rahmen um das fokussierte
  Steuerelement, in zwei Farben gezeichnet (ein weißer und ein schwarzer Strich mit einem Strichmuster `1,1`), nur bei Fokus
  sichtbar. Die Seite nennt **keine Pixelbreite und keinen Versatz**; die WinUI-Ressourcen enthalten sie. Aus einem
  fokussierten Windows-Steuerelement messen.
- Tastaturregeln von derselben Seite: jedes Steuerelement über Tab erreichbar; Tab-Reihenfolge folgt der sichtbaren
  Anordnung; Pfeiltasten in Listen und Rastern; Leertaste und Eingabe aktivieren; F6 wechselt zwischen den Hauptbereichen
  (muss ausdrücklich umgesetzt werden).
- Tastenkürzel werden in QuickInfos gezeigt und als Beschleuniger- und Zugriffstasten bereitgestellt.

## 7. Kontakte in Windows (Personen und Outlook, für People)

Die klassische App Personen ist im aktuellen Windows 11 nicht mehr enthalten (Sekundärquellen sagen, sie wurde mit 24H2
entfernt). Kontakte liegen jetzt in der **neuen Outlook-App für Windows**, die eine Ansicht Personen zeigt.

- **Layout** (laut Topedia-Blog, 11. Januar 2026, ein Drittbericht über die Überarbeitung durch Microsoft): ein **modernes,
  mehrspaltiges Layout** mit Suche; doppelte Kontakte werden automatisch verknüpft; Profildaten der Organisation reichern
  Kontakte an. Profilkarten zeigen **Organisationsdaten zuerst**; ein Anzeiger für mehrere Quellen erscheint bei Kontakten,
  die mit einem Entra-Konto verknüpft sind; persönliche Angaben sind bearbeitbar, Organisationsdaten nicht; ein Kontakt kann
  getrennt werden.
- Quellen: https://blog.topedia.com/2026/01/outlook-gets-an-improved-people-app/ (Drittquelle),
  https://mc.merill.net/message/MC927963 (Microsoft-Message-Center-Hinweis zum People Hub, Ankündigung der Einführung).
- **Maße** (Breiten der Bereiche, Kartenbreite, Zeilenhöhen): **nicht veröffentlicht**. Aus Screenshots der neuen Outlook
  messen und hier mit Quelle und Datum festhalten.

## 8. Windows-Programmvorlagen (genehmigt 2026-11-10)

Vom Eigentümer über den Koordinator genehmigt. Die Liste steht in `docs/en/programs/map.md`, Abschnitt "Windows
templates". Drei Einträge sind offen und brauchen eine Entscheidung (siehe Hinweise dort): Whiteboard (die eigenständige
Windows-App wird laut Microsofts Support-Seite am 2026-10-16 eingestellt), Forms und YouTube Studio (Web-Dienste, keine
Windows-App).

| Kategorie | Windows-Programm | Linux-Gegenstück |
|-----------|------------------|------------------|
| People | Outlook (Ansicht Personen) | keines nativ |
| Mail | Outlook (Mail) | keines nativ |
| Calendar | Outlook (Kalender) | keines nativ |
| Groups | Microsoft Teams | keines nativ |
| Tasks | Microsoft To Do | keines nativ |
| Files | File Explorer | kein Linux-Programm |
| Gallery (Facette von Files) | Microsoft Photos | keines nativ |
| Videos | Media Player (neue App oder Windows Media Player Legacy, noch zu entscheiden) | keines nativ |
| Wiki | Microsoft OneNote | keines nativ |
| Maps | Google Earth Pro (Windows; kein Street-View-Frontend) | zu prüfen (Linux-Desktop-Build) |
| Whiteboard | Microsoft Whiteboard (offen: Einstellung) | nur Web |
| Surveys | Microsoft Forms (offen: nur Web) | nur Web |
| Resources | Microsoft Excel | keines nativ |
| Streaming | YouTube Studio (offen: nur Web) | nur Web |
| Store | Microsoft Store | Linux-Stores sind Linux-Programme; nicht verwendet |
| Start | Startmenü und Widgets | kein Linux-Programm |
| Identity | Einstellungen > Konten, plus Windows Hello | eine Einstellungsseite |
| History | keines | keine Vorlage |

## 9. Offene Schriften (gewählt)

| Schrift | Lizenz (geprüft 2026-11-10) | Verwendung |
|---------|-----------------------------|------------|
| Selawik | SIL Open Font License 1.1; Copyright Microsoft; der Name "Selawik" ist reserviert, abgeleitete Versionen müssen umbenannt werden (Microsoft-Learn-Schriftliste: https://learn.microsoft.com/en-us/typography/font-list/selawik) | Windows-Stil. Offener Ersatz für Segoe UI, metrisch kompatibel dazu |
| Inter | SIL Open Font License 1.1 (Lizenzdatei von https://github.com/rsms/inter, "Copyright (c) 2016 The Inter Project Authors") | Apple-Stil, und Ersatz für Windows, falls Selawik nicht passt |
| Noto Sans | SIL Open Font License 1.1 (Lizenzdatei von https://github.com/notofonts/noto-fonts, "Copyright 2018 The Noto Project Authors") | Schrift-Ersatz für Schriftsysteme |

Vor einem Release die Lizenzdatei neben jeder Schriftdatei ausliefern und die Regel zum reservierten Namen bei Selawik
prüfen.

## 10. Screenshots

Unter `/srv/FreeSynergy/.scratch/reference/windows/` (nie in einem Repository), jeweils ein Ordner mit `SOURCES.txt`:

- `mica/`: `mica-light-theme.png`, `mica-dark-theme.png`, `mica-alt-tabs.png` (Microsoft Learn, Mica material)
- `acrylic/`: `acrylic-light-theme-base.png`, `acrylic-dark-theme-base.png` (Microsoft Learn, Acrylic material)
- `corners/`: `button.png`, `flyout.png` (Microsoft Learn, Geometry in Windows 11)

Noch fehlend, je genehmigtem Programm:

- **Outlook und To Do**: Microsofts Support-Seite "Use My Day with To Do in Outlook" hat Screenshots (`new-outlook-my-day-calendar-tab`, `new-outlook-to-do-my-day-to-do-tab-open-to-do`). Die Bildlinks, die das Werkzeug zurückgab, lösen nicht auf (404), deshalb nicht heruntergeladen.
- **File Explorer**: Support-Seite "File Explorer in Windows" (https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows); von dem Werkzeug zurückgegebene Bildlinks lösen noch nicht auf.
- **Teams**: Support-Seite "Overview of teams and channels" (https://support.microsoft.com/en-us/office/overview-of-teams-and-channels-c3d63c10-77d5-4204-a566-53ddcf723b46).
- **Einstellungen > Anmeldeoptionen**: https://support.microsoft.com/en-us/accounts-billing/security/sign-in-options-in-windows.
- **Fotos, Media Player, OneNote, Excel, Google Earth Pro, Forms, YouTube Studio, Store, Start, Widgets**: in diesem Durchgang kein Screenshot gefunden; die Support-Seiten wurden durchsucht, ihre Bilder aber nicht abgerufen.

Nächster Schritt: die offiziellen Seiten im Browser öffnen, die Bildadressen dort prüfen und jedes Bild mit einem
Eintrag in `SOURCES.txt` herunterladen.
