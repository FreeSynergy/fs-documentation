# OpenBoard - Beschreibung

## Was das Programm macht

OpenBoard ist das digitale Tafelwerkzeug für Unterricht und Meetings: Vollbildseiten, auf denen man mit Stift/Finger schreibt, Medien einbettet und presentiert — komplett lokal und quelloffen (GPL).

## Vorteile

- **kostenlos, offline, datensouverän** (Schulen/Behörden)
- **Sofortbild-Logik**: Seiten wie Tafelabschnitte, kein Ordner-Denken nötig
- **Unterrichtswerkzeuge** (Geo, Timer, Browser) integriert

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Xournal++** | Notiz-Annotation über PDF; OpenBoard ist Präsentations-/Klassen-Tafel |
| **Miro/Mural** | Team-SaaS; OpenBoard Einzelplatz lokal |
| **MyPaint** | Malprogramm, kein Tafel-/Präsentationskonzept |

## Technische Details

- **Stack**: C++, Qt (Multitouch), Linux-first; Windows/macOS-Builds
- **Speicherung**: Bibliothek unter `~/OpenBoard`, Dokumente als `.obz` (ZIP mit SVG-Seiten + Metadaten)
- **Lizenz**: GPL

## Für wen geeignet

- Lehrende/Vortragende mit interaktiven Whiteboards oder Stylus
- FreeSynergy-Skins für **seitenbasierte Tafel-UIs** (Seite/Element/Stift-Modell)
