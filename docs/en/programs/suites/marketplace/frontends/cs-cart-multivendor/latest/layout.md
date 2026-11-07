# CS-Cart Multi-Vendor - Structure and UI/UX

## Layout

```
Frontend: header (search/categories) · product list (tiles,
          "Sold by" label) · cart (vendor split rows)
Vendor dashboard: side menu left (products/orders/finances),
          product form with variant matrix
Admin center: analogous, plus seller/fee management,
          order list with vendor color coding
```

## UI/UX

- classic shop consistency; backend in tab/form style (v4 look)
- vendor labeling and separate shipments visible in checkout

## Interactions

- Product import (CSV), mass changes (select + actions)
- Order status workflows (new → in process → shipped… per merchant)

## Responsive design

- Theme system is responsive; backend is desktop-centric

## Accessibility

- Theme-dependent (operator task); backend uses standard forms

## Performance

- Large catalogs: caching/DB optimization; the choice of add-ons strongly affects speed
