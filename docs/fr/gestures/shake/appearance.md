# Shake - Apparence

## Disposition de base

Un shake est un mouvement rapide de va-et-vient de l'appareil ou de l'élément.

## Retour visuel

```
┌─────────────────────────────────────────┐
│                                         │
│        ┌───┐                            │
│   ←──  │ □ │  ──→  ←──  ──→            │
│        └───┘                            │
│   Mouvement autour du point de départ   │
└─────────────────────────────────────────┘
```

## Options de retour

| Option | Description |
|--------|-------------|
| **Wiggle** | L'élément bascule légèrement de côté et d'autre |
| **Translate** | L'élément se déplace horizontalement |
| **Haptic** | Vibration sur les appareils mobiles |
| **Error Color** | Bordure teintée de rouge en cas de saisie invalide |
| **None** | Aucun retour, uniquement le callback |

## Amplitude

| Intensité | Déplacement | Utilisation |
|-----------|-------------|-------------|
| Légère | 2–4px | Confirmation |
| Moyenne | 5–10px | Retour standard |
| Forte | 10–20px | Erreur, avertissement |

## Durée

- Typique : 300–1000ms
- Animation de retour : 300–500ms

## Différence avec le Swipe

- Swipe : un seul mouvement dans une direction
- Shake : plusieurs mouvements de va-et-vient
