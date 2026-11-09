// ------------------------------------------------------------
// PINNED COVERS
// s01, s04 and s13: #{id}-cover stays fixed while #{id}-container scrolls over it
// ------------------------------------------------------------

import { gsap } from '../core/gsap';

export function initCovers() {
    [
        's01',
        's04',
        's13',
    ]
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
