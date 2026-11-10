// ------------------------------------------------------------
// s09 · FLOATING VIGNETTES
// - left image with a slow parallax: it drifts down the section as it scrolls past (desktop only)
// - group 1: floating drawings that fade in one by one with the scroll
// - group 2: vignettes that fade in and lines that slide in from the side
// - group 3: effect chain (inline SVG + texts): the cable draws itself with the scroll and each
//   effect fades in as the cable reaches it
// ------------------------------------------------------------

import { gsap, ScrollTrigger } from '../core/gsap';

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

// Each drawing fades in on its own, tied to the scroll, as it rises through the screen.
export function initVignettesFloating() {
    gsap.utils.toArray('.js-floating-item').forEach(item => {
        gsap.to(item, {
            scrollTrigger: {
                trigger: item,
                start: 'top 85%',
                end: 'top 60%',
                scrub: true,
            },
            opacity: 1,
            ease: 'none'
        });
    });
}

export function initVignettesAppear() {
    gsap.utils.toArray(".vignette-group .square-card, .vignette-group .vignette p, .vignette__right").forEach(item => {
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

// Group 3 · effect chain. One timeline scrubbed with the scroll: input jack, then each cable draws
// itself and the effect box it reaches fades in (with its text on desktop), then the output jack.
// On mobile the texts sit below the drawing, so each one fades in on its own as it rises.
export function initEffectChain() {
    const chain = document.querySelector('.fx-chain');
    const svg = chain && chain.querySelector('svg');
    if (!svg) return;

    const cables = gsap.utils.toArray(chain.querySelectorAll('.js-fx-cable'));
    const boxes = gsap.utils.toArray(chain.querySelectorAll('.gsap-fx-box'));
    const jacks = gsap.utils.toArray(chain.querySelectorAll('.gsap-fx-jack'));
    const texts = gsap.utils.toArray(chain.querySelectorAll('.gsap-fx-text'));

    // The cables use non-scaling strokes, so their dashes are measured on screen:
    // path length (viewBox units) × scale of the drawing, plus a little margin for the round caps.
    const viewBoxWidth = svg.viewBox.baseVal.width;
    const screenLength = cable => cable.getTotalLength() * svg.getBoundingClientRect().width / viewBoxWidth + 4;

    gsap.matchMedia().add({ desktop: '(min-width: 768px)', mobile: '(max-width: 767px)' }, context => {
        const { desktop } = context.conditions;

        // Each cable keeps its own progress (0 → 1) and is drawn from it. Its screen length changes
        // with the column width, so it is measured again on every refresh and the cable redrawn.
        // (Function-based from-values would not be applied to the cables the scroll has not reached yet.)
        const cableStates = cables.map(cable => ({ cable, progress: 0, length: 0 }));
        const draw = state => {
            state.cable.style.strokeDasharray = state.length;
            state.cable.style.strokeDashoffset = state.length * (1 - state.progress);
        };
        const measure = () => cableStates.forEach(state => {
            state.length = screenLength(state.cable);
            draw(state);
        });
        measure();
        ScrollTrigger.addEventListener('refresh', measure);

        const tl = gsap.timeline({
            scrollTrigger: {
                trigger: chain,
                start: 'top 80%',
                end: 'bottom 55%',
                scrub: true,
            },
            defaults: { ease: 'none' },
        });

        tl.to(jacks[0], { opacity: 1, duration: 0.3 });
        cableStates.forEach((state, i) => {
            // each cable takes a time proportional to its length, so the signal travels at one speed
            tl.to(state, { progress: 1, duration: state.cable.getTotalLength() / 150, onUpdate: () => draw(state) });
            if (boxes[i]) {
                tl.to(desktop && texts[i] ? [boxes[i], texts[i]] : boxes[i], { opacity: 1, duration: 0.6 });
            }
        });
        tl.to(jacks[1], { opacity: 1, duration: 0.3 });

        if (!desktop) {
            texts.forEach(text => {
                gsap.to(text, {
                    scrollTrigger: { trigger: text, start: 'top 85%', end: 'top 65%', scrub: true },
                    opacity: 1,
                    ease: 'none',
                });
            });
        }

        return () => {
            ScrollTrigger.removeEventListener('refresh', measure);
            cables.forEach(cable => gsap.set(cable, { clearProps: 'strokeDasharray,strokeDashoffset' }));
        };
    });
}
