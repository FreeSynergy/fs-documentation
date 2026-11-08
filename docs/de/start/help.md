# Wie du helfen kannst

FreeSynergy wird offen entwickelt, und wir stehen noch am Anfang. Frische Blicke helfen deshalb sehr. Du musst nicht programmieren.

## Lesen und sagen, wo du nicht zustimmst

Lies das [Manifest](../manifesto.md) und den [Gesamtplan](../programs/apps/roadmap.md). Wenn dir etwas falsch, unklar oder fehlend vorkommt, ist das für uns wertvoll zu wissen.

## Dinge ausprobieren und Probleme melden

Installiere den [Store](install.md) und ein Programm, und öffne ein **Issue** im Repository dieses Programms auf GitHub (<https://github.com/FreeSynergy>), wenn etwas unklar oder kaputt ist. Schreib, was du gemacht hast, was du erwartet hast und was passiert ist. Jedes Programm sagt ehrlich, was funktioniert und was nicht. Ein Fehler liegt vor, wenn ein Programm etwas zu können behauptet, es aber nicht kann.

## Prüfen

Jedes Repository hat eine `DESIGN.md` mit einer Zustandstabelle und einer Liste offener Punkte. Lies eine davon und sag uns, was nicht zusammenpasst. Wir hören es lieber jetzt.

## Bauen

Unser Stack ist Rust, zusammen mit einem rein in Rust geschriebenen Oberflächen-Toolkit (Blinc). Wähle ein Programm, lies seine `DESIGN.md` und fang mit etwas an, das dort als noch nicht gebaut aufgeführt ist. Die Regeln sind kurz und gelten für jede Änderung:

1. **Erst das Muster.** Wähle ein Entwurfsmuster aus den [Coding-Konventionen](https://github.com/FreeSynergy/fs-documentation/blob/main/conventions/coding.md) und begründe die Wahl in einem Satz. Passt keines, erfinde keines, sondern frag nach.
2. **Dann das Trait.** Schreib zuerst die Schnittstelle ohne Implementierung, passend zum Vertrag in `fs-interfaces`. Zwischen Programmen sprechen wir immer über [Schnittstellen](../interfaces/index.md), nie über den Kern eines anderen Programms.
3. **Dann Tests gegen das Trait,** und erst danach die Implementierung.
4. Sag offen, was fehlt: Was nicht gebaut ist, antwortet mit `Unsupported` und steht so in der `DESIGN.md`. Keine Dummys und keine Tests, die nur Dummys testen.

## Regeln, die nie gebeugt werden

- **Nichts wird kopiert.** Wir analysieren, was Programme funktional tun, und bauen es selbst. Wo ein offener Standard existiert, nutzen wir ihn; wo keiner existiert, schreiben wir einen.
- **Ein Standard, ein zuständiges Programm.** Kein zweites Modell derselben Sache.
- **Kostenlos für alle.** Keine Bezahlschranke, keine Premium-Stufe, keine Werbung.
- **Lizenz:** Alles ist `MIT OR Apache-2.0`.

## Diese Dokumentation verbessern

Jede Seite hat einen Bearbeiten-Knopf. Die Ausgangssprache ist Englisch (`docs/en/`), Deutsch wird daraus übersetzt. Öffne einen Pull Request im Repository [fs-documentation](https://github.com/FreeSynergy/fs-documentation). Die Entscheidungen hinter all dem sind öffentlich: [Entscheidungen](../decisions/index.md).
