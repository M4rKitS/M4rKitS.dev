/* Ventana de conocimientos: pestañas accesibles, cambio automático y teclado. */
export function initWorkbench() {
  var wb = document.querySelector('[data-wb]');
  if (!wb) {
    return;
  }
  var tabs = [].slice.call(wb.querySelectorAll('[role=tab]')),
    panels = [].slice.call(wb.querySelectorAll('[role=tabpanel]'));
  var DUR = 8000,
    cur = 0,
    timer = null,
    user = false,
    vis = false,
    reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  wb.style.setProperty('--dur', DUR + 'ms');
  var pbox = wb.querySelector('.wb-panels');
  function fit() {
    if (window.innerWidth < 900) {
      pbox.style.height = '';
      return;
    }
    var p = panels[cur];
    pbox.style.height = p.offsetHeight + 'px';
  }
  function show(i, focus) {
    cur = i;
    tabs.forEach(function (t, k) {
      var on = k === i;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      if (on) {
        panels[k].removeAttribute('hidden');
      } else {
        panels[k].setAttribute('hidden', '');
      }
    });
    fit();
    if (focus) {
      tabs[i].focus();
    }
    var t = tabs[i],
      st = wb.querySelector('.wb-tabs');
    if (st.scrollWidth > st.clientWidth + 2) {
      var dx = t.getBoundingClientRect().left - st.getBoundingClientRect().left - 16;
      st.scrollTo({ left: Math.max(0, st.scrollLeft + dx), behavior: 'smooth' });
    }
    restart();
  }
  function stop() {
    clearTimeout(timer);
    wb.classList.remove('auto');
  }
  function restart() {
    stop();
    if (user || reduce || !vis) {
      return;
    }
    void wb.offsetWidth;
    wb.classList.add('auto');
    timer = setTimeout(function () {
      show((cur + 1) % tabs.length);
    }, DUR);
  }
  tabs.forEach(function (t, k) {
    t.addEventListener('click', function () {
      user = true;
      show(k);
    });
    t.addEventListener('keydown', function (e) {
      var n = null,
        L = tabs.length;
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
        n = (k + 1) % L;
      } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
        n = (k - 1 + L) % L;
      } else if (e.key === 'Home') {
        n = 0;
      } else if (e.key === 'End') {
        n = L - 1;
      }
      if (n !== null) {
        e.preventDefault();
        user = true;
        show(n, true);
      }
    });
  });
  window.addEventListener('resize', fit);
  window.addEventListener('load', fit);
  document.addEventListener('click', function (ev) {
    if (ev.target.closest && ev.target.closest('.lang button')) {
      setTimeout(fit, 80);
    }
  });
  fit();
  if ('ResizeObserver' in window) {
    var ro = new ResizeObserver(function () {
      fit();
    });
    panels.forEach(function (p) {
      ro.observe(p);
    });
  }
  wb.addEventListener('mouseenter', function () {
    wb.classList.add('paused');
    clearTimeout(timer);
  });
  wb.addEventListener('mouseleave', function () {
    wb.classList.remove('paused');
    restart();
  });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(
      function (l) {
        vis = l[0].isIntersecting;
        if (vis) {
          restart();
        } else {
          stop();
        }
      },
      { threshold: 0.35 },
    ).observe(wb);
  } else {
    vis = true;
    restart();
  }
}
