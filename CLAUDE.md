# CLAUDE.md

## Project: Synth Dreams

Portfolio site by **Elsa de Alfonso**: a one-page home, heavy on scroll animation, about **drum machines, synthesizers and electronic gadgets** with a colourful, naive feel. Live at https://edealfonso.github.io/synth-dreams/ (static export on GitHub Pages).

The most valuable part is the **frontend JavaScript**: smooth scrolling, scroll-linked animations, lazy-loaded videos, and keeping all of that in sync across desktop and touch devices.

> **Language:** everything in the repo is in **English** (identifiers, comments, configs, admin labels, docs, commit messages). The site *content* is bilingual (ES default, EN).

Private notes (project diary, content and photo decisions) live in a git-ignored `CLAUDE.local.md`, which Claude Code also reads.

## Blocks (structural naming)

The home is a stack of blocks named after their **layout**, with a two-digit prefix in page order. The full name is used for the CSS block class, the JS module, the admin fieldset and the template comment; IDs and model fields use only the prefix.

| # | Block (CSS class / JS module) | IDs used by the JS | `Home` fields / related model |
|---|---|---|---|
| s01 | `s01-pinned-cover` | `#s01-container`, `#s01-cover`, `#s01-logo`, `#s01-chevron` | `s01_logo`, `s01_image(_mobile)` |
| s02 | `s02-parallax-with-title` | `#s02` (chevron target) | `s02_title`, `s02_image`, `s02_text` |
| s03 | `s03-statement` | — | `s03_text` |
| s04 | `s04-video-cover` | `#s04-container`, `#s04-cover` | `s04_video_high/low/poster` |
| s05 | `s05-parallax` | — | `s05_text`, `s05_image` |
| s06 | `s06-three-horizontal-steps` | `#s06`, `#s06-step-1..3` | `s06_step_titleN`, `s06_step_textN` |
| s07 | `s07-pinned-gallery` | `#s07-pair-N` | `s07_title`, `s07_text` · `galleries.FirstGalleryImage` |
| s08 | `s08-parallax-layout` | — | `s08_title`, `s08_text`, `s08_image1/2(_mobile)` |
| s09 | `s09-floating-vignettes` (`.vignette-group--1..3`) | `#s09-container`, `#s09-trigger`, `#s09-image`, `#s09-floating-N` | `s09_title`, `s09_text`, `s09_left_image`, `s09_group_titleN`, `s09_group_image3` · `Vignette` |
| s10 | `s10-image-or-video` | `#s10-image` | `s10_title`, `s10_text`, `s10_image`, `s10_video_*` |
| s11 | `s11-rising-text-over-pinned-image` | `#s11`, `#s11-image`, `#s11-title`, `#s11-body`, `#s11-text-container` | `s11_title`, `s11_text`, `s11_image` |
| s12 | `s12-pinned-gallery` | `#s12-pair-N` | `s12_title`, `s12_text` · `galleries.SecondGalleryImage` |
| s13 | `s13-pinned-cover` | `#s13-container`, `#s13-cover` | `s13_title`, `s13_text`, `s13_image` |
| s14 | `s14-magnify-list` (`.magnify-item`) | `#s14`, `#s14-container`, `#s14-bg`, `#s14-content` | `s14_image`, `s14_text` · `MagnifyItem` |
| s15 | `s15-split-images` | — | `s15_title_line1/2`, `s15_image_left/right`, `s15_text` |
| s16 | `s16-vertical-points` | `#s16`, `#s16-container`, `#s16-image`, `#s16-point-1..3` | `s16_title`, `s16_text`, `s16_image`, `s16_point_titleN/textN` |
| s17 | `s17-full-image-with-text` | — | `s17_text`, `s17_image` |

Adding, removing or reordering a block means renumbering consistently (model + migration, admin, translation, template, SCSS, JS) and checking the ScrollTrigger order in `animations/index.js`.

## Stack

- **Backend:** Django 4.2 (settings split into `base/local/prod`), PostgreSQL (`psycopg2`), `unipath` for paths.
- **Third-party Django apps:** django-modeltranslation (ES/EN), django-solo (singletons), django-admin-sortable, django-clone, django-ckeditor, django-autoslug, cookielaw, django-webpack-loader.
- **Frontend:** webpack 5 + Babel, SCSS (sass-loader; postcss in prod only), **DM Sans** (SIL OFL 1.1) self-hosted via `@fontsource/dm-sans` (imported in `main.js`), jQuery (injected as `$` by `ProvidePlugin`), **GSAP 3 + ScrollTrigger** and **smooth-scrollbar**.
- **i18n:** `es` by default (no URL prefix) and `en` under `/en/`, via `i18n_patterns`.
- **Environment:** Docker Compose with `db` (Postgres 16), `web` (Django, Python 3.12) and `assets` (Node, webpack watch). Config from environment variables in `.env`.

## Layout

Paths are relative to the repo root (where `manage.py`, `docker-compose.yml` and this file live). `synthdreams/` is the settings/urls package.

```
synthdreams/settings/      # base.py, local.py, prod.py (config read from env vars / .env)
synthdreams/urls.py        # admin + i18n_patterns(pages)
apps/pages/                # Header, Home, Footer (singletons), Vignette, MagnifyItem, LegalPage, Credit
│   ├── views.py           # HomeView (puts everything in the context), LegalPageView
│   ├── translation.py     # translatable fields
│   ├── templatetags/site_tags.py   # get_header, get_footer, get_legal_pages, get_credits, |media_url
│   └── management/commands/   # seed_demo.py (real content from seed/), seed_dummy.py (placeholders), export_static.py (static site for GitHub Pages)
apps/galleries/            # FirstGalleryImage, SecondGalleryImage (sortable)
templates/                 # base.html, home.html, legal.html, includes/, cookielaw/, admin/base_site.html (adds static/css/admin.css)
static/js/main.js          # ← webpack entry (lifecycle); modules in core/, animations/, features/
static/js/cookielaw/       # cookie banner JS (not bundled by webpack)
static/favicon/            # favicon.svg (source) + PNG/ICO generated from it
static/img/                # UI icons (own SVGs)
static/scss/               # index.scss (@use, cascade order): abstracts/ (tokens + mixins, no CSS), base/, sections/, special/, templates/
static/bundles/            # webpack output (generated)
webpack.config.js          # single config; --mode development (watch) or production (postcss + minified)
seed/                      # content.json + images loaded by seed_demo; credits.md (photo credits)
docs/screenshots/          # README screenshots
.github/workflows/pages.yml  # static export deployed to GitHub Pages on push to main
```

Almost all home content is edited in the admin (`Home` model, `sNN_*` fields, see "Blocks"). `home.html` relies heavily on **IDs and classes the JS uses as selectors**.

## Commands

All from the repo root (where `docker-compose.yml` is):

```bash
cp .env.example .env                              # first time: fill in values
docker compose up --build                         # starts db + web + assets → http://localhost:8000
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py <cmd>    # any other Django command
docker compose exec web python manage.py seed_demo              # real content from seed/ (wipes the current content); --export writes the DB back to seed/content.json
docker compose exec web python manage.py seed_dummy --video media/placeholder-video.mp4   # placeholder content (wipes the previous one; --video is optional)
docker compose run --rm assets npm run build      # webpack production build (npm run watch is the dev one)
make export                                       # static export for GitHub Pages into dist/ (SITE_PREFIX=/synth-dreams)
docker compose down                               # stop (add -v to also delete the database)
```

`Makefile` shortcuts: `make up`, `make down`, `make logs`, `make migrate`, `make makemigrations`, `make superuser`, `make shell`, `make manage cmd="..."`, `make build` and `make export`.

## Content

- Content lives in the database and is edited in the admin. A fresh clone loads it with `seed_demo` (`seed/content.json` + `seed/images/`, copied to `media/demo/`). After editing content in the admin, run `seed_demo --export` and commit `seed/content.json` (and any new file it adds to `seed/images/`).
- **Photo credits:** every photo is credited in `seed/credits.md` (author, platform, link) and as a `Credit` row in the admin (*Footer · Photo credits*), shown at the bottom of the footer. Add both **at the same time** as the photo.

## Static export and deployment

- `SITE_PREFIX` (env var; empty locally, `/synth-dreams` on GitHub Pages) sets `FORCE_SCRIPT_NAME`, so reversed URLs and the relative `STATIC_URL`/`MEDIA_URL` get the prefix; webpack prepends it to `publicPath`, so build with the same value. ES/EN links use the `translated_url` tag. Never hard-code a root path (`/...`) in templates, JS or SCSS. With the prefix set, `runserver` links do not match its routes: it is only meant for the export.
- `export_static` renders `/`, `/en/` and every legal page (both languages) through the test client into `dist/` (git-ignored): `index.html` per folder, `legal/<slug>.html`. It copies `static/bundles`, `favicon` and `img`, plus every static/media file the pages reference, and adds `.nojekyll`. `make export` = prefixed build + export + dev build again.
- `.github/workflows/pages.yml` runs on every push to `main` (and by hand): Postgres service → `pip install` + `npm ci` → prefixed `npm run build` → `migrate` → `seed_demo` → `export_static` → deploy to Pages. Build-only env values, no secrets. Any commit to `seed/` redeploys the site.

## JavaScript architecture (`static/js/`)

ES modules with a single entry point (`main.js`). jQuery is global (`$`, via `ProvidePlugin`).

| Module | What it does |
|---|---|
| `main.js` | Lifecycle: DOM ready → `calcScreen`, `initSmoothScroll`, anchors, cover; in a nested ready (one tick later) → `checkLocationHash`, `loadAllAnimations`; after 1 s → show content, back to top, `onContentVisible` (cover, videos, header, map), `onScroll(scrollActions)` and resize. |
| `core/gsap.js` | Registers ScrollTrigger and re-exports `gsap` and `ScrollTrigger`. Everyone imports from here. |
| `core/screen.js` | `screen` (live object with `isLaptop/isTablet/isMobile/isMobileSmall`: 1200/990/767/375 px), `calcScreen()`, `isTouchDevice`. |
| `core/scroll.js` | Hides the two scroll systems (smooth-scrollbar on non-touch, native on touch): `initSmoothScroll`, `getScrollTop`, `onScroll`, `isVisible`, `universalYScroll`, `SCROLLER_SELECTOR`. |
| `animations/index.js` | `loadAllAnimations()`: `ScrollTrigger.defaults` and a call to each animation **in a fixed order** (see Gotchas). |
| `animations/*.js` | `generic` (`.gsap-appear`, `.gsap-parallax*`), `covers` (s01, s04, s13), `galleries` (s07, s12) and one module per block with its own animation: `s06-three-horizontal-steps`, `s09-floating-vignettes`, `s11-rising-text-over-pinned-image`, `s14-magnify-list`, `s16-vertical-points`. Desktop-only ones are called inside `gsap.matchMedia`. |
| `features/` | `anchors` (hash and `.js-smooth-anchor`), `autovideo` (lazy videos and controls), `cover` (two-step cover reveal), `header` (`checkHeader`, `slideHeader`, `checkHeaderTheme`: white logo text/menu over `.js-header-dark` elements), `map`. |

### Animation notes
- **s09:** slow parallax on the left image (desktop only, no zoom): while the section crosses the screen (`top bottom` → `bottom top`), a scrubbed `y` transform moves it from the top of the section to its bottom, so it rises into view more slowly than the page and only its lower part shows as the section leaves. A transform, not a pin, so later triggers keep their positions.
- **s11:** title and text sit above the image; the title only fades in, the text fades in and rises a little; the image (tight crop, 85vh) is pinned in the middle of the screen (no pin spacing, the section height gives the distance) and zooms from 0.85 to 1.
- **s14:** each item lights up as it rises to the middle of the screen and stays lit (no dimming afterwards).

### Gotchas
- **ScrollTrigger creation order:** positions are computed in order and pins push the later triggers down. `animations/index.js` keeps a fixed order; do not reorder without checking.
- **Timing:** smooth-scrollbar goes **before** any ScrollTrigger. The nested ready in `main.js` is not redundant: removing it changes the measured heights (verified: the s16 and s14 pins compute `start`/`end` from heights at creation time). The `setTimeout`s (100/500/1000 ms) shape how the page enters.
- **Touch devices and JS motion:** with native scroll (touch), the browser scrolls ahead of the JS, so anything ScrollTrigger pins or moves while scrolling lags and jumps (measured frame by frame on an iPhone recording of the mobile galleries; `anticipatePin` did not help). So on touch the mobile galleries (s07, s12) are pinned by CSS (`.gallery--mobile.sticky`, `position: sticky`, added by `initGalleriesMobile`) and their −40% rise is **not** applied: that rise only exists without touch (smooth-scrollbar). Keep this in mind before adding JS-driven pins or motion on mobile.
- **Coupling with the HTML:** selectors are the contract with `home.html`. Renaming one means changing the template, the SCSS and the module together.
- **Header over dark photos:** the logo text and the menu turn white while they sit over an element marked `.js-header-dark` (`checkHeaderTheme`, checked separately for the logo and the menu, using the first element that actually paints under each one, so overlapping pinned blocks are handled). The header logo is rendered inline (`|inline_svg`) so its text path can change colour. Mark a block `.js-header-dark` whenever its photo is dark.

## Secrets

- Only `.env.example` (sample values) is committed; `.env` is in `.gitignore`. The GitHub Action needs no secrets.
- Also not committed: `node_modules/`, `media/` (what the site needs is in `seed/`), `static/bundles/`, `webpack-stats.json`, `dist/`, `CLAUDE.local.md`, `seed/backup/`.
- `settings/prod.py` has no domains or hosting data: everything comes from the environment.

## Conventions

- **Language:** everything in the repo in English; site content in ES (default) and EN.
- **Blocks:** named after their layout with a two-digit prefix in page order (`s07-pinned-gallery`). The full name is used for the CSS block, the JS module, the admin fieldset and the template comment; IDs and model fields use only the prefix (`#s07-…`, `s07_title`).
- **CSS classes:**
  - BEM for styles: `block`, `block__element`, `block--modifier`. One level of element only (no `__a__b`).
  - `u-` utilities (`u-h1`, `u-text-muted`), in `base/_utilities.scss` (most wrap the mixin of the same name).
  - `gsap-` animation hooks (their initial state lives in CSS); `js-` behaviour hooks, never styled.
  - IDs are JS hooks only: never style an ID.
  - State classes toggled by the JS keep plain names (`hidden`, `visible`, `active`, `loaded`…).
- **SCSS:** every partial starts with `@use "../abstracts" as *;`. Colours, gutters, font sizes and transitions come from tokens in `abstracts/_variables.scss` (named by role, not value). New partials are added to `index.scss` in cascade order. No `@import`, no commented-out code.
- **JS:** ES modules imported from `main.js`; `gsap`/`ScrollTrigger` always from `core/gsap.js`; scroll through `core/scroll.js` (never touch smooth-scrollbar or `#body-scroller` directly). New animations are called from `animations/index.js`, respecting the ScrollTrigger creation order.
- **Links:** two styles. Plain links have no underline until hover, when a lilac line (`$color-accent`) fades in (`hover-underline-line` mixin on an `::after`). Links that must read as links (footer closing text, contact) are always underlined in grey with the same distance and weight (`link-underline` mixin, `text-decoration` in `em`, so it scales with the font and wraps across lines); on hover only the line turns lilac. Lilac = hover; the text never changes colour (the social icons are the exception: they turn peach). Photo credits: no underline until hover, then a closer one in the text colour.
- **Templates:** media through the `|media_url` filter (never `.url` on optional fields). A selector change means template + SCSS + JS together.
- **Django:** config from environment variables (`.env`); model changes need a migration and, if translatable, `translation.py`.
- **Git:** commits only when the user asks; code or structural changes go through a branch and PR, small content tweaks can go straight to `main`. English messages: a short summary prefixed with the phase (`Phase 6: …`), then the details as a list.
