/* Cabecera y navegación: menú móvil, aviso de sección activa y aterrizaje exacto en los enlaces #ancla. */
import { tx } from './i18n.js?v=a4715f7c';
export function initNav() {
  var hdr = document.querySelector('.hdr'),
    spyFn = null;
  var mq = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)');
  var hbc = 0;
  function measureHb() {
    if (hdr && !hdr.classList.contains('open')) {
      hbc = hdr.getBoundingClientRect().bottom;
    }
  }
  function hb() {
    return hbc || (hdr ? hdr.getBoundingClientRect().bottom : 0);
  }
  measureHb();
  window.addEventListener('resize', measureHb);
  window.addEventListener('load', measureHb);
  if (hdr) {
    hdr.addEventListener('transitionend', function () {
      measureHb();
    });
  }
  function maxY() {
    return Math.max(0, document.documentElement.scrollHeight - innerHeight);
  }
  function target(el) {
    var main = document.querySelector('main');
    if (main && main.firstElementChild === el) {
      return 0;
    }
    var first = el.firstElementChild || el;
    var r = first.getBoundingClientRect(),
      er = el.getBoundingClientRect();
    var top = r.top + scrollY,
      h = er.bottom + scrollY - top;
    var gap = 40,
      pv = el.previousElementSibling;
    if (pv && pv.lastElementChild) {
      gap = top - (pv.lastElementChild.getBoundingClientRect().bottom + scrollY);
    }
    var h0 = hb(),
      vis = innerHeight - h0 - 28;
    var lo = h0 + 20,
      hi = Math.max(lo, h0 - 12 + gap);
    var centered = h0 + 14 + Math.max(0, (vis - h) / 2);
    var T = h > vis ? Math.max(lo, Math.min(hi, h0 + 28)) : Math.max(lo, Math.min(centered, hi));
    return Math.max(0, Math.min(maxY(), Math.round(top - T)));
  }
  function go(id, smooth) {
    var el = document.getElementById(id);
    if (!el) return;
    var y = target(el);
    if (smooth && !(mq && mq.matches)) {
      window.scrollTo({ top: y, behavior: 'smooth' });
    } else {
      var de = document.documentElement,
        old = de.style.scrollBehavior;
      de.style.scrollBehavior = 'auto';
      window.scrollTo(0, y);
      de.style.scrollBehavior = old;
      if (spyFn) spyFn();
    }
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href^="#"]') : null;
    if (!a) return;
    var id = a.getAttribute('href').slice(1);
    if (!id || !document.getElementById(id)) return;
    e.preventDefault();
    go(id, true);
    try {
      history.replaceState(null, '', '#' + id);
    } catch (x) {}
  });
  var moved = false;
  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (ev) {
    window.addEventListener(
      ev,
      function () {
        moved = true;
      },
      { passive: true, once: true },
    );
  });
  function fromHash() {
    if (moved) return;
    var id = decodeURIComponent((location.hash || '').slice(1));
    if (id && document.getElementById(id)) {
      go(id, false);
    }
  }
  function hold() {
    var t0 = Date.now();
    (function tick() {
      if (moved || Date.now() - t0 > 2600) {
        return;
      }
      var id = decodeURIComponent((location.hash || '').slice(1)),
        el = id && document.getElementById(id);
      if (el) {
        var y = target(el);
        if (Math.abs(window.scrollY - y) > 2) {
          var de = document.documentElement,
            o = de.style.scrollBehavior;
          de.style.scrollBehavior = 'auto';
          window.scrollTo(0, y);
          de.style.scrollBehavior = o;
        }
      }
      requestAnimationFrame(tick);
    })();
  }
  if ((location.hash || '').length > 1) {
    hold();
  }
  window.addEventListener('load', function () {
    fromHash();
    setTimeout(fromHash, 350);
    setTimeout(fromHash, 1000);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(fromHash);
    }
  });
  if (hdr) {
    var hm = hdr.querySelector('.hm'),
      openY = 0;
    function setOpen(o) {
      hdr.classList.toggle('open', o);
      if (hm) {
        hm.setAttribute('aria-expanded', o ? 'true' : 'false');
        hm.setAttribute('aria-label', tx(o ? 'm_close' : 'm_open') || (o ? 'Cerrar menú' : 'Abrir menú'));
      }
      if (o) {
        openY = window.scrollY;
      }
    }
    if (hm) {
      setOpen(false);
      hm.addEventListener('click', function (e) {
        e.stopPropagation();
        setOpen(!hdr.classList.contains('open'));
      });
      document.addEventListener('click', function (e) {
        if (hdr.classList.contains('open') && !hdr.contains(e.target)) {
          setOpen(false);
        }
      });
      hdr.querySelectorAll('.hn a').forEach(function (a) {
        a.addEventListener('click', function () {
          setOpen(false);
        });
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && hdr.classList.contains('open')) {
          setOpen(false);
          hm.focus();
        }
      });
      window.addEventListener(
        'scroll',
        function () {
          if (hdr.classList.contains('open') && Math.abs(window.scrollY - openY) > 40) {
            setOpen(false);
          }
        },
        { passive: true },
      );
      window.addEventListener('resize', function () {
        if (window.innerWidth >= 960 && hdr.classList.contains('open')) {
          setOpen(false);
        }
      });
      document.addEventListener('click', function (e) {
        if (e.target.closest && e.target.closest('.lang button')) {
          setTimeout(function () {
            hm.setAttribute('aria-label', tx(hdr.classList.contains('open') ? 'm_close' : 'm_open'));
          }, 80);
        }
      });
    }
    var items = [].slice
      .call(hdr.querySelectorAll('.hn a[href^="#"]'))
      .map(function (a) {
        return { a: a, el: document.getElementById(a.getAttribute('href').slice(1)) };
      })
      .filter(function (x) {
        return x.el;
      });
    var tick = false;
    function spy() {
      tick = false;
      if (!items.length) return;
      var probe = hb() + (innerHeight - hb()) * 0.4,
        cur = null;
      items.forEach(function (it) {
        if (it.el.getBoundingClientRect().top <= probe) {
          cur = it;
        }
      });
      if (scrollY >= maxY() - 4) {
        cur = items[items.length - 1];
      }
      var hn = hdr.querySelector('.hn'),
        prevCur = null;
      function edge() {
        if (hn) {
          hn.classList.toggle('at-end', hn.scrollLeft + hn.clientWidth >= hn.scrollWidth - 4);
        }
      }
      items.forEach(function (it) {
        var on = it === cur;
        it.a.classList.toggle('on', on);
        if (on) {
          it.a.setAttribute('aria-current', 'true');
        } else {
          it.a.removeAttribute('aria-current');
        }
      });
      if (hn && cur && cur !== prevCur && hn.scrollWidth > hn.clientWidth + 4) {
        prevCur = cur;
        hn.scrollTo({
          left: Math.max(0, cur.a.offsetLeft - hn.clientWidth / 2 + cur.a.offsetWidth / 2),
          behavior: 'smooth',
        });
      }
      edge();
    }
    if (hdr.querySelector('.hn')) {
      hdr.querySelector('.hn').addEventListener(
        'scroll',
        function () {
          var h = hdr.querySelector('.hn');
          h.classList.toggle('at-end', h.scrollLeft + h.clientWidth >= h.scrollWidth - 4);
        },
        { passive: true },
      );
    }
    window.addEventListener(
      'scroll',
      function () {
        if (!tick) {
          tick = true;
          requestAnimationFrame(spy);
        }
      },
      { passive: true },
    );
    window.addEventListener('resize', spy);
    spyFn = spy;
    spy();
  }
}
