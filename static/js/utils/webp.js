// ----------------------------------------
// WEBP FOR BACKGROUND IMAGES
// - checks whether the browser supports webp
// - if it does, keeps the current background image url as a fallback and adds the webp version
// - if the webp version does not exist, that request returns a 404
// ----------------------------------------

function canUseWebp() {
    let useWebp = false;
    if (typeof document === 'object') {
        // client-side rendering
        const canvas = document.createElement('canvas');

        if (
            canvas.getContext &&
            canvas.getContext('2d') &&
            canvas.toDataURL('image/webp').indexOf('data:image/webp') === 0
        ) {
            useWebp = true;
        }
    }
    return useWebp;
}

function getExtension(filename) {
    return filename.substring(filename.lastIndexOf(".") + 1);
}

export function changeToWebP() {
    if (canUseWebp()) {

        $('*').each(function(){
            let el = $(this);
            let oldbg = el.css('background-image');
            if (oldbg != 'none' && oldbg.startsWith('url(')) {

                let oldurl = /^url\((['"]?)(.*)\1\)$/.exec(oldbg);
                oldurl = oldurl ? oldurl[2] : "";
                let oldext = getExtension(oldurl);

                if (oldext == 'jpg' || oldext == 'jpeg' || oldext == 'png' ) {
                    let url = `${oldurl}.webp`;
                    el.css('background-image', `${oldbg}, url("${url}")`);
                }
            }
        });
    }
}
