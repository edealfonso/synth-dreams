# Synth Dreams

A one-page, scroll-animated portfolio site about drum machines, synthesizers and colourful electronic gadgets, by **Elsa de Alfonso**.

> Work in progress: the content is placeholder for now.

## Highlights

- **Smooth scrolling that adapts to the device:** [smooth-scrollbar](https://github.com/idiotWu/smooth-scrollbar) on desktop, native scroll on touch devices, wired to GSAP ScrollTrigger through `scrollerProxy`. A small scroll module (`static/js/core/scroll.js`) hides the difference from the rest of the code.
- **Scroll-linked animations** with [GSAP 3 + ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/): pinned covers, parallax, staggered reveals, pinned galleries and a "magnifier" list, with desktop-only effects behind `gsap.matchMedia`. On touch devices the mobile galleries are pinned with CSS `position: sticky` and skip their scroll-linked motion: native scroll runs ahead of JavaScript there, so anything the JS moves while scrolling jitters.
- **Lazy-loaded responsive videos** that pick a mobile or desktop source, pause off screen and come with custom controls.
- **Bilingual content (ES/EN)** fully editable from the Django admin.

## Stack

Django 4.2 · PostgreSQL 16 · webpack 5 · SCSS · GSAP 3 · smooth-scrollbar · jQuery · Docker Compose

## Getting started

You only need Docker.

```bash
cp .env.example .env                  # then fill in the values
docker compose up --build             # db + web + assets → http://localhost:8000
docker compose exec web python manage.py migrate
docker compose exec web python manage.py seed_dummy   # placeholder content
docker compose exec web python manage.py createsuperuser   # admin at /admin/
```

Production build of the frontend:

```bash
docker compose run --rm assets npm run build
```

## Project layout

```
apps/pages/        # Home (blocks s01–s17), Header, Footer, vignettes, magnify list, legal pages
apps/galleries/    # sortable gallery images
static/js/         # ES modules: core/ (scroll, screen, gsap), animations/ (one module per block), features/, utils/
static/scss/       # styles
templates/         # Django templates
synthdreams/       # settings and URLs
```

## Author

© Elsa de Alfonso
