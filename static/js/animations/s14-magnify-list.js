// ------------------------------------------------------------
// s14 · MAGNIFY LIST
// - each .magnify-item lights up as it crosses the middle of the screen and dims afterwards
// - the container stays pinned for the whole section
// ------------------------------------------------------------

import { gsap } from '../core/gsap';
import { screen } from '../core/screen';

export function initMagnifyHighlight() {
    gsap.utils.toArray(".magnify-item").forEach(item => {
        gsap.timeline({
            scrollTrigger: {
                trigger: item,
                start: () => {
                    if (screen.isMobile) {
                        return "top bottom";
                    } else {
                        return "top 65%";
                    }
                },
                end: () => {
                    if (screen.isMobile) {
                        return "top top";
                    } else {
                        return "top 35%";
                    }
                },
                scrub: true,
            },
        })
        .to(item, {opacity: 1, ease: "none", duration: 1})
        .to(item, {opacity: 0.3, ease: "none", duration: 1,});
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
