// ------------------------------------------------------------
// s14 · MAGNIFY LIST
// - each .magnify-item lights up as it rises to the middle of the screen and stays lit
// - the container stays pinned for the whole section
// ------------------------------------------------------------

import { gsap } from '../core/gsap';

export function initMagnifyHighlight() {
    gsap.utils.toArray(".magnify-item").forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: item,
                start: "top 90%",
                end: "top 50%",
                scrub: true,
            },
            opacity: 1,
            ease: "none"
        });
    });
}

export function initMagnifyPin() {
    gsap.timeline({
        scrollTrigger:{
            trigger: "#s14-container",
            pin: true,
            pinSpacing: false,
            start: "top top",
            end:'+=' + ($('#s14').height() - window.innerHeight),
        }
    });
}
