// GSAP with ScrollTrigger registered. Every module imports gsap and ScrollTrigger from here,
// so the plugin is registered once and before it is used.

import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

export { gsap, ScrollTrigger };
