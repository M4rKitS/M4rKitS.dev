/* Palabras clave en cursiva: el destello se repite al entrar en pantalla. */
export function initShine() {
  if (!('IntersectionObserver' in window)) {
    return;
  }
  var io = new IntersectionObserver(
    function (list) {
      list.forEach(function (e) {
        var t = e.target;
        if (e.isIntersecting) {
          t.classList.remove('shine');
          void t.offsetWidth;
          t.classList.add('shine');
        } else {
          t.classList.remove('shine');
        }
      });
    },
    { threshold: 0.6 },
  );
  function init() {
    io.disconnect();
    document.querySelectorAll('em').forEach(function (e) {
      io.observe(e);
    });
  }
  init();
  document.addEventListener('click', function (ev) {
    if (ev.target.closest && ev.target.closest('.lang button')) {
      setTimeout(init, 60);
    }
  });
}
