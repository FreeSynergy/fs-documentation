# Profil – Beschreibung

**Was diese Domäne ist:** was man **von sich zeigen möchte** — die öffentlich sichtbare, **publikumsgesteuerte** Ansicht. Ein Profil ist nach Beschluss 1+2 **keine zweite Kopie der Personendaten**, sondern eine **Projektion** der JSContact-Card ([contacts/](../contacts/index.md)) in einen AS2-`Actor`/`Profile`-Rahmen.

**Was sie abdeckt:**

- den sozialen Handle: `id` (absoluter IRI, Beschluss 3), `name` (Anzeigename), `preferredUsername`, `publicKey`
- **Publikumsregeln**: welche Feld/Feldgruppe geht an welches Publikum (`to`/`cc`/`bto`/`bcc` als Offenlegungssteuerung — keine Zugriffskontrolle, Beschluss 2)
- **Zweckbindung sensibler Felder**: das Dating-Beispiel aus dem Gespräch — bei Dating kann es **gefährlich** werden, wenn die Sexualität im Arbeits-/Kalender-Kontext auftaucht. Sensible Felder gehören **nicht** automatisch in jede Projektion
- Folgen von Profilwechsel: `Update` auf Actor, `Follow` — beides Envelope-Vorgänge

**Abgrenzung:**

| Thema | Wo es liegt |
|-------|-------------|
| Die speicherechten Daten, aus denen das Profil projiziert wird | [contacts/](../contacts/index.md) |
| Der Login, der zum Konto gehört | [login/](../login/index.md) |
| Beglaubigungen, ob man dem Handle glauben darf | [identity/](../identity/index.md) |
| Follower-Beziehungen, ActivityPub-Zustellungsmechanik | Envelope (querschnittlich, keine Domäne) |

**Warum das eine eigene Domäne ist:** Die einzige echte Frage dieser Domäne ist **Sichtbarkeit** („welches Feld, für wen, zu welchem Zweck“). Diese Regeln gehören zentral definiert, damit nicht jede App selbst filtert.
