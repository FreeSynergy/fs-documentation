# Pakete

[← Zurück zum Index](../INDEX.md) | [Store](../programme/store/README.md) | [Rollen](rollen.md)

---

## Paket-Lifecycle

```
Browse im Store
  → Installieren (Download + Validierung + in DB registrieren)
    → Konfigurieren
      → Nutzen
        → Update (neue Version aus Store)
          → Deinstallieren (Frage: "Daten behalten?")
```

## Versionierung

Jedes Paket hat SemVer + Git-Tag. Dadurch:
- Updates erkennbar
- Rollback auf ältere Version möglich
- Changelog abrufbar (aus Git-Commit-Messages)
- Wenn eine Version entfernt wird, bleibt sie über den Tag erreichbar

## Pflicht-Metadaten

Jedes Paket MUSS haben:
- `id` (einzigartiger Name, KEIN Typ-Prefix)
- `name` (Anzeigename)
- `version` (SemVer, aus Git-Tag)
- `type` (container, language, theme, widget, bot, bridge, task)
- `description` (Kurzbeschreibung)
- `tags` (für Suche — muss aussagekräftig sein)
- `icon` (SVG oder Icon-Name; wenn fehlt → generisches Icon für den Typ)

## Variable-System (für Container-Pakete)

Variablen haben Basis-Typen und Rollen. Siehe [Conductor](../programme/conductor/README.md) für die Analyse und [Rollen](rollen.md) für die Hierarchie.

Secrets (`secret`, `password`, `api-key`) werden mit `age` verschlüsselt gespeichert.
Rollen-typisierte Variablen (z.B. `iam.oidc-discovery-url`) werden automatisch befüllt wenn ein passender Service installiert ist.

---

Weiter: [Conductor](../programme/conductor/README.md) | [Rollen](rollen.md)
