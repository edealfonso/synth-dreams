// ------------------------------------------------------------
// GENERIC CLASS-BASED ANIMATIONS
// - .gsap-appear: fades in when it enters the screen
// - .gsap-parallax[-min|-reverse|-scale|-bg]: scroll-linked parallax; the trigger is the parent
// ------------------------------------------------------------

import { gsap } from '../core/gsap';

export function initAppear() {
    gsap.utils.toArray(".gsap-appear").forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: item,
                toggleActions: "resume pause resume none",
                start: "top 90%",
            },
            opacity: 1,
            duration: 1.5
        });
    });
}

export function initParallax() {

    // parallax
    gsap.utils.toArray( '.gsap-parallax' ).forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: $(item).parent()[0],
                start: "top bottom",
                end: "bottom 50%",
                scrub: true,
            },
            yPercent: 40,
        });
    });

    // parallax (minimal)
    gsap.utils.toArray( '.gsap-parallax-min' ).forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: $(item).parent()[0],
                start: "top 80%",
                end: "bottom bottom",
                scrub: true,
            },
            y: "0",
        });
    });

    // parallax (reverse)
    gsap.utils.toArray( '.gsap-parallax-reverse' ).forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: $(item).parent()[0],
                start: "top bottom",
                end: "bottom 50%",
                scrub: true,
            },
            yPercent: -20,
        });
    });

    // parallax with scale
    gsap.utils.toArray( '.gsap-parallax-scale' ).forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: $(item).parent()[0],
                start: "top bottom",
                end: "bottom 50%",
                scrub: true,
            },
            yPercent: 40,
            scale: 1.08
        });
    });

    // parallax for background images
    gsap.utils.toArray( '.gsap-parallax-bg' ).forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: $(item).parent()[0],
                start: "top bottom",
                end: "bottom top",
                scrub: true,
            },
            top: "0"
        });
    });
}
