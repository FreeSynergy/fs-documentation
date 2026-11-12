# 0074 – Stil, Bausteine, Bewegung, Klang und Menüs: getrennte Schichten aus Standards

Status: **akzeptiert** (Gründer, 2026-11-12, mit Änderungen zu 3, 7 und 8 eingearbeitet); Code nach dem Meilenstein „Wir benutzen es selbst“, das Umstellen des Bestands beginnt sofort · baut auf ADR 0045 (Unsupported, SupportReport), 0065 (Standard-Fensterhülle), 0066 (Typen, Befehle mit `supported`, vier Frontends), 0068 (Fähigkeiten, provides/requires), 0069 (Wiederherstellen), 0073 (Kollaboration)

Grundlage: die Berichte in `.scratch/schichten/` (Stand 2026-11-12): BESTAND-theme-vertrag, BAUSTEINE, KLANG, MENUES, BEWEGUNG-STANDARDS, RECHERCHE-bewegung, KDE-THEMING, BLINC-GLAS. Was dort als „[nicht belegt]“ markiert ist, wird hier nicht als Tatsache übernommen.

## Ausgangslage

- Wir haben mehrere Frontends nach Vorbildern gebaut (ArtCraft, Fluent/Windows 11, Things 3, Jira, Confluence, Notion, KDE Discover). Aussehen und Anordnung stecken dabei noch **zusammen** im Code.
- Bestand (gezählt per Skript): fs-components hat 474 Klassen-/Id-Namen und **205 feste Farben im Code**. fs-store hat 76 feste Abstände. fs-files, fs-tasks, fs-wiki, fs-people und fs-groups haben keine eigenen Farben oder Klassen. Das Umstellen trifft also vor allem die Bausteine.
- Blinc (fs-blinc-3.1) kann Federn, Keyframes, Zeitleisten, Layout-Animation, Hintergrund-Unschärfe/Glas, Transluzenz und Schatten. Es hat aber **keinen globalen Schalter**, der Bewegung abschaltet.
- Für Menüs aus einer Beschreibung gibt es **keinen** desktopübergreifenden Standard. KDE (KXMLGUI) und GTK (GMenuModel) haben je eine eigene Lösung. Es gibt aber Standards drumherum (siehe 6).

## Grundsatz

**Ein Programm liefert Funktionen und Daten. Ein Frontend ordnet an. Ein Stil gestaltet. Bewegung und Klang sind eigene, abschaltbare Schichten.** Keine Schicht greift in eine andere ein. Jede Schicht ist ein eigenes Paket im Store.

Wo ein Standard existiert, nutzen wir ihn. **Wo keiner existiert, schreiben wir einen, veröffentlichen ihn als Vorschlag und geben ihn allen** (Manifest, „Erst Standards“).

## Entscheidung

### 1. Fünf Schichten

| Schicht | Was sie festlegt | Standard-Grundlage | Paketart im Store |
|---|---|---|---|
| **Stil (Theme)** | Farben, Schrift, Ecken, Linien, Abstände, Schatten, Glas; Regeln je Baustein | W3C Design Tokens Format (DTCG); CSS für die Baustein-Regeln | `theme` |
| **Icons** | Bilder für Aktionen, Typen, Orte | freedesktop Icon Theme + Icon Naming (Vollfarbe groß, `-symbolic` klein) | `icon-theme` |
| **Anordnung (Frontend)** | Welche Bausteine wo stehen, Navigation, welche Funktion in welchem Menü | Programm-Manifest + Anordnungsdatei (5, 6) | `frontend` |
| **Bewegung** | Dauer, Kurven, Übergang je Ereignis | DTCG `duration`, `cubicBezier`, `transition`; Ereignisliste (7) | `motion` |
| **Klang** | Klang je Ereignis | freedesktop Sound Theme + Sound Naming | `sound-theme` |
| **Haptik** (Telefone, Tablets; Vorschlag, offen) | Vibrationsmuster je Ereignis | W3C Vibration API; Muster wie bei Klang an Ereignisse gebunden | `haptics` |
| **Tastenkürzel** (Vorschlag, offen) | Tasten je Funktion | IBM CUA als Grundlage (Strg+C …); Profile, z. B. nach KDE, GNOME, macOS, Emacs, Vim | `shortcuts` |
| **Sprache und Formate** (Vorschlag, offen) | Texte, Datum, Zahlen, Schreibrichtung | BCP 47, Unicode CLDR | `language` |

Dazu werden **Systemeinstellungen immer gelesen und beachtet**: hell/dunkel (`color-scheme`), Akzentfarbe (`accent-color`), hoher Kontrast (`contrast`) und reduzierte Bewegung (`reduced-motion`) über das Portal `org.freedesktop.appearance`. Schrift und Mauszeiger gehören zum Stil; die Schriften sind frei lizenziert (z. B. SIL OFL).

Im Store bekommt jede Schicht eine **eigene Gruppe** mit Untergruppen, ebenso Programme und Server.

### 2. Der Theme-Vertrag: feste Baustein-Namen, keine Sonderklassen

- Jeder Baustein hat einen **festen, dokumentierten Namen** und benannte Teile und Zustände. Beispiel: `program-card` mit den Teilen `icon`, `title`, `summary`, `badge`, `action` und den Zuständen `installed`, `update`, `busy`.
- Die Namen folgen **WAI-ARIA-Rollen** (W3C), wo es eine passende gibt (`button`, `menu`, `menuitem`, `tab`, `dialog`, `alert`, `grid` …). Wo Open UI einen gebräuchlichen Namen hat, folgen sie Open UI.
- **Reiche Bausteine sind ausdrücklich gewollt.** Eine Programmkarte im Store, eine Board-Spalte und eine Aufgabenzeile sind eigene Bausteine, nicht „eine Box mit Text“. Nur so kann ein Stil sie gezielt gestalten, und nur so können Menschen ohne KI eigene Frontends bauen.
- **Ein Stil gestaltet nur diese Namen.** Er funktioniert damit auf jedem Programm, auch auf künftigen. Programmeigene Feinheiten darf ein Stil zusätzlich mitbringen, aber nie als Voraussetzung.
- **Programme und Frontends enthalten keine Farben, Abstände oder Schriften.** Der Inhalt (Farben einer Zeichnung, Formatierung eines Dokuments) gehört dem Inhalt, nicht dem Stil.
- Die Werte liegen als **Design Tokens im DTCG-Format** vor. Ein späterer Editor ändert nur Tokens, ohne CSS oder Code.
- Die Liste aller Bausteine mit Teilen und Zuständen ist der **Theme-Vertrag**. Er steht in fs-components, ist versioniert und wird als Standard-Vorschlag veröffentlicht.

### 3. Eigene Stile statt Markenstile

- Wir bauen **5 bis 6 eigene Stile**, jeweils hell und dunkel, von dezent bis verspielt. **Namen immer auf Englisch:** **Calm**, **Office**, **Craft**, **Glass**, **Playful**, **Contrast** (hoher Kontrast, große Schrift, für Barrierefreiheit).
- Der Name ist unser eigener. **Die Beschreibung nennt fair, woran der Stil angelehnt ist**, damit Menschen sich vorstellen können, wie er aussieht. Beispiel: „Calm – angelehnt an Notion und Things“, „Office – angelehnt an Jira, Confluence und Fluent“, „Craft – angelehnt an ArtCraft“.
- Gefällt uns beim Nachbauen eines Vorbilds ein Stil, bauen wir ihn **zusätzlich als eigenes Theme** nach, wenn der Aufwand klein ist. Die Zeit ist dann schon investiert.
- **Admin-Frontends** (alle Einstellungen, ADR 0066) sind standardmäßig an **SAP Fiori** angelehnt (Entscheidung des Gründers). SAP ist damit kein eigener Stil neben den anderen, sondern der Admin-Standard.
- Logos, Markenicons und Markenfarben übernehmen wir nicht.
- **Glas** ist mit Blinc ohne Änderung machbar (Hintergrund-Unschärfe, Transluzenz, ein Schatten). Mehrere Schatten auf Glas bräuchten eine Änderung an Blinc. Dafür gibt es keinen neuen Upstream-PR ohne Freigabe.

### 4. Vorbilder: 1:1 nachbauen, dann zerlegen

- Ein Vorbild wird zuerst **pixelgenau nachgebaut**. Das ist die Messlatte, ob unsere Bausteine alles können.
- Dann wird der Nachbau zerlegt: die **Anordnung** bleibt (sie macht das Programm aus), das **Aussehen** wird durch unseren Stil ersetzt, dazu kommen Bewegung und Klang.
- **Der 1:1-Nachbau bleibt lokal und wird nie veröffentlicht.** Veröffentlicht wird nur die Anordnung mit unseren Stilen. Wir übernehmen Muster (Board mit Spalten, Seitenleiste mit Listen), keine markanten Einzelheiten.
- Vorbilder sind **bezahlte Produkte** (Entscheidung des Gründers, 2026-11-12).

### 5. Programm-Manifest: was ein Programm anbietet

Jedes Programm veröffentlicht maschinenlesbar:

- **Funktionen** (Befehle nach ADR 0066, mit `supported`). Die Namen kommen aus den Standard-Aktionsnamen von freedesktop Icon Naming, wo es einen gibt (`document-new`, `document-save`, `edit-copy`, `edit-undo`, `list-add` …); sonst `<programm>.<befehl>`.
- **Objekte**, die es zeigen kann (`board`, `card`, `page`, `file`, …), jeweils mit dem Baustein, der sie darstellt.
- **Attribute** je Objekt (`board:columns`, `card:due`, …) mit Typ nach ADR 0066.

Das Manifest ist Teil des Pakets und wird im Katalog als Fähigkeit geführt (ADR 0068).

### 6. Anordnungsdatei: Frontends als Beschreibung

- Ein Frontend ist **eine Datei**, die die Bausteine anordnet und Funktionen in Menüs, Werkzeugleisten, Kontextmenüs und Tastenkürzel legt.
- Muster: KDE KXMLGUI (`ui.rc`) und GTK GMenuModel. Beide trennen Aktionen von ihrer Anordnung und haben das jahrelang bewiesen.
- Nach außen: freedesktop Desktop Entry `Actions`, `org.freedesktop.Application` (`ActivateAction`) und DBusMenu (de facto, von Canonical). Damit verstehen auch KDE und GNOME unsere Menüs.
- **Menschen bearbeiten die Datei über einen Editor**, wie bei KDE „Werkzeugleisten einrichten“. Die Datei ist der Standard, nicht die Bedienung.
- Ein Frontend, das eine nicht unterstützte Funktion anordnet, zeigt sie gesperrt mit Grund (ADR 0066).
- Weil es dafür keinen desktopübergreifenden Standard gibt, **veröffentlichen wir dieses Format als Standard-Vorschlag**.
- Übergang: Heute sind die Frontends Rust-Code im Programm. Sie werden in Schritten auf Anordnungsdateien umgestellt. WASM-Frontends folgen dem gleichen Vertrag.

### 7. Ereignisse, Bewegung und Klang

- Es gibt **eine Liste von Oberflächen-Ereignissen**, die jedes Programm gleich meldet: erscheinen, verschwinden, verschieben, auswählen, ziehen, ablegen, erledigt, Fehler, Warnung, neue Nachricht …
- Es gibt **eine standardisierte Liste von Animationsarten** (z. B. einblenden, ausblenden, durchblenden, gleiten, skalieren, Feder), jede mit ihren Parametern als DTCG-Tokens (Dauer, Kurve, Weg).
- Ein **Animationsprofil** ordnet jedem Ereignis eine Animationsart mit Standardwerten zu. Profile benutzen **nur** die standardisierten Ereignisse und Animationsarten. Wir bauen **mehrere Profile** (z. B. aus, sanft, lebhaft). Jeder Mensch kann die Werte eines Profils ändern.
- Neue Animationen, die wir bauen, werden als neue Animationsart in die Liste aufgenommen und stehen dann allen Profilen zur Verfügung.
- Ein **Klang-Theme** ordnet Ereignissen Klänge zu, und zwar **nur mit Namen aus der freedesktop Sound Naming Specification** (125 Namen in 5 Gruppen laut Abschnittszählung: Warnungen 7, Benachrichtigungen 40, Aktionen 29, Eingabe-Rückmeldung 44, Spiel 5). Wir erfinden keine Klangnamen. Wo uns ein Name fehlt, schlagen wir ihn upstream vor.
- Vorhandene Klang-Themes (freedesktop-Referenz, KDE Ocean, Yaru) sind **vor der Aufnahme je Datei auf ihre Lizenz zu prüfen**, denn die Angaben der Paketierer widersprechen sich.
- **Abschaltbar, immer:** Wir lesen die Systemeinstellung (Portal `org.freedesktop.appearance` `reduced-motion`, GNOME `enable-animations`, KDE `AnimationDurationFactor`). Dazu kommen eigene Einstellungen aus / dezent / verspielt sowie Klang an/aus, je Programm überschreibbar. Weil Blinc keinen globalen Schalter hat, setzt fs-components ihn um.
- Effekte und Animationen in **Inhalten** (Video, Bild, Präsentation) bleiben Workflow-Module und sind nicht Teil dieser Schicht.

### 8. Das Frontend bringt Standards mit, der Mensch ändert

- **Ein Frontend legt sein Standard-Aussehen fest:** Stil, Icons, Animationsprofil, Klang-Theme, Tastenkürzel-Profil. Es nennt sie im Manifest beim Namen. Ist eines nicht installiert, gilt der Systemstandard.
- **Der Mensch kann jede Schicht einzeln ändern**, für alle Programme oder nur für eines.
- Reihenfolge: Wahl des Menschen für dieses Programm → Wahl des Menschen für alle Programme → Standard des Frontends → Systemstandard.
- Ein **Stil-Paket** kann als Metapaket mehrere Schichten zusammen mitbringen (z. B. Glass mit passendem Animationsprofil und Klang-Theme).
- **Ein Standard-Frontend kommt immer mit dem Programm.** Ein Programm ist nie ohne Gesicht.

## Folgen

- **Umstellen, was wir haben (zuerst, vor neuen Frontends):**
  1. Theme-Vertrag aus dem Bestand ableiten;
  2. die 205 festen Farben und die festen Abstände in Tokens überführen;
  3. Craft, Breeze, Standard und Admin als Stile nach dem Vertrag;
  4. die vorhandenen Frontends nach Anordnung und Stil trennen.
- fs-components bekommt den globalen Bewegungs- und Klang-Schalter.
- Der Store bekommt die Gruppen Frontends, Server, Themes, Icons, Bewegung und Klänge.
- Eine Doku-Seite **„Unsere Standard-Vorschläge“** listet alles, was wir als Standard vorschlagen: Theme-Vertrag, Anordnungsformat, Ereignisliste, Programm-Manifest, Fähigkeiten auf Feature-Ebene.

## Offen

- Werte der fünf bis sechs Stile (nach Bildern, wie immer).
- Die standardisierte Liste der Ereignisse und Animationsarten (Entwurf nach den Berichten in `.scratch/schichten/`).
- Wer die Standard-Vorschläge annimmt (freedesktop, W3C-Gruppen) und in welcher Form.
- Lizenzprüfung der Klang-Themes je Datei.
- Ob der Editor für Anordnungsdateien ein eigenes Programm oder eine Facette des künftigen Zeichenprogramms wird.
