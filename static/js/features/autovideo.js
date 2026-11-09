// ------------------------------------------------------------
// AUTOVIDEO
// - lazy loading: the video is loaded (from data-src) when its container becomes visible
// - .js-autovideo: a single video
// - .js-autovideo-responsive: two videos (.autovideo__video--mobile / --desktop); the right one is kept
// - once loaded (.js-autovideo-loaded): paused when off screen and resumed when back
// - controls: [data-action=audio|rewind|playpause] inside .js-autovideo-controls
// ------------------------------------------------------------

import { ScrollTrigger } from '../core/gsap';
import { screen, calcScreen } from '../core/screen';
import { isVisible } from '../core/scroll';

// runs when the cover is revealed, on scroll and on resize
export function checkVideos() {

    $('.js-autovideo').each(function () {

        let container = $(this);

        if (isVisible(container)) {
            loadVideo(container);
        }
    });

    $('.js-autovideo-responsive').each(function () {

        let container = $(this);

        calcScreen();

        if (isVisible(container)) {
            if (screen.isTablet) {
                loadVideo(container, 'mobile');
            } else {
                loadVideo(container, 'desktop');
            }
        }

    });

    $('.js-autovideo-loaded').each(function () {

        let container = $(this);

        if (isVisible(container)) {
            if (!container.hasClass('playing')) replayVideo(container);
        } else {
            if (container.hasClass('playing')) stopVideo(container);
        }
    });
}

function loadVideo($container, responsive = false) {

    let $video;

    // find the video
    if (responsive) {
        $video = $container.find(".autovideo__video--" + responsive);
        $container.removeClass('js-autovideo-responsive');
        $container.addClass('js-autovideo-loaded');
    } else {
        $video = $container.find("video");
        $container.removeClass('js-autovideo');
        $container.addClass('js-autovideo-loaded');
    }

    $container.addClass('playing');

    var video_src = $video.data('src');
    $video.find('source').attr('src', video_src);
    $video.css('opacity', '0');
    $video.css('transition','opacity 0.5s ease');

    const video = $video[0];

    setTimeout(function () {
        video.load();
        video.play();
        $video.css('opacity', '1');

        // event listeners
        $container.find('.js-autovideo-controls [data-action=audio]').on('click', function() {
            if ($container.hasClass('sound-on')) {
                video.muted = true;
                $container.removeClass('sound-on');
            } else {
                video.muted = false;
                $container.addClass('sound-on');
            }
        });
        $container.find('.js-autovideo-controls [data-action=rewind]').on('click', function() {
            video.currentTime = 0;
        });
        $container.find('.js-autovideo-controls [data-action=playpause]').on('click', function() {
            if ($container.hasClass('playing')) {
                video.pause();
                $container.removeClass('playing');
            } else {
                video.play();
                $container.addClass('playing');
            }
        });

    }, 500);

    setTimeout(function () {
        $video.addClass('loaded');
        $container.find("video:not(.loaded)").remove();

        // removing the video breaks ScrollTrigger's pinSpacing calculation,
        // so refresh to get it right again
        ScrollTrigger.refresh();
    }, 100);
}

function stopVideo($container) {
    let $video = $container.find("video.loaded");
    $video[0].pause();
    $container.removeClass('playing');
}

function replayVideo($container) {
    let $video = $container.find("video.loaded");
    $video[0].play();
    $container.addClass('playing');
    $video.css('opacity', '1');
}
