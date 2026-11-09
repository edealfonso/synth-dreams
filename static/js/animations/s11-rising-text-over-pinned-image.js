// ------------------------------------------------------------
// s11 · RISING TEXT OVER PINNED IMAGE
// - the image is pinned for a while and the text rises over it
// ------------------------------------------------------------

import { gsap } from '../core/gsap';

export function initRisingText() {

    gsap.to('#s11-image', {
        scrollTrigger: {
            trigger: '#s11',
            start: "top 50%",
            end: "top -65%",
            pin: true,
            pinSpacing: false,
        },
    });

    gsap.to('#s11-text', {
        scrollTrigger: {
            trigger: '#s11-container',
            start: "top top",
            end: "top -20%",
            scrub: 2.5,
        },
        y: () => {
            if (window.innerHeight > 1200) {
                return "-65%";
            } else {
                return "-55%";
            }
        },
        opacity: 1
    });
}
