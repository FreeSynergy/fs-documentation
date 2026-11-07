# Funktionsanalyse: ArtCraft Launcher (storytold/craft-launcher)

Gelesen am 2026-11-07: README, Releases, Kopfkommentare von `crates/core` und `crates/native`. Nichts ausgeführt, nichts kopiert (ADR 0013).
Stand: v0.16.0 (2026-11-07), seit 2026-10-09, MIT OR Apache-2.0, Rust, „early alpha“, rund 5.000 Sterne, ein Release fast jeden Tag.

## Was es tut
- **Ein Ort** zum Installieren, Aktualisieren und Starten aller Apps einer Suite (17 eigene, eine aus der Gemeinschaft, als solche markiert).
- **Richtige Datei je System:** DMG, MSI, `.deb`, `.rpm`, Flatpak, AppImage, FreeBSD; nach `os-release` die Paketverwaltung der Distribution, mit Passwortabfrage über polkit, sonst Flatpak, sonst AppImage.
- **Installiert wie von Hand:** an den üblichen Orten; erkennt auch selbst installierte Apps.
- **Aktualisiert sich selbst:** „Update and restart“ im selben Format, in dem es installiert wurde; ersetzt nie ein laufendes Programm.
- **Prüfung:** gegen die SHA-256-Summen des Releases. Die Releases tragen zusätzlich `.asc`-Signaturen und einen Schlüssel.
- **Katalog:** fest im Programm, als Daten, „damit eine spätere Version ihn von einer API holen kann“. Quelle der Versionen: GitHub-Releases.
- **Bedienung:** Raster oder sortierbare Tabelle, Tray und Menüleiste, 13 Sprachen mit „Auto“ nach Systemsprache, Webversion als statische Seite mit demselben Katalog.
- **Aufbau:** `core` ohne Ein- und Ausgabe (Katalog, Versionen, Release-Auswertung, Plattformwahl, Status), getrennt von Desktop-Hülle und Web.

## Was wir übernehmen (als Idee)
- Kern ohne I/O, getrennt von der Oberfläche: passt zu unserer Engine/Frontend-Trennung.
- Installieren auf die Art des Systems, und schon Installiertes erkennen.
- Selbst-Update im selben Format, laufende Programme nie ersetzen.
- Gemeinschafts-Angebote sichtbar markieren.
- Webversion als statische Seite.

## Was wir anders machen müssen
- **Signatur statt nur Prüfsumme:** Eine SHA-256-Summe aus demselben Release schützt nicht, wenn jemand das Release austauscht. Wir prüfen die OpenPGP-Signatur gegen einen Schlüssel, dem der Launcher vertraut (ADR 0051).
- **Quellen über Git (ADR 0036), nicht über die GitHub-API:** eine Liste von Git-Servern; unserer fest drin, abschaltbar, nicht löschbar (Nutzer, 2026-11-07).
- **Mehr als Programme:** Frontends, Components, Themes, Medien.
- **Unsere Oberfläche** auf Blinc und `fs-components`, nicht egui.
- **Zurückdrehen,** wenn ein Update scheitert (in den gelesenen Teilen nicht gefunden).
