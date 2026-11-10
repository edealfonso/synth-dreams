// ------------------------------------------------------------
// ALL SCROLL ANIMATIONS
// MIND THE ORDER! ScrollTrigger computes positions in creation order, and pins push down the
// triggers created after them. Do not reorder without checking the result on desktop and mobile.
// Requires the scroll (initSmoothScroll) to be initialised already.
// ------------------------------------------------------------

import { gsap, ScrollTrigger } from '../core/gsap';
import { isTouchDevice } from '../core/screen';
import { SCROLLER_SELECTOR } from '../core/scroll';

import { initAppear, initParallax } from './generic';
import { initCovers } from './covers';
import { initThreeHorizontalSteps } from './s06-three-horizontal-steps';
import { initGalleriesMobile, initGalleriesDesktop } from './galleries';
import { initVignettesImage, initVignettesFloating, initVignettesAppear, initVignettesLines, initEffectChain } from './s09-floating-vignettes';
import { initRisingText } from './s11-rising-text-over-pinned-image';
import { initMagnifyHighlight, initMagnifyPin } from './s14-magnify-list';
import { initVerticalPoints, initVerticalPointsPin } from './s16-vertical-points';

export function loadAllAnimations() {

    ScrollTrigger.defaults({
        toggleActions: "restart pause resume none",
        markers: false,
        scroller: SCROLLER_SELECTOR,
        pinType: isTouchDevice ? 'fixed' : 'transform'
    });

    initAppear();
    initParallax();
    initCovers();
    initThreeHorizontalSteps();
    initGalleriesMobile();
    initRisingText();
    initVerticalPoints();

    // desktop only
    gsap.matchMedia().add("(min-width: 768px)", () => {
        initGalleriesDesktop();
        initVignettesImage();
        initVerticalPointsPin();
    });

    initMagnifyHighlight();
    initVignettesFloating();
    initVignettesAppear();
    initVignettesLines();
    initEffectChain();
    initMagnifyPin();
}
