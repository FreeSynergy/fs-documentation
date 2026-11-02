# Kontaktdaten – Beschreibung

**Was diese Domäne ist:** Kontakt-Datensätze über **Menschen, Organisationen, Gruppen und Geräte** — mit Erreichbarkeiten (E-Mail, Telefon, Messenger, Postadresse) und Namensinformationen. Kanonisches Modell: **JSContact** (RFC 9553, ✅).

**Was sie abdeckt:**

- Anlegen, Ändern, Patchen, Zusammenführen (`merge`) von Karten (`Card`)
- Namen mit Komponenten (nicht `firstName`/`lastName` — siehe [jscontact/beschreibung.md](jscontact/beschreibung.md))
- Organisationen und Rollen einer Person (`organizations`, `titles`)
- Erreichbarkeiten: `emails`, `phones`, `onlineServices`, `impp`, Scheduling-Adressen
- Postadressen als Teil der Card (Geometrien und Karten liegen in [geodata/](../geodata/index.md))
- Import/Export über vCard/jCard, Zugriff/Sync über CardDAV

**Abgrenzung zu anderen Domänen:**

| Domäne | Was dort liegt | Warum nicht hier |
|--------|----------------|------------------|
| [login/](../login/index.md) | Konto, Anmeldung, `sub`-Claim | Ein Login ist ein Zugang, kein Datenmodell |
| [profile/](../profile/index.md) | Was man **von sich zeigt** (Publikumssteuerung) | Profil ist eine **Projektion** der Card, keine zweite Kopie |
| [identity/](../identity/index.md) | Wem man **glaubt** (Beglaubigungen, Schlüssel) | Misstrauen kann eine Card nicht löschen |
| [events/](../events/index.md) | Teilnehmer **an Terminen** | Die Person ist hier verknüpft (`sendTo`/`email`), nicht gespeichert |
| [geodata/](../geodata/index.md) | Orte als Karten-Features | Die Postadresse **einer Person** gehört zur Card |

**Person vs. Kontakt (Beschluss-Kandidat 6, offen):** Der „Mensch, der sich anmeldet“ braucht nach unserem Vorschlag **kein eigenes `person/`-Verzeichnis**: die Person ist diejenige JSContact-`Card` (Rolle `individual`), die mit dem Konto aus [login/](../login/index.md) verknüpft ist. Alle Personen-Daten bleiben also in dieser Domäne. Siehe [anforderungen.md → 6.4](../anforderungen.md).

** Lifecycle-Lücke:** `lifecycle` (lead/prospect/customer/churned) existiert in keinem Standard (❌ belegt) → geplant als JSContact-`extensions`-Eintrag (⚠️ Mechanismus noch belegen). Siehe [standards.md](standards.md).
