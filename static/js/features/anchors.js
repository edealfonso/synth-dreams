// ----------------------------------------
// SMOOTH SCROLL TO ANCHORS (HASH)
// - when the URL has a #hash, scrolls down to that element
// - .js-smooth-anchor links smooth-scroll (iteratively) to their href
// ----------------------------------------

import { universalYScroll } from '../core/scroll';

export function checkLocationHash() {
    const the_hash = location.hash;

    if (the_hash) {
        universalYScroll({
            element: $(the_hash),
            time: 10
        });
    }
}

export function initSmoothAnchors() {
    $('.js-smooth-anchor').click( function(event) {

        event.preventDefault();

        let target_element = $($(this).attr('href'));

        universalYScroll({
            element: target_element,
            time: 1500,
            iterative: true,
            iterative_time: 300,
        });
    });
}
