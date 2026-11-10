// ============================================================================
// ENTRY POINT (webpack)
// Only orchestrates the lifecycle; the logic lives in the modules.
// The setTimeouts (100/500/1000 ms) shape how the page enters: do not change them lightly.
// jQuery (`$`) is global: ProvidePlugin injects it.
// ============================================================================

// DM Sans (free font, SIL OFL 1.1, self-hosted through @fontsource): the weights and styles the SCSS uses
import '@fontsource/dm-sans/400';
import '@fontsource/dm-sans/400-italic';
import '@fontsource/dm-sans/500';
import '@fontsource/dm-sans/500-italic';
import '@fontsource/dm-sans/600';
import '../scss/index.scss';

import { ScrollTrigger } from './core/gsap';
import { calcScreen } from './core/screen';
import { initSmoothScroll, getScrollTop, onScroll, universalYScroll } from './core/scroll';
import { loadAllAnimations } from './animations';
import { checkLocationHash, initSmoothAnchors } from './features/anchors';
import { checkVideos } from './features/autovideo';
import { initFirstContentfulSection, revealSecondContentfulSection, releaseScroll } from './features/cover';
import { checkHeader, checkHeaderTheme, slideHeader } from './features/header';
import { initMap, closeMap } from './features/map';
import { changeToWebP } from './utils/webp';

$(function () {

    // stop the browser from restoring the scroll position on reload
    if ('scrollRestoration' in history) {
        history.scrollRestoration = 'manual';
    }

    // ______________________________
    // Runs BEFORE the content becomes visible
    // ''''''''''''''''''''''''''''''

    calcScreen();
    initSmoothScroll(); // before creating any ScrollTrigger
    changeToWebP();
    initSmoothAnchors();
    initFirstContentfulSection();

    // One tick later (jQuery 3 defers a nested ready): lets the layout settle before the
    // ScrollTriggers measure heights. Removing it changes the computed positions.
    $(function () {

        checkLocationHash();
        loadAllAnimations();

        setTimeout(()=>{ // give the animations time to settle before showing the content

            // ______________________________
            // make visible
            // ''''''''''''''''''''''''''''''
            $('#loader-content').removeClass('onload-hidden').addClass('onload-showed');

            // back to the top in case the user has already scrolled
            universalYScroll({
                y: 0,
                callback: onContentVisible
            });

            onScroll(scrollActions);

            $(window).on('resize orientationchange', function(){
                calcScreen();
                checkVideos();
                checkHeaderTheme();
            });

        }, 1000);

    });
});

// ______________________________
// Runs AFTER the content becomes visible
// ''''''''''''''''''''''''''''''

function onContentVisible() {
    revealSecondContentfulSection();
    releaseScroll();
    checkVideos();
    checkHeader(getScrollTop());
    checkHeaderTheme();
    initMap();
}

// ============================================================================
// ON SCROLL
// ============================================================================

let previousScroll = 0;
let firstScroll = false;

function scrollActions(scroll) {

    // during a programmatic scroll, videos and header are not checked
    if (!$('body.smooth-scrolling')[0]) {
        checkVideos();
        checkHeader(scroll);
    }
    checkHeaderTheme();

    if (scroll > previousScroll) {
        // scrolling down
        slideHeader(false);
    } else {
        // scrolling up
        slideHeader(true);
        closeMap();
    }
    previousScroll = scroll;

    // on the first scroll, refresh gsap
    if (!firstScroll) {
        ScrollTrigger.refresh();
        firstScroll = true;
    }
}
