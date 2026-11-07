# Arcemall - Structure and UI/UX

## Building blocks

```
Marketplace page:  search bar + cards/list toggle
  Listing tiles: image · price · provider · rating
  Detail: gallery · booking form (calendar) · chat · reviews
Operator cockpit: model editor (entities/fields) · UI components ·
                  payment rules · webhooks
```

## UI/UX

- Template-based, but customizable by the operator; geo maps are central
- Status display per booking (requested/accepted/completed)

## Interactions

- Drag modeling in the editor (relations by click)
- Booking process with confirmation stages (requested → confirmed)

## Responsive design

- Templates are responsive; map view optimized for mobile

## Accessibility

- Standard web components; editor forms are keyboard-operable

## Performance

- Search index is internal to the platform; large listing volumes via categorization
