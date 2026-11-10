/* Vista previa de proyectos: ventana con aviso de consentimiento antes de cargar contenido externo. */
import { tx, lang } from './i18n.js';
export function initProjects() {
  var wl = document.getElementById('wl');
  if (!wl) return;
  var dlg = document.getElementById('bw'),
    fr = document.getElementById('bw-f'),
    hostEl = document.getElementById('bw-host'),
    ext = document.getElementById('bw-ext'),
    extt = document.getElementById('bw-extt'),
    dsc = document.getElementById('bw-d'),
    load = document.getElementById('bw-load'),
    xb = document.getElementById('bw-x');
  var gate = document.getElementById('bw-gate'),
    gp = document.getElementById('bw-gate-p'),
    go = document.getElementById('bw-go'),
    gx = document.getElementById('bw-gx'),
    pending = '';
  wl.querySelectorAll('button.wk').forEach(function (b) {
    b.addEventListener('click', function () {
      open(b);
    });
  });
  var last = null;
  function open(b) {
    if (!dlg || typeof dlg.showModal !== 'function') {
      window.open(b.getAttribute('data-ext'), '_blank', 'noopener');
      return;
    }
    last = b;
    var src = b.getAttribute('data-src');
    if (!/^https?:/.test(src)) {
      src = src + (src.indexOf('?') < 0 ? '?' : '&') + 'lang=' + lang;
    }
    dlg.setAttribute('aria-label', b.querySelector('.wk-t').textContent);
    fr.title = b.querySelector('.wk-t').textContent;
    hostEl.textContent = b.getAttribute('data-host');
    ext.href = b.getAttribute('data-ext');
    var ek = b.getAttribute('data-extk');
    extt.setAttribute('data-t', ek);
    extt.innerHTML = tx(ek);
    ext.setAttribute('aria-label', tx(ek));
    var dk = b.getAttribute('data-desc');
    dsc.setAttribute('data-t', dk);
    dsc.innerHTML = tx(dk);
    xb.setAttribute('aria-label', tx('w_close'));
    var external = /^https?:/.test(src) && !/^https?:\/\/(www\.)?m4rkits\.dev(\/|$)/.test(src);
    pending = '';
    gate.hidden = !external;
    load.hidden = external;
    if (external) {
      gp.innerHTML = tx('w_gate_p').replace('{h}', '<b>' + b.getAttribute('data-host') + '</b>');
      gx.href = b.getAttribute('data-ext');
      pending = src;
    }
    document.documentElement.classList.add('bw-lock');
    dlg.showModal();
    if (external) {
      go.focus({ preventScroll: true });
    } else {
      fr.src = src;
    }
  }
  go.addEventListener('click', function () {
    if (!pending) return;
    gate.hidden = true;
    load.hidden = false;
    fr.src = pending;
    pending = '';
  });
  fr.addEventListener('load', function () {
    if (fr.getAttribute('src') && fr.getAttribute('src') !== 'about:blank') {
      load.hidden = true;
    }
  });
  function shut() {
    if (dlg.open) {
      dlg.close();
    }
  }
  xb.addEventListener('click', shut);
  dlg.addEventListener('click', function (e) {
    if (e.target === dlg) {
      shut();
    }
  });
  dlg.addEventListener('close', function () {
    fr.src = 'about:blank';
    pending = '';
    gate.hidden = true;
    document.documentElement.classList.remove('bw-lock');
    if (last) {
      last.focus({ preventScroll: true });
    }
  });
}
