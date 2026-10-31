# Thunderbird - Structure & UI/UX

## Vue d'ensemble

Thunderbird a une UI classique et fonctionnelle avec barre d'activité, zone de navigation, zone de contenu et barre d'état, optimisée pour la communication par email.

## Structure de la fenêtre

### Zones principales

```
┌─────────────────────────────────────────────────────────────────┐
│  Barre de titre (Menu, Titre, Contrôles de fenêtre)             │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Bar. │   Navigation     │   Contenu        │   Barre latérale  │
│  Act. │   (Gauche)       │   (Centre)       │   (Droite)        │
│ (Int.)│  - Comptes       │  - Messages      │  - Aperçu        │
│       │  - Calendrier    │  - Rendez-vous   │  - Contacts       │
│       │  - Contacts      │  - Contacts      │  - Résultats de recherche │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Barre d'activité (Gauche)

La barre d'activité contient la navigation principale (intégrée dans la barre de navigation):

| Élément | Fonction |
|---------|----------|
| Comptes | Gestion des comptes |
|Boîte de réception | Dossiers email |
|Éléments envoyés | Messages envoyés |
| Brouillons | Brouillons |
| Corbeille | Éléments supprimés |
|Courrier indésirable | Dossier spam |
| Calendrier | Vue d'ensemble rendez-vous (Lightning) |
| Carnet d'adresses | Gestion des adresses (Lightning) |

### Navigation (Gauche)

Gauche dans la barre de navigation:

| Élément | Fonction |
|---------|----------|
| Boîtes mail | Dossiers email |
| Comptes | Gestion des comptes |
| Calendrier | Vue d'ensemble calendrier (Lightning) |
| Carnet d'adresses | Carnet d'adresses (Lightning) |
| Flux d'abonnement | Flux RSS/Atom |

### Zone de contenu (Centre)

La zone de contenu prend la plus grande partie de l'écran :

- **Liste boîte mail**: Boîte mail sélectionnée
- **Liste dossier**: Sous-dossiers
- **Liste éléments**: Messages/rendez-vous/contacts
- **Vue calendrier**: Vue mois/semaine (pour calendrier)

### Barre latérale (Droite)

Optionnellement à droite : Affichage des détails selon l'élément sélectionné

- **Fenêtre d'aperçu**: Contenu du message sélectionné
- **Aperçu rendez-vous**: Détails du rendez-vous sélectionné
- **Aperçu contact**: Détails du contact sélectionné
- **Résultats de recherche**: Résultats de recherche en direct

## UI/UX

### Principes de conception

- **Fonctionnel**: Fonction avant forme
- **Cohérent**: Design cohérent dans toutes les zones
- **Personnalisable**: Options de mise en page variées
- **Style Mozilla**: Suit les directives de conception Mozilla
- **Accessible**: Focus sur l'accessibilité

### Schéma de couleurs

- **Thème clair**: Schéma de couleurs clair classique
- **Thème sombre**: Schéma de couleurs sombre
- **Personnalisé**: Couleurs personnalisables via système de thème
- **Couleurs contextuelles**: Couleurs pour calendrier, catégories

### Typographie

- **Titres**: Hiérarchie claire
- **Texte**: Tailles de police lisibles (10-12pt)
- **Listes**: Listes à puces claires avec cases à cocher
- **Monospace**: Pour les en-têtes email

### Interactions

- **Effets hover**: Feedback visuel au survol
- **Feedback clic**: Feedback direct aux clics
- **Drag & Drop**: Pour déplacer emails, rendez-vous
- **Auto-sauvegarde**: Sauvegarde automatique des brouillons
- **Menus contextuels**: Clic droit pour actions contextuelles

### Design responsive

- **Bureau**: Fonctionnalités complètes avec barre latérale
- **Tablette**: Limité (application de bureau)
- **Mobile**: Application séparée (Thunderbird Mobile en développement)

## Structure de l'éditeur

### Éditeur email

```
┌─────────────────────────────────────────────────────────────────┐
│  Sujet                                                          │
├─────────────────────────────────────────────────────────────────┤
│  À : [Destinataire]                                             │
│  Cc : [Copie]                                                   │
│  Cci : [Copie cachée]                                           │
├─────────────────────────────────────────────────────────────────┤
│  Barre de formatage (menu)                                      │
├─────────────────────────────────────────────────────────────────┤
│  Zone de contenu (plein écran)                                  │
│                                                                 │
│  [Texte email]                                                  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Pièces jointes                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Éditeur calendrier (Lightning)

```
┌─────────────────────────────────────────────────────────────────┐
│  Sujet                                                          │
├─────────────────────────────────────────────────────────────────┤
│  De : [Date]     À : [Date]                                     │
│  Emplacement : [Emplacement]                                    │
│  Participants : [Participants]                                  │
├─────────────────────────────────────────────────────────────────┤
│  Description                                                    │
│                                                                 │
│  [Description rendez-vous]                                      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Options (Durée, Rappel, Couleur, etc.)                        │
└─────────────────────────────────────────────────────────────────┘
```

## Accessibilité

- **Navigation au clavier**: Contrôle complet via clavier
- **Support lecteur d'écran**: Attributs ARIA
- **Contraste**: Contraste élevé pour une meilleure lisibilité
-**Zoom**: UI évolutive (100-400%)
- **Accessibilité**: Paramètres d'accessibilité Mozilla

## Performance

- **Chargement rapide**: Ouverture rapide des messages
- **Mise en cache**: Mise en cache côté client
- **Pagination**: Pour les grandes listes
- **Debounce**: Pour les fonctions de recherche
- **Chargement paresseux**: Pour les grands calendriers et carnets d'adresses
