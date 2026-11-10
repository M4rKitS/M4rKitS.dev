/* Selector ES/EN: marca el idioma activo y lleva a la misma página en el otro idioma. */
import { lang } from './i18n.js';

export function initLangSwitch() {
  document.querySelectorAll('.lang button').forEach(function (b) {
    b.setAttribute('aria-pressed', b.getAttribute('data-l') === lang ? 'true' : 'false');
    b.addEventListener('click', function () {
      var h = b.getAttribute('data-href');
      if (b.getAttribute('data-l') !== lang && h) {
        location.href = h + location.hash;
      }
    });
  });
}
