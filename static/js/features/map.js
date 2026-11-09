// ------------------------------------------------------------
// FOOTER MAP
// - .js-activate-map toggles it; clicking the map or scrolling up closes it
// ------------------------------------------------------------

export function initMap() {

    $('#map').removeClass('initial');

    $('.js-activate-map').on('click', () => {
        $('#map').toggleClass('active');
    });

    $('#map').on('click', () => {
        closeMap();
    });
}

export function closeMap() {
    $('#map').removeClass('active');
}
