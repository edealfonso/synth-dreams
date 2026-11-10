// ------------------------------------------------------------
// s07 AND s12 · PINNED GALLERIES
// - mobile: each image is pinned and moves up a little while the next one scrolls past
//   (on touch devices it is pinned by CSS instead, and does not move: see initGalleriesMobile)
// - desktop: each pair of images (#s07-pair-0/2, #s12-pair-0/2) is pinned and its .gallery__row moves up
// ------------------------------------------------------------

import { gsap } from '../core/gsap';
import { isTouchDevice } from '../core/screen';

export function initGalleriesMobile() {
    // Touch devices: native scroll runs ahead of the JS, so a JS pin (and the JS rise) jumped on
    // every image. The images are pinned with position: sticky instead (special/_images.scss).
    if (isTouchDevice) {
        $('.gallery--mobile').addClass('sticky');
        return;
    }

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
