# Backlog

Things parked for later.

## Pending

- [ ] **Medium-urgent: bring back the s04 video cover.** Hidden on 2026-11-10 before going public, because it only had the colour-bars placeholder (it is also the only block marked TODO in `seed/texts/script.md`).
  - How it is hidden: `templates/home.html` skips the whole s04 section when `s04_video_high` and `s04_video_low` are both empty, and `initCovers` (`static/js/animations/covers.js`) skips covers that are not on the page. The dev DB fields were emptied (the placeholder files are still in `media/video/dummy/`).
  - To bring it back: generate the video with `ffmpeg` test sources (no timecode, see CLAUDE.md phase 5), add high/low versions and a poster in the admin and in `seed_demo`. No code change needed, but re-check the ScrollTrigger positions after s04 (its pin is created between s01 and s13).
  - s10 can also show a video (`s10_video_*`), but it shows its photo while those fields are empty, so nothing is hidden there.

- [ ] **Opening a URL with a `#hash` does not land on its section.** With `/#s06` the page ends up much further down (around gallery 2). The original code did the same (the logic was copied as is). Seen on 2026-11-08 with the placeholder content.
  - Hint: `checkLocationHash()` scrolls before the animations are created (pins have not shifted positions yet), and one second later `main.js` scrolls back to the top with `universalYScroll({ y: 0 })`.
  - Where: `static/js/features/anchors.js` and `static/js/main.js`.

- [ ] **Scroll gets stuck at the `s06` block** (three horizontal steps). Seen on 2026-11-08 with an empty database and no `media/`.
  - Check again now that there is placeholder content. It may only happen without images or texts, when heights are computed wrong.
  - Where: `templates/home.html` (`#s06`, `#s06-step-1..3`), `static/js/animations/s06-three-horizontal-steps.js` (`initThreeHorizontalSteps`, the per-step trigger) and `static/scss/special/scroll-animations.scss` (initial state of the steps).

- [ ] **Legal pages return 404 with a trailing slash.** `/legal/aviso-legal` works but `/legal/aviso-legal/` gives 404. Pre-existing (not caused by the renaming). Seen on 2026-11-09.
  - Hint: the route is `path('legal/<str:slug>', ...)` without a trailing slash, while Django's convention (and `APPEND_SLASH`) expects one.
  - Where: `apps/pages/urls.py` (and any hard-coded legal links in the templates).

- [ ] **Breakpoints are inconsistent between SCSS and JS.** Found on 2026-11-09 during phase 3d. Unifying them changes how the page looks at some widths, so it needs visual checking.
  - SCSS tokens (`static/scss/abstracts/_variables.scss`, all `max-width`): `$desktop` 1400 px, `$laptop` 1024 px, `$tablet` 990 px, `$mobile` 767 px, `$mobile-sm` 500 px.
  - Hard-coded media queries in `static/scss/templates/_home.scss`: `1635px` (s06, step titles narrow to 69%), `882px` (s06, the three steps stack into one column) and `1200px` (s09, vignettes get smaller paddings and fonts).
  - JS (`static/js/core/screen.js`, all `<=`): `isLaptop` 1200 px, `isTablet` 990 px, `isMobile` 767 px, `isMobileSmall` 375 px. Only `isTablet` (`features/autovideo.js`: loads the mobile video up to 990 px) and `isMobile` (`animations/s06-three-horizontal-steps.js`, `animations/s14-magnify-list.js`) are used; `isLaptop` and `isMobileSmall` are dead.
  - JS `gsap.matchMedia("(min-width: 768px)")` in `animations/index.js` for the desktop-only animations: matches `$mobile` (767 px).
  - Fluid font sizes (`$f-*` tokens) reach their max at 1666 px wide (the `0.6vw` factor): another implicit breakpoint.
  - Mismatches: laptop is 1024 px in CSS but 1200 px in JS; small mobile is 500 px in CSS but 375 px in JS; 1635, 882 and 1200 px are not tokens.
  - Proposal: one breakpoint scale shared by SCSS and JS (e.g. SCSS tokens + a `breakpoints` map exported to JS, or CSS custom properties read by `screen.js`), the three hard-coded values turned into tokens or snapped to the nearest one, and the dead `isLaptop`/`isMobileSmall` removed.

- [ ] **Unsupported CKEditor 4.** `django-ckeditor` ships CKEditor 4.22.1 and Django warns (`ckeditor.W001`) about unfixed security issues.
  - Needs a proper look: it matters for how admin texts render.
  - Options: CKEditor 5 (`django-ckeditor-5`, check the licence) or another rich-text editor. Before deciding, check which fields and which `CKEDITOR_CONFIGS` are really used.
