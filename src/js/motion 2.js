/* Capa de movimiento con GSAP + ScrollTrigger (alojados en /vendor, sin CDN).
   Se carga cuando la página ya ha terminado de cargar, para no retrasar la primera pintura.
   La entrada del hero se hace en CSS; aquí van la barra de progreso, las apariciones en cascada
   y la cinta de tecnologías, que se acelera con la velocidad del scroll.
   Todo se desactiva con prefers-reduced-motion. */

function startMotion() {
  if (!window.gsap || !window.ScrollTrigger) {
    return;
  }
  gsap.registerPlugin(ScrollTrigger);
  var mm = gsap.matchMedia();
  mm.add('(prefers-reduced-motion: no-preference)', function () {
    var cleanups = [];
    /* 1. barra de progreso */
    var bar = document.createElement('div');
    bar.className = 'sp';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);
    gsap.to(bar, {
      scaleX: 1,
      ease: 'none',
      scrollTrigger: {
        trigger: document.documentElement,
        start: 'top top',
        end: 'bottom bottom',
        scrub: 0.25,
      },
    });
    /* 2. aparición en cascada al hacer scroll */
    function run(els) {
      els.forEach(function (e) {
        e.style.transition = 'none';
      });
    }
    function done(els) {
      els.forEach(function (e) {
        e.style.transition = '';
      });
    }
    function batchIn(sel, y, st) {
      var list = gsap.utils.toArray(sel);
      if (!list.length) {
        return;
      }
      gsap.set(list, y ? { y: y, opacity: 0 } : { opacity: 0 });
      ScrollTrigger.batch(list, {
        start: 'top 90%',
        once: true,
        onEnter: function (els) {
          run(els);
          gsap.to(els, {
            y: 0,
            opacity: 1,
            duration: 0.85,
            stagger: st,
            ease: 'power3.out',
            overwrite: true,
            clearProps: 'transform,opacity',
            onComplete: function () {
              done(els);
            },
          });
        },
      });
    }
    batchIn('main .sec .pl,main .sec .h2,main .sec p.one,main .sec .note', 22, 0.1);
    batchIn('.cc', 26, 0.07);
    batchIn('.plc', 40, 0.14);
    batchIn('.wk', 40, 0.14);
    batchIn('.who > *,.goal > *', 36, 0.14);
    batchIn('.ctab', 0, 0.1);
    /* 3. la cinta de tecnologías se acelera con la velocidad del scroll */
    var mq = document.querySelector('.mq-t');
    if (mq && mq.getAnimations) {
      var an = mq.getAnimations()[0];
      if (an) {
        var target = 1,
          rate = 1;
        ScrollTrigger.create({
          start: 0,
          end: 'max',
          onUpdate: function (self) {
            target = 1 + Math.min(5, Math.abs(self.getVelocity()) / 700);
          },
        });
        var tick = function () {
          target += (1 - target) * 0.05;
          rate += (target - rate) * 0.12;
          an.playbackRate = rate;
        };
        gsap.ticker.add(tick);
        cleanups.push(function () {
          gsap.ticker.remove(tick);
          an.playbackRate = 1;
        });
      }
    }
    /* tipografías y carga: recalcular posiciones */
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () {
        ScrollTrigger.refresh();
      });
    }
    window.addEventListener('load', function () {
      ScrollTrigger.refresh();
    });
    return function () {
      cleanups.forEach(function (f) {
        f();
      });
      bar.remove();
    };
  });
}

function loadScript(src, cb) {
  var e = document.createElement('script');
  e.src = src;
  e.onload = cb;
  document.head.appendChild(e);
}

function load() {
  loadScript('/vendor/gsap.min.js', function () {
    loadScript('/vendor/ScrollTrigger.min.js', startMotion);
  });
}

export function initMotion() {
  if (document.readyState === 'complete') {
    setTimeout(load, 0);
  } else {
    window.addEventListener('load', function () {
      setTimeout(load, 0);
    });
  }
}
