/* Visor de certificados: al pulsar una tarjeta se abre una ventana con la imagen. */
import { tx } from './i18n.js?v=a4715f7c';
export function initCerts() {
  var dlg = document.getElementById('cd');
  if (!dlg || typeof dlg.showModal !== 'function') {
    return;
  }
  var img = document.getElementById('cd-img'),
    ico = document.getElementById('cd-ico'),
    tt = document.getElementById('cd-tt'),
    ext = document.getElementById('cd-ext'),
    xb = document.getElementById('cd-x'),
    last = null;
  document.querySelectorAll('.cc[data-cert]').forEach(function (b) {
    b.addEventListener('click', function () {
      last = b;
      var s = b.getAttribute('data-cert'),
        n = b.querySelector('b').textContent,
        a = tx('cert_alt').replace('{n}', n);
      img.alt = a;
      img.sizes = '(max-width:760px) 100vw, 1100px';
      img.srcset = '/img/cert-' + s + '-800.webp 800w, /img/cert-' + s + '-1400.webp 1400w';
      img.src = '/img/cert-' + s + '-1400.webp';
      ico.textContent = '';
      (b.getAttribute('data-ic') || '').split(' ').forEach(function (p) {
        if (!p) {
          return;
        }
        var t = document.createElement('i'),
          m = document.createElement('img');
        m.src = p;
        m.alt = '';
        m.width = 16;
        m.height = 16;
        t.appendChild(m);
        ico.appendChild(t);
      });
      tt.textContent = n;
      ext.href = '/img/cert-' + s + '-1400.webp';
      dlg.setAttribute('aria-label', a);
      xb.setAttribute('aria-label', tx('w_close') || 'Cerrar');
      document.documentElement.classList.add('bw-lock');
      dlg.showModal();
    });
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
    img.removeAttribute('src');
    img.removeAttribute('srcset');
    document.documentElement.classList.remove('bw-lock');
    if (last) {
      last.focus({ preventScroll: true });
    }
  });
}
