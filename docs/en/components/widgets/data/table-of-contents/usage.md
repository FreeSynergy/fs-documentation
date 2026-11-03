# Table of Contents - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A table of contents is an overview of chapters/sections.

- Documentation
- Books
- Websites
- Chapter overview

## Examples

### Documentation

```jsx
<TableOfContents items={entries} activeItem="activeItem" />
```

### Books

```jsx
<TableOfContents items={entries} collapsible={false} />
```

### Websites

```jsx
<TableOfContents items={entries} interactive={false} />
```
