// ------------------------------------------------------------
// s09 · FLOATING VIGNETTES
// - left image with a slow parallax: it drifts down the section as it scrolls past (desktop only)
// - group 1: three floating images that fade in one after another
// - groups 2 and 3: vignettes that fade in and lines that slide in from the side
// ------------------------------------------------------------

import { gsap } from '../core/gsap';

// desktop only (called inside gsap.matchMedia)
// Slow parallax on the left image: while the section crosses the screen, the image drifts from the
// top of the section to its bottom, so it rises into view more slowly than the page and, when the
// section leaves, only its lower part is still showing.
// A transform instead of a pin, so the triggers created after this one keep their positions.
export function initVignettesImage() {
    const travel = () => $('#s09-container').outerHeight() - $('#s09-image').outerHeight();

    gsap.to('#s09-image', {
        scrollTrigger: {
            trigger: '#s09-container',
            start: 'top bottom',
            end: 'bottom top',
            scrub: true,
            invalidateOnRefresh: true,
        },
        y: travel,
        ease: 'none'
    });
}

export function initVignettesFloating() {
    gsap.timeline({
        scrollTrigger: {
            trigger: ".vignette-group--1",
            start: "top 30%",
            toggleActions: "resume pause resume none",
        }
    })
    .to('#s09-floating-0', {
        opacity: 1,
        duration: 1.5,
        ease: 'ease-in-out'
    })
    .to('#s09-floating-1', {
        opacity: 1,
        duration: 1.5,
        ease: 'ease-in-out'
    },'-=1')
    .to('#s09-floating-2', {
        opacity: 1,
        duration: 1.5,
        ease: 'ease-in-out'
    },'-=1');
}

export function initVignettesAppear() {
    gsap.utils.toArray(".vignette-group .square-card, .vignette-group .vignette p, .vignette-group .vignette__right-alt .vignette__text, .vignette-group .vignette__right-alt .vignette__extra, .vignette__right").forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: item,
                start: "top 70%",
                toggleActions: "resume pause resume none",
            },
            opacity: 1,
            duration: 1.5,
            ease: 'ease-in-out'
        });
    });
}

export function initVignettesLines() {
    gsap.utils.toArray(".js-vignette-line").forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: item,
                start: "top 70%",
                toggleActions: "resume pause resume none",
            },
            x: 0,
            duration: 1,
            ease: 'ease'
        });
    });
}
