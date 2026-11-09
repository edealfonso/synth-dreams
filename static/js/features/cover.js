// ________________________________
// COVER REVEAL, IN TWO STEPS
// 1. revealFirstContentfulSection: photo at 75% as soon as its image loads
// 2. revealSecondContentfulSection: the photo fades toward white, logo and arrow appear
//    (once the content is shown, or earlier on the first scroll gesture)
// ''''''''''''''''''''''''''''''''

const SCROLL_KEYS = [' ', 'ArrowDown', 'ArrowUp', 'PageDown', 'PageUp', 'Home', 'End'];

export function initFirstContentfulSection() {

    // when the cover image loads (or right away if it was already cached)
    $(".js-firstload").one("load", function() {
        revealFirstContentfulSection();
    }).each(function() {
        if (this.complete) {
            setTimeout(function() {
                revealFirstContentfulSection();
            },100);
        }
    });

    // in case the image is slow or missing
    setTimeout(function() {
        revealFirstContentfulSection();
    },1000);

    // during the entry sequence the page must not move (the content is still hidden and is
    // scrolled back to the top when it appears): a scroll gesture only reveals the logo
    ['wheel', 'touchmove', 'keydown'].forEach(function(type) {
        window.addEventListener(type, holdScrollDuringEntry, { capture: true, passive: false });
    });
}

function holdScrollDuringEntry(event) {
    if (event.type === 'keydown' && !SCROLL_KEYS.includes(event.key)) return;
    event.preventDefault();
    event.stopImmediatePropagation();
    revealSecondContentfulSection();
}

// called once the content is visible: scrolling works normally from here on
export function releaseScroll() {
    ['wheel', 'touchmove', 'keydown'].forEach(function(type) {
        window.removeEventListener(type, holdScrollDuringEntry, { capture: true });
    });
}

let fullyRevealed = false;

function revealFirstContentfulSection() {
    // the 1 s fallback can fire after a scroll gesture: never undo the second step
    if (fullyRevealed) return;
    $('#s01-container').css('opacity',0.75);
}

export function revealSecondContentfulSection() {
    if (fullyRevealed) return;
    fullyRevealed = true;
    $('#s01-container').css('opacity',1).addClass('faded');
    $('#s01-logo').removeClass('hidden');
    $('#s01-chevron').css('opacity',1);
}
