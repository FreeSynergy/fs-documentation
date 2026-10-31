# Gestes tactiles

Les gestes tactiles sont des méthodes d'interaction pour les appareils à écran tactile.

## Gestes

| Geste | Description | Utilisation |
|-------|-------------|-------------|
| **Tap** | Toucher bref | Clic de bouton, sélection d'élément |
| **Double Tap** | Deux touchers rapides | Zoom, ouverture |
| **Long Press** | Appui prolongé | Menu contextuel, marquage |
| **Swipe** | Glissement dans une direction | Navigation, changement |
| **Drag** | Glisser | Réordonner, faire défiler |
| **Pinch** | Rapprocher deux doigts | Zoom out |
| **Spread** | Écarter deux doigts | Zoom in |
| **Rotate** | Pivoter deux doigts | Rotation |
| **Shake** | Mouvement rapide de va-et-vient | Annuler, retour d'erreur, remélanger |

## Attributs des gestes

| Attribut | Type | Description |
|----------|------|-------------|
| `onTap` | function | Exécuté lors du Tap |
| `onDoubleTap` | function | Exécuté lors du Double Tap |
| `onLongPress` | function | Exécuté lors du Long Press |
| `onSwipe` | function | Exécuté lors du Swipe |
| `onDragStart` | function | Exécuté au début du Drag |
| `onDragEnd` | function | Exécuté à la fin du Drag |
| `onPinch` | function | Exécuté lors du Pinch |
| `onSpread` | function | Exécuté lors du Spread |
| `onRotate` | function | Exécuté lors du Rotate |
| `onShake` | function | Exécuté lors du Shake |

## Configuration

| Attribut | Type | Description |
|----------|------|-------------|
| `tapThreshold` | number | Limite de temps pour le Tap en ms |
| `longPressThreshold` | number | Limite de temps pour le Long Press en ms |
| `swipeThreshold` | number | Distance minimale pour le Swipe |
| `shakeThreshold` | number | Accélération/mouvement minimal pour le Shake |
| `minShakes` | number | Nombre minimal de changements de direction pour le Shake |
| `enabled` | boolean | Activer les gestes ? |

## Voir aussi

- [Shake](shake/description.md)
- [Animations](../animations/index.md)
