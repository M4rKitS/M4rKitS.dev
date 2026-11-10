/* Formulario de contacto: validación, envío con EmailJS y enlace de WhatsApp con el mensaje del idioma y del plan. */
import { tx, lang, cfg } from './i18n.js?v=7e053824';
export function initContactForm() {
  var f = document.getElementById('contact-form');
  if (!f) return;
  var st = document.getElementById('cf-st'),
    btn = document.getElementById('cf-btn'),
    send = f.querySelector('.cf-send'),
    wa = document.getElementById('cf-wa');
  var SERVICE = 'service_utwds39',
    T_OWNER = 'template_9bv8r1n',
    T_REPLY = 'template_dnumxnq',
    KEY = 'd4w05JCeQd75BiH0Q';
  var PRIV = cfg.priv,
    THANKS = cfg.thanks,
    t0 = Date.now();
  var live = !/^(localhost|127\.0\.0\.1)$/.test(location.hostname) || /[?&]send=1/.test(location.search);
  function say(k, cls) {
    st.className = 'cf-st' + (cls ? ' ' + cls : '');
    if (k) {
      st.setAttribute('data-t', k);
      st.innerHTML = tx(k);
    } else {
      st.removeAttribute('data-t');
      st.textContent = '';
    }
  }
  function bad(el, k) {
    el.setAttribute('aria-invalid', 'true');
    say(k, 'err');
    el.focus();
  }
  function plan() {
    return f.elements.plan.value;
  }
  function waLink() {
    var t = tx('cf_wa_text'),
      p = plan();
    if (p !== '0') {
      var nm = tx('pl' + p + '_n');
      if (nm) {
        t += ' ' + tx('cf_wa_plan').replace('{n}', nm);
      }
    }
    return wa.getAttribute('data-base') + '?text=' + encodeURIComponent(t);
  }
  wa.setAttribute('data-base', wa.getAttribute('href').split('?')[0]);
  ['click', 'mouseenter', 'focus', 'touchstart'].forEach(function (ev) {
    wa.addEventListener(
      ev,
      function () {
        wa.href = waLink();
      },
      { passive: true },
    );
  });
  f.addEventListener('input', function (e) {
    if (e.target.removeAttribute) e.target.removeAttribute('aria-invalid');
    say('');
  });
  document.querySelectorAll('[data-plan]').forEach(function (a) {
    a.addEventListener('click', function () {
      var r = f.querySelector('input[name=plan][value="' + a.getAttribute('data-plan') + '"]');
      if (r) {
        r.checked = true;
      }
    });
  });
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var n = f.elements.name,
      m = f.elements.email,
      t = f.elements.message,
      c = f.elements.consent;
    [n, m, t, c].forEach(function (x) {
      x.removeAttribute('aria-invalid');
    });
    if (!n.value.trim()) {
      return bad(n, 'cf_e_name');
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(m.value.trim())) {
      return bad(m, 'cf_e_email');
    }
    if (!t.value.trim()) {
      return bad(t, 'cf_e_msg');
    }
    if (!c.checked) {
      return bad(c, 'cf_e_consent');
    }
    if (f.elements.website.value) {
      return;
    }
    if (Date.now() - t0 < 2500) {
      return;
    }
    send.disabled = true;
    btn.setAttribute('data-t', 'cf_sending');
    btn.innerHTML = tx('cf_sending');
    say('');
    var nm = n.value.trim(),
      em = m.value.trim(),
      biz = (f.elements.business.value || '').trim(),
      p = plan();
    var svc = p !== '0' ? tx('pl' + p + '_n') : tx('cf_idk');
    var subject = svc + (biz ? ' · ' + biz : '');
    var message =
      t.value.trim() +
      ' — Negocio: ' +
      (biz || '(no indicado)') +
      ' · Servicio: ' +
      svc +
      ' · Idioma: ' +
      lang.toUpperCase();
    var priv =
      location.origin.replace(/^http:\/\/(127\.0\.0\.1|localhost)(:\d+)?$/, 'https://m4rkits.dev') +
      '/' +
      PRIV;
    var owner = { from_name: nm, from_email: em, subject: subject, message: message };
    var reply = {
      from_name: nm,
      from_email: em,
      subject: subject,
      reply_subject: tx('cf_re_subj'),
      reply_message: tx('cf_re_msg').replace('{name}', nm).replace('{priv}', priv),
    };
    function done() {
      f.reset();
      window.location.href = THANKS;
    }
    function fail() {
      send.disabled = false;
      btn.setAttribute('data-t', 'cf_send');
      btn.innerHTML = tx('cf_send');
      say('cf_e_send', 'err');
    }
    if (!live || !window.emailjs) {
      setTimeout(done, 700);
      return;
    }
    /* EmailJS: aviso para Marcos y respuesta automatica al visitante */
    window.emailjs.init(KEY);
    Promise.all([
      window.emailjs.send(SERVICE, T_OWNER, owner),
      window.emailjs.send(SERVICE, T_REPLY, reply),
    ]).then(done, function (err) {
      if (window.console) {
        console.error('EmailJS', err && err.status);
      }
      fail();
    });
  });
}
