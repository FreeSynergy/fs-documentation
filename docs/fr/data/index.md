# Données standardisées

Les données standardisées décrivent dans quels **formats**, **modèles** et **champs** les programmes, composants et skins FreeSynergy échangent des informations.

## Pourquoi la standardisation ?

- **Interopérabilité**: Messenger, wiki, calendrier et tableaux de bord de bureau utilisent les mêmes noms de champs
- **Réutilisabilité**: les composants (`table`, `list-view`, `calendar-view`) fonctionnent avec n'importe quel modèle
- **Capacité de migration**: les données peuvent passer d'un programme à l'autre (export/import)
- **Prévisibilité**: les skins (`apps/<catégorie>/skins/<programme>/api.md`) décrivent le même style d'API
- **Automatisation**: les workflows et webhooks accèdent à des chemins stables

## Domaines de données

| Fichier | Contenu |
|---------|---------|
| `formate.md` | Formats d'échange (JSON, YAML, TOML, CSV, NDJSON, ICS, VCF, GeoJSON, …) |
| `modelle.md` | Modèles standard (User, Message, Document, Event, Task, Contact, …) |
| `felder.md` | Champs standard, types, enums, champs obligatoires |
| `konventionen.md` | Nommage, structures de fichiers, versionnement, validation, i18n |
| `api.md` | Motif CRUD unifié, pagination, filtres, format d'erreur, webhooks |

## Modèles standard (aperçu)

| Modèle | Description courte | Référence de catégorie |
|--------|--------------------|------------------------|
| **User** | Compte avec profil, rôles, statut | tous |
| **Team** | Organisation, groupe, espace de travail | tous |
| **Message** | Message de chat, de commentaire ou de mail | messenger |
| **Document** | Page, contribution, article avec blocs | wiki |
| **Block** | Élément de contenu dans un Document | components |
| **Event** | Rendez-vous avec début, fin, participants | kalender |
| **Task** | Tâche avec échéance et statut | projektmanagement |
| **Contact** | Personne avec coordonnées et organisation | kontakt, crm |
| **Location** | Lieu avec adresse et coordonnée GeoJSON | maps |
| **File** | Fichier avec emplacement, type, taille | tous |
| **Tag** | Mot-clé de catégorisation | tous |
| **Comment** | Commentaire rattaché à une ressource | tous |
| **Notification** | Notification à un User | tous |
| **Revision** | Version d'une ressource | wiki, components |
| **Integration** | Webhook, clé API, connecteur | workflows |

## Types de données

| Type | Écriture | Exemple |
|------|----------|---------|
| `string` | Texte dans `"..."` | `"Anna Weber"` |
| `number` | Entier ou nombre décimal | `42`, `19.99` |
| `boolean` | `true` / `false` | `true` |
| `datetime` | ISO 8601 | `"2026-10-31T06:00:00+01:00"` |
| `date` | `YYYY-MM-DD` | `"2026-10-31"` |
| `duration` | Durée ISO 8601 | `"PT30M"` |
| `enum` | liste de valeurs fixes | `"active"` |
| `array[]` | liste | `["tag-a", "tag-b"]` |
| `object` | objet imbriqué | `{ "city": "Berlin" }` |
| `reference` | ID vers un autre modèle | `"user_01H…" \| User` |
| `markdown` | Texte Markdown | `"**Important**"` |
| `null` | explicitement vide | `null` |

## Règles de base

1. **Les ID sont des chaînes opaques** — ne jamais les interpréter comme des numéros
2. **Les heures toujours avec un décalage de fuseau horaire** ou explicitement `allDay: true`
3. **Les valeurs vides sont `null`**, pas `""` (exception : champs texte obligatoires)
4. **Les enums sont en minuscules et au singulier** (`active`, pas `Active`)
5. **Les nouveaux champs sont additifs** — les champs existants ne sont jamais renommés
6. **Chaque ressource porte `id`, `createdAt`, `updatedAt`**

## Structure de répertoire

```
docs/fr/data/
├── index.md            (ce fichier)
├── formate.md          Formats d'échange
├── modelle.md          Modèles standard
├── felder.md           Champs standard et types
├── konventionen.md     Règles de nommage et de versionnement
└── api.md              motif API unifié
```

## Voir aussi

- [Gestes](../gestures/index.md) — données d'interaction (seuils, callbacks)
- [Animations](../animations/index.md) — attributs et durées d'animation
- [Wiki](../apps/wiki/index.md) — programme avec ses propres skins
- [Messenger](../apps/messenger/index.md) — programme avec ses propres skins
