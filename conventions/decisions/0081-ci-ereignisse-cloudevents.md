# 0081 – CI-Ereignisse (CloudEvents) ≠ Programm-Ereignisse (AS2, fs-history)

Status: **akzeptiert** (Strategie, 2026-11-14) · baut auf ADR 0076 (Grundmodell), 0020 (AS2-Hülle), 0062 (Paketrepos, Katalog), 0068 (Pakete, Katalog) · berührt `fs-release` (Workflows), `fs-catalog` (bump, sign)

## Kontext
Das Wort „Ereignis“ meint heute zwei Dinge. ADR 0076 §1: Ereignis = „was tatsächlich passiert ist, unveränderlich“, AS2 Activity, Ort **fs-history**; ADR 0020 verlangt AS2 für Daten. Daneben brauchen die CI-Abläufe Steuersignale („Release veröffentlicht“, „Katalog geändert“, „Lauf rot“). Serverless Workflow 1.0 (Profil, ADR 0076 §1) kennt dafür `emit`, `listen` und `schedule.on`; die Spezifikation bevorzugt CloudEvents als Form. Kein ADR regelt CI-Ereignisse, `repository_dispatch` oder ein CI-Token (Stichwortsuche; Volltext nur der genannten Stellen gelesen). Ohne Festlegung würden beide Ebenen vermischt.

## Entscheidung
1. **Zwei getrennte Ebenen, keine Vermischung.**
   - **CI-/Workflow-Steuerungsereignisse** (Release veröffentlicht, Katalog geändert, Text veröffentlicht, Lauf rot) sind **CloudEvents**, `type` = `net.freesynergy.<gegenstand>.<ereignis>`. Pflichtfelder `id`, `source`, `specversion`, `type`; `source` = Repo-URL des Senders; `data` klein (Namen, Zahlen, Tags), nie Geheimnisse oder Befehle. Mapping auf Serverless Workflow 1.0: Senden = `emit`, Warten mitten im Ablauf = `listen`, Start = `schedule.on`.
   - **Programm-Ereignisse** (Handlungen und Zustände der Nutzer und Programme, der Verlauf) sind **AS2-Aktivitäten in fs-history** (ADR 0076, 0020). Dieser ADR regelt die CI-Ebene. Auf Programm-Ebene darf fs-workflows auf AS2-Aktivitäten reagieren (z. B. Aufgabe erledigt → nächster Schritt); die Brücke (Abbildung AS2 → Workflow-Start) regelt ein späterer ADR. CI-Ereignisse werden nie in fs-history geschrieben.
2. **Ereignisse sind Weckrufe, keine Freigaben.** Ein Ereignis startet nur Schritte, deren Gate erfüllt oder `none` ist; es setzt nie ein Gate außer Kraft. Gates, die **nie automatisch** laufen: Veröffentlichung, Tag, Pre-release, ADR-Push, Löschen.
3. **Kein Token: Pull.** Der 15-Minuten-Zeitplan von `bump.yml` bleibt. `bump` läuft automatisch als Folge eines veröffentlichten Releases (Gate `none`); die Freigabe (`opus-ja`, Bild-OK) liegt vorher beim Push/Tag. Die Katalog-Prüfung („wie ein Nutzer“: frischer Klon, Signatur) läuft im **selben `sign.yml`-Lauf**, weil ein Push mit `GITHUB_TOKEN` keinen weiteren Lauf startet.
4. **Rot-Meldung ohne Statusboard.** Ein wiederverwendbarer Workflow `_notify-red.yml` (in `fs-release`) öffnet je Repo ein Issue `rot: <Workflow> <Repo>` mit Label `rot` (kein Duplikat, schließt sich bei Grün; `issues: write` über `permissions`, kein PAT). Der Koordinator stellt **eine** Abfrage über die Organisation (`gh search issues --owner FreeSynergy --label rot --state open`).
5. **Grundsatz „Stille bei grün“:** Der Koordinator handelt nur bei Rot oder an Freigabe-Gates; Folgeschritte nach einer Freigabe (bump, sign, Prüfung, Paket-Repos, Doku-Bau) startet er nie von Hand.

## Folgen
- `fs-release`: Ereignis-Katalog (Tabelle der `type`-Werte mit Sender, Empfänger, `data`) im FS-Profil; `release-flow` bekommt einen `emit`-Schritt, `catalog-bump` ein `schedule.on`; `check_workflows.py` prüft Präfix, Sender/Empfänger je `type` und Geheimnisfreiheit. Heute führt niemand die YAMLs aus, sie werden nur geprüft.
- `sign.yml` bekommt den Prüfschritt; `_notify-red.yml` und der Schritt `rot-pruefen` in `coordination-round` entstehen als getrennte, später freigegebene Läufe.
- `verify` (Prüfschritt in `sign.yml`) ist **rot bei einem übersprungenen Tag**; das erzwingt „die neue Version steht im Katalog“. Ausnahme nur für ausdrücklich als Entwurf markierte Releases.
- Wartezeit Release → Katalog bleibt bis etwa 15 Minuten; GitHub kann Zeitplanläufe verzögern oder verwerfen und deaktiviert sie nach 60 Tagen ohne Aktivität, daher bleibt der Zeitplan ein Netz.

## Alternativen
- **Alles AS2:** verworfen, CI-Signale sind Steuerung, nicht Programmdaten; die SW-Spezifikation bevorzugt CloudEvents.
- **`repository_dispatch` aus Programm-Repos nach `fs-catalog`:** verworfen. Es verlangt fine-grained **Contents: write** auf `fs-catalog`; wer in einem Programm-Repo Code im Release-Lauf ausführt, könnte `packages.toml` fälschen, und `sign.yml` würde das signieren.
- **Falls später ein Token nötig wird:** `workflow_dispatch` auf `bump.yml` (vorhanden), Token fine-grained nur auf `fs-catalog`, **Actions: write**, Ablauf 90 Tage, vom Kontoinhaber angelegt; Restrisiko: Läufe starten/abbrechen, kein Code-Push, kein Schlüsselzugriff (Schlüssel nur in `sign.yml`). Der Empfänger vertraut dem Payload nie (Whitelist `packages.toml`, Tag `^v\d+\.\d+\.\d+$`).
- **Statusboard** (Sammel-Lauf über alle Repos): nicht jetzt; höchstens später als Netz für ausgefallene Zeitpläne.

## Offen
- **[nicht belegt]** `schedule.read` und gleichzeitiges `every` + `on` in Serverless Workflow 1.0.3 (gegen das Schema des Tags v1.0.3 prüfen; Fallback: zwei `document`-Dateien).
- **[nicht belegt]** `concurrency`-Verhalten bei zwei wartenden Läufen (Doppelläufe sind harmlos, `bump_catalog.py` ist idempotent).
- **[nicht belegt]** Mindestintervall von 5 Minuten für `schedule` (nicht per Zitat belegt).
- **[nicht belegt]** `gh search issues --owner … --label …` nicht ausgeführt; vor Gebrauch ein Probelauf.
- **[nicht belegt]** Wortlaut „GITHUB_TOKEN gilt nur im eigenen Repo“ nicht wörtlich aus der GitHub-Doku zitiert (`bump.yml` sagt es selbst).
