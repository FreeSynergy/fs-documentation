# Rechte-System (Rechte-Kaskade)

[← Zurück zum Index](../INDEX.md) | [Rollen](rollen.md) | [Föderation](foederation.md)

---

## Grundregel

**Rechte können in jeder Weitergabe nur gleich bleiben oder abnehmen — NIEMALS zunehmen.**

Wenn ein Projekt der Föderation `read` und `write` gibt, kann die Föderation davon nur `read` und `write` oder weniger weitergeben. Sie kann NIEMALS `execute` oder `search` hinzufügen, wenn das Projekt es nicht freigegeben hat.

## Rechte-Typen

| Recht | Bedeutung |
|---|---|
| `read` | Daten lesen/anzeigen |
| `write` | Daten erstellen/ändern |
| `execute` | Aktionen ausführen (Service starten, Bot-Command senden) |
| `search` | Daten durchsuchen (für die föderale Suche) |

## Kaskade-Beispiel

```
Projekt "Helfa Köln"
  Wiki: gibt frei → read, write, search
  Chat: gibt frei → read (nur lesen, nicht schreiben, nicht durchsuchen)
  Tasks: gibt frei → (nichts — bleibt privat)
    │
    ▼
Föderation "FreeSynergy Deutschland"
  Bekommt von Helfa Köln:
    Wiki: read, write, search (alles was freigegeben wurde)
    Chat: read (nur das was freigegeben wurde)
    Tasks: (nichts)
  
  Gibt weiter an nächste Föderation:
    Wiki: read, search (write WEGGENOMMEN)
    Chat: read (kann nicht mehr als read geben)
    Tasks: (nichts — kann nichts geben was es nicht hat)
      │
      ▼
Föderation "FreeSynergy Europa"
  Bekommt:
    Wiki: read, search
    Chat: read
  
  Kann weitergeben: Höchstens read, search für Wiki und read für Chat.
  Kann NIEMALS write oder execute hinzufügen.
```

## Standard: Alles ist PRIVAT

Alle Einstellungen sind standardmäßig **nicht öffentlich**. Es muss EXPLIZIT eine Öffnung gemacht werden.

Wenn jemand:
- Alle Daten freigibt → **Warnung** + Bestätigung
- Einen ganzen Host freigibt → **Warnung** + Bestätigung
- Die Rechte-Kaskade verletzt (mehr Rechte als das Original) → **Fehler**, wird blockiert

Jede Rechte-Änderung wird **protokolliert**: Wer hat was wann freigegeben?

```rust
pub struct RightsAuditEntry {
    pub timestamp: DateTime<Utc>,
    pub actor: UserId,            // Wer hat das gemacht?
    pub target: ResourceId,       // Was wurde geändert?
    pub old_rights: Vec<Right>,   // Vorher
    pub new_rights: Vec<Right>,   // Nachher
    pub federation_id: Option<FederationId>,
    pub reason: Option<String>,   // Optional: Warum?
}
```

## Einzelne Services können überschreiben

Ein Projekt kann sagen: "Standardmäßig gebe ich `read` für alles." Aber ein einzelner Service kann das überschreiben: "Mein Wiki ist `read + write + search`, aber mein Chat ist NICHTS."

```
Projekt-Standard: read
  ├── Wiki: read, write, search (überschrieben: MEHR als Standard)
  ├── Chat: (nichts) (überschrieben: WENIGER als Standard)
  ├── Tasks: read (Standard beibehalten)
  └── Git: read, search (überschrieben: mehr als Standard, aber weniger als Wiki)
```

---

Weiter: [Föderation](foederation.md) | [Bus](bus.md)
