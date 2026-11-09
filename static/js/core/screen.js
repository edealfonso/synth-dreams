// ------------------------------------------------------------
// SCREEN AND DEVICE
// - `screen`: responsive flags. It is a live object: calcScreen() updates its properties,
//   so importers always read the current value (screen.isMobile, etc.)
// - `isTouchDevice`: computed once on load
// ------------------------------------------------------------

export const screen = {
    isLaptop: false,      // <= 1200 px
    isTablet: false,      // <= 990 px
    isMobile: false,      // <= 767 px
    isMobileSmall: false, // <= 375 px
};

export function calcScreen() {
    const screenWidth = window.innerWidth;

    screen.isLaptop = screenWidth <= 1200;
    screen.isTablet = screenWidth <= 990;
    screen.isMobile = screenWidth <= 767;
    screen.isMobileSmall = screenWidth <= 375;
}

export const isTouchDevice = (('ontouchstart' in window) ||
        (navigator.maxTouchPoints > 0) ||
        (navigator.msMaxTouchPoints > 0));
