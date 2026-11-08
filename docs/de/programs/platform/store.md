# FreeSynergy.Store

**Ein Ort, um FreeSynergy zu bekommen, wobei jeder Download geprüft wird, bevor er deinen Rechner berührt.**

Der Store ist die App, aus der du alles Weitere installierst, aktualisierst und erweiterst: Programme, Frontends, Komponenten und Themes. Du installierst den Store einmal, von Hand ([so](../../start/install.md)), und danach musst du nichts mehr von Hand installieren. Er hält sich und alles Weitere auf dem neuesten Stand, rollt ein Update zurück, wenn es fehlschlägt, und ersetzt nie ein Programm, während es läuft.

Status: **Pre-release, früh.** Lies vor dem Ausprobieren unten den Abschnitt „Wo es heute steht“.

## Was hier anders ist

- **Signiert, oder gar nicht.** Jedes Paket muss eine gültige OpenPGP-Signatur von einem vertrauenswürdigen Schlüssel tragen, sonst kann es nicht installiert werden. Das ist keine Warnung, die man wegklicken kann: Im Code kann ein unsigniertes Paket dem Installer gar nicht übergeben werden. Eine Prüfsumme allein zählt nicht als Signatur.
- **Pakete liegen in Git** ([ADR 0062](../../decisions/0062-paket-repos-in-git.md)). Ein Katalog-Repository enthält die Liste der Apps im offenen AppStream-Format, mit signierten Metadaten nach der TUF-Spezifikation (The Update Framework). Jede Version eines Pakets ist ein Git-Tag mit den fertigen Paketen und ihren Signaturen. Der Store holt nur diesen einen Tag, nie die ganze Historie. Jeder Ort, der Git hosten kann, kann ein Spiegel sein; Vertrauen hängt an den Signaturen, nicht am Ort. HTTPS bleibt ein zweiter Weg, zum Beispiel GitHub-Releases.
- **Facetten sind Apps für sich** ([ADR 0061](../../decisions/0061-facetten.md)). Der Katalog listet jede Facette, etwa Contacts, als App mit eigenem Logo. Sie zu installieren, installiert das dahinterliegende Programm, hier People. Eine zweite Facette desselben Programms fügt nur deren Menüeintrag und Frontends hinzu.
- **Ein Programm, ein Befehl** ([ADR 0063](../../decisions/0063-ein-programm-ein-befehl.md)). Der Store ist der Befehl `fs-store`. Ohne Argumente öffnet er das Fenster. Mit Unterbefehlen funktioniert er wie `git`: `fs-store sources`, `fs-store available`, `fs-store install <package>`, `fs-store update`, `fs-store installed`. Jede Facette bekommt einen eigenen Befehl, einen Link zu ihrem Programm (`fs-contacts` für `fs-people`), den der Store bei der Installation anlegt.
- **Deine Quellenliste.** Pakete kommen aus einer Liste von Git-Quellen. Du kannst eigene hinzufügen. Die eingebaute FreeSynergy-Quelle kann abgeschaltet, aber nie entfernt werden, damit der Weg zurück immer offen bleibt.

## Wo es heute steht

- Pre-releases gibt es auf GitHub ([releases](https://github.com/FreeSynergy/fs-store/releases)); am 2026-11-08 ist `v0.1.0-rc.9` das neueste. Das erste (`v0.1.0-rc.1`) ist als „Do not use“ markiert: Es kann keine Pakete prüfen, die vom Release-Workflow signiert wurden.
- Der Kern funktioniert: die Quellenliste, das Lesen des Katalogs, die Signaturprüfung gegen den Projektschlüssel, die Installation aus einer `tar.gz` in deinen Home-Ordner, das Umschalten auf die neue Version in einem Schritt bei gleichzeitigem Behalten der alten sowie eine Prüfung, ob das Programm gerade läuft. Getestet wurde er mit einem echten signierten Paket von Tasks über einen lokalen Git-Katalog.
- Die Kommandozeile funktioniert für die oben genannten Unterbefehle. Das Fenster ist das Erste und vorläufig.
- Die Installation eines rpm über `dnf` und `pkexec` ist geschrieben, aber noch nicht echt ausgeführt worden (root-Rechte fragt das System ab, nie der Store).

## Was noch fehlt

- Der vollständige Katalog: [fs-catalog](https://github.com/FreeSynergy/fs-catalog) bietet bisher nur den Store, Tasks und People. Was von den TUF-Metadaten schon da ist, steht in der DESIGN.md des Stores.
- Das Ersetzen des laufenden Stores durch sich selbst.
- Facetten-Befehle (`fs-contacts` und Ähnliche): Das Format ist vorläufig und noch nicht gebaut.
- Windows und Prüfungen auf abgelaufene Schlüssel.
- Der Name und die Crate-Namen sind vorläufig.

## Teil von FreeSynergy

Der Store ist der Teil der [Plattform](../index.md), der alles Weitere auf deinen Rechner bringt. Die Statustabelle steht in der [DESIGN.md](https://github.com/FreeSynergy/fs-store/blob/main/DESIGN.md) des Repositorys.
