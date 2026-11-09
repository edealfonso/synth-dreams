// ________________________________
// COVER REVEAL, IN TWO STEPS
// 1. revealFirstContentfulSection: cover at half opacity as soon as its image loads
// 2. revealSecondContentfulSection: full cover, logo and arrow (once the content is shown)
// ''''''''''''''''''''''''''''''''

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
}

function revealFirstContentfulSection() {
    $('#s01-container').css('opacity',0.6);
}

export function revealSecondContentfulSection() {
    $('#s01-container').css('opacity',1);
    $('#s01-logo').removeClass('hidden');
    $('#s01-chevron').css('opacity',1);
}
