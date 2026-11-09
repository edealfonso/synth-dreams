// ------------------------------------------------------------
// HEADER
// - checkHeader(scroll): hidden/visible classes depending on position (on the home it appears after the cover)
// - slideHeader(visible): hides it when scrolling down and shows it when scrolling up
// ------------------------------------------------------------

let headerFixed = true;
let headerUnfixing = false;

export function checkHeader(scroll) {

    let header = $('header');
    let screenHeight = window.innerHeight;

    // the header appears from this scroll position on (not before)
    let headerMinScroll = $('.template-home')[0] ? screenHeight - 200 : 0;

    // the first time the user scrolls between headerMinScroll and this value, the header stays put for a moment
    let headerFixScroll = $('.template-home')[0] ? 2*screenHeight - 5 : 100;

    if (scroll < headerMinScroll ) {
        header.addClass('hidden');
        header.removeClass('visible');
    } else {
        if (scroll >= headerFixScroll) {
            if (headerFixed) {
                if (!headerUnfixing) {
                    headerUnfixing = true;
                    setTimeout(() => {
                        headerFixed = false;
                    },1000);
                }
            } else {
                header.removeClass('hidden');
                header.removeClass('visible');
            }
        } else {
            header.addClass('visible');
            header.removeClass('hidden');
        }
    }
}

export function slideHeader(visible) {
    $("header").css('top', visible ? '0' : '-200px');
}
