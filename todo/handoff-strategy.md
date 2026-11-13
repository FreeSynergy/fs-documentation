# Übergabe: Strategie-Sitzung (Stand 2026-11-13, Mittag)

Für eine neue Strategie-Sitzung (Opus). **Zuerst lesen:** diese Datei, dann das Memory `/home/kal/.claude/projects/-srv-FreeSynergy/memory/MEMORY.md` (alle verlinkten Dateien), dann ADR 0074, 0075, 0076 in `conventions/decisions/`.

## Rollen
- **Strategie (Opus):** spricht als Einzige mit dem Nutzer (Deutsch, einfache Sprache, Fragen am Ende nach „@@@“), entscheidet, schreibt ADRs, prüft Bilder, gibt Aufträge an den Koordinator. Programmiert und installiert nicht selbst.
- **Koordinator (Sonnet, /loop, in Zed):** heißt nach jedem Zed-Neustart anders. Den Namen findet man mit ListAgents, zuletzt `freesynergy-e2`. Er startet Bau-Läufe (Sonnet), Reviews (Opus) und Recherchen (Haiku) über den API-Runner oder als Abo-Agenten. Er pusht, taggt und veröffentlicht erst nach Opus-JA und grüner CI.
- **API-Runner:** `/srv/FreeSynergy/.scratch/api-runner/` (`run.sh`, `prompts/`); das Kostenlog liegt in `.scratch/api-kosten.md`. API-Agenten arbeiten nur auf `unreviewed/*`-Branches und haben keine Secrets. `ant auth status` ist verboten.
- **Entwurf eines zustandslosen API-Koordinators:** `.scratch/api-runner/coordinator/`. Er wird erst gestartet, wenn das Arbeitsboard live ist, ein Trockenlauf gelaufen ist und Opus ihn geprüft hat.

## Budget-Plan (Nutzer, 2026-11-13)
- **API-Guthaben:** ≈ 160 $. Es muss **bis 6.12.** verbraucht sein. Bis Sonntag, 15.11., 18 Uhr nutzen wir die API kräftig (Abo bei 82 %).
- **Woche ab So 15.11., 18 Uhr: KEINE API, nur Abo, Vollgas.** Das Kontingent soll bis Mi/Do aufgebraucht sein. Dann setzt der Nutzer das Wochenkontingent zurück (einmal im Monat möglich), und wir arbeiten bis Sonntag weiter, wieder ohne API.
- **Woche danach:** Fable für ein gründliches Audit des ganzen Projekts (Plan siehe unten), Kontingent bis Mitte der Woche.
- **Rest-API:** in den Tagen bis 6.12.

## Stand der Programme (GitHub, Katalog)
- Veröffentlicht und im Katalog:
  - fs-store 0.0.14 (Frontends Craft, kompakt);
  - fs-tasks 0.0.7 (Frontends Board, Liste);
  - fs-wiki 0.0.8;
  - fs-files 0.0.10;
  - fs-people 0.0.3, fs-calendar 0.0.2, fs-maps 0.0.2.
- Bausteine und Werkzeuge: fs-components v0.0.13, fs-interfaces v0.0.19 (v0.0.20 sammelt sich auf einem Branch), fs-release v0.0.1.
- Neue Repos ohne Code (ADR 0076): fs-workflows, fs-marketplace, fs-text, fs-data, fs-draw, fs-paint.
- **Befund aus dem echten Test des Nutzers (13.11.):**
  - Store-Bug: Facetten-Links zeigten auf alte tar-Installationen (Tasks und People von Hand korrigiert).
  - Wiki: Das normale Fenster ist das erzeugte Admin-Fenster, Pfade müssen getippt werden, das Wiki ist unbenutzbar.
  - Files zeigt nur die eigene Ablage, ist also noch kein Dateimanager.
  - Store: Neu-laden unzuverlässig, Symbol schlecht erkennbar, doppelte Bestätigung, Meldungen bleiben stehen, „Start“ und „Programme“ verwirrend, Icons fehlen.
- **Läuft gerade:**
  - store-015 (Links, verify);
  - wiki-009 (normaler Start zeigt das Frontend; vor dem Push „Gesicht“ in „Frontend“ umbenennen);
  - tasks-008b (Arbeitsboard: Fenster als Client, live);
  - die Dossiers Wiki und Files: fertig, sollen in die Doku gepusht werden.
- **Danach:**
  - B4 Store a–e und B5 Icons (Nutzer-JA, `program-icons-final` 2ba0551) mit Katalog schema 2;
  - B1 Datei-Wähler (FileChooser-Portal);
  - Wiki-Bau entlang `workflows.md`;
  - B3 Files mit lokalem Dateisystem;
  - Total Commander als eigenes Frontend-Modul;
  - Lifts people → calendar → maps → groups.

## Regeln, die sich gerade gebildet haben (Details im Memory)
- Es heißt **„Frontend“**, nie „Gesicht“. Ansichtsarten sind keine Frontends.
- **Kein Frontend ohne Dossier:** Zustände, Menüs, Dialoge, Kürzel, **Arbeitsabläufe**. Abgenommen wird durch Durchklicken der Abläufe, nicht per Bild.
- Vorbilder sind **bezahlte** Produkte. Theme-Namen auf Englisch, mit fairer Anlehnung in der Beschreibung. Admin-Frontends sind an SAP Fiori angelehnt.
- Jede Planung beginnt mit der Prüffrage „wessen Daten?“: Programm, Facette oder Suite (ADR 0076).
- Bugs in veröffentlichten Programmen gehen vor. Der Nutzer soll sie ohne Sorge melden.
- Tokens sparen heißt effektiver arbeiten: Wiederverwendung (Schichten, ADR 0074), Workflows und das Arbeitsboard.

## Offene Nutzerfragen / Termine
- ~19.11.: Text für ArtCraft/VectorCraft vorbereiten (Memory `project-artcraft-outreach`).
- ~24.11.: Präsentation für Anthropic vorbereiten (Claude for Open Source, Bewerbung ~26.11.).
- SignPath: Nutzer-JA. Zuerst ein unsignierter Windows-Installer als Release, dann die Policy-Seite, dann bewirbt sich der Nutzer.
- Hetzner node1: der Nutzer meldet sich, wenn er im Rescue-System ist.
