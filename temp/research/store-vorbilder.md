# Empfehlung: Store-Frontend (fs-store) nach Vorbildern

Stand: 2026-11-11. Grundlage: `BEFUND.md` (Haiku) + Stichproben (WebFetch, s. u.) + ADR 0068 (`origin/main`).

## 0. Stichproben der Quellen

| Quelle | Ergebnis |
|---|---|
| flathub.org/en/apps/org.gnome.Calculator | Bestätigt: „Changes in version 51.1“ + relative Zeit, „2 MiB Download“, „Low Risk“, 1 Bildschirmfoto, Altersfreigabe 3+, Links (Website, Hilfe, Übersetzen, Fehler melden, Quellcode, Manifest). Auf dieser Seite **kein** Verifiziert-Häkchen (Calculator ist nicht verifiziert), Lizenz wurde im Abruf nicht gefunden. |
| docs.flathub.org/blog/app-safety-… | Bestätigt: Clients zeigen statische Rechte + Wirkung, OARS-Freigabe, Warnung bei veralteter Runtime, Release Notes je Version, **Hinweis bei Rechte-Zunahme** zwischen Versionen. |
| docs.flathub.org/docs/for-users/verification | Bestätigt: blaues Häkchen = Besitz der App-ID per Token nachgewiesen. Also Herkunftsnachweis, keine Code-Prüfung. |
| github.com/storytold/craft-launcher (README) | Bestätigt: Raster **und** sortierbare Tabelle (Status, installierte/neueste Version, Datum), Tray/Menüleiste, SHA-256 gegen `SHA256SUMS.txt`, MIT OR Apache-2.0. **Nicht bestätigt:** `.asc`-Signaturprüfung – das README nennt nur SHA-256. Befund-Zeile „`.asc` in Releases“ bleibt unbelegt. |

**Korrektur zum Befund:** „Fähigkeiten nach ADR 0068“ sind **provides / requires / recommends von Themen-Schnittstellen** (z. B. `people.persons 1.2`), keine Sandbox-Berechtigungen. Flathub-Rechte und unsere Fähigkeiten sind zwei verschiedene Blöcke. Das Muster „Zunahme zwischen Versionen anzeigen“ passt trotzdem auf beide.

## 1. Antworten auf die Frageliste

1. **Fähigkeiten auf Karte oder Seite?** Karte: nur Zustandssymbol der Auflösung (✔ alles erfüllt / ⚠ fehlt etwas / ⇄ Auswahl nötig). Seite: volle Liste provides/requires/recommends mit aufgelöstem Anbieter. Änderungen gegenüber installierter Version hervorheben (Flathub-Muster).
2. **Bildschirmfotos:** Der Macher liefert sie (AppStream `<screenshots>` bzw. Repo-Ordner); wir spiegeln sie wie Pakete nach Lizenzprüfung (ADR 0068 §2). Bei eigenen Paketen Pflicht: mind. 1, empfohlen 3. Bei fremden: 0 erlaubt, dann Hinweis „keine Bilder vom Macher“. Nie aus Vorbildern.
3. **Release Notes:** Quelle der Wahrheit ist `fs-catalog` (Feld je Version, AppStream `<releases>`). Beim Spiegeln wird der Upstream-Release-Text übernommen und dort abgelegt; der Store liest nur den Katalog (offline, signiert via TUF).
4. **Signatur-Anzeige:** Drei klar unterschiedene Stufen als Abzeichen: (a) **Macher-signiert + von uns gespiegelt** (beide Schlüssel geprüft), (b) **nur von uns signiert** (Macher ohne Signatur, Prüfsumme aus Upstream übernommen), (c) **nur Prüfsumme** – nur für lokale/Test-Quellen, mit Warnfarbe. Auf der Seite: Schlüssel-Fingerprint (gekürzt, aufklappbar), Prüfzeitpunkt, Quellcode-Datei-Link.
5. **Altersfreigabe:** Nicht als Pflicht. Optionales Feld (OARS übernehmen, wenn der Macher es liefert). Kein eigener Prozess.
6. **Datenschutz-Label:** Ja, aber schlank und später: Feld „Speicherort der Daten“ (lokal / eigener Server / Dritte) + „sendet nach außen an …“. Für eine föderierte Suite wichtiger als Altersfreigabe. Erst ab Runde nach 3b.
7. **Bewertungen:** Nein. Keine Sterne, keine Zähler. Höchstens später Organisations-interne Notizen.
8. **Logo:** Icon ist Pflichtfeld im Katalog (SVG, sonst PNG ≥ 128 px, AppStream `<icon>`). Buchstaben-Platzhalter nur bei fehlendem Icon und dann sichtbar als „Icon fehlt“ in der Quellen-Ansicht.
9. **Größe:** Aus dem Katalog (Download-Größe ist in TUF-Targets ohnehin bekannt). Installierte Größe optional im Katalog, sonst nach Installation gemessen und lokal angezeigt.
10. **Layout:** Siehe Varianten unten. Empfehlung: **Variante B (Launcher-artig) jetzt**, Detailseite aus Variante A übernehmen; A als Ausbaustufe, wenn der Katalog viele Arten/Pakete hat.
11. **Offene ADR-0068-Prüfung (Kanidm/Zentinel/Stalwart):** Eigener Haiku-Auftrag, unabhängig vom Frontend; Ergebnis füllt Abzeichen-Stufe (a) vs. (b).

## 2. Gemeinsame Paketseite (Pflichtinhalt, alle Varianten)

```
[Icon]  Name                      [Installieren | Öffnen | Aktualisieren | Entfernen]
        Art · Macher · Lizenz     Abzeichen: Signatur-Stufe a/b/c
----------------------------------------------------------------------------
Version   installiert 1.2.0 · angeboten 1.3.0 · 2026-11-03
Größe     Download 14 MiB · installiert ~40 MiB
Herkunft  Macher-Quelle (Link) → gespiegelt von FreeSynergy am …
          Signatur: Macher-Schlüssel ABCD…  ✔  · Katalog-Schlüssel (TUF) ✔
          Quellcode dieser Version: Datei (Link)
Fähigk.   bietet:   people.persons 1.2, groups
          braucht:  identity.oidc ≥1.0  → erfüllt durch Kanidm  ✔
          empfiehlt: mail.smtp          → fehlt  [Anbieter wählen]
          NEU in 1.3.0: braucht zusätzlich  files.storage   (hervorgehoben)
Bilder    [Foto 1] [Foto 2] [Foto 3]   (gespiegelt, Lizenz: …)
Änderungen  1.3.0 – … (aufklappbar: ältere Versionen)
Links     Website · Hilfe · Fehler melden · Quellcode
Beschreibung (Text; später Wiki-Block, siehe Merkposten)
```

## 3. Drei Frontend-Varianten

### Variante A – Katalog-artig (Flathub / Discover)

```
+-----------+-----------------------------------------------+
| Suche     |  Empfohlen (Band, 3 große Kacheln mit Foto)   |
| --------- |-----------------------------------------------|
| Entdecken |  Kategorie „Identität“   [mehr →]             |
| Programme |  [Kachel][Kachel][Kachel][Kachel]             |
| Frontends |  Kategorie „Kommunikation“                    |
| Server    |  [Kachel][Kachel][Kachel][Kachel]             |
| Themes    |                                               |
| Icons     |                                               |
| --------- |                                               |
| Installiert (3) / Updates (2) / Quellen                   |
+-----------+-----------------------------------------------+
Kachel: Icon, Name, 1 Satz, Abzeichen (Signatur, Fähigkeiten-Zustand)
Paketseite: zweispaltig (links Bilder+Beschreibung+Änderungen,
            rechts Kasten Version/Größe/Herkunft/Fähigkeiten/Links)
```
- **Stärken:** skaliert auf viele Pakete und alle Arten; vertraut für Desktop-Nutzer; Bilder kommen zur Geltung.
- **Schwächen:** braucht Kuratierung (Empfohlen, Kategorien) und gute Bilder, sonst wirkt es leer; meiste Arbeit.
- **Zusätzliche Katalogfelder:** `categories[]`, `featured` (+ Banner-Bild), `screenshots[]` mit Bildunterschrift + Lizenz, `summary` (1 Satz) getrennt von `description`, `kind` (programm/frontend/server/theme/iconset).
- **Aufwand:** hoch – ca. 3–4 Agenten-Runden (Navigation + Startseite + Kategorien + Paketseite + Bildspiegel/Cache).

### Variante B – Launcher-artig (ArtCraft) – **empfohlen für jetzt**

```
+---------------------------------------------------------------+
| FreeSynergy.Store   [Suche.............]  [Raster|Tabelle] ⟳ ⚙ |
| Filter: Alle · Installiert · Updates (2) · Art ▾ · Quelle ▾    |
|---------------------------------------------------------------|
| Raster:  [Icon Name  v1.3 · 03.11.  ✔sig ✔fäh  [Öffnen] ]      |
|          [Icon Name  v0.9 · 28.10.  ⚠fäh       [Install]]      |
| Tabelle: Icon | Name | Art | installiert | neu | Datum | Größe | Sig | Fäh | Aktion |
|---------------------------------------------------------------|
| Fußzeile: Jobs (Phasen-Fortschritt) · „Alle aktualisieren“    |
+---------------------------------------------------------------+
Klick auf Zeile/Karte → Paketseite als Seitenleiste rechts (eine Spalte),
breit genug: als eigene Seite mit Zurück.
Tray-Symbol (später): Updates-Zähler, Schnellstart.
```
- **Stärken:** nah am heutigen Code (Karten, Phasen, Update-all, Quellen bleiben); Tabelle zeigt Version/Größe/Signatur auf einen Blick – genau „mehr Infos je Paket“; funktioniert auch ohne Bilder.
- **Schwächen:** wenig Entdecken/Kuratierung; bei sehr vielen Paketen braucht es Filter.
- **Zusätzliche Katalogfelder:** `released_at` je Version, `download_size`, `installed_size` (opt.), `icon`, `signature_level` (abgeleitet: a/b/c), `upstream_key_fpr`, `mirror_key_fpr`, `source_archive`, `releases[]` mit Text, `provides/requires/recommends` (ADR 0068).
- **Aufwand:** mittel – ca. 1–2 Agenten-Runden (Tabellenansicht + Paketseite + Abzeichen; Datenfelder im Katalog parallel).

### Variante C – Kompakt-einfach (Liste + Detail)

```
+----------------------+--------------------------------------+
| [Suche......]        |  Paketseite (siehe §2), eine Spalte   |
| ● Kanidm      1.4 ✔  |                                      |
| ○ Stalwart    0.11 ⚠ |                                      |
| ● fs-people   1.2 ↑  |                                      |
| ...                  |                                      |
+----------------------+--------------------------------------+
● installiert  ○ nicht installiert  ↑ Update  ⚠ Fähigkeit fehlt
```
- **Stärken:** am schnellsten, gut für Admin/Server-Kontext und schmale Fenster; dient als Gegenprobe-Frontend (Frontend-Tausch als Querprüfung).
- **Schwächen:** wirkt nüchtern; keine Bilder in der Übersicht; Entdecken fehlt.
- **Zusätzliche Katalogfelder:** nur die Pflichtfelder der Paketseite (wie B, ohne Datum in der Liste).
- **Aufwand:** niedrig – ca. 1 Agenten-Runde, wenn Variante B die Datenfelder schon bringt.

## 4. Empfehlung in Kürze

- Jetzt **B** bauen, Paketseite nach §2; **C** als zweites, schlankes Frontend auf derselben Engine (Gegenprobe). **A** erst, wenn Kategorien, Bilder und mehrere Arten im Katalog stehen.
- Reihenfolge: zuerst Katalogfelder (Icon, Größe, Datum, Releases, Signatur-Herkunft, Fähigkeiten), dann Darstellung – das Problem ist die Datenlage, nicht der Ablauf.
- Keine Bewertungen, Altersfreigabe optional, Datenschutz-Feld später.

## 5. Merkposten (nicht entworfen)

- Beschreibungstexte werden später **Wiki-Blöcke** statt Freitext.
- Der Store bietet später **alle Arten** an (Programme, Frontends, Server, Themes, Icon-Sets) aus einer **signierten Eigenquelle** (`catalog.freesynergy.net`).

---
# Befund (Haiku-Recherche)

# Befund: Vorbilder für den Store / Installer (fs-store)

Stand: 2026-11-11. Nur gelesen und recherchiert; nichts installiert, nichts geklont, keine Desktop-Sitzung berührt.
Bilder: keine gespeichert, nur Quellen verlinkt. Geprüft wurden Primärseiten, wo möglich; Lücken sind markiert.

## Grundlagen aus dem Repo

- `fs-documentation`: die lokale Kopie ist gegenüber `origin/main` divergiert. Gelesen wurde `origin/main`:
  - `temp/research/craft-launcher.md` (Stand 2026-11-07, v0.16.0)
  - `conventions/decisions/0068-faehigkeiten-und-spiegel.md` (akzeptiert 2026-11-10, Bau nach Runde 3b). Sie verlangt Fähigkeiten (provides/requires/recommends), gespiegelte Pakete mit Upstream-Signatur und Quellcode, Herkunftsfelder im Katalog.
- Heutiger Store (`/srv/FreeSynergy/fs-store`, Code gelesen, nicht gestartet):
  - Karte (`crates/fs-store-app/src/model/cards.rs`, `struct Card`): Name, Art, Zustand, angebotene und installierte Version, **eine** Beschreibung (kann leer sein), eine Projektseite, „Neu“-Marke, Fortschritt in Phasen, Fehlertext, Buttons. Logo ist ein **Buchstabe auf farbigem Feld** (`Placeholder`).
  - Detailzeilen (`model/text.rs`, `detail_lines`): Art, Befehle, Ordner, Quelle. Keine Größe, keine Signatur, kein Lizenz-Feld, keine Berechtigungen, keine Bilder, keine Versionshistorie oder Release Notes.
  - Bedienung: Hover, Klick zeigt Beschreibung, Deinstallation mit Rückfrage, „Update all“, Quellen-Ansicht.

## Vergleichstabelle

Legende: ✔ gezeigt, ~ teilweise, ✘ nicht gezeigt, ? nicht verifiziert.

| Kriterium | fs-store heute | ArtCraft Launcher | KDE Discover | GNOME Software | Microsoft Store | Mac App Store | Flathub (Web) |
|---|---|---|---|---|---|---|---|
| Startseite / Kategorien | Kartenraster, Suche, „Neu“-Marke; keine Kuratierung | Raster oder sortierbare Tabelle; Tray/Menüleiste | Kategorien, Sidebar | Kategorien, Empfohlen | Kuratiert, Kategorien | Kuratiert (Heute, Spiele …) | Kategorien, Trends, verifizierte Apps |
| Logo / Bild | Buchstabe auf Farbfeld | App-Icon | Icon | Icon | Icon | Icon | Icon |
| Version | installiert + angeboten | installiert + neueste + Datum | Versionsliste mit Datum | ✔ | ✔ | ✔ | ✔ (Datum) |
| Größe | ✘ | ✘ | ✘ | ✔ (Download) | ✔? | ✔? | ✔ (Download, z. B. 2 MiB) |
| Herkunft / Quelle | Quellenliste, Befehl/Ordner | GitHub-Releases (Git-Quelle geplant) | Quellen oben rechts, „Standard machen“ | Quelle, Repo | Store (Publisher) | Entwickler | Entwickler, Repo-Links, Manifest |
| Signatur / Verifikation | ✘ (Signatur nur im Installer) | SHA-256 gegen Release geprüft; `.asc` in Releases | ✘ | ✘ auf Seite; Verifiziert-Abzeichen Flathub | Store-Prüfung (allgemein) | Notarisierung (allgemein, ?) | **blaues Häkchen** „Verified“ (Token-Nachweis) |
| Lizenz | ✘ | MIT OR Apache-2.0 (Projekt) | ✔ (GPL-2.0+) | ? | ? | ? | ✘ auf Seite |
| Berechtigungen / Fähigkeiten | ✘ | ✘ (nur Installationshinweise) | ✔ Flatpak-Berechtigungen (nur Flatpak), unten auf Seite; Plasma 6.5: eigene Seite zum Freigeben | ~ Flatpak-Berechtigungen, Risikobewertung (Flathub-Richtlinie) | ✘? (Manifest-Fähigkeiten, nicht verifiziert) | ✘ (nur Datenschutz-Label) | ✔ statische Berechtigungen + Sicherheitsbewertung („Low Risk“) |
| Bildschirmfotos | ✘ | ✘ (2 im README) | ✔ (1 auf Kachel, Demo) | ✔ | ✔ | ✔ | ✔ (1 auf Calculator) |
| Änderungen / Release Notes | ✘ | ✔ GitHub-Release-Text („What's Changed“) | ✘ auf Seite (nur Versionen); Changelog im Projekt | ✔ | ✔ „What's new“ (Feld, 1500 Zeichen bei Spielen) | ✔ „What's New“ (?) | ✔ „Changes in version …“ |
| Altersfreigabe | ✘ | ✘ | ✘ | ✔ (IARC/OARS) | ✔ IARC (Pflicht) | ✔ | ✔ (3+) |
| Datenschutz | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ App Privacy (Datenarten, Tracking) | ✘ |
| Bewertungen / Reviews | ✘ | ✘ | ✘ (Hinweis, keine Zahlen) | ✔ (Bewertungen) | ✔ (Durchschnitt, letzte Bewertungen) | ✔ | ✘ auf Seite (Downloads/Monat ✔) |
| Entwickler / Kontakt | ✘ | Projekt, Marken-Hinweis | ✔ Forum, Bugs | ✔ | ✔ | ✔ | ✔ Website, Hilfe, Bug, Übersetzung |
| Installieren-Fluss | Button je Karte, Phasen | Install/Open, Prüfung, pro Plattform | Install, Quellen wählen | Install | Get/Install | Get/Install | Install (Manuell möglich) |
| Fortschritt | Phasen-Text je Job | ? | Balken | Balken | Balken | Balken | ? |
| Aktualisieren | „Update all“, Prüfintervall | Prüfung, „Update and restart“ (eigener Launcher) | Updates-Seite | Updates-Seite | Updates | Updates | über Flatpak |
| Entfernen | Rückfrage, dann Entfernen | ✘ (nicht beschrieben) | ✔ | ✔ | ✔ | ✔ | ✔ |
| Suche / Filter | Suche, Sortierung ? | Sortierbare Tabelle | Suche, Filter | Suche, Filter | Suche, Filter | Suche | Suche, Filter |
| Rückroll bei Fehler | ✔ (Design, ADR 0051-nah) | ✘ (nicht gefunden) | ✘ | ✘ | ✘ | ✘ | ✘ |

### Quellen je Vorbild

- **ArtCraft Launcher:** https://github.com/storytold/craft-launcher (README, Kopfkommentare, gelesen 2026-11-07); Release-Seite https://github.com/storytold/craft-launcher/releases/latest (Stand: v0.19.0 „Latest“, Datum „11 Nov“, Jahr nicht sichtbar). Hinweis: Die Analyse vom 2026-11-07 nennt v0.16.0 – inzwischen neuer.
- **KDE Discover:** https://apps.kde.org/discover (Listing); https://userbase.kde.org/Discover (Doku); https://docs.fedoraproject.org/ro/kde/appinstallation/ (Berechtigungen, Quellen); https://www.neowin.net/amp/kde-plasma-65-brings-a-better-way-to-handle-app-permissions/ (Plasma 6.5, Sekundärquelle); https://discuss.kde.org/t/discover-doesnt-tell-users-about-itself-no-homepage-or-who-makes-this-link-in-the-app/48380 (Kritik „kein Entwickler-Link“).
- **GNOME Software:** https://docs.flathub.org/blog/app-safety-layered-approach-source-to-user (was Stores zeigen sollen); https://gitlab.gnome.org/GNOME/gnome-software/issues/504 („Berechtigungen vor Installation zeigen“, älter). Layout selbst nicht primär geprüft.
- **Microsoft Store:** https://learn.microsoft.com/en-us/gaming/game-publishing/concepts/store-listing (Feld „What's new in this version“, früher „Release notes“, 1500 Zeichen; Spiele-Spezifika); https://learn.microsoft.com/en-us/windows/apps/publish/store-policies (Altersfreigabe, Pflicht). Listing-Seite einer Standard-App nicht direkt geprüft (Primärseite 404).
- **Mac App Store:** https://developer.apple.com/support/app-privacy-on-the-app-store (App-Privacy-Label: Datenarten, verknüpft, Tracking; Privacy Policy). In-App-Kauf-Hinweis und Ähnliches: Suchtreffer aus TechRadar und Apple-Supportseiten, nicht selbst geöffnet. „What's New“-Feld der Produktseite: nicht belegt (die Apple-Seite dazu handelt von Datenschutz-Pflichten).
- **Flathub:** https://flathub.org/en/apps/org.gnome.Calculator (Seitenaufbau, gelesen 2026-11-11); https://docs.flathub.org/blog/app-safety-layered-approach-source-to-user (Liste: statische Berechtigungen und Wirkung, Altersfreigabe, Runtime-Warnung, Release Notes, Berechtigungszunahme); https://docs.flathub.org/docs/for-users/verification (Verifiziert, blaues Häkchen).

## Fazit (10 Zeilen)

1. Der heutige Store zeigt je Paket fast nur Name, Version, einen Satz Beschreibung und Buttons. Das Logo ist ein Buchstabe auf Farbfeld, das wirkt schnell „Platzhalter“.
2. Flathub ist das stärkste Vorbild für Infos je Paket: Versionshistorie mit Änderungen, Größe, Risikoabzeichen, Verifiziert-Häkchen, Altersfreigabe, Links zu Website/Bugs/Quellcode.
3. Berechtigungen sind das Feld, das fs-store am meisten braucht: Die Flathub-Richtlinie (statische Rechte + Wirkung + Zunahme zwischen Versionen) passt zu unseren Fähigkeiten (ADR 0068) fast 1:1.
4. ArtCraft zeigt die Übernahme in unserem Umfeld: Version + Datum, Release-Text aus dem Release, SHA-256 und Signatur beim Installieren, Hinweis auf Gemeinschafts-Angebote.
5. KDE Discover zeigt Quellen sichtbar (oben rechts, Standard wählbar) und Berechtigungen als eigene Seite, aber ohne Entwickler-Info; das ist der Fehler, den wir vermeiden sollten.
6. GNOME Software und Mac App Store setzen auf Bilder, Bewertungen und Datenschutz-Angaben; Bilder fehlen bei uns ganz.
7. Der Fluss „Installieren/Aktualisieren/Entfernen“ mit Rückfrage und Fortschritt in Phasen ist bei uns schon ordentlich; das Problem ist die Darstellung, nicht der Ablauf.
8. Wunsch „deutlich mehr Infos je Paket“ lässt sich ohne neuen Ablauf umsetzen: je Paket eine Detailseite mit Blöcken Version/Größe/Herkunft/Signatur/Fähigkeiten/Fotos/Änderungen/Lizenz/Links.
9. Bewertungen sind für eine föderierte Suite schwer (Missbrauch, Datenschutz); zuerst weglassen oder später mit eigener Politik.
10. Bilder: nur verlinken oder mit freier Lizenz vom Macher spiegeln (ADR 0068 Spiegelpflicht gilt auch für Bilder); nie aus Vorbildern übernehmen.

## Frageliste für Opus

1. Sollen Berechtigungen/Fähigkeiten auf der Karte oder nur auf der Detailseite stehen? (Vorschlag: Symbol auf der Karte, volle Liste auf der Seite.)
2. Wer liefert Bildschirmfotos: Macher (Repo-Ordner), wir (Spiegel mit Lizenzprüfung), oder keine? Welche Mindestanzahl?
3. Release Notes: aus dem Quell-Repo-Release (GitHub), aus `fs-catalog` (Feld pro Version) oder beides?
4. Signatur-Anzeige: „geprüft mit Schlüssel X“ je Paket als Abzeichen? Wie unterscheiden wir Macher-Signatur, Spiegel-Signatur (unser Schlüssel) und Nur-Prüfsumme?
5. Altersfreigabe: brauchen wir sie überhaupt (Suite für Organisationen), oder reicht ein Hinweisfeld?
6. Datenschutz-Label (Mac-Vorbild): eigenes Feld „Datenarten/Speicherort“ im Katalog?
7. Bewertungen: gar nicht, oder nur Nutzungsmeldungen ohne Sterne?
8. Logo: Woher kommt das Icon im Katalog (Pflicht im Format)? Platzhalter nur bei fehlendem Icon, nicht als Standard?
9. Größe: Download-Größe aus dem Katalog oder bei Installation ermittelt?
10. Layout: Gitter wie ArtCraft oder Kachel mit Kategorien wie Discover/Flathub? Desktop-Hülle (Blinc) mit einer oder zwei Spalten für die Detailseite?
11. Wer prüft die noch offene Frage aus ADR 0068 („Welche Pakete bieten Kanidm, Zentinel, Stalwart selbst an, signiert, welche Formate, welche Lizenz“)? Diese Recherche war nicht Teil dieses Auftrags.

## Lücken und Vorbehalte

- Microsoft Store und Mac App Store: die Feldliste ist nur teilweise belegt (Spiel-Dokumentation und App-Privacy). Felder mit „?“ sind aus Erfahrung, nicht belegt.
- KDE Discover: Layout aus Listing-Seite und Doku; Discover-App selbst nicht gestartet.
- GNOME Software: kein aktueller Layout-Beleg; nur Flathub-Richtlinie und ältere GitLab-Issues.
- ArtCraft: Remove, Fortschritt und Suche sind im README nicht beschrieben; für ein genaues Bild wäre ein Lauf der Webversion nötig (nicht erlaubt in diesem Auftrag).
- Der heutige fs-store wurde nur am Code gelesen, nicht gestartet. Die Aussage „wirkt kindisch“ ist eine Hypothese (Buchstaben-Logo, eine Textzeile, keine Bilder), keine Nutzerprüfung.
- Lizenz-Hinweis: Screenshots von Vorbildern nicht gespeichert.
