# Documentation des skins Wiki

## Vue d'ensemble

Ce répertoire contient la documentation des menus et des éditeurs de divers systèmes de logiciels wiki et outils de développement.

## Documentation incluse

- [Wiki.js](/de/wiki/skins/wikijs/index.md) - Logiciel wiki moderne et léger
- [XWiki](/de/wiki/skins/xwiki/index.md) - Plateforme wiki d'entreprise
- [MediaWiki](/de/wiki/skins/mediawiki/index.md) - Le logiciel wiki le plus populaire (Wikipedia)
- [Tango.io](/de/wiki/skins/tango.io/index.md) - Plateforme de gestion des connaissances
- [Notion](/de/wiki/skins/notion/index.md) - Plateforme tout-en-un pour la collaboration
- [Confluence](/de/wiki/skins/confluence/index.md) - Wiki d'entreprise d'Atlassian
- [VSCodium](/de/wiki/skins/vscodium/index.md) - Éditeur de code open source (fork de VS Code)

## Structure de répertoire

```
docs/fr/wiki/skins/
├── index.md              (ce fichier)
├── wikijs/
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   └── structure.md
├── xwiki/
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   └── structure.md
├── mediawiki/
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   └── structure.md
├── tango.io/
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   └── structure.md
├── notion/
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   └── structure.md
├── confluence/
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   └── structure.md
└── vscodium/
    ├── menu.md
│   ├── features.md
│   ├── description.md
│   └── structure.md
```

## Contenu de chaque documentation

Chaque répertoire de projet contient quatre fichiers :

### menu.md
- Tous les menus principaux
- Menus contextuels
- Menus dépendants des droits utilisateurs

### features.md
- Fonctionnalités de l'éditeur
- Ce que l'éditeur peut faire
- Ce que l'éditeur NE PEUT PAS faire
- Extensions et plugins
- Raccourcis

### description.md
- Ce que fait le programme
- Avantages
- Différentiation par rapport à d'autres systèmes
- Détails techniques
- Pour qui le programme est-il adapté ?

### structure.md
- Structure de la fenêtre
- Design UI/UX
- Structure de l'éditeur
- Design responsive
- Accessibilité

## Notes

- Toute la documentation est rédigée en français
- Le contenu convient aux utilisateurs et aux administrateurs
- Les descriptions des éditeurs incluent la coloration syntaxique, les extraits, l'intégration Git et les extensions
- VSCodium est un fork open source de VS Code avec des fonctionnalités identiques mais sans la télémétrie Microsoft
