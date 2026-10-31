# Animations

Les animations décrivent la modification pilotée dans le temps des éléments (entrée, sortie, retour d'information, changement d'état).

## Vue d'ensemble

| # | Animation | Groupe | Description |
|---|-----------|--------|-------------|
| 1 | **Fade In** | Entrée | L'élément apparaît progressivement (opacité 0 → 1) |
| 2 | **Fade Out** | Sortie | L'élément disparaît progressivement (opacité 1 → 0) |
| 3 | **Slide In** | Entrée | L'élément glisse depuis l'extérieur (gauche/droite/haut/bas) |
| 4 | **Slide Out** | Sortie | L'élément glisse vers l'extérieur |
| 5 | **Zoom In** | Entrée | L'élément passe de petit à pleine taille |
| 6 | **Zoom Out** | Sortie | L'élément passe de pleine taille à zéro |
| 7 | **Bounce In** | Entrée | L'élément rebondit en arrivant |
| 8 | **Bounce Out** | Sortie | L'élément rebondit avant de disparaître |
| 9 | **Flip** | Changement d'état | L'élément tourne de 180° (recto/verso) |
| 10 | **Rotate** | Changement d'état | L'élément tourne sur son propre axe |
| 11 | **Spin** | Endless | Rotation permanente (loader, activité) |
| 12 | **Scale In** | Entrée | L'élément grandit de 0 % à 100 % |
| 13 | **Scale Out** | Sortie | L'élément rétrécit de 100 % à 0 % |
| 14 | **Collapse** | Sortie | Hauteur/largeur réduite à 0 (accordéon fermé) |
| 15 | **Expand** | Entrée | Hauteur/largeur croît de 0 jusqu'au contenu (accordéon ouvert) |
| 16 | **Unfold** | Entrée | L'élément se déplie comme une feuille |
| 17 | **Shake** | Retour d'information | L'élément tremble brièvement à l'horizontale (erreur) |
| 18 | **Wiggle** | Retour d'information | L'élément tremblote légèrement (mode édition) |
| 19 | **Pulse** | Endless | Enflure/atténuation cyclique (attention) |
| 20 | **Heartbeat** | Endless | Double pulsation au rythme d'une fréquence cardiaque |
| 21 | **Ripple** | Retour d'information | Une onde se propage depuis le point de clic |
| 22 | **Highlight** | Retour d'information | Le fond s'illumine brièvement (emplacements trouvés) |
| 23 | **Glow** | Endless | Halo lumineux autour du contour (sélection, statut en direct) |
| 24 | **Progress** | Endless | Indicateur de progression (barre, cercle, squelette) |
| 25 | **Skeleton** | Endless | Scintillement de substitution pendant le chargement |
| 26 | **Typing** | Endless | Indicateur de frappe (trois points dans les chats) |
| 27 | **Elastic** | Retour d'information | L'élément dépasse la position finale en rebondissant |
| 28 | **Rubber Band** | Retour d'information | Un tirage excessif revient en rebondissant (over-scroll) |
| 29 | **Morph** | Changement d'état | La forme se transforme en douceur en une autre forme |
| 30 | **Cross Fade** | Changement d'état | Deux éléments se fondent l'un dans l'autre |
| 31 | **Parallax** | Mouvement | Des niveaux bougent à des vitesses différentes |
| 32 | **Stagger** | Organisation | Les éléments enfants démarrent décalés les uns après les autres |

## Groupes

### Entrée (Enter)

Fade In, Slide In, Zoom In, Scale In, Bounce In, Expand, Unfold

### Sortie (Exit)

Fade Out, Slide Out, Zoom Out, Scale Out, Bounce Out, Collapse

### Retour d'information (Interaction)

Shake, Wiggle, Ripple, Highlight, Elastic, Rubber Band

### Endless (Loop)

Spin, Pulse, Heartbeat, Glow, Progress, Skeleton, Typing, Parallax

### Changement d'état (Transition)

Flip, Rotate, Morph, Cross Fade

### Organisation

Stagger

## Les animations comme répertoire

Chaque animation possède son propre répertoire selon le modèle `animations/<name>/` :

| Fichier | Contenu |
|---------|---------|
| `description.md` | Qu'est-ce que l'animation ? À quoi sert-elle ? Quand l'utiliser ? |
| `attributes.md` | Attributs/options (durée, timing, amplitude, callbacks) |
| `appearance.md` | À quoi ressemble-elle ? Déroulé ASCII, variantes, durée |

## Attributs standard (pour toutes les animations)

| Attribut | Type | Défaut | Description |
|----------|------|--------|-------------|
| `animation` | string | `none` | Nom de l'animation |
| `duration` | number | `300` | Durée en ms |
| `timingFunction` | string | `ease` | `linear`, `ease-in`, `ease-out`, `ease-in-out`, `cubic-bezier(...)` |
| `delay` | number | `0` | Délai avant le démarrage en ms |
| `iterationCount` | number \| `infinite` | `1` | Nombre de répétitions |
| `direction` | string | `normal` | `normal`, `reverse`, `alternate`, `alternate-reverse` |
| `fillMode` | string | `none` | `none`, `forwards`, `backwards`, `both` |
| `playState` | string | `running` | `running`, `paused` |
| `onAnimateStart` | function | - | Exécuté au démarrage |
| `onAnimateEnd` | function | - | Exécuté à la fin |

## Configuration (globale)

| Attribut | Type | Description |
|----------|------|-------------|
| `animationsEnabled` | boolean | Activer les animations globalement ? |
| `defaultDuration` | number | Durée par défaut pour toutes les animations |
| `respectReducedMotion` | boolean | Respecter `prefers-reduced-motion` ? |
| `staggerStep` | number | Décalage entre éléments enfants en ms |

## Durées indicatives

| Domaine | Durée | Utilisation |
|---------|-------|-------------|
| Micro | 100–200ms | Survol, retour du tap |
| Standard | 200–400ms | Fenêtres, menus, listes |
| Attention | 400–800ms | Intégration (onboarding), highlights |
| Boucle | 800–2000ms | Loaders, pulse, skeleton |

## Accessibilité

- `prefers-reduced-motion: reduce` → réduire les animations à 0 ms ou à un fondu
- Mettre en pause les animations endless lorsque l'élément n'est pas visible
- Ne jamais utiliser les animations de couleur comme seule information (toujours ajouter icône/texte)

## Voir aussi

- [Gestes](../gestures/index.md) — Shake, Wiggle comme retour aux gestes
- [Données standardisées](../data/index.md) — champs comme `animation`, `duration` dans les attributs des composants
