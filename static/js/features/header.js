// ------------------------------------------------------------
// HEADER
// - checkHeader(scroll): hidden/visible classes depending on position (on the home it appears after the cover)
// - slideHeader(visible): hides it when scrolling down and shows it when scrolling up
// - checkHeaderTheme(): white logo text / menu while they sit over a `.js-header-dark` element
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

// Checks the logo and the menu separately (a split section can be dark on one side only).
// Positions are measured as if the header were at the top, so it is right when it slides back in.
export function checkHeaderTheme() {

    let header = document.querySelector('header');
    if (!header) return;

    let darkElements = [...document.querySelectorAll('.js-header-dark')]
        .map(el => el.getBoundingClientRect())
        .filter(rect => rect.width && rect.height);
    let headerTop = header.getBoundingClientRect().top;

    [['.header__logo', 'header__logo--light'], ['.header__menu', 'header__menu--light']].forEach(([selector, lightClass]) => {
        let el = header.querySelector(selector);
        if (!el) return;
        let rect = el.getBoundingClientRect();
        let x = rect.left + rect.width / 2;
        let y = rect.top - headerTop + rect.height / 2;
        let overDark = darkElements.some(d => x >= d.left && x <= d.right && y >= d.top && y <= d.bottom);
        el.classList.toggle(lightClass, overDark);
    });
}
