# Shake (secousse)

## Description

Un shake est un mouvement rapide de va-et-vient de l'appareil ou d'un élément. Le geste est généralement détecté par l'accéléromètre ; avec la souris/le pavé tactile, il est aussi détecté par un mouvement horizontal rapide du pointeur.

## Utilisation

- Annuler / rejeter (classique : « secouer pour annuler »)
- Signaler une erreur (secouer un champ de formulaire lorsque la saisie est invalide)
- Changer d'application (iOS : secouer pour « trouver une correspondance »)
- Remélanger le contenu / lancer des dés
- Débloquer des fonctions cachées (Easter Eggs)

## Durée

- Typique : 300–1000ms
- Au moins 2 changements de direction dans la fenêtre de temps

## Détection

| Méthode | Description |
|---------|-------------|
| **Accelerometer** | Le capteur mesure les changements d'accélération (mobile) |
| **Pointer Movement** | Mouvement X rapide à la souris/au doigt (bureau) |
| **Threshold** | L'écart par rapport à la moyenne doit être dépassé |

## Différence avec le Swipe

- **Swipe** : un seul mouvement dans une direction (distance > 50px)
- **Shake** : plusieurs mouvements de va-et-vient (les changements de direction comptent)

## Différence avec Wiggle (animation)

- **Shake (geste)** : l'utilisateur bouge l'appareil/l'élément
- **Wiggle (animation)** : l'élément bouge de lui-même comme retour d'information
