/* En pantallas táctiles, destaca el plan más cercano al centro al hacer scroll. */
export function initPlanHighlight() {
  var box = document.querySelector('.plans');
  if (!box) return;
  var cards = [].slice.call(box.querySelectorAll('.plc'));
  if (!cards.length) return;
  if (!(window.matchMedia && matchMedia('(hover:none)').matches)) return;
  var tick = false;
  function update() {
    tick = false;
    var H = window.innerHeight,
      mid = H / 2,
      hot = null,
      best = 1e9;
    cards.forEach(function (c) {
      var r = c.getBoundingClientRect();
      var d = r.top <= mid && r.bottom >= mid ? 0 : Math.min(Math.abs(r.top - mid), Math.abs(r.bottom - mid));
      if (d < best) {
        best = d;
        hot = c;
      }
    });
    var on = hot && best < H * 0.3;
    box.classList.toggle('focus', !!on);
    cards.forEach(function (c) {
      c.classList.toggle('hot', !!on && c === hot);
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
