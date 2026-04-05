# Activity Hub

[← Zurück zum Index](../INDEX.md)

---

## Grundidee

Klassische Desktops fragen: "Welches Programm willst du öffnen?"
Der Activity Hub fragt: "**Was willst du tun?**"

Statt Programme zu verwalten, verwaltet der Mensch **Absichten (Activities)**.
Das passende Programm im Hintergrund ist eine Implementierungsdetail.

---

## Was ist eine Activity?

Eine Activity ist eine Kategorie von Tätigkeiten, nicht ein konkretes Programm.

Beispiele:
- "Wiki" — Information nachschlagen oder bearbeiten (Outline, Wiki.js, ...)
- "Code" — Quellcode lesen oder schreiben (Forgejo, Editor, ...)
- "Chat" — Kommunikation (Tuwunel/Matrix, ...)
- "Office" — Bürodokumente (Write, Tabelle, Präsentation)

---

## Nesting: Activities in Activities

Activities können beliebig tief geschachtelt werden:

```
Office (Activity)
├── Write        (Activity → z.B. OnlyOffice Writer)
├── Tabelle      (Activity → z.B. OnlyOffice Calc)
└── Präsentation (Activity → z.B. OnlyOffice Impress)
```

"Office" ist selbst eine Activity mit eigenem Icon und eigenen Aktionen.
Die Unter-Activities erben die Kategorie des Parents.

---

## Activity-Views

Jede Activity bietet folgende Einsprungpunkte:

| View | Beschreibung |
|------|-------------|
| **Neu** | Neues Dokument / Datei / Eintrag / Termin erstellen |
| **Zuletzt bearbeitet** | Die N zuletzt bearbeiteten Elemente anzeigen |
| **Programme** | 2. Ebene: welches konkrete Programm nutzen? |

"Programme" erlaubt die explizite Programm-Auswahl wenn man sie braucht —
aber normalerweise ist das Standard-Programm voreingestellt.

---

## Standard-Programm + Start-View

Pro Activity konfigurierbar:
- **Standard-Programm:** welches Programm für "Neu" / "Öffnen" genutzt wird
- **Start-View:** mit welcher View die Activity standardmäßig öffnet

Diese Einstellung ist pro Programm und pro Activity individuell.

---

## ActivityEngine-Trait

Ein Programm bietet Activities an, indem es den `ActivityEngine`-Trait implementiert
(via Adapter):

```rust
pub trait ActivityEngine: Send + Sync {
    fn activity_id(&self) -> &str;
    fn activity_name_key(&self) -> &str;
    fn supported_actions(&self) -> Vec<ActivityAction>;
    fn default_view(&self) -> ProgramView;
    fn category(&self) -> ActivityCategory;
}
```

**ActivityAction:** New | Open | Recent | Browse | Custom(String)

**ActivityCategory:** Document | Communication | Media | Data | Code | System | Custom(String)

---

## Activity als eigenständiges Programm

Eine Activity kann verschieden implementiert sein:

| Art | Beschreibung |
|-----|-------------|
| **Eingebettet** | Kein eigener Container, Adapter läuft im Host-Prozess |
| **Container + Adapter** | Eigener Container, Adapter implementiert ActivityEngine |
| **Mit GUI** | Eigene GUI via FsView-Trait (optional) |
| **Im Store** | Als `program`-Paket mit `ActivityEngine`-Capability veröffentlicht |

Der Activity Hub fragt nur den Trait — die Implementierung dahinter ist egal.

---

## ActivityHub Registry

```
ActivityHub
├── register(activity: Activity) — Activity anmelden
├── by_category(cat) -> Vec<Activity> — nach Kategorie filtern
├── search(query) -> Vec<Activity> — Volltextsuche
└── installed_only() -> Vec<Activity> — nur was in fs-inventory ist
```

Nur installierte Activities werden angezeigt (fs-inventory gRPC).
Der Store kann weitere Activities anbieten (dann: "installieren" Hinweis).

---

## Im Store

Activities sind Store-Artifacts:
- Im Store als `program`-Paket mit Capability `activity.engine.<id>`
- Adapter wird automatisch mitinstalliert
- Adapter registriert Capability in fs-registry
- Activity Hub liest fs-registry → weiß was verfügbar ist

---

## Beziehung zum Program-Modell

Activities sind **unabhängig** von Programmen, aber verbunden:

```
InstalledResource (fs-inventory)
  └── ProgramGroup (mehrere Instanzen)
        └── caption: "Wiki.js — helfe.org"

Activity "Wiki"
  └── engine: WikiJsActivityEngine (Adapter)
        └── wraps: WikiJsAdapter
              └── connected to: InstalledResource "wikijs"
```

Ein Programm kann mehrere Activities anbieten.
Eine Activity kann von mehreren Programmen angeboten werden (Auswahl in "Programme"-View).
