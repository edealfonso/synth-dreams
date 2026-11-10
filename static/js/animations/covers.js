// ------------------------------------------------------------
// PINNED COVERS
// s01, s04 and s13: #{id}-cover stays fixed while #{id}-container scrolls over it
// A cover missing from the page (s04 is skipped by the template when it has no video) gets no trigger
// ------------------------------------------------------------

import { gsap } from '../core/gsap';

export function initCovers() {
    [
        's01',
        's04',
        's13',
    ]
    .filter(id => document.getElementById(`${id}-container`))
    .forEach(function(id) {
        gsap.to(`#${id}-cover`, {
            scrollTrigger: {
                trigger: `#${id}-container`,
                start: "top top",
                end: "bottom top",
                scrub: 1,
                pin: true,
                pinSpacing: false
            },
        });
    });
}
