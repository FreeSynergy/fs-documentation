# Glossar

Kurze Erklärungen zu den Wörtern, die wir verwenden. Hinter den Wörtern stehen Entscheidungen, die du unter [Entscheidungen](../decisions/index.md) nachlesen kannst.

**App.** Das, was Menschen sehen und installieren. Von außen heißt alles eine App, ob es ein Programm, eine Facette oder ein Frontend ist. „Facette" und „Programm" sind Begriffe für uns und für diese Dokumentation.

**Programm.** Die Engine für ein Thema: Personen, Aufgaben, Dateien, Nachrichten. Sie besitzt die Daten, die Regeln und einen offenen Standard. Beispiel: `fs-people`. Siehe [Programme](../programs/index.md).

**Facette (facet).** Ein Teil eines Programms, der wie eine eigene App aussieht, mit eigenem Namen, eigenem Logo und eigenem Menüeintrag, und mit einem festen Filter auf die Daten des Programms. Sie hat keine eigenen Daten. Beispiel: Kontakte und Benutzer sind Facetten von `fs-people`. Eine Facette ist das Gegenteil einer Suite. Jede Facette hat außerdem einen eigenen Befehl, zum Beispiel `fs-contacts` ([ADR 0061](../decisions/0061-facetten.md), [ADR 0063](../decisions/0063-ein-programm-ein-befehl.md)).

**Frontend.** Eine Art, ein Programm oder eine Facette anzuschauen: sehr einfach, klassisch, vertraut oder vollständig. Davon gibt es je Programm viele. Du kannst jederzeit wechseln, und deine Daten bleiben, wo sie sind.

**Admin-Frontend.** Das Frontend mit allen Einstellungen. Jedes Programm und jede Facette hat eines. Versteckt ein einfaches Frontend etwas, das du brauchst, kann das Admin-Frontend es immer richtigstellen.

**Component (Baustein).** Ein Stück Bildschirm, das etwas zeigt, ohne zu wissen, was die Daten bedeuten, etwa ein Kalenderraster oder ein Diagramm. Frontends sind aus Komponenten gebaut. Siehe [Komponenten](../components/index.md).

**Workbench.** Eine große Komponente, die einen ganzen Arbeitsbereich bildet, etwa einen Dateimanager.

**Suite.** Mehrere Programme, die für einen Zweck zusammengestellt sind, zum Beispiel Groupware, Projektmanagement oder CRM.

**Vertrag (Schnittstelle, interface).** Die vereinbarte Art, wie Programme miteinander sprechen, je eine pro Thema. Er ist ein Ziel und wächst nicht laufend weiter: Eine Änderung ist ein Sprung zu einer neuen Version. Siehe [Schnittstellen](../interfaces/index.md).

**Hub.** Das Programm, das dafür sorgt, dass sich die Programme auf einem Gerät finden, und das das Aktivitätsprotokoll führt.

**Store.** FreeSynergy.Store, die App, über die du alles andere installierst, aktualisierst und erweiterst. Siehe [den Store](../programs/platform/store.md).

**Katalog.** Die Liste der Pakete, die eine Quelle anbietet: Name, Logo, Beschreibung, Versionen und Facetten, im offenen AppStream-Format, mit Signaturen. Siehe [ADR 0062](../decisions/0062-paket-repos-in-git.md).

**Vorabversion (pre-release).** Eine erste Version zum Ausprobieren und Testen, offen veröffentlicht und ehrlich gekennzeichnet. Sie kann Fehler enthalten.
