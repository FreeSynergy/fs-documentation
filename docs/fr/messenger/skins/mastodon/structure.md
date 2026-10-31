# Mastodon - Structure & UI/UX

## Vue d'ensemble

Mastodon a une UI moderne et claire avec barre d'activité, zone de navigation, zone de contenu et barre d'état, optimisée pour le microblogging.

## Structure de la fenêtre

### Zones principales

```
┌─────────────────────────────────────────────────────────────────┐
│  Barre de titre (Menu, Titre, Contrôles de fenêtre)             │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Bar. │   Navigation     │   Contenu        │   Barre latérale  │
│  Act. │   (Gauche)       │   (Centre)       │   (Droite)        │
│ (Int.)│  - Ligne de temps│  - Toots         │  - Utilisateurs   │
│       │  - Toots         │  - Ligne de temps│  - Notifications  │
│       │  - Profil        │                  │  - Profil         │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Barre d'activité (Gauche)

La barre d'activité contient la navigation principale (intégrée dans la barre de navigation):

| Élément | Fonction |
|---------|----------|
| Ligne de temps | Vue d'ensemble ligne de temps |
| Toots | Champ de saisie toot |
| Profil | Profil personnel |
| Notifications | Notifications |
| Messages directs | Messages directs |

### Navigation (Gauche)

Gauche dans la barre de navigation:

| Élément | Fonction |
|---------|----------|
| Maison | Ligne de temps maison |
| Local | Ligne de temps locale |
| Fédéré | Ligne de temps fédérée |
| Hashtags | Ligne de temps hashtag |
| Profil | Profil personnel |
| Notifications | Notifications |
| Messages directs | Messages directs |

### Zone de contenu (Centre)

La zone de contenu prend la plus grande partie de l'écran :

- **Vue d'ensemble ligne de temps**: Sélection ligne de temps (Maison, Local, Fédéré)
- **Liste toots**: Toots dans l'ordre chronologique
- **Champ de saisie toot**: Saisir toots

### Barre latérale (Droite)

Optionnellement à droite : Affichage des détails selon l'élément sélectionné

- **Profils utilisateur**: Informations profil
- **Notifications**: Liste des notifications
- **Profil**: Profil personnel
- **Recherche**: Rechercher dans la ligne de temps

## UI/UX

### Principes de conception

- **Minimal**: Design minimaliste avec focus sur le contenu
- **Clair**: Hiérarchie claire et navigation
- **Fonctionnel**: Fonction avant forme
- **Cohérent**: Design cohérent dans toutes les zones

### Schéma de couleurs

- **Thème clair**: Schéma de couleurs clair (par défaut)
- **Thème sombre**: Schéma de couleurs sombre
- **Personnalisé**: Couleurs personnalisables via système de thème
- **Couleurs contextuelles**: Couleurs pour le statut toot

### Typographie

- **Titres**: Hiérarchie claire
- **Texte**: Tailles de police lisibles (14-16pt)
- **Listes**: Listes à puces claires
- **Monospace**: Pour les blocs de code

### Interactions

- **Effets hover**: Feedback visuel au survol
- **Feedback clic**: Feedback direct aux clics
- **Drag & Drop**: Pour les téléchargements de médias
- **Auto-sauvegarde**: Sauvegarde automatique des brouillons
- **Aperçu en direct**: Aperçu en direct lors de la saisie des toots

### Design responsive

- **Bureau**: Fonctionnalités complètes avec barre latérale
- **Tablette**: Limité (application de bureau)
- **Mobile**: Applications mobiles séparées (iOS, Android)

## Structure de l'éditeur

### Éditeur toot

```
┌─────────────────────────────────────────────────────────────────┐
│  Nouveau toot                                                   │
├─────────────────────────────────────────────────────────────────┤
│  [Champ de saisie toot]                                         │
├─────────────────────────────────────────────────────────────────┤
│  Médias                                                         │
├─────────────────────────────────────────────────────────────────┤
│  [Sélectionner images/vidéos]                                   │
├─────────────────────────────────────────────────────────────────┤
│  Sensible                                                                       │
├─────────────────────────────────────────────────────────────────┤
│  [Case à cocher sensible]                                       │
├─────────────────────────────────────────────────────────────────┤
│  Visibilité                                                     │
├─────────────────────────────────────────────────────────────────┤
│  [Public/Non répertorié/Privé/Direct]                           │
├─────────────────────────────────────────────────────────────────┤
│  [Envoyer toot]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Vue ligne de temps

```
┌─────────────────────────────────────────────────────────────────┐
│  En-tête ligne de temps                                         │
├─────────────────────────────────────────────────────────────────┤
│  Maison  Local  Fédéré  Hashtags                               │
├─────────────────────────────────────────────────────────────────┤
│  Liste toots                                                    │
├─────────────────────────────────────────────────────────────────┤
│  [Toot]                                                         │
│  [Toot]                                                         │
│  [Toot]                                                         │
└─────────────────────────────────────────────────────────────────┘
```

## Accessibilité

- **Navigation au clavier**: Contrôle complet via clavier
- **Support lecteur d'écran**: Attributs ARIA
- **Contraste**: Contraste élevé pour une meilleure lisibilité
- **Zoom**: UI évolutive (100-400%)
- **Accessibilité**: Conformité WCAG

## Performance

- **Chargement rapide**: Ouverture rapide des toots
- **Mise en cache**: Mise en cache côté client
- **Pagination**: Pour les grandes listes
- **Debounce**: Pour les fonctions de recherche
- **Chargement paresseux**: Pour les grandes lignes de temps
