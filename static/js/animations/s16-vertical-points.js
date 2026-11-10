// ------------------------------------------------------------
// s16 · VERTICAL POINTS
// - the three points slide in from the side
// - desktop only: the image stays vertically centred while the points scroll past
// ------------------------------------------------------------

import { gsap } from '../core/gsap';

export function initVerticalPoints() {
    [
        '#s16-point-1',
        '#s16-point-2',
        '#s16-point-3'
    ]
    .forEach(function(id) {
        gsap.to(id, {
            scrollTrigger: {
                trigger: id,
                start: "top 85%",
                end: "top 70%",
                scrub: 3,
            },
            x: 0,
            opacity: 1
        });
    });
}

// desktop only (called inside gsap.matchMedia)
export function initVerticalPointsPin() {
    gsap.timeline({
        scrollTrigger:{
            trigger: "#s16-image",
            pin: true,
            pinSpacing: false,
            start: () => "top " + (window.innerHeight - $('#s16-image').height()) * 0.5,
            end: () => '+=' + ($('#s16-container').height() - $('#s16-image').height()),
        }
    });
}
