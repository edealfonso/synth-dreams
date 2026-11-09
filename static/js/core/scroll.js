// ------------------------------------------------------------
// SCROLL
// Two systems depending on the device:
// - non-touch: smooth-scrollbar on #body-scroller, wired to ScrollTrigger with scrollerProxy
// - touch: native scroll of #body-scroller
// This module hides the difference: the rest of the code uses getScrollTop(), onScroll(),
// isVisible() and universalYScroll() without asking which system is active.
// ------------------------------------------------------------

import Scrollbar from 'smooth-scrollbar';
import { gsap, ScrollTrigger } from './gsap';
import { isTouchDevice } from './screen';

export const SCROLLER_SELECTOR = '#body-scroller'; // project-specific!

let bodyScrollBar = null;

// Must be called BEFORE creating any ScrollTrigger
export function initSmoothScroll() {
    if (isTouchDevice) return;

    const body_scroller_element = document.querySelector(SCROLLER_SELECTOR);

    bodyScrollBar = Scrollbar.init(body_scroller_element, {
        damping: 0.1,
        delegateTo: document,
        alwaysShowTracks: true
    });

    ScrollTrigger.scrollerProxy(body_scroller_element, {
        scrollTop(value) {
            if (arguments.length) {
                bodyScrollBar.scrollTop = value;
            }
            return bodyScrollBar.scrollTop;
        }
    });

    bodyScrollBar.addListener(ScrollTrigger.update);

    // Only needed to fix the position of the debug markers; not needed in production
    if (document.querySelector('.gsap-marker-scroller-start')) {
        const markers = gsap.utils.toArray('[class *= "gsap-marker"]');
        bodyScrollBar.addListener(({ offset }) => {
            gsap.set(markers, { marginTop: -offset.y });
        });
    }
}

// Current vertical scroll, with either system
export function getScrollTop() {
    return !isTouchDevice ? bodyScrollBar.scrollTop : $(SCROLLER_SELECTOR).scrollTop();
}

// Calls callback(scrollY) on every scroll
export function onScroll(callback) {
    if (!isTouchDevice) {
        bodyScrollBar.addListener(({ offset }) => {
            callback(offset.y);
        });
    } else {
        $(SCROLLER_SELECTOR).on('scroll', () => {
            callback($(SCROLLER_SELECTOR).scrollTop());
        });
    }
}

// ------------------------------------------------------------
// IS VISIBLE
// - returns whether an element (jQuery object) is on screen
// ------------------------------------------------------------

export function isVisible(element) {
    if (!isTouchDevice) {
        // on regular screens, use smooth-scrollbar's method
        return bodyScrollBar.isVisible(element[0]);
    } else {
        // on touch screens, use ScrollTrigger's method
        return ScrollTrigger.isInViewport(element[0]);
    }
}

// --------------------------------------------------------------------------------
// UNIVERSAL SCROLL (WITH OR WITHOUT SMOOTH SCROLLBAR)
// - scrolls with smooth scrollbar (desktop) or native scroll (touch)
// - while it runs, body has the `smooth-scrolling` class (scrolling does not trigger videos or header)
// --------------------------------------------------------------------------------

export function universalYScroll(opt) {

    const {
        scroll_container = $(SCROLLER_SELECTOR), // container with native scroll on touch devices
        scroll_bar = bodyScrollBar,

        y = 0,
        element = false,
        time = 500,
        callback = ()=>{},

        iterative = false, // optional iterative scroll
        iterative_time = 100, // iterative scroll duration

    } = opt;

    $('body').addClass('smooth-scrolling');
    adaptiveScroll(time);

    setTimeout(function() {

        if (iterative) {
            const loop = setInterval(function() {
                if ( getElementOffset() > 5 ) {
                    adaptiveScroll(iterative_time);
                } else {
                    clearInterval(loop);
                    $('body').removeClass('smooth-scrolling');
                    callback();
                }
            }, iterative_time);

        } else {
            $('body').removeClass('smooth-scrolling');
            callback();
        }
    },time);


    function adaptiveScroll(t) {

        // on desktop, scroll with the "smooth-scrollbar" plugin
        if (!isTouchDevice) {
            scroll_bar.scrollTo( 0, getTargetScroll(), t );

        // on touch devices, use the native scroll
        } else {
            scroll_container.animate({
                scrollTop: getTargetScroll()
            }, t);
        }
    }

    function getTargetScroll() {
        return element? getScrolled() + getElementOffset() : y;
    }

    function getElementOffset() {
        return element.offset().top;
    }

    function getScrolled() {
        return isTouchDevice ? scroll_container.scrollTop() : scroll_bar.scrollTop;
    }
}
