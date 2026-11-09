// ------------------------------------------------------------
// s06 · THREE HORIZONTAL STEPS
// - the three steps rise and fade in
// - mobile: each step is its own trigger; desktop: staggered along the #s06 scroll
// ------------------------------------------------------------

import { gsap } from '../core/gsap';
import { screen } from '../core/screen';

export function initThreeHorizontalSteps() {
    [
        '#s06-step-1',
        '#s06-step-2',
        '#s06-step-3'
    ]
    .forEach(function(id) {
        gsap.to(id, {
            scrollTrigger: {
                trigger: () => {
                    if (screen.isMobile) {
                        return id;
                    } else {
                        return '#s06';
                    }
                },
                start: () => {
                    if (screen.isMobile) {
                        return "top 85%";
                    } else {
                        switch (id) {
                            case '#s06-step-1':
                                return "top 75%";
                            case '#s06-step-2':
                                return "top 50%";
                            case '#s06-step-3':
                                return "top 30%";
                        }
                    }
                },
                end: () => {
                    if (screen.isMobile) {
                        return "top 65%";
                    } else {
                        switch (id) {
                            case '#s06-step-1':
                                return "top 40%";
                            case '#s06-step-2':
                                return "top 30%";
                            case '#s06-step-3':
                                return "top 20%";
                        }
                    }
                },
                scrub: 2,
            },
            y: 0,
            opacity: 1,
        });
    });
}
