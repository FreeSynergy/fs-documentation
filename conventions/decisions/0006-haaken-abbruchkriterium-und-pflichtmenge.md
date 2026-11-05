# 0006 – Haken, Abbruchkriterium und Pflichtmenge pro Kategorie

Status: Punkt 2 und 3.4 **ersetzt durch 0013** (2026-11-05), Rest gilt

## Kontext
Der Abarbeitungsplan (`temp/apps-plan.md`) hat 869 Datei-Zeilen, davon 42 mit `[x]`, aber
520 Dateien liegen geschrieben ohne Haken. Ohne klare Bedeutung des Hakens ist nicht
entscheidbar, wie viel Restarbeit vorliegt (Faktor 10 Unterschied). Ohne Abbruchkriterium
ist die Schnittmenge aller Masken (= Pflichtmenge, CONVENTIONS/Protokoll §1) bei 119 Masken
nach wenigen Masken eingefroren — die restlichen Dateien wären dann das Ziel statt das Mittel.
Zentral ist der Grundsatz des Nutzers: die Skin-Doku ist ein **Spiegel** (wer macht was, wie,
wo ist das Problem), nicht ein Selbstzweck.

## Entscheidung
1. **Bedeutung der Markierung** im Plan:
   - `[x]` = **an Primärquellen verifiziert** (Quelltext-Tag, offizielle API-Referenz,
     offizielle Hilfeseite; Fundstellen in `index.md` der Maske).
   - `[~]` = Datei **vorhanden**, Inhalt **nicht** verifiziert (kann veraltet oder mit einem
     anderen Produkt vermischt sein).
   - `[ ]` = Datei fehlt.
   Der Haken ist kein Zähler geschriebener Dateien, sondern der Nachweis des Nachprüfens.
2. **Abbruchkriterium pro Kategorie:** mindestens **3, höchstens 5 Masken** vollständig
   verifizieren, dann die Schnittmenge als **Pflichtmenge einfrieren** und die
   Freeze-Zeile der Kategorie abhaken. Die übrigen Masken sind **Stichprobe**: abarbeiten,
   wenn sie eine Fähigkeit zeigen, die in `requirements.md` fehlt, sonst nicht.
3. **Reihenfolge pro Kategorie** (Brückenprinzip, von beiden Seiten bauen):
   1. Daten sammeln: was braucht die Kategorie (Masken-Doku lesen).
   2. **Standards suchen, die das Bild abbilden** — Muss, absolute Priorität.
   3. Crates suchen, die das Standards-Bild tragen.
   4. **3 Programme zum Nachbauen auswählen: 2 nicht-OSS, 1 OSS** (kann variieren). OSS gibt es
      schon reichlich; nachgebaut werden die Programme, die **Standards setzen und nicht offen
      für OSS sind**.
   5. Suiten und Plattformen vorher auf Apps **herunterrechnen** (stabile Basis); aus Apps wird
      der Baukasten nach oben zusammengesetzt.
4. **Ort der Pflichtmenge:** pro Programmkategorie eine Datei
   `programs/<ebene>/<kategorie>/requirements.md` — initially fast leer, später das, was
   unser Programm kann und braucht. Sie ist der Input für Fähigkeiten (§9) und Datenanschluss
   (§10) des Protokolls.
5. **Erste Anlaufstellen:** visuell **Blinc** (UI-Härtung), inhaltlich **Daten + Standards**,
   dann Crates; erst danach am Programm selbst arbeiten.

## Folgen
- `temp/apps-plan.md` trägt die Legende und pro Kategorie eine Freeze-Zeile; alle Pfade zeigen
  jetzt auf `programs/…` (vorher `apps/…`, nach dem Umzug ins Leere).
- Der Plan ist nicht mehr „869 Dateien abarbeiten“, sondern „17 Kategorien je 3–5 Masken
  verifizieren, dann einfrieren“. Geschätzte Restarbeit bis zur ersten Grundmaske:
  ~17 Kategorien × ~4 Masken × 7 Dateien ≈ 480 Dateien, davon 42 schon belegt.
- Neue Kategorien und neue Programme sind ausdrücklich vorgesehen (der Plan wächst).
- Vorgearbeitetes Muster einer abgeleiteten Liste: `temp/ableitungen/` (Plan-Ordner, kein `docs/`).
