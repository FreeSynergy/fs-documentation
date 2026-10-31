# Shake - Attributs

## Attributs principaux

| Attribut | Type | Défaut | Description |
|----------|------|--------|-------------|
| `onShake` | function | - | Exécuté lors du Shake |
| `onShakeStart` | function | - | Exécuté au début du Shake |
| `onShakeEnd` | function | - | Exécuté à la fin du Shake |

## Attributs de retour d'information

| Attribut | Type | Description |
|----------|------|-------------|
| `shakeAnimation` | boolean | `true` | Afficher un retour shake/wiggle sur l'élément ? |
| `confirmBeforeAction` | boolean | `true` | Confirmer l'action avant son exécution ? |
| `hapticFeedback` | boolean | `true` | Vibration à la détection ? |
| `soundFeedback` | boolean | `false` | Son à la détection ? |

## Attributs de seuil

| Attribut | Type | Défaut | Description |
|----------|------|--------|-------------|
| `shakeThreshold` | number | `15` | Accél. minimale (m/s²) ou mouvement en px |
| `minShakes` | number | `2` | Nombre minimal de changements de direction |
| `maxTime` | number | `1000` | Fenêtre de temps pour le Shake en ms |
| `cooldown` | number | `1000` | Pause après le Shake en ms (empêche le double déclenchement) |

## Attributs de direction

| Attribut | Type | Description |
|----------|------|-------------|
| `axis` | string | `x` \| `y` \| `xy` — axe du mouvement |
| `requireAxis` | boolean | `true` | Axe requis ? |

## Accessibilité

| Attribut | Type | Description |
|----------|------|-------------|
| `aria-label` | string | Texte descriptif |
| `role` | string | Rôle ARIA : `application` |
| `alternativeAction` | function | Action équivalente via bouton/clavier |
| `respectReducedMotion` | boolean | `true` | Désactiver le retour avec `prefers-reduced-motion` ? |
