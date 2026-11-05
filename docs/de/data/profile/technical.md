# Profil – Technische Erklärung

## Projektions-Pipeline (kein zweiter Datenspeicher)

```
JSContact-Card (contacts/)            AS2-Actor (Handle, publicKey)
        │                                      │
        └──────────► Feldgruppen-Regeln ◄──────┘
                          │
              Publikum A: öffentliche Ansicht
              Publikum B: Arbeits-Kontext
              Publikum C: Dating-Kontext
```

- **Gespeichert wird nur:** die Handle-Zeile (`id`-IRI ↔ Konto aus [login/](../login/index.md) ↔ `self_card_id`) und die **Regeln** (Feldgruppen → Publikum). Feldwerte selbst bleiben ausschließlich in der Card.
- Eine Projektion wird **bei Bedarf berechnet**, nicht dauerhaft abgelegt (sonst gäbe es Kopien mit Zerfallsdatum — gegen Beschluss 4).

## Feldgruppen und Zweckbindung (eigene Festlegung — noch nicht beschlossen, offen in [requirements.md §6.3](../requirements.md))

Vorschlag: jede Card-Feld-Referenz bekommt genau eine Feldgruppe:

| Feldgruppe | Beispiele | Standard-Publikum |
|------------|-----------|-------------------|
| `public` | `name` (Anzeigename), Avatar-`media` | alle |
| `work` | `organizations`, `titles`, Arbeits-E-Mail | Projekt-/Arbeits-Publikum |
| `private` | private E-Mail, Telefon, Postadresse | Kontakt-Publikum |
| `sensitive` | z. B. `personalInfo`-Anteile wie sexuelle Orientierung | **nur** explizit gewähltes Publikum (z. B. Dating-Kontext) |

**Regel (Dating-Beispiel):** die Arbeit-/Kalender-Projektion zieht `sensitive` **niemals** ein, auch nicht wenn das Publikum „alle Kollegen“ ist. Rechtlich berührt das besondere Kategorien personenbezogener Daten (DSGVO/BDSG) — ⚠️ einzelne Rechtsgrundlagen sind in dieser Doku **nicht belegt**; die Datenmodell-Regel steht davon unabhängig.

## Fluss

1. Handle anlegen: Actor-IRI nach Beschluss 3, verknüpft mit Konto und Card.
2. Person ändert Card → Projektionen ändern sich **sofort** (Single Source).
3. Person ändert **Regeln** → `Update` auf Actor-Regeln (Envelope).
4. Externe sehen nur die berechnete Ansicht; `publicKey` gehört in jede Ansicht (Andockpunkt für [identity/](../identity/index.md)).

## Offene technische Punkte

- Feldgruppen-Modell als eigene Festlegung beschließen (bisher offen)
- `bto`/`bcc`: AS2 behandelt sie als Offenlegung an Benannte — Durchsetzung pro Ressource bleibt separat (Beschluss 2)
- Mehrsprachige Profile (`nameMap`) — Mechanismus ✅, welche Felder übersetzbar sind, offen
