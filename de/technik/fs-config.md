# fs-config

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

`fs-config` ist der TOML-Konfigurations-Loader für FreeSynergy — eine reine Library, kein Daemon.
Sie lädt und speichert TOML-Konfigurationsdateien mit Validierung und Auto-Repair.

---

## Architektur

```
ConfigLoader        ← Repository Pattern: lädt/speichert TOML-Dateien
ConfigValidator     ← Validierungsregeln (ConfigSchema)
ConfigAutoRepair    ← Auto-Repair bei ungültigen Werten (RepairOutcome)
FeatureFlags        ← Feature-Flags als JSON (enable/disable/is_enabled)
```

---

## API

| Typ/Funktion                      | Beschreibung                                           |
|-----------------------------------|--------------------------------------------------------|
| `ConfigLoader::new(base_dir)`     | Loader mit Basis-Verzeichnis initialisieren            |
| `loader.load<T>(path)`            | TOML laden + validieren → `(T, Option<RepairOutcome>)` |
| `loader.save<T>(path, value)`     | TOML speichern                                         |
| `loader.read_raw(path)`           | Roher TOML-String laden                                |
| `loader.write_raw(path, content)` | Rohen String schreiben                                 |
| `parse_str<T>(content)`           | TOML-String deserialisieren                            |
| `load_toml<T>(path)`              | Direktes Laden ohne Loader-Objekt                      |
| `save_toml<T>(path, value)`       | Direktes Speichern ohne Loader-Objekt                  |
| `FeatureFlags::load_json(path)`   | Feature-Flags aus JSON laden                           |
| `FeatureFlags::is_enabled(key)`   | Feature-Flag prüfen                                    |

---

## Validierung + Auto-Repair

`ConfigSchema` definiert erlaubte Werte, Typen und Standardwerte.
Bei ungültigen Werten greift `ConfigAutoRepair` ein und gibt ein `RepairOutcome`
mit einer Liste der vorgenommenen Korrekturen zurück.

---

## Repo

- Lokal: `/home/kal/Server/fs-config/`
- GitHub: `git@github.com:FreeSynergy/fs-config.git`

---

Weiter: [← Index](../INDEX.md)
