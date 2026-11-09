/* En pantallas táctiles, resalta la tarjeta de certificado más cercana al centro al hacer scroll. */
export function initCardHighlight() {
  var cards = [].slice.call(document.querySelectorAll('.cc'));
  if (!cards.length) return;
  if (!(window.matchMedia && matchMedia('(hover:none)').matches)) return;
  var tick = false;
  function update() {
    tick = false;
    var mid = window.innerHeight / 2,
      best = null,
      bd = 1e9;
    cards.forEach(function (c) {
      var r = c.getBoundingClientRect();
      var d = Math.abs((r.top + r.bottom) / 2 - mid);
      if (d < bd) {
        bd = d;
        best = r.top;
      }
    });
    var on = bd < window.innerHeight * 0.42;
    cards.forEach(function (c) {
      var r = c.getBoundingClientRect();
      c.classList.toggle('lit', on && Math.abs(r.top - best) < 8);
    });
  }
  function req() {
    if (!tick) {
      tick = true;
      requestAnimationFrame(update);
    }
  }
  window.addEventListener('scroll', req, { passive: true });
  window.addEventListener('resize', req);
  update();
}
