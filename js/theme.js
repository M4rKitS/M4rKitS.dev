/* Modo claro y oscuro, recordado en localStorage (clave prop_theme). */
import { tx } from './i18n.js?v=7e053824';
export function initTheme() {
  var root = document.documentElement;
  function cur() {
    return root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
  }
  function label() {
    var d = cur() === 'dark';
    document.querySelectorAll('.th').forEach(function (b) {
      var t = tx(d ? 'th_light' : 'th_dark');
      b.setAttribute('aria-pressed', d ? 'true' : 'false');
      if (t) {
        b.setAttribute('aria-label', t);
        b.setAttribute('title', t);
      }
      var s = b.querySelector('.th-t');
      if (s) {
        var u = tx(d ? 'th_l_light' : 'th_l_dark');
        if (u) {
          s.textContent = u;
        }
      }
    });
    var m = document.querySelector('meta[name=theme-color]');
    if (m) {
      m.setAttribute('content', d ? '#0A1226' : '#DAE1EB');
    }
  }
  function set(t, anim) {
    if (anim) {
      root.classList.add('th-anim');
      setTimeout(function () {
        root.classList.remove('th-anim');
      }, 600);
    }
    if (t === 'dark') {
      root.setAttribute('data-theme', 'dark');
    } else {
      root.removeAttribute('data-theme');
    }
    try {
      localStorage.setItem('prop_theme', t);
    } catch (e) {}
    label();
  }
  document.querySelectorAll('.th').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.stopPropagation();
      set(cur() === 'dark' ? 'light' : 'dark', true);
    });
  });
  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('.lang button')) {
      setTimeout(label, 80);
    }
  });
  label();
}
