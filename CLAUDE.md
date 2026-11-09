# CLAUDE.md

## Project: Synth Dreams

Portfolio site by **Elsa de Alfonso**: a one-page home, heavy on scroll animation, about **drum machines, synthesizers and electronic gadgets** with a colourful, naive feel (no complicated modular rigs).

It is built on an existing Django codebase. The most valuable part is the **frontend JavaScript**: smooth scrolling, scroll-linked animations, lazy-loaded videos, and keeping all of that in sync across desktop and touch devices.

> **Golden rule: the origin must not be traceable.** No previous brand, company, author, domain or repository may appear in the code, the commits or this file — nor the sector of the original content. If you find something like that, delete or replace it; never document or quote it. The only author who appears is Elsa de Alfonso.

> **Language:** everything in the repo is in **English** (identifiers, comments, configs, admin labels, docs, commit messages). The site *content* is bilingual (ES default, EN). The conversation with the user is in Spanish.

## Current status (2026-11-09)

- ✅ **Phase 1 (Docker):** done and validated. Docker Compose with `db`, `web` and `assets`; settings read from `.env`; pinned versions in `requirements.txt`; settings package `synthdreams/`; flat layout (everything at the repo root).
- ✅ **Phase 2 (comments):** done, then **superseded**: the user decided everything goes in English, so comments and names were translated to English during phase 3.
- ✅ **Phase 3 (improvements):** done and validated, in sub-phases: 3a bugs and dead code → 3b modularise the JS → English translation (literal) → 3c structural naming → 3d SCSS (modules, tokens, BEM) → 3e conventions.
- ✅ **Phase 4 (remove traces of the origin):** done and validated. Admin CSS copies and logo removed (own `static/css/admin.css`), a free font instead of the paid one (now DM Sans), new favicon (a black pixel "wave" pulse over a lilac `#a99cff` / white split, same icon as the logo; PNG/ICO rasterised from the same geometry as `favicon.svg`), own rounded UI icons (circular back arrow, struck-through speaker while muted) and map pin, solid social icons GitHub/LinkedIn/Pinterest/Wikipedia (Simple Icons, CC0; LinkedIn drawn by hand), no social title, copyright rendered as `© <current year> <footer.copyright>`. Exhaustive search with the user's terms (files, binaries, file names, node_modules, database, git history): clean.
- 📋 Parked issues live in `backlog.md` (anchor `#hash`, scroll stuck at `s06`, legal URLs with trailing slash, CKEditor 4, inconsistent breakpoints).
- **Git:** history restarted on 2026-11-09 with a single clean initial commit on `main` (the old history is kept outside the project and must never be published). Published on 2026-11-09 as a **private** GitHub repo (`origin`); code or structural changes go through branches and PRs that the user reviews; small content tweaks (a photo crop, a text fix) can be committed straight to `main`.
- The dev database holds **placeholder content** from `seed_dummy` (silly text and images showing their field name). No users. Temporary: phase 5 replaces it with `seed_demo`.

## Goals (by phase)

Work **one phase at a time**. The user validates each phase before moving on. Do not get ahead.

### 1. Run the project locally (Docker) — done
- Everything runs in **Docker Compose**; nothing (Python, Postgres, Node) is installed on the host.
  - **Python 3.12** in `web` (Django + `runserver`), **PostgreSQL 16** in `db` (persistent volume, no SQLite), **Node LTS** in `assets` (webpack watch → `static/bundles/` + `webpack-stats.json`).
  - **Secrets in `.env`** (not committed) + `.env.example` (committed). Settings read environment variables.
- Django 4.2 LTS; `sass` (Dart Sass) instead of `node-sass`.

### 2. Comments — superseded by the English rule above

### 3. Improve what can be improved
- **Bugs:** go through the list below and fix them.
- **Modularise the JS:** ES modules with a single webpack entry point, without changing behaviour. ✅
- **English translation (step 1 of naming):** literal translation of every name and comment. Where a literal translation would reveal the original content's sector, use the block's **role** instead (e.g. `featured`). ✅
- **Structural naming (3c):** blocks are named after their **layout, not their content**, so the theme can be reused for another topic. See "Blocks" below. ✅
- **CSS (3d):** polish the SCSS: consistent BEM, tokens in `variables.scss`, remove duplicates and dead code, `@use` instead of `@import`.
- **Conventions (3e):** write them down in the "Conventions" section of this file.

### 4. Remove every trace of the origin
- Rename whatever still carries old names: admin titles, `package.json` (name, description, author, repo, keywords), favicons, `site.webmanifest`, logos and legal texts.
- Migrations were already regenerated from scratch in phase 3; regenerate again if models change.
- Remove assets that are not ours: paid fonts (swap for a free one, e.g. Google Fonts), images, videos, map and brand SVGs.
- Delete generated artifacts (`static/bundles/`, `webpack-stats.json`) and leftovers such as `.bash_history`, `.DS_Store`, `reqfreeze.txt`.
- Finish with an exhaustive search (`grep -ri`) for the old names. The user gives the list of terms in the conversation and it is **never written to any file**.

### 5. New content: Synth Dreams
- New texts (ES and EN, the site is bilingual) and free photos/videos from **Unsplash** or **Pexels**.
- **Credits:** record every one (author, platform, link) and show them in a credits block at the end of the footer that does not interfere with the animations.
- Content lives in the database (admin), so a fresh clone must be able to load it on its own: a `python manage.py seed_demo` command (or fixtures) reading a `seed/` directory with images and texts.

#### Proposed content per block (pending validation)

| Block | New content |
|---|---|
| s01 pinned cover (logo + image) | "Synth Dreams" logo over a very colourful synth photo |
| s02 parallax with title (+ s03 statement) | "Machines that make you smile" |
| s04 video cover | Pexels video: hands playing a synth or drum machine |
| s05 parallax + s06 three horizontal steps | "Three ways to make noise": drum machines · synths · gadgets |
| s07 pinned gallery | Drum machine gallery |
| s08 parallax layout | "Keys and knobs": close-ups of knobs, pads and keys |
| s09 floating vignettes | "Anatomy of a synth": oscillator, filter, envelope… |
| s10 image or video | "From circuit to sound" |
| s11 rising text over pinned image | An iconic, colourful machine up close |
| s12 pinned gallery | Pocket synths and quirky gadgets |
| s13 pinned cover | "Tiny home studios" |
| s14 magnify list | "Our rules": play first, big buttons, fearless colours… |
| s15 split images (two-line title) | "Beep" / "Boop" |
| s16 vertical points | "Start today": pick a machine · plug it in · record |
| s17 full image with text | Closing line |
| Footer (map, social, copyright) | **Keep the map overlay and its animation** (map image from OpenStreetMap, credited, not a Google Maps capture) with the address of *This Museum Is (Not) Obsolete* (https://maps.app.goo.gl/1jeT92y8vf4r98GDA). Made-up contact email (e.g. `wishlist@…`; prefer a reserved domain such as `.example` so it never reaches a real inbox). Social: GitHub, LinkedIn, a Pinterest search for synth/drum machine gear, and Wikipedia's *Electronic music* article (https://en.wikipedia.org/wiki/Electronic_music) instead of Instagram. © Elsa de Alfonso and **image credits** |

#### Logo (approved)

- Favicon icon (lilac/white, black pixel wave) + "Synth Dreams" in **Silkscreen** (pixel font, Google Fonts, SIL OFL 1.1), text converted to SVG paths (no font dependency). Logo icon: the pulse is drawn on a 9×9 pixel grid scaled so one icon pixel equals one font pixel (12.5 units), so the line has the weight of the letters; the top-left and bottom-right corner pixels are left empty ("wave" look) and the white band is exactly 4 grid rows. Both logos share the same icon/text proportion (icon 112.5 units tall, text cap height 62.5). Horizontal logo: 6 font pixels between icon and text. Optical kerning: tighter between N and T, DREAMS opened by half a pixel per gap. The favicon uses the same icon.
- `seed/images/logo-cover.svg`: icon above `#111` text, for the s01 cover (the photo fades to 45% under it once revealed). `seed/images/logo-header.svg`: icon left, `#111` text, for the white header.

#### Content review status

- ✅ Approved: s01 cover (white macro keypad with aluminium knobs, abstract and soft-focus; mobile = vertical crop centred on the device; photo at 75% on load, fading to 45% when the black pixel logo rises), s10 (grey Elektron Model:Cycles on wood in window light), s09 photo (top view of keyboards and a mixer: Korg wavestate, Moog Grandmother, Zoom mixer; navy→lilac duotone like s02, then contrast 0.85 and brightness 1.3 baked in; vignettes still pending), s14, s17, s07 gallery, s12 gallery (slot 1 = Pocket Operator KO on speckled white), s08 (JX-08 split into two sharp crops), s11 (Elektron Digitakt on a white table, cropped, background curved to pure white), logo and favicon, s13 (small home studio with black walls, wood trim, a mixing desk and a window onto green trees, in warm light), s02 (TR-808 close-up as a navy→lilac duotone, whole width of the photo, top cropped (y 300–1500 of 2000×1500) so fewer light labels show, with **white** title and text), s05 (green ADSR envelope screen, abstract, dark, unfaded, with **white** text), s16 (vintage VU meters and tape-deck knobs, landscape photo cropped to the column by object-fit), s15 (left: blue-lit SP-404 with the **white** "Beep / Boop" title; right: Zoom H6 recorder).
- ✅ Footer bottom strip (`seed/images/footer-bottom.jpg`): the s01 cover photo again (keys, frame and big knob), vertical centre band y 455–1375 of the 3000×2000 original, light blur (1.5 px) and 35% fade toward white, so the page ends with the object it starts with.

#### Still to do (phase 5)

- **s04 video** (and the optional s10 video): generate with `ffmpeg` test sources, without the timecode overlay. s04 currently shows a colour-bars placeholder.
- **s09 vignettes:** simple SVG pictograms (oscillator, filter, envelope…), not photos.
- **Footer map:** OpenStreetMap image (credited) with the museum address, plus the real address text (currently "Calle del Ruido, 1"), the `.example` email and the social links.
- **Credits:** finish `seed/credits-todo.md` (some entries still say "credit from earlier list") and show them in the footer credits block.
- **Texts:** every block still has "Bip bup" placeholder text, ES and EN.
- **`seed_demo`:** load everything from `seed/` on a fresh clone (unique gallery `the_order`).
- **Mobile check:** s09, s11, s14, cover/logo and the new photos.
- Header readability over dark photos was raised and never settled; re-check it on s02 (TR-808) and s05.

#### Photo constraints (final selection)

- **Theme:** the site is about the author's dream gear (see the wish list in the conversation). Photos from Unsplash/Pexels only (Unsplash+ excluded), beautiful, with special/coloured light; abstract close-ups are fine, they need not show the whole device. **Validated look:** product close-ups in natural light with cheerful, slightly vintage/pastel colours (favourite: TR-808 button close-up; also OP-Z detail, Moog Grandmother panels). Warm, moody coloured light (orange/red-pink) is acceptable as a secondary accent. Avoid flat "still life" shots on plain coloured backgrounds and abstract light-painting. Keep it simple: download each chosen photo once into `seed/` and record its credit (no image pipeline).
- **s11_image:** the photo's background must match the block's background colour. (s09 now uses a full-bleed top-view photo, so the rule no longer applies there.)
- **s09 vignettes:** drawn as simple SVG pictograms (e.g. oscillator, filter, envelope), not photos.
- **Photos under text (s01, s14):** faded toward white before seeding (`ffmpeg lutrgb`, out = val·(1−a) + 255·a; a ≈ 0.7 for s01, 0.45 for s14) so the black text has little contrast to fight.
- **Galleries:** s07 = classic Roland drum machines only; s12 = Teenage Engineering only.
- **Backup photos** (good, not placed yet) live in `seed/backup/`. Every photo removed from a block goes there; files the author deletes from it are rejected and must not be restored.
- **Gallery order:** `seed_demo` must give gallery rows unique `the_order` values (the dev DB ended up with duplicates, which made the rendered order differ from the intended one).
- **s14_image:** very light, low contrast (or reduced opacity) so the text on top stays readable.
- **s17_image:** text sits top-right on desktop and at the bottom on mobile (white text), so those areas must be plain and dark.
- **Videos (s04, s10):** procedurally generated with `ffmpeg` test sources (no rights needed; remove the timecode overlay). The author may add her own audio.

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
| s09 | `s09-floating-vignettes` (`.vignette-group--1..3`) | `#s09-container`, `#s09-trigger`, `#s09-image`, `#s09-floating-N` | `s09_title`, `s09_text`, `s09_left_image`, `s09_group_titleN` · `Vignette` |
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
apps/pages/                # Header, Home, Footer (singletons), Vignette, MagnifyItem, LegalPage
│   ├── views.py           # HomeView (puts everything in the context), LegalPageView
│   ├── translation.py     # translatable fields
│   ├── templatetags/site_tags.py   # get_header, get_footer, get_legal_pages, |media_url
│   └── management/commands/seed_dummy.py
apps/galleries/            # FirstGalleryImage, SecondGalleryImage (sortable)
templates/                 # base.html, home.html, legal.html, includes/, cookielaw/, admin/base_site.html (adds static/css/admin.css)
static/js/main.js          # ← webpack entry (lifecycle); modules in core/, animations/, features/, utils/
static/js/cookielaw/       # cookie banner JS (not bundled by webpack)
static/favicon/            # favicon.svg (source) + PNG/ICO generated from it
static/img/                # UI icons (own SVGs)
static/scss/               # index.scss (@use, cascade order): abstracts/ (tokens + mixins, no CSS), base/, sections/, special/, templates/
static/bundles/            # webpack output (generated)
webpack.config.js          # single config; --mode development (watch) or production (postcss + minified)
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
docker compose exec web python manage.py seed_dummy --video media/placeholder-video.mp4   # placeholder content (wipes the previous one; --video is optional)
docker compose run --rm assets npm run build      # webpack production build (npm run watch is the dev one)
docker compose down                               # stop (add -v to also delete the database)
```

`Makefile` shortcuts: `make up`, `make down`, `make logs`, `make migrate`, `make makemigrations`, `make superuser`, `make shell`, `make manage cmd="..."` and `make build`.

## JavaScript architecture (`static/js/`)

ES modules with a single entry point (`main.js`). jQuery is global (`$`, via `ProvidePlugin`).

| Module | What it does |
|---|---|
| `main.js` | Lifecycle: DOM ready → `calcScreen`, `initSmoothScroll`, webp, anchors, cover; in a nested ready (one tick later) → `checkLocationHash`, `loadAllAnimations`; after 1 s → show content, back to top, `onContentVisible` (cover, videos, header, map), `onScroll(scrollActions)` and resize. |
| `core/gsap.js` | Registers ScrollTrigger and re-exports `gsap` and `ScrollTrigger`. Everyone imports from here. |
| `core/screen.js` | `screen` (live object with `isLaptop/isTablet/isMobile/isMobileSmall`: 1200/990/767/375 px), `calcScreen()`, `isTouchDevice`. |
| `core/scroll.js` | Hides the two scroll systems (smooth-scrollbar on non-touch, native on touch): `initSmoothScroll`, `getScrollTop`, `onScroll`, `isVisible`, `universalYScroll`, `SCROLLER_SELECTOR`. |
| `animations/index.js` | `loadAllAnimations()`: `ScrollTrigger.defaults` and a call to each animation **in the original order** (see below). |
| `animations/*.js` | `generic` (`.gsap-appear`, `.gsap-parallax*`), `covers` (s01, s04, s13), `galleries` (s07, s12) and one module per block with its own animation: `s06-three-horizontal-steps`, `s09-floating-vignettes`, `s11-rising-text-over-pinned-image`, `s14-magnify-list`, `s16-vertical-points`. Desktop-only ones are called inside `gsap.matchMedia`. |
| `features/` | `anchors` (hash and `.js-smooth-anchor`), `autovideo` (lazy videos and controls), `cover` (two-step cover reveal), `header` (`checkHeader`, `slideHeader`), `map`. |
| `utils/webp.js` | `changeToWebP()`: adds the `.webp` version to `background-image`s. |

### Animation adjustments (branch `animation-adjustments`)
- **s09:** slow parallax on the left image (desktop only, no zoom): while the section crosses the screen (`top bottom` → `bottom top`), a scrubbed `y` transform moves it from the top of the section to its bottom, so it rises into view more slowly than the page and only its lower part shows as the section leaves. A transform, not a pin, so later triggers keep their positions.
- **s11:** title and text sit above the image; the title only fades in, the text fades in and rises a little; the image (tight crop, 85vh) is pinned in the middle of the screen (no pin spacing, the section height gives the distance) and zooms from 0.85 to 1.
- **s14:** each item lights up as it rises to the middle of the screen and stays lit (no dimming afterwards).

### Gotchas
- **ScrollTrigger creation order:** positions are computed in order and pins push the later triggers down. `animations/index.js` keeps the original order; do not reorder without checking.
- **Timing:** smooth-scrollbar goes **before** any ScrollTrigger. The nested ready in `main.js` is not redundant: removing it changes the measured heights (verified: the s16 and s14 pins compute `start`/`end` from heights at creation time). The `setTimeout`s (100/500/1000 ms) shape how the page enters.
- **Coupling with the HTML:** selectors are the contract with `home.html`. Renaming one means changing the template, the SCSS and the module together.
- **3d verification:** computed styles and boxes of every element (matched by DOM position) were compared before/after the BEM renaming at 390, 900, 1100 and 1600 px, home and legal, with and without the cookie banner: identical.
- **3b verification:** the 65 ScrollTriggers (order, `start`, `end`, pin) of the original `script.js` and of the modular version were compared on desktop: identical.

## Bugs and leftovers (phase 3)

Fixed in 3a:
- `universalYScroll`: on touch it used `the_scroller` (undefined) and animated `#scroll-content`, which only exists with smooth-scrollbar. Now it uses `#body-scroller`.
- The `load` handler of `.js-firstload` was empty; now it reveals the cover when the image loads.
- In s10 (then "section 5"), the high/low quality videos had their `desktop`/`mobile` classes swapped.
- Desktop galleries created one tween per element, all targeting the same class. Now there is one per gallery.
- `/media/{{ field }}` paths → `{{ field|media_url }}` filter, which returns `''` for empty fields (`.url` would raise `ValueError`).
- Dead JS removed (old scroll library, old "magnifier" code, `vh()`, `ScrollbarPlugin`, `console.log`s, a no-op `split('#')` line, `data-parent`).
- webpack configs merged into `webpack.config.js` (mode from the CLI); npm scripts reduced to `watch`, `build` and `clean`.
- Static, media and webpack settings moved from `local.py`/`prod.py` to `base.py`. Docs links → Django 4.2.
- Unused fast-forward icon deleted.

Fixed during the English translation:
- Mobile gallery 2 rendered the images of gallery 1.
- The second image of s08 (then "section 3") checked the fields of the first one.
- `asgi.py`/`wsgi.py` pointed to `synthdreams.settings` (not a settings module); now `synthdreams.settings.prod`.
- `apps/pages/fields.py` (`ResponsiveImageField`) was only used by an old migration: deleted.

Fixed in 3d:
- `@import` → `@use`/`@forward` (no more Sass deprecation warnings); `unquote()` removed.
- Dead CSS removed (commented-out code, empty rules, unused utilities, rem fallbacks always overridden by vw/vh, the `.onload-showing` style in `base.html`, the undefined `mw-1100` class).
- Stray `</a>` after the copyright in the footer.

Pending:
- Unused `devDependencies` (`video.js`, `file-loader`, `url-loader`, `style-loader`, `babel` 6…) and no Babel config (the loader transforms nothing). `django-debug-toolbar` is installed but not used.
- Meta descriptions in `base.html` are Spanish only; they should follow the page language (phase 5).

## Secrets and publishing on GitHub

- Only `.env.example` (sample values) is committed; `.env` is in `.gitignore`.
- Also not committed: `node_modules/`, `media/` (except what the seed needs, which goes in `seed/`), `static/bundles/`, `webpack-stats.json`, `.DS_Store`, `.bash_history`.
- `settings/prod.py` has no domains or hosting data: everything comes from the environment.
- The local git repo exists, but **the published one must start clean**. See "Current status".

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
- **Templates:** media through the `|media_url` filter (never `.url` on optional fields). A selector change means template + SCSS + JS together.
- **Django:** config from environment variables (`.env`); model changes need a migration and, if translatable, `translation.py`.
- **Git:** commits only when the user asks; code or structural changes go through a branch and PR, small content tweaks can go straight to `main`. English messages: the phase plus a short summary (`Phase 3d: …`), then the details as a list.
