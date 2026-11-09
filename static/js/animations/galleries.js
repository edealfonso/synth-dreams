// ------------------------------------------------------------
// s07 AND s12 · PINNED GALLERIES
// - mobile: each image is pinned and moves up a little while the next one scrolls past
// - desktop: each pair of images (#s07-pair-0/2, #s12-pair-0/2) is pinned and its .gallery__row moves up
// ------------------------------------------------------------

import { gsap } from '../core/gsap';

export function initGalleriesMobile() {
    gsap.utils.toArray( '.gsap-mobilegallerypic' ).forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: $(item).parent()[0],
                start: "top top",
                end: "top -100%",
                pin: true,
                pinSpacing: false,
                scrub: true,
            },
            yPercent: -40
        });
    });
}

// desktop only (called inside gsap.matchMedia)
export function initGalleriesDesktop() {
    [
        's07-pair-0','s07-pair-2',
        's12-pair-0','s12-pair-2'
    ]
    .forEach(function(id) {
        gsap.to('#' + id + ' .gallery__row', {
            scrollTrigger: {
                trigger: '#' + id,
                start: "top top",
                end: "bottom top",
                pin: true,
                pinSpacing: false,
                scrub: true,
                pinType: 'transform'
            },
            yPercent: -40
        });
    });
}
