# -*- coding: utf-8 -*-
"""CSS de la capa de movimiento: barra de progreso y entrada del hero (solo CSS, sin esperar a JavaScript).
El resto (GSAP + ScrollTrigger) vive en js/motion.js."""

MOTION_CSS = """.sp{position:fixed;left:0;top:0;width:100%;height:3px;transform-origin:0 50%;transform:scaleX(0);background:linear-gradient(90deg,#1B46C8,#38BDF8);z-index:90;pointer-events:none}
@keyframes hin{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
@media(prefers-reduced-motion:no-preference){
.hero .pl{animation:hin .6s cubic-bezier(.2,.7,.2,1) backwards}
.hero .h1{animation:hin .95s cubic-bezier(.2,.7,.2,1) .12s backwards}
.hero .lead{animation:hin .75s cubic-bezier(.2,.7,.2,1) .32s backwards}
.hero .cta>*{animation:hin .6s cubic-bezier(.2,.7,.2,1) .52s backwards}
.hero .cta>*:nth-child(2){animation-delay:.62s}
}"""
