# Fähigkeitenliste — Begriffsschicht, Ablauf, offene Punkte

Vorgearbeitet am 2026-11-03 als Antwort auf **P6** (§19). Der Nutzer hat entschieden:
**beides** — zentral dokumentiert **und** abfragbar (API, CLI, MCP). Dieses Blatt ist bewusst
**keine fertige Liste**: die Liste entsteht pro Kategorie aus `requirements.md` (ADR 0006).
Es hält fest, was eine Fähigkeit ist, wie sie gemeldet und geprüft wird, und was noch zu
entscheiden ist.

## Warum eine geschlossene Liste nötig ist

Ohne zentrale Liste kann das Register (§13) nicht auflösen („wer kann diesen Termin öffnen?“)
und der Masken-Prüfer nicht feststellen, dass eine Maske eine Fähigkeit **nicht** anbietet.
Eine freie Liste pro Programm macht beides unprüfbar. Die Liste ist der Nenner, auf dem sich
Maske und Programm treffen — die Brückenmitte (P4).

## Was eine Fähigkeit ist

Eine Fähigkeit ist **eine abgeschlossene Handlung am Objekt, ohne Hinweis auf eine Oberfläche**.

| ist eine Fähigkeit | ist keine Fähigkeit |
|--------------------|---------------------|
| `event.create` | „Menüpunkt Neu“ |
| `calendar.subscribe` | „Knopf in der Seitenleiste“ |
| `event.move` | „Drag & Drop“ (das ist ein Weg zur Fähigkeit, §12) |
| `object.address` | „Deep Link /objekt/{uid}“ (das ist die Adresse, nicht die Handlung) |

Der Test: **verschwindet die Handlung, wenn die Maske wechselt?** Nein → Fähigkeit.
Deshalb sind die vier Masken-Dateien eines Programms (`menu.md`, `shortcuts.md`,
Gesten, `structure.md`) **vier Abbildungen derselben Fähigkeitsmenge** (§9).

## Zwei Ebenen, ein Eintrag

1. **Domänenübergreifende Grundfähigkeiten** — dieselben in jeder Kategorie. Nach calendar
   sind das mindestens: `object.open`, `object.list`, `object.search`, `object.create`,
   `object.edit`, `object.move`, `object.delete`, `object.share`, `object.subscribe`,
   `object.export`, `object.import`, `object.address`.
2. **Kategorie-Fähigkeiten** — aus der Pflichtmenge der Kategorie, also aus
   `programs/<ebene>/<kategorie>/requirements.md` (calendar-Vorarbeit: 22 Nummern).

Die Grundfähigkeiten sind die **konstante Menge**, auf die sich jede Maske verlassen kann;
die Kategorie-Fähigkeiten wachsen mit den Kategorien.

## Wie sie gemeldet und geprüft wird (P6 + §18 Nr. 4)

- **Ein Dokument pro Programm:** `abilities.md` neben `menu.md`/`features.md`
  (Antwort auf §18 Nr. 9: eigene Datei, nicht neuer Zweig).
- **Zustand:** die Grundfähigkeiten sind **gesetzt**; der Kern ist **geschlossen**
  (Maske darf nur gemeldetes benutzen), Wachstum läuft über neue Einträge, nicht über freie
  Namen.
- **Abruf:** dieselbe Liste über **API** (Ressource am Programm), **CLI** und **MCP**.
  Standard versteht sich — die Liste ist Teil des Manifests (P5).
- **Wer meldet:** das **Programm**; die Maske fragt **beim Start** ab und merkt sie sich
  (Build-Time-Vertrag, §2; damit ist §18 Nr. 4 beantwortet).
- **Version:** nicht die Programmversion zählt, sondern die **Schnittstellenform** (§9).
  Geprüft wird ein **Bereich**, nicht Gleichheit: Maske braucht Form 2–4, Programm bietet 3 →
  passt. Gleichheit erzwingt Gleichschritt, und den wollen wir loswerden.
- **Prüfer** (zwei Werkzeuge, Muster `scripts/check_components.py`):
  - Programmprüfung: meldet es alle Grundfähigkeiten korrekt?
  - Maskenprüfung: benutzt sie nur Components und nur gemeldete Fähigkeiten?

## Offene Punkte (Rat gefragt)

1. **Form der Einträge.** Vorschlag: `<domaene>.<aktion>` lowercase (passt zu
   `data/konventionen.md`: Events sind `<resource>.<aktion>`), z. B. `event.create`.
   Alternative: zwei Spalten `domaene` + `aktion` in einer Tabelle. Eine Zeile Entscheidung.
2. **Bindung an Rechte.** Ist „teilen dürfen“ Teil der Fähigkeit oder eine zweite
   Antwort des Programms? Ohne Rechte-Modell (§8 Lücke, §18 Nr. 17) ist das nicht entscheidbar
   → Vorschlag: Fähigkeit meldet **Existenz**, Recht separat, beides im Manifest.
3. **Größe des Kerns.** Vorschlag: **keine harte Zahl**, sondern Regel: eine Fähigkeit kommt
   in den Grundkern, wenn sie in **mindestens zwei Kategorien** Pflichtmenge ist. Nach dem
   calendar-Durchlauf sind das die zwölf Grundfähigkeiten oben.
4. **Wo steht die Liste zentral?** Kandidaten: `data/faehigkeiten.md` (wie `felder.md`,
   Querschnitt) oder `programs/faehigkeiten.md`. Empfehlung `data/`, weil Fähigkeiten an
   Modellen hängen und die Modelle dort stehen.

## Siehe auch

- `temp/architektur-protokoll.md` §9 (Fähigkeiten statt Attribute), §13 (Register, Prüfer),
  §18 Nr. 4 und 9, §19 P6
- `temp/ableitungen/calendar-requirements.md` (Pflichtmenge calendar, 22 Fähigkeiten)
- `docs/de/data/konventionen.md` (Namensregel `<resource>.<aktion>`)
- `conventions/decisions/0006` (Abbruchkriterium, Pflichtmenge)
