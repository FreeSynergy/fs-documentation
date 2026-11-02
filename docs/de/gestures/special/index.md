# Spezielle Gesten (special)

Spezielle Gesten laufen **ohne klassisches Berührungselement**: hover braucht
überhaupt keinen Kontakt, und fingerprint richtet sich nicht auf ein
UI-Element, sondern auf einen Biometrie-Sensor.

Beide Gesten sind bewusst ohne Multipoint: Hover existiert nur als ein
schwebender Zeiger, und der Fingerabdruck-Sensor liest genau eine
Fingerkuppe.

## Elemente

- **hover** - Zeiger über Element ohne Kontakt (Tooltip, Vorschau)
- **fingerprint** - Biometrie-Sensor berühren (Entsperren, Autorisieren)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Tooltip / Vorschau ohne Klick | hover |
| Entsperren, Zahlungen freigeben | fingerprint |

## Barrierefreiheit

Hover ist auf reinen Touchscreens nicht verfügbar – Inhalte dürfen nie nur
per Hover erreichbar sein. Biometrie braucht immer eine gleichwertige
Alternative ohne Biometrie (PIN, Muster, Passwort).

## Siehe auch

- [Gesten Übersicht](../index.md)
- [Tap](../tap/tap/description.md) - Abgrenzung: Geste auf einem Element
- [Swipe](../swipe/swipe/description.md) - Wischen über den Sensor (Swipe-Verfahren)
