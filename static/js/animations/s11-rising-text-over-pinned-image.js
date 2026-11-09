// ------------------------------------------------------------
// s11 · RISING TEXT OVER PINNED IMAGE
// - the title fades in in place; the text fades in and rises a little
// - the image, below it, stays pinned in the middle of the screen and zooms in until the end of the section
// ------------------------------------------------------------

import { gsap } from '../core/gsap';

export function initRisingText() {
    // the title stays in place and only fades in
    gsap.to('#s11-title', {
        scrollTrigger: {
            trigger: '#s11-title',
            start: "top 85%",
            end: "top 60%",
            scrub: 1,
        },
        opacity: 1
    });

    // the text fades in and rises a little, slightly after the title
    gsap.to('#s11-body', {
        scrollTrigger: {
            trigger: '#s11-body',
            start: "top 90%",
            end: "top 55%",
            scrub: 1,
        },
        y: 0,
        opacity: 1
    });

    // pinned without spacing: the section's own height gives the scroll distance,
    // so the triggers below do not move
    gsap.to('#s11-image', {
        scrollTrigger: {
            trigger: '#s11-image',
            start: "center center",
            end: () => '+=' + Math.max(0, $('#s11').outerHeight() - $('#s11-text-container').outerHeight() - $('#s11-image').outerHeight()),
            pin: true,
            pinSpacing: false,
            scrub: 1,
            invalidateOnRefresh: true,
        },
        scale: 1,
        ease: "none"
    });
}
