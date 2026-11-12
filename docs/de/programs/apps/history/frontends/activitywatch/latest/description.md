# ActivityWatch latest — Beschreibung

## Überblick
Eine Open-Source-Sammlung, die die Computernutzung automatisch erfasst und die Daten unter deiner Kontrolle hält.

## Was es tut
- Watcher beobachten: Tastatur- und Mausaktivität (standardmäßig nach 3 Minuten als abwesend), Titel des aktiven Fensters und Anwendung, Browser-Tab (Titel, URL, hörbar, Inkognito).
- Ein lokaler Server speichert Ereignisse in Buckets.
- Eine Weboberfläche und ein Tray-Symbol zeigen und filtern die Daten; Kategorien mit Regeln.
- Export, Pausieren, Filtern.

## Für wen es passt
Menschen, die einen automatischen, privaten Verlauf davon wollen, wie ihre Zeit verging.

## Abgrenzung
### ActivityWatch vs. Day One
Automatisch und technisch gegenüber schriftlich und persönlich. Exist.io holt Daten aus vielen Diensten und findet Zusammenhänge; ActivityWatch bleibt auf dem Rechner.

## Technische Details
Lokaler Server, Standardport 5600, nur auf localhost lauschend. Zwei Server-Implementierungen existieren (Python und Rust). Fenster-Watcher: Windows, macOS, Linux (nur X11). Browser-Erweiterung: Chrome, Edge, Firefox. Lizenzname: Open.
