# Propuesta 1 · Aire (referencia portfolio1, Spaceful)
from common import *
import re
import re as _re
from urllib.parse import quote as _quote
from wbdata import AREAS

ES['c9'] = 'SOLID y Bases de datos'
EN['c9'] = 'SOLID and Databases'
ES['c10'] = 'ORMs en Python'
EN['c10'] = 'ORMs in Python'
ES['pl_badge'] = 'Más completo'
EN['pl_badge'] = 'Most complete'
ES['p_kicker'] = 'Soluciones'
EN['p_kicker'] = 'Solutions'
ES['n_plans'] = 'Soluciones'
EN['n_plans'] = 'Solutions'
ES['p_title'] = 'Una web a tu <em>medida</em>'
EN['p_title'] = 'A website <em>made to measure</em>'
ES['w_lead'] = 'Tu negocio merece una web a su altura. Te escucho, lo planteamos juntos y te entrego el resultado listo para publicar.'
EN['w_lead'] = 'Your business deserves a website that matches it. I listen, we shape it together and I hand over a site ready to launch.'
ES['p_note'] = 'Cada proyecto es distinto: hablamos de lo que necesitas, lo ajustamos y entonces te doy un presupuesto concreto.'
EN['p_note'] = 'Every project is different: we talk about what you need, adjust it and then I give you a concrete quote.'
ES['pl_cta'] = 'Pedir presupuesto'
EN['pl_cta'] = 'Request a quote'
ES['p_extras'] = 'Y, si lo necesitas, se puede sumar:'
EN['p_extras'] = 'And, if you need it, you can add:'
ES['pl1_t'] = 'Landing sencilla'; EN['pl1_t'] = 'Simple landing'
ES['pl2_t'] = 'Landing + mantenimiento'; EN['pl2_t'] = 'Landing + maintenance'
ES['pl3_t'] = 'Web completa con SEO y mantenimiento'; EN['pl3_t'] = 'Full website with SEO and maintenance'
ES['pl1_n'] = 'Para empezar'; EN['pl1_n'] = 'To get started'
ES['pl2_n'] = 'Para crecer'; EN['pl2_n'] = 'To grow'
ES['pl3_n'] = 'A medida'; EN['pl3_n'] = 'Tailor-made'
ES['g_card'] = 'Construyo mientras llego'
EN['g_card'] = 'Building while I get there'
ES['g_pending'] = 'Un destino claro y proyectos propios por el camino.'
EN['g_pending'] = 'A clear destination, with projects of my own along the way.'
ES['g_text'] = 'Sigo mi camino hacia ser desarrollador de software Full&nbsp;Stack y, mientras tanto, he decidido crear mi propia marca, M4rKitS.dev, y poner lo que voy aprendiendo al servicio de empresas que necesitan soluciones digitales.'
EN['g_text'] = 'I keep moving toward becoming a Full Stack software developer and, meanwhile, I decided to build my own brand, M4rKitS.dev, and put what I learn to work for companies that need digital solutions.'
ES['cf_name'] = 'Nombre'
EN['cf_name'] = 'Name'
ES['cf_email'] = 'Correo electrónico'
EN['cf_email'] = 'Email'
ES['cf_msg'] = 'Mensaje'
EN['cf_msg'] = 'Message'
ES['cf_ph_name'] = 'Tu nombre'
EN['cf_ph_name'] = 'Your name'
ES['cf_ph_email'] = 'tu@correo.com'
EN['cf_ph_email'] = 'you@email.com'
ES['cf_ph_msg'] = 'Cuéntame a qué te dedicas, qué web imaginas y para cuándo la necesitas…'
EN['cf_ph_msg'] = 'Tell me what you do, what kind of site you imagine and when you need it…'
ES['cf_send'] = 'Enviar mensaje'
EN['cf_send'] = 'Send message'
ES['cf_sending'] = 'Enviando…'
EN['cf_sending'] = 'Sending…'
ES['cf_ok'] = '¡Mensaje enviado! Te respondo muy pronto.'
EN['cf_ok'] = 'Message sent! I will reply very soon.'
ES['cf_e_name'] = 'Escribe tu nombre.'
EN['cf_e_name'] = 'Please enter your name.'
ES['cf_e_email'] = 'Escribe un correo válido para poder responderte.'
EN['cf_e_email'] = 'Please enter a valid email so I can reply.'
ES['cf_e_msg'] = 'Cuéntame un poco qué necesitas.'
EN['cf_e_msg'] = 'Tell me a bit about what you need.'
ES['cf_e_send'] = 'No se ha podido enviar. Inténtalo de nuevo o escríbeme a contact@m4rkits.dev.'
EN['cf_e_send'] = 'It could not be sent. Please try again or write to contact@m4rkits.dev.'
ES['cf_priv'] = 'Solo usaré tus datos para responderte.'
EN['cf_priv'] = 'I will only use your details to reply to you.'
ES['cf_plan'] = '¿Qué tipo de servicio te interesa?'
EN['cf_plan'] = 'What kind of service are you interested in?'
ES['cf_idk'] = 'Aún no lo sé'
EN['cf_idk'] = 'Not sure yet'
ES['cf_biz'] = 'Tu negocio o web actual'
EN['cf_biz'] = 'Your business or current site'
ES['cf_opt'] = 'opcional'
EN['cf_opt'] = 'optional'
ES['cf_ph_biz'] = 'Nombre del negocio o enlace'
EN['cf_ph_biz'] = 'Business name or link'
ES['cf_consent'] = 'Acepto que uses estos datos solo para responder a mi mensaje.'
EN['cf_consent'] = 'I agree that you use these details only to reply to my message.'
ES['cf_re_subj'] = 'He recibido tu mensaje | M4rKitS.dev'; EN['cf_re_subj'] = 'I got your message | M4rKitS.dev'
ES['cf_re_msg'] = 'Hola {name}, gracias por escribirme. He recibido tu mensaje y te responderé lo antes posible. Usaré tus datos solo para responderte; puedes leer cómo los trato en {priv}. Un saludo, Marcos Rodríguez (M4rKitS.dev)'
EN['cf_re_msg'] = 'Hi {name}, thanks for writing to me. I have received your message and will reply as soon as I can. I will use your details only to reply; you can read how I handle them at {priv}. Best regards, Marcos Rodríguez (M4rKitS.dev)'
ES['cf_e_consent'] = 'Marca la casilla para poder enviar el mensaje.'
EN['cf_e_consent'] = 'Tick the box so the message can be sent.'
ES['cf_wa'] = 'Contactar por WhatsApp'
EN['cf_wa'] = 'Contact via WhatsApp'
ES['cf_wa_text'] = 'Hola Marcos, vengo de tu web y me gustaría hablar de un proyecto.'
EN['cf_wa_text'] = "Hi Marcos, I found you through your website and I'd like to talk about a project."
ES['cf_wa_plan'] = 'Me interesa «{n}».'
EN['cf_wa_plan'] = "I'm interested in \u201c{n}\u201d."
ES['cta_text'] = 'Cuéntame qué necesitas y buscamos juntos la mejor solución.'
EN['cta_text'] = 'Tell me what you need and we will find the best solution together.'
ES['w_explore'] = 'Explorar'
EN['w_explore'] = 'Explore'
ES['w_r1'] = 'Web de consultoría de redes sociales'
EN['w_r1'] = 'Social media consultancy website'
ES['w_r2'] = 'Portfolio y captación de clientes'
EN['w_r2'] = 'Portfolio and client acquisition'
ES['w_open'] = 'Abrir en pestaña nueva'
EN['w_open'] = 'Open in a new tab'
ES['w_close'] = 'Cerrar ventana'
EN['w_close'] = 'Close window'
ES['w_loading'] = 'Cargando…'
EN['w_loading'] = 'Loading…'
ES['w_gate_t'] = 'Vas a ver un sitio externo'; EN['w_gate_t'] = 'You are about to view an external site'
ES['w_gate_p'] = 'Se cargará {h} dentro de esta ventana. Es una web de un tercero: puede usar sus propias cookies y verá tu visita. Yo no guardo nada de lo que hagas en ella.'
EN['w_gate_p'] = '{h} will load inside this window. It is a third-party site: it may use its own cookies and will see your visit. I do not store anything you do on it.'
ES['w_gate_go'] = 'Cargar el sitio'; EN['w_gate_go'] = 'Load the site'
ES['w_gate_ext'] = 'Abrir en pestaña nueva'; EN['w_gate_ext'] = 'Open in a new tab'
ES['w_noload'] = '¿No carga? Ábrela en una pestaña nueva'
EN['w_noload'] = 'Not loading? Open it in a new tab'
ES['pr_title'] = 'Proyectos y <em>trabajo real</em>'
EN['pr_title'] = 'Projects and <em>real work</em>'
ES['m_kicker'] = 'Máster Full Stack en <a class="cb" href="https://www.conquerblocks.com/" target="_blank" rel="noopener noreferrer">Conquer Blocks</a>'
EN['m_kicker'] = 'Full Stack Master at <a class="cb" href="https://www.conquerblocks.com/" target="_blank" rel="noopener noreferrer">Conquer Blocks</a>'
ES['h_short'] = 'Estudio el máster Full Stack de <a class="cb" href="https://www.conquerblocks.com/" target="_blank" rel="noopener noreferrer">Conquer Blocks</a> y cuento cada módulo con mis palabras.'
EN['h_short'] = 'I\'m studying the Full Stack master at <a class="cb" href="https://www.conquerblocks.com/" target="_blank" rel="noopener noreferrer">Conquer Blocks</a> and I tell each module in my own words.'
ES['btn_web'] = 'Desarrollo web'
EN['btn_web'] = 'Web development'
ES['mt_home'] = 'Marcos Rodríguez | Desarrollador de software Full Stack'
EN['mt_home'] = 'Marcos Rodriguez | Full Stack software developer'
ES['md_home'] = 'Portfolio de Marcos Rodríguez, desarrollador de software Full Stack en formación: lo que he aprendido en el máster, mis certificados y mis proyectos.'
EN['md_home'] = "Portfolio of Marcos Rodriguez, a Full Stack software developer in training: what I've learned on the master's, my certificates and my projects."
ES['mt_web'] = 'Desarrollo web para pequeños negocios | M4rKitS.dev'
EN['mt_web'] = 'Web development for small businesses | M4rKitS.dev'
ES['md_web'] = 'Diseño y desarrollo web para pequeños negocios: webs claras, rápidas y bien cuidadas, en español e inglés. Cuéntame tu proyecto y buscamos la solución.'
EN['md_web'] = 'Web design and development for small businesses: clear, fast, carefully built websites in Spanish and English. Tell me about your project.'
ES['m_open'] = 'Abrir menú'
EN['m_open'] = 'Open menu'
ES['m_close'] = 'Cerrar menú'
EN['m_close'] = 'Close menu'
ES['th_dark'] = 'Activar modo oscuro'
EN['th_dark'] = 'Switch to dark mode'
ES['th_light'] = 'Activar modo claro'
EN['th_light'] = 'Switch to light mode'
ES['th_l_dark'] = 'Modo oscuro'
EN['th_l_dark'] = 'Dark mode'
ES['th_l_light'] = 'Modo claro'
EN['th_l_light'] = 'Light mode'
ES['m_kicker'] = 'Mi stack'; EN['m_kicker'] = 'My stack'
ES['mq_title'] = 'Con qué <em>trabajo</em>'; EN['mq_title'] = 'What I <em>work with</em>'
ES['k_title'] = 'Lo que he aprendido, <em>por áreas</em>'; EN['k_title'] = 'What I have learned, <em>by area</em>'
ES['who_text'] = 'Soy español y, junto con mi familia, resido actualmente en Finlandia. Desde aquí sigo mi camino hacia convertirme en desarrollador de software. Ahora estoy estudiando el máster Full&nbsp;Stack en <a class="cb" href="https://www.conquerblocks.com/" target="_blank" rel="noopener noreferrer">Conquer Blocks</a>, donde cada módulo me enseña a entender y mantener lo que hay detrás de cada software.'
EN['who_text'] = 'I am Spanish and, together with my family, I currently live in Finland. From here I keep working toward becoming a software developer. I am now studying the Full&nbsp;Stack master at <a class="cb" href="https://www.conquerblocks.com/" target="_blank" rel="noopener noreferrer">Conquer Blocks</a>, where each module teaches me to understand and maintain what sits behind every piece of software.'
LEGAL_FILES = {'aviso': '1-aire-aviso-legal.html', 'priv': '1-aire-privacidad.html', 'cook': '1-aire-cookies.html'}
ES['f_aviso'] = 'Aviso legal'; EN['f_aviso'] = 'Legal notice'
ES['f_priv'] = 'Privacidad'; EN['f_priv'] = 'Privacy'
ES['f_cook'] = 'Cookies'; EN['f_cook'] = 'Cookies'
ES['mt_aviso'] = 'Aviso legal | M4rKitS.dev'; EN['mt_aviso'] = 'Legal notice | M4rKitS.dev'
ES['md_aviso'] = 'Aviso legal de m4rkits.dev: titular del sitio, condiciones de uso y ley aplicable.'; EN['md_aviso'] = 'Legal notice for m4rkits.dev: site owner, terms of use and governing law.'
ES['mt_priv'] = 'Política de privacidad | M4rKitS.dev'; EN['mt_priv'] = 'Privacy policy | M4rKitS.dev'
ES['md_priv'] = 'Política de privacidad de m4rkits.dev: qué datos recojo con el formulario, para qué, con quién los comparto y qué derechos tienes.'; EN['md_priv'] = 'Privacy policy for m4rkits.dev: what data the contact form collects, why, who receives it and your rights.'
ES['mt_cook'] = 'Política de cookies | M4rKitS.dev'; EN['mt_cook'] = 'Cookie policy | M4rKitS.dev'
ES['md_cook'] = 'Política de cookies de m4rkits.dev: qué se guarda en tu navegador y por qué no hace falta banner.'; EN['md_cook'] = 'Cookie policy for m4rkits.dev: what is stored in your browser and why no banner is needed.'
ES['cf_consent'] = 'Acepto que uses estos datos solo para responder a mi mensaje. <a class="cf-pv" href="' + LEGAL_FILES['priv'] + '" target="_blank" rel="noopener">Política de privacidad</a>'
EN['cf_consent'] = 'I agree that my details are used only to reply to my message. <a class="cf-pv" href="' + LEGAL_FILES['priv'] + '" target="_blank" rel="noopener">Privacy policy</a>'
ES['mt_gracias'] = 'Mensaje enviado | M4rKitS.dev'; EN['mt_gracias'] = 'Message sent | M4rKitS.dev'
ES['md_gracias'] = 'Gracias por escribirme. He recibido tu mensaje.'; EN['md_gracias'] = 'Thanks for writing to me. I have received your message.'
ES['cert_view'] = 'Ver certificado'; EN['cert_view'] = 'View certificate'
ES['cert_alt'] = 'Certificado de Conquer Blocks: {n}'; EN['cert_alt'] = 'Conquer Blocks certificate: {n}'
ES['cert_open'] = 'Abrir imagen'; EN['cert_open'] = 'Open image'
ES['lg_upd'] = 'Última actualización'; EN['lg_upd'] = 'Last updated'
ES['who_text2'] = 'Mi meta es seguir creciendo cada día sin ponerme límites.'
EN['who_text2'] = 'My goal is to keep growing every day without setting limits for myself.'
ES['g_text2'] = 'La informática me atrae desde niño y el máster me está dando el método para convertir esa afición en un oficio. Aspiro a vivir de la tecnología sin renunciar a lo que más me importa, que es disfrutar de mi tiempo en familia. Por eso busco trabajar en remoto, con la libertad de dar lo mejor de mí: un trabajo hecho con pasión y cuidado en cada detalle, y soluciones digitales útiles para quien las necesite, esté donde esté.'
EN['g_text2'] = 'Computing has drawn me in since I was a boy, and the master is giving me the method to turn that passion into a profession. I aim to make a living from technology without giving up what matters most to me: enjoying my time with my family. That is why I look for remote work, with the freedom to give my best: work done with passion and attention to every detail, and useful digital solutions for whoever needs them, wherever they are.'


CSS = """
:root{--ink:#0B1F3A;--muted:#566579;--line:#E1E6EE;--card:#F8FAFC;--acc:#2457E6;--acc2:#38BDF8;--f:'Barlow',system-ui,sans-serif;--hd:'Barlow',system-ui,sans-serif;--s:'Fraunces',Georgia,serif;
--rb:linear-gradient(#0B1F3A,#0B1F3A);
--pastel:linear-gradient(#E3E9F2,#E3E9F2)}
body{background:#DAE1EB;color:var(--ink);font-family:var(--f);font-size:1.0625rem;line-height:1.5;font-weight:400}
.frame{max-width:1320px;margin:20px auto 0;background:#fff;border-radius:34px 34px 0 0;position:relative;overflow:clip;box-shadow:0 0 0 1px #ECEEF0}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}
@media(min-width:760px){.wrap{padding:0 32px}}
h1,h2,h3,h4,.pr,.ce b,.fq summary>span:first-child,.logo{font-family:var(--hd)}
em{font-family:var(--s);font-style:italic;font-weight:400;font-size:1.06em;letter-spacing:0;color:var(--acc);padding-right:.06em}
.h1,.h2{font-weight:600;color:var(--ink);text-wrap:balance}
.h1{font-size:clamp(2.35rem,6.2vw,4.5rem);line-height:1.05;letter-spacing:-.01em;text-align:center}
.h2{font-size:clamp(2rem,4.6vw,3.4rem);line-height:1.08}
html{scroll-padding-top:96px}
.hdr{position:fixed;top:14px;left:50%;transform:translateX(-50%);z-index:60;width:calc(100% - 24px);max-width:1120px;background:rgba(236,239,243,.8);-webkit-backdrop-filter:blur(16px) saturate(1.2);backdrop-filter:blur(16px) saturate(1.2);border:1px solid rgba(255,255,255,.85);border-radius:30px;box-shadow:0 16px 36px -22px rgba(11,42,71,.45)}
.hw{padding:8px 10px 8px 14px;display:flex;flex-wrap:wrap;align-items:center;gap:6px 18px}
@media(min-width:960px){.hdr{border-radius:99px}.hw{flex-wrap:nowrap;padding:8px 10px 8px 16px}}
.hero:not(.hero-b),.hero.hero-b{padding-top:clamp(120px,14vw,190px)}
.logo{display:inline-flex;align-items:center;gap:10px;text-decoration:none;font-weight:500;font-size:1.45rem;letter-spacing:-.01em}
.lm{width:30px;height:30px;display:grid;place-items:center;border-radius:7px;border:2px solid transparent;background:linear-gradient(#fff,#fff) padding-box,var(--rb) border-box;font-weight:700;font-size:1rem}
.hn{font-weight:400;order:3;width:100%;display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;color:#5B6F82;font-size:1rem;padding-bottom:2px}
.hn a{padding:7px 12px;border-radius:99px}.hn a.on{color:var(--ink);font-weight:500}.hn a:hover{background:rgba(255,255,255,.7)}
.hn::-webkit-scrollbar{display:none}
.hn a{text-decoration:none;white-space:nowrap}.hn a:hover{color:var(--ink)}
.hr{margin-left:auto;display:flex;align-items:center;gap:12px}
.lang{color:#5B6F82}.lang button[aria-pressed=true]{color:var(--ink);background:#EEF1F4}
@media(min-width:960px){.hn{order:0;width:auto;overflow:visible;margin:0 auto}.hr{margin-left:0}}
.lang button[aria-pressed=true]{background:#fff;box-shadow:0 1px 0 rgba(11,42,71,.08)}
@media(max-width:959px){.hr{gap:4px}.hr .gb.sm{height:36px;padding:0 13px;font-size:.88rem;border-width:2.5px}.logo{font-size:1.1rem;gap:8px}.lm{width:26px;height:26px;font-size:.9rem}.lang button{padding:5px 8px}.hero:not(.hero-b),.hero.hero-b{padding-top:136px}}
.gb{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:50px;padding:0 30px;border-radius:99px;border:3px solid transparent;background:linear-gradient(#fff,#fff) padding-box,var(--rb) border-box;font-weight:500;text-decoration:none;color:#25435F;transition:transform .2s}
.gb.sm{height:42px;padding:0 22px;font-size:.95rem}
.gb:hover,.dk:hover{transform:translateY(-2px)}
.dk{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:46px;padding:0 28px;border-radius:99px;background:var(--ink);color:#fff;font-weight:500;text-decoration:none;box-shadow:0 0 0 3px #fff,0 0 0 4px #E3E7EB;transition:transform .2s}
.og{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:50px;padding:0 28px;border-radius:99px;border:1.5px solid #D8DDE2;background:#fff;color:#5B6F82;text-decoration:none;font-weight:500}
.pl{display:inline-block;padding:10px 22px;border-radius:99px;background:#fff;box-shadow:0 1px 0 #E8EBEE,0 8px 20px -12px rgba(11,42,71,.3);color:#5B6F82;font-size:.95rem}
.hero{position:relative;text-align:center;padding:clamp(56px,9vw,120px) 0 clamp(56px,8vw,96px);isolation:isolate}
.hero::before{content:"";position:absolute;inset:0;z-index:-1;background-image:linear-gradient(#EEF1F4 1px,transparent 1px),linear-gradient(90deg,#EEF1F4 1px,transparent 1px);background-size:82px 82px;-webkit-mask-image:radial-gradient(75% 85% at 50% 35%,#000 25%,transparent 78%);mask-image:radial-gradient(75% 85% at 50% 35%,#000 25%,transparent 78%)}
.hero::after{content:"";position:absolute;inset:-5% -5% 0;z-index:-1;background:radial-gradient(30% 45% at 8% 35%,rgba(246,209,239,.55),transparent 70%),radial-gradient(32% 45% at 96% 18%,rgba(210,241,217,.6),transparent 70%),radial-gradient(28% 40% at 80% 60%,rgba(252,227,210,.55),transparent 70%),radial-gradient(30% 40% at 30% 5%,rgba(207,227,250,.6),transparent 70%);filter:blur(18px)}
.hero .h1{margin:26px auto 0;max-width:15em}
.hero .lead{max-width:30em;margin:22px auto 0;color:var(--muted);font-size:1.15rem}
.cta{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin-top:34px}
.bento{position:relative;max-width:1160px;margin:0 auto;padding:22px;border-radius:32px;background:var(--pastel);display:grid;gap:18px;grid-template-columns:1fr}
.bento img{width:100%;height:100%;object-fit:cover;border-radius:20px}
.bento .mock-bar{display:flex}
.b1{aspect-ratio:4/5;overflow:hidden;border-radius:20px}.b1 img{object-position:50% 12%}
.b2{position:relative;overflow:hidden;border-radius:20px;aspect-ratio:16/9;background:#C7DDF8}.b2 img{object-position:50% 40%}
.chip{position:absolute;left:14px;bottom:14px;display:inline-flex;align-items:center;gap:8px;padding:8px 14px 8px 10px;border-radius:99px;background:rgba(255,255,255,.82);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);box-shadow:0 8px 24px -12px rgba(11,42,71,.5);color:var(--ink);font-size:.9rem;font-weight:500}
.b2 .chip{left:auto;right:14px}
.chip svg{width:18px;height:18px;color:#6a3df0}
.chip small{color:var(--muted);font-size:.82rem;font-weight:400}
.b3{position:relative;display:block;overflow:hidden;border-radius:20px;background:#fff;text-decoration:none;aspect-ratio:4/3;box-shadow:0 0 0 1px rgba(0,0,0,.06)}
.b3 .mock-bar{padding:8px 11px}
.b3 img{display:block;width:100%;height:calc(100% - 30px);object-fit:cover;object-position:top;border-radius:0;clip-path:inset(0 0 9% 0)}
.b3 .go{position:absolute;left:14px;right:14px;bottom:15px;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:6px 7px 6px 15px;border-radius:99px;background:var(--ink);box-shadow:0 10px 24px -10px rgba(11,31,58,.7);color:#fff;font-size:.95rem;font-weight:500;transition:transform .25s,background .25s}
.b3 .go svg{width:30px;height:30px;padding:6px;border-radius:50%;background:#fff;color:var(--ink)}
.b3:hover .go{background:var(--acc)}.b3:hover .go svg{color:var(--acc)}
.b3:hover .go{transform:translateY(-3px)}
.b4{position:relative;overflow:hidden;border-radius:20px;background:#101A2E;color:#DCE6F7;display:flex;flex-direction:column;min-height:230px}
.b4 .ed-bar{display:flex;align-items:center;gap:6px;padding:11px 14px;background:rgba(255,255,255,.05);border-bottom:1px solid rgba(255,255,255,.07)}
.b4 .ed-bar i{width:10px;height:10px;border-radius:50%;background:#FF6B6B}.b4 .ed-bar i:nth-child(2){background:#FFC857}.b4 .ed-bar i:nth-child(3){background:#5BD68A}
.b4 .ed-bar span{margin-left:10px;font:500 .78rem/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:#9FB0CC}
.b4 pre{margin:0;padding:14px 16px 16px;font:400 .84rem/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre;overflow:hidden;flex:1;counter-reset:l}
.b4 pre span.l{display:block;counter-increment:l}
.b4 pre span.l::before{content:counter(l);display:inline-block;width:1.6em;margin-right:12px;text-align:right;color:#4C5B78}
.b4 .k{color:#C792EA}.b4 .p{color:#82AAFF}.b4 .s{color:#9BE3B5}.b4 .o{color:#9FB0CC}
.b4 .cur{display:inline-block;width:7px;height:1.05em;margin-left:2px;vertical-align:-.15em;background:#9BE3B5;animation:blink 1.1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
@media(min-width:860px){.bento{grid-template-columns:1fr 1.15fr 1fr;grid-template-rows:330px minmax(230px,auto)}.b1{grid-row:1/3;aspect-ratio:auto}.b2{grid-column:2/4;aspect-ratio:auto}.b3{aspect-ratio:auto;min-height:230px}}
.tb{position:absolute;left:-18px;bottom:64px;z-index:3;display:flex;flex-direction:column;gap:8px;padding:8px;border-radius:24px;background:#C8CCD1;box-shadow:0 14px 30px -14px rgba(11,42,71,.5)}
.tb a{width:46px;height:46px;display:grid;place-items:center;border-radius:15px;background:#fff;color:var(--ink)}
@media(max-width:859px){.tb{left:10px;bottom:auto;top:30px;flex-direction:row;padding:6px;gap:6px}.tb a{width:38px;height:38px;border-radius:12px}}
.sec{padding:clamp(72px,10vw,140px) 0 0}
.center{text-align:center}
.center .h2{margin-top:22px}
.center p{color:var(--muted);max-width:32em;margin:16px auto 0}
.fl{position:relative;min-height:600px;padding-top:120px}
.fl-c{max-width:620px;margin:0 auto;text-align:center;position:relative;z-index:2}
.fl-p{position:absolute;padding:8px 22px;border-radius:99px;color:#fff;font-weight:500;font-size:1rem;display:none;box-shadow:0 8px 18px -10px rgba(0,0,0,.4)}
.fl-i{position:absolute;display:none;overflow:hidden;box-shadow:0 14px 26px -16px rgba(11,42,71,.5)}
.fl-i img{width:100%;height:100%;object-fit:cover}
.fl-i.ti{background:#fff;place-items:center;color:var(--ink)}
.fl-i.ti svg{width:42%;height:42%}
@media(min-width:900px){.fl-i.ti{display:grid}}
.pillrow{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:32px}
@media(min-width:900px){.fl-p,.fl-i{display:block}.pillrow{display:none}}
.pk{background:#D80FBE}.bl{background:#2AA6F4}.rd{background:#F2503F}.yl{background:#FFB81F;color:#3b2b00}.gr{background:#19B746}.vi{background:#7C5CFF}
.three{display:grid;gap:18px;grid-template-columns:1fr;max-width:1160px;margin:60px auto 0;padding:0 20px}
@media(min-width:860px){.three{grid-template-columns:repeat(3,1fr);padding:0 32px}}
.cd{background:#fff;border:1px solid var(--line);border-radius:28px;padding:18px;box-shadow:0 1px 0 #F1F3F5}
.cd h3{font-weight:500;font-size:1.4rem;margin:22px 10px 10px}
.cd p{margin:0 10px 14px;color:#33506B;font-size:1rem}
.pn{height:210px;border-radius:20px;background:#F3F4F5;display:grid;place-items:center;position:relative;overflow:hidden}
.pn .tool{display:flex;gap:8px;padding:8px;border-radius:24px;background:#C8CCD1}
.pn .tool i{width:46px;height:46px;display:grid;place-items:center;border-radius:15px;background:#fff;color:var(--ink)}
.pn svg.ln{position:absolute;inset:0;width:100%;height:100%}
.pn .nd{position:absolute;width:48px;height:48px;border-radius:14px;background:#fff;display:grid;place-items:center;box-shadow:0 6px 14px -8px rgba(0,0,0,.3)}
.faq{display:grid;gap:14px;grid-template-columns:1fr;max-width:1160px;margin:56px auto 0;padding:0 20px;align-items:start}
@media(min-width:860px){.faq{grid-template-columns:1fr 1fr;padding:0 32px}}
.fq{background:var(--card);border:1px solid var(--line);border-radius:28px;box-shadow:0 1px 0 #F1F3F5}
.fq summary{display:flex;align-items:center;gap:12px;padding:22px 28px;font-weight:500;font-size:1.2rem;color:var(--ink)}
.fq summary svg{margin-left:auto;flex:none;transition:transform .25s}
.fq[open] summary svg{transform:rotate(180deg)}
.fq .tg{font-size:.72rem;font-weight:500;letter-spacing:.04em;padding:3px 10px;border-radius:99px;background:#EAF1FF;color:#2B4A8B;white-space:nowrap}
.fq dl{padding:0 28px 24px;display:grid;gap:12px;font-size:1rem}
.fq dt{font-weight:500;color:var(--ink)}.fq dd{color:var(--muted);font-style:normal}
.goal{display:grid;gap:18px;max-width:1160px;margin:44px auto 0;padding:0 20px}
@media(min-width:860px){.goal{grid-template-columns:.9fr 1.1fr;padding:0 32px}}
.goal .ph{position:relative;border-radius:30px;overflow:hidden;aspect-ratio:4/5}.goal .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 11%}
@media(min-width:560px) and (max-width:859px){.goal .ph{aspect-ratio:3/2}}
@media(min-width:860px){.goal .ph{aspect-ratio:auto;min-height:460px}}
.goal .gc{background:var(--card);border:1px solid var(--line);border-radius:30px;padding:36px;display:flex;flex-direction:column;justify-content:space-between;gap:30px}
.goal h3{font-weight:500;font-size:1.55rem;color:var(--ink)}
.goal p{color:#33506B}
.gh{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:12px 40px;max-width:1160px;margin:0 auto;padding:0 20px}
@media(min-width:760px){.gh{padding:0 32px}}
.gh p{color:var(--muted);max-width:22em}
.certs{display:grid;gap:14px;grid-template-columns:1fr;max-width:1160px;margin:56px auto 0;padding:0 20px}
@media(min-width:560px){.certs{grid-template-columns:1fr 1fr}}@media(min-width:960px){.certs{grid-template-columns:repeat(4,1fr);padding:0 32px}}
.ce{background:var(--card);border:1px solid var(--line);border-radius:28px;padding:26px;box-shadow:0 1px 0 #F1F3F5}
.ce i{display:grid;place-items:center;width:46px;height:46px;border-radius:13px;margin-bottom:20px;color:var(--ink)}
.ce:nth-child(4n+1) i{background:#DAD9FA}.ce:nth-child(4n+2) i{background:#FBD3CC}.ce:nth-child(4n+3) i{background:#F6D3F0}.ce:nth-child(4n) i{background:#D5F5DC}
.ce b{display:block;font-weight:500;font-size:1.2rem;line-height:1.25;color:var(--ink)}
.ce small{color:var(--muted);font-size:.9rem}
.hero-b .h1{max-width:12em}
.pbox{max-width:1160px;margin:0 20px;border-radius:34px;padding:clamp(48px,7vw,84px) clamp(16px,4vw,40px);background:linear-gradient(90deg,#EAF3FF,#F7F2FA 50%,#FFF0F0)}
@media(min-width:1220px){.pbox{margin:0 auto}}
.plans{display:grid;gap:16px;margin-top:48px}
@media(min-width:900px){.plans{grid-template-columns:repeat(3,1fr)}}
.pc{background:#fff;border:1px solid var(--line);border-radius:26px;padding:26px;display:flex;flex-direction:column;gap:14px;box-shadow:0 1px 0 #F1F3F5}
.pc i{display:grid;place-items:center;width:44px;height:44px;border-radius:12px;color:var(--ink)}
.pc:nth-child(1) i{background:#DAD9FA}.pc:nth-child(2) i{background:#FBD3CC}.pc:nth-child(3) i{background:#D5F5DC}
.pc h3{font-weight:500;font-size:1.4rem;line-height:1.2;color:var(--ink)}
.pc p{color:#33506B;font-size:1rem}
.pc ul{display:grid;gap:8px;font-size:.98rem;color:#33506B}
.pc li{display:flex;gap:10px;align-items:flex-start}.pc li svg{flex:none;margin-top:3px;color:#16A34A}
.pr{font-size:2.6rem;font-weight:600;color:var(--ink);line-height:1;margin-top:auto;padding-top:8px}
.pr em{font-size:.62em;margin-left:6px}
.pc .gb{width:100%}
.note{margin-top:30px;color:var(--muted);text-align:center}
.ex{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:22px}
.ex span{background:#fff;border-radius:99px;padding:8px 18px;font-size:.95rem;color:#33506B;box-shadow:0 1px 0 #E6E9EC}
.ex b{font-weight:600;color:var(--ink);margin-left:6px}
.pj{display:grid;gap:18px;max-width:1160px;margin:52px auto 0;padding:0 20px}
@media(min-width:900px){.pj{grid-template-columns:1.25fr 1fr;padding:0 32px}}
.pcard{background:var(--card);border:1px solid var(--line);border-radius:30px;padding:30px;display:flex;flex-direction:column;gap:16px}
.pcard.gh2{border-style:dashed;background:transparent}
.pcard h3{font-weight:500;font-size:1.55rem;color:var(--ink)}
.bd{align-self:flex-start;font-size:.78rem;font-weight:500;padding:4px 12px;border-radius:99px;background:#fff;border:1px solid #DDE2E6;color:#5B6F82}
.pcard p{color:#33506B}
.tg2{display:flex;flex-wrap:wrap;gap:8px}.tg2 li{padding:4px 12px;border-radius:99px;background:#fff;border:1px solid var(--line);font-size:.88rem;color:#33506B}
.pcard .dk{align-self:flex-start}
.stack{display:grid;gap:18px;align-content:start}
.gnote{font-size:.9rem;color:var(--muted);border-top:1px dashed #D5DADF;padding-top:12px}
.who{display:grid;gap:18px;max-width:1160px;margin:0 auto;padding:0 20px}
@media(min-width:860px){.who{grid-template-columns:.85fr 1.15fr;padding:0 32px}}
.who .ph{border-radius:30px;overflow:hidden;aspect-ratio:4/5}.who .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 14%}
.who .gc{background:var(--card);border:1px solid var(--line);border-radius:30px;padding:clamp(28px,4vw,52px);display:flex;flex-direction:column;justify-content:center;gap:22px;align-items:flex-start}
.who p{color:#33506B;font-size:1.1rem}
.ctab{max-width:1160px;margin:0 20px;border-radius:34px;background:linear-gradient(115deg,#FDEDEE,#F8F0F6 45%,#EEF2FD);display:grid;gap:30px;padding:clamp(34px,6vw,74px) clamp(24px,5vw,64px);position:relative;overflow:hidden}
@media(min-width:1220px){.ctab{margin:0 auto}}
@media(min-width:860px){.ctab{grid-template-columns:1.4fr .6fr;align-items:center}}
.ctab p{color:var(--muted);margin-top:16px;max-width:28em}
.ctab .cta{justify-content:flex-start}
.tile{justify-self:center;width:min(210px,50vw);aspect-ratio:1;border-radius:36px;background:#fff;display:grid;place-items:center;box-shadow:0 0 0 14px rgba(255,255,255,.55),0 30px 50px -24px rgba(11,42,71,.4)}
.tile img{width:76%;height:auto}
.lh{display:block;height:46px;width:auto}
.logo{padding:2px 4px}
.flogo,.sg{display:block;width:min(290px,85%)}
.flogo img,.sg img{width:100%;height:auto;display:block}
.sg{width:min(250px,75%);margin-top:12px}
@media(max-width:959px){.lh{height:27px}.logo{padding:0}.hr .gb.sm{padding:0 11px}.lang button{padding:5px 6px}}
.ftr{max-width:1160px;margin:0 auto;padding:72px 20px 60px;display:grid;gap:36px;grid-template-columns:1fr}
@media(min-width:860px){.ftr{grid-template-columns:1.4fr 1fr 1.2fr;padding:90px 32px 64px}}
.ftr h4{font-weight:500;font-size:1.15rem;margin-bottom:14px;color:var(--ink)}
.ftr li{margin:6px 0}.ftr a{text-decoration:none;color:#33506B}.ftr a:hover{color:var(--ink)}
.fs{display:flex;gap:10px;margin-top:18px}
.fs a,.fs .off{width:38px;height:38px;border-radius:12px;border:1px solid #DDE2E6;display:grid;place-items:center;color:var(--ink);transition:background .2s,color .2s}
.fs a:hover{background:var(--ink);border-color:var(--ink);color:#fff}
.fs .off{opacity:.5;cursor:default}
.ftr .ct li{display:flex;gap:10px;align-items:center}
.cp{max-width:1160px;margin:0 auto;padding:0 20px 90px;color:var(--muted);font-size:.9rem}
@media(min-width:760px){.cp{padding:0 32px 90px}}

/* paleta A: medianoche */
.frame{box-shadow:0 0 0 1px #CBD4E1,0 30px 60px -40px rgba(11,31,58,.35)}
.gb{background:var(--ink);border-color:var(--ink);color:#fff}
.gb:hover{background:var(--acc);border-color:var(--acc)}
.hero::before{background-image:linear-gradient(#E9EDF3 1px,transparent 1px),linear-gradient(90deg,#E9EDF3 1px,transparent 1px)}
.hero::after{background:radial-gradient(30% 45% at 6% 30%,rgba(36,87,230,.09),transparent 70%),radial-gradient(30% 45% at 96% 20%,rgba(56,189,248,.12),transparent 70%),radial-gradient(28% 40% at 80% 62%,rgba(36,87,230,.06),transparent 70%)}
.chip svg{color:var(--acc)}
.b2{background:var(--line)}
.b4{background:#0B1F3A}.b4 .k{color:#7DD3FC}.b4 .p{color:#93B4FF}
.tb,.pn .tool{background:#D3DAE6}
.fl-i{box-shadow:0 14px 26px -16px rgba(11,31,58,.5)}
.pk{background:#0B1F3A}.bl{background:#2457E6}.rd{background:#1D3F8F}.yl{background:#38BDF8;color:#06223F}.gr{background:#3E6BEA}.vi{background:#14305C}
.ce:nth-child(n) i,.pc:nth-child(n) i{background:#E3EBFD;color:var(--acc)}
.pc li svg{color:var(--acc)}
.pbox{background:#E8EDF5}
.ctab{background:#E8EDF5}
.fq .tg{background:#E3EBFD;color:#1B3FA8}
.og{background:transparent;border:1.5px solid var(--ink);color:var(--ink)}
.og:hover{background:var(--ink);color:#fff}
/* menu flotante, separado del borde superior */
.hdr{top:18px;box-shadow:0 24px 44px -24px rgba(11,31,58,.5),0 2px 0 rgba(255,255,255,.6) inset}
html{scroll-padding-top:128px}
.hdr{border-radius:22px}
@media(min-width:960px){.hdr{border-radius:22px}.hn a{border-radius:12px}}
.hn a{border-radius:12px}
@media(max-width:959px){.hero:not(.hero-b),.hero.hero-b{padding-top:142px}}
@media(min-width:960px){.hdr{top:38px}.hero:not(.hero-b),.hero.hero-b{padding-top:clamp(150px,15.5vw,212px)}}
.fl-i.ti.a{color:var(--acc)}
.fl-i.ti img{width:54%;height:54%;object-fit:contain;border-radius:0}
.fl-i.ti.sm img{width:58%;height:58%}
/* seccion del master: cinta de logos y tarjetas */
/* Dos cintas que se mueven. El ancho de cada cinta es el de una tanda de 6 iconos (--g es la separación), así no se ve ningún
   icono repetido; las otras dos copias solo sirven para que el bucle no tenga salto. */
.mqs{--g:22px;--set:calc(6 * (84px + var(--g)));max-width:1160px;margin:34px auto 0;padding:0 20px;display:grid;justify-items:center}
@media(min-width:760px){.mqs{padding:0 32px}}
.mq{width:min(100%,var(--set));overflow:hidden;padding:6px 0 20px;-webkit-mask-image:linear-gradient(90deg,transparent,#000 26px,#000 calc(100% - 26px),transparent);mask-image:linear-gradient(90deg,transparent,#000 26px,#000 calc(100% - 26px),transparent)}
.mq-t{display:flex;width:max-content;animation:mq 14s linear infinite}
.mq:hover .mq-t{animation-play-state:paused}
.mq-s{display:flex}
.mq-s i{margin-right:var(--g)}
@keyframes mq{to{transform:translateX(-33.3333%)}}
.mq.rev .mq-t{animation-direction:reverse}
.mq i{flex:none;width:84px;height:84px;border-radius:22px;background:#fff;border:1px solid var(--line);display:grid;place-items:center;box-shadow:0 12px 24px -18px rgba(11,31,58,.45);color:var(--ink)}
.mq i img{width:42px;height:42px;object-fit:contain}
@media(prefers-reduced-motion:reduce){.mq{-webkit-mask-image:none;mask-image:none;padding-bottom:6px}.mq-t{width:auto;justify-content:center;animation:none}.mq-s[aria-hidden]{display:none}.mq-s{flex-wrap:wrap;justify-content:center;gap:14px}.mq-s i{margin-right:0}}
.mods{display:grid;gap:14px;grid-template-columns:1fr;margin-top:34px;align-items:start}
@media(min-width:620px){.mods{grid-template-columns:1fr 1fr}}
@media(min-width:1000px){.mods{grid-template-columns:repeat(4,1fr)}}
.mc{position:relative;background:#fff;border:1px solid var(--line);border-radius:24px;transition:border-color .2s,box-shadow .2s}
.mc:hover{border-color:#C9D3E3}
.mc[open]{border-color:var(--acc);box-shadow:0 18px 36px -26px rgba(36,87,230,.55)}
.mc summary{list-style:none;cursor:pointer;display:flex;flex-direction:column;gap:14px;padding:20px;min-height:186px}
.mc summary::-webkit-details-marker{display:none}
.mi{display:grid;place-items:center;width:54px;height:54px;border-radius:16px;background:var(--card);border:1px solid var(--line);color:var(--acc)}
.mi img{width:30px;height:30px;object-fit:contain}
.mn{position:absolute;top:22px;right:22px;font:500 .85rem ui-monospace,SFMono-Regular,Menlo,monospace;color:#5F6E83}
.mt b{display:block;font-weight:500;font-size:1.2rem;line-height:1.25;color:var(--ink)}
.mt .tg{display:inline-block;margin-top:8px;font-size:.72rem;font-weight:500;letter-spacing:.04em;padding:3px 10px;border-radius:99px;background:#E3EBFD;color:#1B3FA8}
.mc summary>svg{margin-top:auto;align-self:flex-end;color:var(--muted);transition:transform .25s}
.mc[open] summary>svg{transform:rotate(180deg)}
.mc dl{padding:0 20px 20px;display:grid;gap:10px;font-size:.98rem}
.mc dt{font-weight:500;color:var(--ink)}.mc dd{color:var(--muted)}
.mcta{display:flex;flex-direction:column;justify-content:space-between;gap:10px;min-height:186px;padding:20px;background:var(--ink);border-color:var(--ink);color:#fff;text-decoration:none}
.mcta b{font-size:3.6rem;font-weight:600;line-height:1}
.mcta span{font-size:1.1rem}
.mcta i{align-self:flex-end;display:grid;place-items:center;width:38px;height:38px;border-radius:50%;background:#fff;color:var(--ink)}
.mcta:hover{background:var(--acc);border-color:var(--acc)}
@media(max-width:619px){.mc summary{min-height:0;flex-direction:row;align-items:center;gap:14px;padding:16px}.mc summary>svg{margin:0 0 0 auto;align-self:center}.mn{display:none}.mt{flex:1}.mcta{min-height:0;flex-direction:row;align-items:center}.mcta b{font-size:2.4rem}.mcta i{margin-left:auto}.mc dl{padding:0 16px 16px}}
.hdr{max-width:1200px}
.soc{display:none;align-items:center;gap:2px;margin-right:6px}
@media(min-width:1280px){.soc{display:flex}}
.soc a,.soc .off{width:34px;height:34px;display:grid;place-items:center;border-radius:11px;color:#5B6F82;transition:background .2s,color .2s}
.soc a:hover{background:rgba(255,255,255,.85);color:var(--ink)}
.soc .off{opacity:.5;cursor:default}
.lang button{display:inline-flex;align-items:center;gap:7px;padding:5px 10px}
.lang button img{width:20px;height:15px;border-radius:3px;object-fit:cover;box-shadow:0 0 0 1px rgba(11,31,58,.14)}
.lang button[aria-pressed=false] img{opacity:.7}
@media(max-width:959px){.lang button span{display:none}.lang button{padding:6px 7px}}
#master .center p,#conocimientos .center p{max-width:none}
@media(min-width:760px){#master .center p,#conocimientos .center p{white-space:nowrap}}
.wb{max-width:1160px;margin:34px auto 0;background:#fff;border:1px solid var(--line);border-radius:28px;box-shadow:0 34px 60px -44px rgba(11,31,58,.5);overflow:hidden}
.wb-bar{display:flex;align-items:center;gap:7px;padding:13px 20px;background:var(--card);border-bottom:1px solid var(--line)}
.wb-bar i{width:10px;height:10px;border-radius:50%;background:#D5DBE5}
.wb-bar span{margin-left:12px;font:500 .8rem ui-monospace,SFMono-Regular,Menlo,monospace;color:#5C6B80}
.wb-body{display:grid;grid-template-columns:1fr}
@media(min-width:900px){.wb-body{grid-template-columns:292px 1fr}}
.wb-tabs{display:flex;gap:4px;padding:10px;overflow-x:auto;scrollbar-width:none;border-bottom:1px solid var(--line)}
.wb-tabs::-webkit-scrollbar{display:none}
@media(min-width:900px){.wb-tabs{flex-direction:column;overflow:visible;padding:16px 14px;border-bottom:0;border-right:1px solid var(--line);background:linear-gradient(180deg,#FBFCFE,#F6F8FB)}}
.wb-tabs button{position:relative;flex:none;display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:12px;padding:13px 15px;border:0;border-radius:14px;background:none;font:inherit;color:var(--muted);text-align:left;cursor:pointer;transition:background .2s,color .2s}
.wb-tabs button:hover{background:#fff;color:var(--ink)}
.wb-tabs button small{font:500 .78rem ui-monospace,SFMono-Regular,Menlo,monospace;color:#5F6E83}
.wb-tabs button b{font-weight:500;font-size:1.02rem;color:inherit;white-space:nowrap}
.wb-tabs .ext{font:500 .78rem ui-monospace,SFMono-Regular,Menlo,monospace;color:#5F6E83}
.wb-tabs button[aria-selected=true]{background:#fff;color:var(--ink);box-shadow:0 10px 22px -16px rgba(11,31,58,.55),0 0 0 1px var(--line)}
.wb-tabs button[aria-selected=true] b{font-weight:600}
.wb-tabs button[aria-selected=true] .ext{color:var(--acc)}
.wb-tabs button::after{content:"";position:absolute;left:15px;right:15px;bottom:5px;height:2px;border-radius:2px;background:var(--acc);transform:scaleX(0);transform-origin:left}
.wb.auto:not(.paused) .wb-tabs button[aria-selected=true]::after{animation:wbp var(--dur,8s) linear forwards}
.wb.auto.paused .wb-tabs button[aria-selected=true]::after{transform:scaleX(0)}
@keyframes wbp{to{transform:scaleX(1)}}
.wb-panels{display:grid;min-width:0}
.wb-panels>section{grid-area:1/1;display:flex;flex-direction:column;gap:20px;padding:28px 30px 26px;min-width:0}
.wb-panels>section[hidden]{display:flex;visibility:hidden;opacity:0;pointer-events:none}
.wb-panels>section:not([hidden]){animation:wbin .5s cubic-bezier(.2,.7,.2,1)}
@keyframes wbin{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.wb-panels header h3{font-weight:700;font-size:clamp(1.5rem,2.8vw,2rem);line-height:1.15;color:var(--ink)}
.wb-panels header p{color:var(--muted);margin-top:6px;max-width:40em}
.wb-panels header p.wbs{font-size:1.1rem;color:var(--ink);font-weight:500;margin-top:8px}
.wb-panels header p.wbp{color:#3F566B;font-size:1.03rem;margin-top:10px;max-width:46em}
.wbh{font:500 .76rem ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.09em;text-transform:uppercase;color:#5C6B80;margin-bottom:12px;display:flex;align-items:center;gap:12px}
.wbh::after{content:"";flex:1;height:1px;background:var(--line)}
.wbk{display:grid;gap:10px;grid-template-columns:1fr}
@media(min-width:700px){.wbk{grid-template-columns:repeat(2,1fr)}}
.wbk li{display:flex;gap:12px;align-items:flex-start;padding:14px 16px;border-radius:16px;background:var(--card);color:var(--ink);font-size:.98rem;line-height:1.4}
.wbk li svg{flex:none;margin-top:1px;color:var(--acc)}
.wbk .ck{stroke-dasharray:1;stroke-dashoffset:1}
.wb-panels>section:not([hidden]) .wbk li{animation:wbrise .55s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(.15s + var(--i)*.14s)}
.wb-panels>section:not([hidden]) .wbk .ck{animation:wbck .6s ease forwards;animation-delay:calc(.4s + var(--i)*.14s)}
@keyframes wbrise{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes wbck{to{stroke-dashoffset:0}}
@media(prefers-reduced-motion:reduce){.wbk .ck{stroke-dashoffset:0;animation:none!important}.wbk li{animation:none!important}}
.wbl{display:grid;gap:10px;grid-template-columns:1fr}
@media(min-width:700px){.wbl{grid-template-columns:repeat(2,1fr)}}
.wbl li{display:flex;gap:14px;align-items:flex-start;padding:15px 16px;border:1px solid var(--line);border-radius:18px;background:#fff;transition:border-color .2s,transform .2s}
.wbl li:hover{border-color:#C5D2EC;transform:translateY(-2px)}
.wbl li i{flex:none;display:grid;place-items:center;width:30px;height:30px;color:var(--ink)}
.wbl li i img{width:28px;height:28px;object-fit:contain}
.wbl li i svg{width:24px;height:24px}
.wbl li b{display:block;font-weight:600;font-size:1.02rem;line-height:1.25;color:var(--ink)}
.wbl li span{display:block;color:var(--muted);font-size:.93rem;margin-top:3px}
.wbc{margin-top:auto;display:flex;align-items:center;gap:6px;padding:13px 18px;border-radius:14px;background:#0B1F3A;color:#BFD0EA;overflow:hidden}
.wbc code{font:400 .86rem ui-monospace,SFMono-Regular,Menlo,monospace;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.wbc u{flex:none;width:7px;height:1.05em;background:#7DD3FC;animation:blink 1.1s steps(1) infinite}
@media(max-width:899px){.wb-panels>section[hidden]{display:none}}
@media(max-width:620px){.wb-panels>section{padding:22px 18px 20px}}
/* ventana algo mas corta que la version inicial; la altura sigue a la pestana activa */
.wb-panels{transition:height .45s cubic-bezier(.2,.7,.2,1);overflow:hidden}
.wb-panels>section{align-self:start;gap:16px;padding:24px 28px 22px}
.wb-panels header h3{font-size:clamp(1.45rem,2.6vw,1.9rem)}
.wb-panels header p.wbs{font-size:1.06rem;line-height:1.45;margin-top:14px}
.wb-panels header p.wbp{font-size:1rem;margin-top:18px}
.wb-panels header{margin-bottom:6px}
.wbh{margin-bottom:10px;font-size:.74rem}
.wbk{gap:9px}
.wbk li{padding:11px 15px;font-size:.96rem}
.wbl{gap:8px}
.wbl li{padding:12px 15px;gap:13px}
.wbl li b{font-size:1rem}.wbl li span{font-size:.91rem;margin-top:3px}
.wbc{padding:12px 18px}
@media(max-width:899px){.wb-panels{height:auto!important}}
@media(prefers-reduced-motion:reduce){.wb-panels>section:not([hidden]){animation:none}}
/* cursiva con brillo tipo espejo: degradado oscuro y destello que recorre la palabra */
em{padding:.14em .08em .3em 0;color:var(--acc);background-image:linear-gradient(104deg,transparent 0 42%,rgba(47,107,255,0) 42%,rgba(56,189,248,.9) 46.5%,rgba(125,211,252,1) 48.5%,rgba(56,189,248,.9) 50.5%,rgba(47,107,255,0) 55%,transparent 55% 100%),linear-gradient(95deg,#0B1F3A 0%,#1F46C9 38%,#2F6BFF 54%,#12306E 78%,#0B1F3A 100%);background-size:260% 100%,100% 100%;background-repeat:no-repeat;background-position:0% 0,0 0;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
em.shine{animation:shine 1.9s cubic-bezier(.45,.05,.3,1) 1}
@keyframes shine{from{background-position:0% 0,0 0}to{background-position:100% 0,0 0}}
/* legibilidad: interlineado y respiro en bloques con mucho texto */
.pc{gap:16px;padding:28px}
.pc h3{line-height:1.25}
.pc p{line-height:1.6}
.pc ul{gap:10px;line-height:1.5}
.pc li{gap:11px}
.pc .pr{font-size:2.3rem;font-weight:600;color:var(--ink);line-height:1.05;margin-top:auto;padding-top:14px}
.pc .pr em{display:block;font-size:.42em;margin:8px 0 0;padding:0;background:none;-webkit-text-fill-color:currentColor;color:var(--muted);animation:none;letter-spacing:0}
.ex span{line-height:1.4;padding:9px 18px}
.note{line-height:1.6}
.pcard{padding:32px;gap:18px}
.pcard p{line-height:1.65}
.tg2 li{line-height:1.4}
.who .gc{gap:24px}
.who p{line-height:1.7}
.ctab p{line-height:1.65}
.goal .gc{justify-content:flex-start;gap:22px;padding:36px}
.goal .gc p{line-height:1.7;font-size:1.04rem}
.goal .gc .sg{margin-top:auto}
.ce{text-align:left;padding:24px}
.ce b{line-height:1.3}
.ce small{display:block;margin-top:5px}
.gh p{line-height:1.6}
.center p{line-height:1.65}
.ftr li{margin:9px 0}
.ftr h4{margin-bottom:16px}
.cp{line-height:1.6}
.wb-panels header p.wbp{line-height:1.68}
.wb-panels header p.wbs{line-height:1.5}
.wbk li{line-height:1.5}
.wbl li span{line-height:1.5;margin-top:4px}
.wbl li b{line-height:1.3}
.lead{line-height:1.65}
/* robustez en ingles y en Safari: nada de botones ni etiquetas partidos en dos lineas */
.hdr{max-width:1260px}
.hr{flex:none}
.gb,.og,.dk,.pl,.bd,.lang button,.wb-tabs button b,.tg,.eye{white-space:nowrap}
.gb.sm{flex:none}
.hn{min-width:0}
.hn a{padding:7px 11px}
.mock-bar span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
.b3 .go span{white-space:nowrap}
.b4 pre{font-size:.8rem;padding:20px 18px;overflow:visible;flex:1;display:flex;flex-direction:column;justify-content:center}
.b4 pre span.l{white-space:pre-wrap;overflow-wrap:anywhere;padding-left:2.4em;text-indent:-2.4em}
.b4 pre span.l::before{width:1.4em;margin-right:10px}
html[lang=en] .cap-es,html:not([lang=en]) .cap-en{display:none}
/* certificados: rejilla compacta */
.certs{max-width:1160px;margin:34px auto 0;padding:0 20px;display:grid;gap:10px;grid-template-columns:repeat(2,1fr)}
@media(min-width:700px){.certs{padding:0 32px}}
@media(min-width:1040px){.certs{grid-template-columns:repeat(5,1fr)}}
.cc{position:relative;display:grid;grid-template-columns:1fr auto;grid-template-rows:auto auto;gap:8px 10px;align-content:start;padding:14px 16px 16px;background:#fff;border:1px solid var(--line);border-radius:18px;text-align:left;box-shadow:0 8px 18px -16px rgba(11,31,58,.4);transition:transform .2s,border-color .2s}
.cc:hover{transform:translateY(-2px);border-color:#C5D2EC}
.cn{font:500 .76rem ui-monospace,SFMono-Regular,Menlo,monospace;color:#5F6E83;letter-spacing:.04em}
.cc svg{grid-column:2;grid-row:1;color:var(--acc);justify-self:end}
.cn{grid-column:1;grid-row:1}
.cc b{grid-column:1/-1;grid-row:2;font-weight:700;font-size:1.02rem;line-height:1.28;color:var(--ink)}
/* pie: caja oscura */
.frame{border-radius:34px;margin-bottom:20px}
.ft{margin-top:clamp(56px,7vw,96px);padding:0 20px 20px}
@media(min-width:760px){.ft{padding:0 24px 24px}}
.ft-box{position:relative;overflow:hidden;isolation:isolate;max-width:1272px;margin:0 auto;border-radius:30px;padding:clamp(26px,4vw,48px) clamp(22px,4.5vw,56px) 0;background:radial-gradient(60% 90% at 88% -10%,rgba(36,87,230,.55),transparent 62%),radial-gradient(45% 70% at 4% 110%,rgba(56,189,248,.22),transparent 65%),#0B1F3A;color:#fff;display:grid;gap:clamp(26px,3.6vw,40px)}
.ft-box::before{content:"";position:absolute;inset:0;z-index:-1;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:64px 64px;-webkit-mask-image:radial-gradient(80% 90% at 50% 0%,#000,transparent 75%);mask-image:radial-gradient(80% 90% at 50% 0%,#000,transparent 75%)}
.ft-top{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.ft-logo img{display:block;height:44px;width:auto}
.up{display:inline-flex;align-items:center;gap:10px;height:46px;padding:0 10px 0 20px;border-radius:99px;background:#fff;color:#0B1F3A;font-weight:600;font-size:.98rem;text-decoration:none;transition:transform .25s,background .25s,color .25s}
.up svg{width:30px;height:30px;padding:6px;border-radius:50%;background:#0B1F3A;color:#fff;transition:transform .25s,background .25s}
.up:hover{transform:translateY(-3px);background:#E6EEFF}
.up:hover svg{transform:translateY(-3px);background:var(--acc)}
.ft-msg{font-weight:700;font-size:clamp(1.7rem,3.6vw,2.7rem);line-height:1.12;letter-spacing:-.01em;max-width:18em;text-wrap:balance}
.ft-sub{margin-top:12px;font:500 .98rem ui-monospace,SFMono-Regular,Menlo,monospace;color:#9DB6DD}
.ft-prompt{color:#38BDF8;margin-right:4px}
.ft-fs{display:flex;flex-wrap:wrap;gap:10px;margin:0}
.ft-fs a,.ft-fs .off{width:46px;height:46px;border-radius:14px;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.06);color:#fff;display:grid;place-items:center;transition:background .2s,color .2s,transform .2s}
.ft-fs a svg,.ft-fs .off svg{width:20px;height:20px}
.ft-fs a:hover{background:#fff;color:#0B1F3A;transform:translateY(-3px)}
.ft-fs .off{opacity:.4}
.ft-cp{font-size:.9rem;color:#8FA6C9}
.ft-big{position:relative;margin:clamp(2px,1vw,14px) -.04em 0;font-weight:700;font-size:clamp(3.4rem,15.4vw,14.6rem);line-height:.74;letter-spacing:-.045em;white-space:nowrap;user-select:none;background:linear-gradient(180deg,rgba(255,255,255,.24),rgba(255,255,255,.02) 78%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;padding-bottom:.02em;height:.62em;overflow:hidden}
.ft-big span{color:inherit}
@media(max-width:620px){.ft-logo img{height:36px}.ft-fs a,.ft-fs .off{width:44px;height:44px}}
/* certificados: tipografia de la web y efecto de color al pasar el raton */
.certs{gap:12px}
.cc{position:relative;overflow:hidden;isolation:isolate;display:flex;flex-direction:column;gap:14px;justify-content:space-between;min-height:106px;padding:17px 19px 19px;background:#fff;border:0;outline:1px solid var(--line);outline-offset:-1px;border-radius:20px;box-shadow:0 8px 18px -16px rgba(11,31,58,.4);transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s,outline-color .25s .3s}
.cc::before{content:"";position:absolute;inset:-3px;will-change:transform;z-index:-1;background:linear-gradient(135deg,#0B1F3A 0%,#1B46C8 55%,#38BDF8 120%);transform:translateY(102%);transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.cc::after{content:"";position:absolute;top:-30%;bottom:-30%;left:-60%;width:40%;z-index:-1;background:linear-gradient(100deg,transparent,rgba(255,255,255,.28),transparent);transform:translateX(0) skewX(-18deg);opacity:0}
.cc b{grid-column:auto;grid-row:auto;font-weight:700;font-size:1.06rem;line-height:1.25;color:var(--ink);transition:color .35s}
.cc svg{grid-column:auto;grid-row:auto;justify-self:auto;align-self:flex-start;color:var(--acc);transition:color .35s,transform .45s cubic-bezier(.2,.7,.2,1)}
.cc .ck{stroke-dasharray:1;stroke-dashoffset:0}
.cc:hover{transform:translateY(-4px);outline-color:transparent;transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s,outline-color 0s;box-shadow:0 22px 34px -18px rgba(27,70,200,.65)}
.cc:hover::before{transform:translateY(0)}
.cc:hover::after{opacity:1;animation:ccshine .9s .1s ease-out}
.cc:hover b{color:#fff}
.cc:hover svg{color:#7DD3FC;transform:scale(1.12) rotate(-6deg)}
.cc:hover .ck{animation:ccck .55s .2s ease-out both}
@keyframes ccshine{from{transform:translateX(0) skewX(-18deg)}to{transform:translateX(420%) skewX(-18deg)}}
@keyframes ccck{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
@media(prefers-reduced-motion:reduce){.cc,.cc::before,.cc svg{transition:none}.cc:hover::after,.cc:hover .ck{animation:none}.cc:hover{transform:none}}
/* tipografia general (Barlow) en etiquetas decorativas; solo el codigo real va en monoespaciada */
.wb-bar span{font:500 .84rem/1 var(--f);letter-spacing:.03em;color:#5C6B80}
.wb-tabs button small{font:600 .8rem/1 var(--f);font-variant-numeric:tabular-nums;letter-spacing:.04em;color:#5F6E83}
.wb-tabs .ext{font:500 .82rem/1 var(--f);letter-spacing:.02em;color:#5F6E83}
.wbh{font:600 .74rem/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:#5C6B80}
.ft-sub{font:500 1rem/1.4 var(--f);letter-spacing:.01em;color:#9DB6DD}
/* pie mas compacto, sin palabra gigante */
.ft{margin-top:clamp(44px,5.5vw,72px)}
.ft-box{padding:clamp(22px,3vw,34px) clamp(22px,3.6vw,44px);gap:clamp(18px,2.4vw,26px);border-radius:26px}
.ft-logo img{height:38px}
.up{height:42px;font-size:.94rem}
.ft-msg{font-size:clamp(1.45rem,2.6vw,2rem)}
.ft-sub{margin-top:6px;font-size:.96rem}
.ft-bot{display:flex;align-items:center;justify-content:space-between;gap:14px 24px;flex-wrap:wrap;padding-top:clamp(14px,2vw,20px);border-top:1px solid rgba(255,255,255,.12)}
.ft-fs a,.ft-fs .off{width:42px;height:42px;border-radius:13px}
.ft-cp{margin:0}
@media(max-width:620px){.ft-logo img{height:32px}.ft-fs a,.ft-fs .off{width:40px;height:40px}}
/* barra social del hero: Instagram sin enlace */
.tb .off{width:46px;height:46px;display:grid;place-items:center;border-radius:15px;background:#fff;color:var(--ink);opacity:.45;cursor:default}
@media(max-width:859px){.tb .off{width:38px;height:38px;border-radius:12px}}
/* cursivas: zona de pintura holgada para que no se corten los rabos de p, g, q ni las cursivas inclinadas */
em{padding:.18em .16em .36em .16em;margin:0 -.16em}
.hero-b .lead{max-width:47em}
/* planes como niveles, sin cifras */
.pc .pt{font-size:.78rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--acc);margin-top:2px}
.pc h3{font-size:1.75rem;font-weight:700;line-height:1.15;margin-top:-6px}
.pc .gb{margin-top:auto;width:100%}
.pc ul{margin-bottom:10px}
.exl{text-align:center;color:var(--muted);margin-top:26px;font-size:1rem}
.ex{margin-top:12px}
.ex span{padding:9px 20px;font-weight:500}
/* planes: tarjetas con ilustracion, lista y boton con flecha */
.plans{gap:18px;align-items:stretch;margin-top:44px}
.plc{display:flex;flex-direction:column;padding:12px;border-radius:30px;background:#fff;border:1px solid var(--line);position:relative}
.plc-img{position:relative;margin:0;border-radius:20px;overflow:hidden;aspect-ratio:16/10;background:#DCE8FF}
.plc-img svg{display:block;width:100%;height:100%}
.plc-badge{position:absolute;left:12px;top:12px;padding:7px 14px;border-radius:99px;background:rgba(255,255,255,.88);color:var(--ink);font-size:.86rem;font-weight:600;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.plc-b{display:flex;flex-direction:column;gap:12px;flex:1;padding:22px 14px 12px}
.plc .pt{font-size:.76rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--acc)}
.plc h3{font-size:1.9rem;font-weight:700;line-height:1.1;margin:-4px 0 0;color:var(--ink)}
.plc-b>p{color:var(--muted);line-height:1.6}
.plc ul{display:grid;gap:11px;margin:6px 0 10px;color:var(--ink);font-size:1rem;line-height:1.45}
.plc li{display:flex;gap:12px;align-items:flex-start}
.plc li svg{flex:none;width:24px;height:24px;padding:4px;border-radius:50%;background:#E3EBFD;color:var(--acc);margin-top:0}
.plc .gb{margin-top:auto;width:100%;height:56px;justify-content:space-between;padding:0 9px 0 26px;font-size:1.02rem}
.plc .gb i{display:grid;place-items:center;width:38px;height:38px;border-radius:50%;background:rgba(255,255,255,.16);transition:transform .25s}
.plc .gb:hover i{transform:translateX(3px) rotate(0)}
/* nivel 1: suave */
.plc.p1{background:#FBFCFE}
.plc.p1 .plc-b>p,.plc.p1 li{color:#4F6177}
.plc.p1 h3{color:#33465E}
.plc.p1 .gb{background:#fff;color:var(--ink);border-color:#C9D3E3}
.plc.p1 .gb i{background:#EEF2F8}
/* nivel 2: destacado */
.plc.p2{border-color:#C5D2EC;box-shadow:0 30px 50px -34px rgba(36,87,230,.55)}
/* nivel 3: oscuro */
.plc.p3{background:linear-gradient(160deg,#16367F 0%,#0B1F3A 70%);border-color:transparent;color:#fff}
.plc.p3 h3,.plc.p3 li{color:#fff}
.plc.p3 .plc-b>p{color:#B9C9E6}
.plc.p3 .pt{color:#7DD3FC}
.plc.p3 li svg{background:rgba(255,255,255,.14);color:#7DD3FC}
.plc.p3 .gb{background:#fff;color:var(--ink);border-color:#fff}
.plc.p3 .gb i{background:var(--ink);color:#fff}
/* planes con fotos: seleccion y boton */
.plc{transition:opacity .4s,filter .4s,transform .5s cubic-bezier(.2,.7,.2,1),box-shadow .4s}
.plc-img img{display:block;width:100%;height:100%;object-fit:cover;transition:transform 1s cubic-bezier(.2,.7,.2,1)}
.plc:focus-within{transform:translateY(-8px)}
@media(hover:hover){.plc:hover{transform:translateY(-8px)}}
.plc:hover .plc-img img,.plc:focus-within .plc-img img{transform:scale(1.07)}
.plc.p1:hover{box-shadow:0 34px 50px -30px rgba(11,31,58,.5)}
.plc.p2:hover{box-shadow:0 38px 56px -30px rgba(36,87,230,.7)}
.plc.p3:hover{box-shadow:0 38px 56px -26px rgba(11,31,58,.85)}
@media(hover:hover){@supports selector(:has(*)){
.plans:has(.plc:hover) .plc:not(:hover),.plans:has(.plc:focus-within) .plc:not(:focus-within){opacity:.42;filter:saturate(.55) blur(.4px);transform:scale(.985)}
}}
.plc .gb{position:relative;overflow:hidden;isolation:isolate;--sweep:linear-gradient(100deg,#0B1F3A,#1B46C8)}
.plc.p2 .gb{--sweep:linear-gradient(100deg,#1B46C8,#38BDF8)}
.plc.p3 .gb{--sweep:linear-gradient(100deg,#2457E6,#38BDF8)}
.plc .gb::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--sweep);transform:translateX(-102%);transition:transform .55s cubic-bezier(.2,.7,.2,1)}
.plc .gb::after{content:"";position:absolute;top:-40%;bottom:-40%;left:-40%;width:28%;z-index:-1;background:linear-gradient(100deg,transparent,rgba(255,255,255,.4),transparent);transform:skewX(-20deg);opacity:0}
.plc .gb span{transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.plc .gb:hover::before,.plc .gb:focus-visible::before{transform:translateX(0)}
.plc .gb:hover::after{opacity:1;animation:gbshine .9s .15s ease-out}
.plc .gb:hover,.plc .gb:focus-visible{color:#fff;border-color:transparent;box-shadow:0 18px 30px -14px rgba(27,70,200,.8)}
.plc .gb:hover span{transform:translateX(5px)}
.plc .gb:hover i,.plc .gb:focus-visible i{background:#fff;color:#1B46C8;transform:translateX(4px) rotate(45deg)}
@keyframes gbshine{from{left:-40%}to{left:130%}}
@media(prefers-reduced-motion:reduce){.plc,.plc-img img,.plc .gb::before,.plc .gb span,.plc .gb i{transition:none}.plc .gb:hover::after{animation:none}.plc:hover{transform:none}}
/* pildoras de extras: texto centrado y sin segunda capa */
.ex span{display:inline-flex;align-items:center;justify-content:center;text-align:center;min-height:42px}
.ex span span{display:inline;background:none;box-shadow:none;border-radius:0;padding:0;min-height:0;font:inherit;color:inherit;line-height:inherit}
.who .ph img{object-position:50% 22%}
.who .gc p+p{margin-top:-4px}
/* contacto: formulario y tira de redes */
.ctab{background:linear-gradient(135deg,#E8EDF5,#EEF2FB);gap:clamp(28px,4vw,56px);padding:clamp(28px,5vw,60px) clamp(22px,4.5vw,60px)}
@media(min-width:900px){.ctab{grid-template-columns:.9fr 1.1fr;align-items:center}}
.ct-l p{max-width:24em}
.cf{background:#fff;border:1px solid var(--line);border-radius:28px;padding:clamp(20px,3vw,34px);display:flex;flex-direction:column;gap:16px;box-shadow:0 30px 50px -36px rgba(11,31,58,.5)}
.cf-row{display:grid;gap:16px}
@media(min-width:620px){.cf-row{grid-template-columns:1fr 1fr}}
.cf-f{display:flex;flex-direction:column;gap:7px;min-width:0}
.cf-l{font-size:.9rem;font-weight:500;color:var(--ink)}
.cf input,.cf textarea{width:100%;font:inherit;font-size:1rem;color:var(--ink);background:#F6F8FC;border:1px solid var(--line);border-radius:16px;padding:14px 16px;transition:border-color .2s,box-shadow .2s,background .2s;resize:vertical;min-height:50px}
.cf textarea{min-height:140px;line-height:1.5}
.cf input::placeholder,.cf textarea::placeholder{color:#8A97A9}
.cf input:focus,.cf textarea:focus{outline:0;background:#fff;border-color:var(--acc);box-shadow:0 0 0 4px rgba(36,87,230,.14)}
.cf [aria-invalid="true"]{border-color:#D14343;box-shadow:0 0 0 4px rgba(209,67,67,.12)}
.cf-hp{position:absolute!important;left:-9999px;width:1px;height:1px;opacity:0}
.cf-send{position:relative;overflow:hidden;isolation:isolate;display:flex;align-items:center;justify-content:space-between;width:100%;height:56px;padding:0 9px 0 26px;border:0;border-radius:99px;background:var(--ink);color:#fff;font:inherit;font-weight:500;font-size:1rem;cursor:pointer;transition:box-shadow .3s}
.cf-send::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(100deg,#1B46C8,#38BDF8);transform:translateX(-102%);transition:transform .55s cubic-bezier(.2,.7,.2,1)}
.cf-send i{display:grid;place-items:center;width:38px;height:38px;border-radius:50%;background:rgba(255,255,255,.14);transition:background .3s,color .3s,transform .4s cubic-bezier(.2,.7,.2,1)}
.cf-send:hover::before,.cf-send:focus-visible::before{transform:translateX(0)}
.cf-send:hover,.cf-send:focus-visible{box-shadow:0 18px 30px -14px rgba(27,70,200,.8)}
.cf-send:hover i,.cf-send:focus-visible i{background:#fff;color:#1B46C8;transform:translateX(3px) rotate(45deg)}
.cf-send[disabled]{opacity:.7;cursor:progress}
.cf-st{min-height:1.4em;font-size:.95rem;margin:0;color:var(--muted)}
.cf-st.ok{color:#15803D}.cf-st.err{color:#B42323}
.cf-pv{margin:0;font-size:.85rem;color:var(--muted)}
.ctab .cf p{margin:0;max-width:none;line-height:1.5}
@media(prefers-reduced-motion:reduce){.cf-send::before,.cf-send i{transition:none}}
/* contacto v2: cabecera en una linea y formulario completo */
.ctab{grid-template-columns:1fr;align-items:start;gap:clamp(26px,3.4vw,44px)}
.ct-head{grid-column:1/-1}
.ct-head p{max-width:none;margin-top:16px}
@media(min-width:700px){.ct-head h2,.ct-head p{white-space:nowrap}}
@media(min-width:900px){.ctab{grid-template-columns:.78fr 1.22fr}}
.cf{gap:18px}
.cf-fs{border:0;margin:0;padding:0;min-width:0;display:flex;flex-direction:column;gap:10px}
.cf-fs legend{padding:0;margin-bottom:10px}
.cf-o{font-style:normal;font-weight:400;color:var(--muted);-webkit-text-fill-color:currentColor;background:none;animation:none;padding:0;margin:0;font-family:inherit}
.cf-chips{display:flex;flex-wrap:wrap;gap:8px}
.cf-chips label{position:relative;cursor:pointer}
.cf-chips input{position:absolute;opacity:0;inset:0;width:100%;height:100%;margin:0;cursor:pointer}
.cf-chips label>span{display:inline-flex;align-items:center;padding:9px 16px;border-radius:99px;border:1px solid var(--line);background:#F6F8FC;color:#33506B;font-size:.95rem;transition:background .2s,color .2s,border-color .2s,transform .25s}
.cf-chips label:hover>span{border-color:#B7C4DD;transform:translateY(-1px)}
.cf-chips input:checked+span{background:var(--ink);border-color:var(--ink);color:#fff}
.cf-chips input:focus-visible+span{box-shadow:0 0 0 4px rgba(36,87,230,.2);border-color:var(--acc)}
.cf-ck{display:flex;gap:12px;align-items:flex-start;cursor:pointer;font-size:.92rem;color:#33506B;line-height:1.45}
.cf-ck input{flex:none;width:20px;height:20px;min-height:0;margin:1px 0 0;padding:0;accent-color:var(--acc);cursor:pointer}
.cf-ck input[aria-invalid="true"]{outline:2px solid #D14343;outline-offset:2px;box-shadow:none}
/* contacto v3: formulario horizontal */
.ct-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:22px 32px}
.ctab{gap:clamp(22px,3vw,34px);padding:clamp(26px,4.2vw,52px) clamp(20px,4vw,52px)}
@media(min-width:900px){.ctab{grid-template-columns:1fr}}
.cf{display:grid;grid-template-columns:1fr;gap:16px 18px;padding:clamp(18px,2.6vw,30px);align-items:start}
.cf>*{min-width:0}
@media(min-width:620px){.cf{grid-template-columns:1fr 1fr}.f-biz,.f-msg,.f-plan,.cf-bar,.cf-st{grid-column:1/-1}}
@media(min-width:900px){.cf{grid-template-columns:repeat(3,1fr)}.f-msg{grid-column:span 2}.f-plan{grid-column:3}.f-biz{grid-column:auto}}
.f-msg{height:100%}
.f-msg textarea{flex:1;min-height:132px}
.cf-bar{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px 28px;padding-top:4px}
.cf-bar .cf-ck{flex:1 1 260px;max-width:420px}
.cf-act{display:flex;flex-wrap:wrap;gap:12px;margin-left:auto}
.cf-send{width:auto;min-width:230px;gap:24px}
.cf-wa{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:56px;padding:0 24px;border-radius:99px;border:1.5px solid #C9D3E4;background:#fff;color:var(--ink);font-weight:500;font-size:1rem;white-space:nowrap;transition:background .3s,color .3s,border-color .3s,transform .3s cubic-bezier(.2,.7,.2,1),box-shadow .3s}
.cf-wa,.cf-wa:hover{text-decoration:none}
.cf-wa svg{color:#1FAF54;transition:color .3s}
.cf-wa:hover,.cf-wa:focus-visible{background:var(--ink);color:#fff;border-color:var(--ink);transform:translateY(-2px);box-shadow:0 16px 26px -16px rgba(11,31,58,.7)}
.cf-wa:hover svg,.cf-wa:focus-visible svg{color:#4ADE80}
.cf-st{min-height:0;text-align:right}
.cf-st:empty{display:none}
@media(max-width:619px){.cf-act{width:100%;flex-direction:column}.cf-send,.cf-wa{width:100%}.cf-st{text-align:left}}
@media(prefers-reduced-motion:reduce){.cf-wa{transition:none}.cf-wa:hover{transform:none}}
/* barridos con borde difuminado */
.plc .gb,.cf-send,.og,.cf-wa{position:relative;overflow:hidden;isolation:isolate}
.plc.p1 .gb,.plc .gb{--c1:#0B1F3A;--c2:#1B46C8}
.plc.p2 .gb{--c1:#1B46C8;--c2:#38BDF8}
.plc.p3 .gb{--c1:#2457E6;--c2:#38BDF8}
.cf-send{--c1:#1B46C8;--c2:#38BDF8}
.og,.cf-wa{--c1:#0B1F3A;--c2:#16367F}
.plc .gb::before,.cf-send::before,.og::before,.cf-wa::before{content:"";position:absolute;top:0;bottom:0;left:0;right:auto;inset:0 auto 0 0;width:250%;z-index:-1;background:linear-gradient(100deg,var(--c1) 0,var(--c2) 40%);-webkit-mask-image:linear-gradient(100deg,#000 56%,transparent 100%);mask-image:linear-gradient(100deg,#000 56%,transparent 100%);transform:translateX(-100%);transition:transform .7s cubic-bezier(.22,.7,.2,1)}
.plc .gb:hover::before,.plc .gb:focus-visible::before,.cf-send:hover::before,.cf-send:focus-visible::before,.og:hover::before,.og:focus-visible::before,.cf-wa:hover::before,.cf-wa:focus-visible::before{transform:translateX(0)}
.og,.cf-wa,.plc .gb{transition:color .3s .2s,border-color .3s .1s,transform .3s cubic-bezier(.2,.7,.2,1),box-shadow .4s}
.og:hover,.og:focus-visible{background:transparent;color:#fff;border-color:var(--c1);transform:translateY(-2px);box-shadow:0 16px 26px -16px rgba(11,31,58,.7)}
.cf-wa:hover,.cf-wa:focus-visible{background:#fff;color:#fff;border-color:var(--c1)}
.cf-wa svg{position:relative}
@media(prefers-reduced-motion:reduce){.og::before,.cf-wa::before{transition:none}}
/* efecto comun de los botones blancos (el de "Pedir presupuesto") */
.og,.cf-wa,.up,.tb a{position:relative;overflow:hidden;isolation:isolate;--c1:#0B1F3A;--c2:#1B46C8}
.up{--c1:#1B46C8;--c2:#38BDF8}
.og::before,.cf-wa::before,.up::before,.tb a::before{content:"";position:absolute;top:0;bottom:0;left:0;right:auto;width:250%;z-index:-1;background:linear-gradient(100deg,var(--c1) 0,var(--c2) 40%);-webkit-mask-image:linear-gradient(100deg,#000 56%,transparent 100%);mask-image:linear-gradient(100deg,#000 56%,transparent 100%);transform:translateX(-100%);transition:transform .7s cubic-bezier(.22,.7,.2,1)}
.og:hover::before,.og:focus-visible::before,.cf-wa:hover::before,.cf-wa:focus-visible::before,.up:hover::before,.up:focus-visible::before,.tb a:hover::before,.tb a:focus-visible::before{transform:translateX(0)}
.og::after,.cf-wa::after,.up::after,.tb a::after{content:"";position:absolute;top:-40%;bottom:-40%;left:-40%;width:28%;z-index:-1;background:linear-gradient(100deg,transparent,rgba(255,255,255,.4),transparent);transform:skewX(-20deg);opacity:0;pointer-events:none}
.og:hover::after,.cf-wa:hover::after,.up:hover::after,.tb a:hover::after{opacity:1;animation:gbshine .9s .15s ease-out}
.og,.cf-wa,.up,.tb a{transition:color .3s .2s,border-color .3s .1s,transform .3s cubic-bezier(.2,.7,.2,1),box-shadow .4s}
.og:hover,.og:focus-visible,.cf-wa:hover,.cf-wa:focus-visible,.up:hover,.up:focus-visible,.tb a:hover,.tb a:focus-visible{color:#fff;background:#fff;box-shadow:0 18px 30px -14px rgba(27,70,200,.8);transform:translateY(-2px)}
.og:hover,.og:focus-visible,.cf-wa:hover,.cf-wa:focus-visible{background:transparent;border-color:var(--c1)}
.cf-wa:hover,.cf-wa:focus-visible{background:#fff}
.og>span,.cf-wa>span{display:inline-block;transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.og:hover>span,.cf-wa:hover>span{transform:translateX(4px)}
.cf-wa svg{transition:color .3s .2s,transform .4s cubic-bezier(.2,.7,.2,1)}
.cf-wa:hover svg{color:#4ADE80;transform:scale(1.12) rotate(-8deg)}
.up>span{transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.up:hover svg,.up:focus-visible svg{background:#fff;color:#1B46C8;transform:translateY(-3px)}
.tb a svg{transition:color .3s .2s,transform .4s cubic-bezier(.2,.7,.2,1)}
.tb a:hover svg{transform:scale(1.12)}
@media(prefers-reduced-motion:reduce){.og::before,.cf-wa::before,.up::before,.tb a::before{transition:none}.og:hover::after,.cf-wa:hover::after,.up:hover::after,.tb a:hover::after{animation:none}.og:hover,.cf-wa:hover,.up:hover,.tb a:hover{transform:none}}
/* etiqueta del hero: que no toque el borde en movil */
@media(max-width:520px){.hero .pl{white-space:normal;max-width:calc(100% - 40px);padding:9px 18px;font-size:.88rem;line-height:1.35;text-align:center;text-wrap:balance;border-radius:26px}}
/* parrafo del hero: dos lineas en pantallas anchas */
@media(min-width:760px){.hero .lead{max-width:47em;text-wrap:balance}}
/* trabajo real: ventana de navegacion */
html.bw-lock{overflow:hidden}
.bw{border:0;padding:0;margin:0;background:transparent;max-width:none;max-height:none;width:100vw;height:100vh;height:100dvh;color:var(--ink)}
.bw[open]{display:grid;place-items:center}
.bw::backdrop{background:rgba(11,31,58,.58);-webkit-backdrop-filter:blur(7px);backdrop-filter:blur(7px)}
.bw-win{width:min(1180px,calc(100vw - 48px));height:min(780px,calc(100vh - 48px));height:min(780px,calc(100dvh - 48px));background:#fff;border-radius:24px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 44px 90px -30px rgba(0,0,0,.65);animation:bwin .4s cubic-bezier(.2,.8,.2,1)}
@keyframes bwin{from{opacity:0;transform:translateY(22px) scale(.97)}}
.bw-bar{display:flex;align-items:center;gap:12px;padding:10px 12px;background:#ECEFF3;border-bottom:1px solid var(--line)}
.bw-dots{display:flex;gap:6px;padding:0 4px}.bw-dots i{width:11px;height:11px;border-radius:50%;background:#C9D0DA}
.bw-url{flex:1;min-width:0;margin:0;display:flex;align-items:center;gap:8px;height:36px;padding:0 15px;border-radius:99px;background:#fff;border:1px solid var(--line);font-size:.93rem;font-weight:400;line-height:1;color:#33506B;white-space:nowrap;overflow:hidden}
.bw-url svg{flex:none;color:#16A34A}
.bw-ext{display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 8px 0 16px;border-radius:99px;background:var(--ink);color:#fff;font-size:.92rem;font-weight:500;text-decoration:none;white-space:nowrap;transition:background .25s,transform .3s}
.bw-ext svg{width:22px;height:22px;padding:4px;border-radius:50%;background:rgba(255,255,255,.16)}
.bw-ext:hover{background:var(--acc);transform:translateY(-1px)}
.bw-x{flex:none;width:36px;height:36px;border-radius:50%;border:1px solid var(--line);background:#fff;color:var(--ink);display:grid;place-items:center;cursor:pointer;transition:background .25s,color .25s,transform .3s}
.bw-x:hover{background:var(--ink);color:#fff;transform:rotate(90deg)}
.bw-ext:focus-visible,.bw-x:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
.bw-body{position:relative;flex:1;min-height:0;background:#fff}
.bw-body iframe{position:absolute;inset:0;width:100%;height:100%;border:0;background:#fff}
.bw-load{position:absolute;inset:0;z-index:1;display:grid;place-items:center;color:var(--muted);background:#fff}
.bw-load[hidden]{display:none}
.bw-ft{display:flex;gap:20px;align-items:center;justify-content:space-between;padding:12px 20px;border-top:1px solid var(--line);font-size:.93rem;color:#33506B;background:#F8FAFC}
.bw-ft p{margin:0;flex:1;min-width:0;line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.bw-nl{color:var(--muted);white-space:nowrap}
@media(max-width:760px){.bw-win{width:100vw;height:100vh;height:100dvh;border-radius:0}.bw-dots{display:none}.bw-ext>span{display:none}.bw-ext{padding:0 7px}.bw-ft{display:none}}
@media(prefers-reduced-motion:reduce){.bw-win{animation:none}.wk,.wk-t,.wk-go i,.wk-lb{transition:none}}
/* enlace a la academia: se lee como texto normal */
a.cb,a.cb:hover,a.cb:visited,a.cb:active{color:inherit;text-decoration:none;font:inherit;cursor:pointer;background:none}
a.cb,a.cb:hover,a.cb:visited,a.cb:active{font-weight:700}
a.cb:focus-visible{outline:2px solid var(--acc);outline-offset:3px;border-radius:4px}
/* movil: la tira del menu se desliza con degradado en el borde */
@media(max-width:959px){.hn{-webkit-mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 36px),transparent 100%);mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 36px),transparent 100%);scroll-snap-type:x proximity}.hn.at-end{-webkit-mask-image:none;mask-image:none}.hn a{scroll-snap-align:center;padding:11px 12px}}
/* tactil: zonas de toque de al menos 44 px sin cambiar el aspecto */
@media(pointer:coarse){.lang button,.hdr .logo,.gb.sm,.ft-logo{position:relative}
.lang button::after,.hdr .logo::after,.gb.sm::after,.ft-logo::after{content:"";position:absolute;inset:-9px -5px}
.hdr .logo{display:inline-flex;align-items:center}
.up{height:44px}
.ft-fs a,.ft-fs .off{width:44px;height:44px}}
@media(max-width:620px){.ft-fs a,.ft-fs .off{width:44px;height:44px}}
/* moviles muy estrechos: las etiquetas pueden pasar a dos lineas */
@media(max-width:420px){.pl{white-space:normal;max-width:100%;line-height:1.35;text-align:center;text-wrap:balance;border-radius:24px;padding:9px 18px}}
.bw-win:focus,.bw-win:focus-visible{outline:0}
/* movil: frases en una linea, parrafo del hero en 3 lineas y barra de redes vertical */
.center p.one{white-space:nowrap;max-width:none}
@media(max-width:759px){.center p.one{font-size:min(1.0625rem,4.7vw)}
.hero .lead{font-size:.93rem;line-height:1.55;max-width:none;margin:22px -10px 0;text-wrap:balance}}
/* tarjetas de codigo del panel: sin cortes con puntos suspensivos */
.wbc{align-items:center}
.wbc code{white-space:nowrap;overflow:hidden;text-overflow:clip;line-height:1.5;min-width:0}
@media(max-width:700px){.wbc code{font-size:min(.86rem,3.25vw)}}
.wb-tabs{scroll-padding-inline:16px}
/* barra de redes: mismo aspecto que en escritorio, colgando del borde izquierdo de la foto */
@media(max-width:859px){.tb{left:-8px;top:calc((100vw - 84px) * 1.25 - 270px);bottom:auto;flex-direction:column;padding:8px;gap:8px;border-radius:24px}.tb a,.tb .off{width:44px;height:44px;border-radius:15px}}
/* revision: logotipo centrado, frases equilibradas, pie en una linea, certificados tactiles */
.goal .gc .sg,.who .gc .sg{align-self:center;margin-left:auto;margin-right:auto}
.center p:not(.one){text-wrap:balance}
p{text-wrap:pretty}
.ft-sub{white-space:nowrap;font-size:min(.84rem,3.05vw)}
@media(hover:none){
.cc{transition:transform .5s cubic-bezier(.2,.7,.2,1),outline-color .25s .4s,box-shadow .5s}
.cc.lit{transform:translateY(-3px);outline-color:transparent;transition:transform .5s cubic-bezier(.2,.7,.2,1),box-shadow .5s,outline-color 0s;box-shadow:0 22px 34px -18px rgba(27,70,200,.65)}
.cc.lit::before{transform:translateY(0)}
.cc.lit::after{opacity:1;animation:ccshine .9s .15s ease-out}
.cc.lit b{color:#fff}
.cc.lit svg{color:#7DD3FC;transform:scale(1.12) rotate(-6deg)}
.cc.lit .ck{animation:ccck .55s .25s ease-out both}
.cc:active{transform:scale(.98)}
}
@media(prefers-reduced-motion:reduce){.cc.lit::after,.cc.lit .ck{animation:none}.cc.lit{transform:none}}
/* menu superior un poco mas separado del borde */
@media(max-width:959px){.hdr{top:28px}}
/* márgenes laterales iguales en todas las secciones a partir de 760 px (antes cambiaban a 700, 860 y 900) */
@media(min-width:760px){.three,.faq,.goal,.who,.pj,.wl,.certs{padding-left:32px;padding-right:32px}}
/* certificados: diez en total (SOLID y Bases de datos es uno solo): 2 columnas en móvil y tablet, 5 en escritorio */
/* movil: la tarjeta de plan que estas viendo se ilumina y las otras quedan opacas; extras en 2 x 2 */
@media(hover:none){
.plans.focus .plc{transition:opacity .45s,filter .45s,transform .55s cubic-bezier(.2,.7,.2,1),box-shadow .45s}
.plans.focus .plc:not(.hot){opacity:.42;filter:saturate(.55);transform:scale(.985)}
.plans.focus .plc.hot{transform:translateY(-4px);box-shadow:0 30px 50px -30px rgba(11,31,58,.55)}
.plans.focus .plc.p2.hot{box-shadow:0 34px 54px -30px rgba(36,87,230,.7)}
}
@media(max-width:620px){
.ex{display:grid;grid-template-columns:1fr 1fr;gap:10px;max-width:420px;margin-left:auto;margin-right:auto}
.ex span{display:flex;align-items:center;justify-content:center;text-align:center;padding:10px 12px;min-height:50px;font-size:.92rem;line-height:1.25;text-wrap:balance}
}
/* menu movil: una sola linea que se despliega al tocar el boton */
.hm,.lang-m{display:none}
@media(max-width:959px){
.hw{display:grid;grid-template-columns:minmax(0,1fr) auto auto;grid-template-areas:"logo cta tog" "nav nav nav";align-items:center;column-gap:8px;row-gap:0;padding:6px 6px 6px 14px}
.hw .logo{grid-area:logo;justify-self:start}
.hr{grid-area:cta;margin:0}
.hr .lang,.hr .soc{display:none}
.hm{grid-area:tog;display:block;position:relative;width:44px;height:44px;padding:0;border:0;border-radius:14px;background:transparent;color:var(--ink);cursor:pointer;-webkit-tap-highlight-color:transparent}
.hm span{position:absolute;left:13px;right:13px;height:2px;border-radius:2px;background:currentColor;transition:transform .4s cubic-bezier(.2,.7,.2,1),top .4s cubic-bezier(.2,.7,.2,1)}
.hm span:first-child{top:18px}.hm span:last-child{top:25px}
.hdr.open .hm span:first-child{top:21.5px;transform:rotate(45deg)}
.hdr.open .hm span:last-child{top:21.5px;transform:rotate(-45deg)}
.hm:focus-visible{outline:2px solid var(--acc);outline-offset:-2px}
.hn{grid-area:nav;width:100%;display:flex;flex-direction:column;gap:2px;overflow:hidden;max-height:0;opacity:0;visibility:hidden;padding:0;-webkit-mask-image:none;mask-image:none;transition:max-height .5s cubic-bezier(.2,.7,.2,1),opacity .25s,visibility 0s .5s}
.hdr.open .hn{max-height:min(440px,calc(100dvh - 140px));overflow-y:auto;opacity:1;visibility:visible;padding:4px 0 8px;transition:max-height .5s cubic-bezier(.2,.7,.2,1),opacity .35s .05s,visibility 0s}
.hn a{display:flex;align-items:center;justify-content:space-between;padding:13px 14px;border-radius:14px;font-size:1.05rem;opacity:0;transform:translateY(-8px);transition:opacity .3s,transform .45s cubic-bezier(.2,.7,.2,1),background .2s}
.hdr.open .hn a{opacity:1;transform:none}
.hdr.open .hn a:nth-child(1){transition-delay:.06s}.hdr.open .hn a:nth-child(2){transition-delay:.11s}.hdr.open .hn a:nth-child(3){transition-delay:.16s}.hdr.open .hn a:nth-child(4){transition-delay:.21s}.hdr.open .hn a:nth-child(5){transition-delay:.26s}
.hn a.on{background:rgba(255,255,255,.8);color:var(--ink);font-weight:500}
.hn a.on::after{content:"";width:8px;height:8px;border-radius:50%;background:var(--acc)}
.lang-m{display:flex;gap:8px;margin-top:8px;padding:12px 2px 2px;border-top:1px solid rgba(11,42,71,.1);opacity:0;transform:translateY(-8px);transition:opacity .3s,transform .45s cubic-bezier(.2,.7,.2,1)}
.hdr.open .lang-m{opacity:1;transform:none;transition-delay:.3s}
.lang-m button{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:11px 12px;border-radius:14px;border:1px solid rgba(11,42,71,.1);background:transparent;font-weight:500}
.lang-m button span{display:inline}
.lang-m button[aria-pressed=true]{background:#fff;color:var(--ink);box-shadow:0 8px 16px -12px rgba(11,31,58,.5)}
.hero:not(.hero-b),.hero.hero-b{padding-top:112px}
.hdr{transition:background .35s}
.hdr.open{background:rgba(244,246,249,.95)}
}
@media(prefers-reduced-motion:reduce){.hm span,.hn,.hn a,.lang-m{transition:none}}
/* proyectos: tarjetas con visual */
.wl{max-width:1160px;margin:48px auto 0;padding:0 20px;list-style:none;display:grid;gap:22px}
@media(min-width:900px){.wl{padding:0 32px;gap:26px}}
.wk{position:relative;display:grid;grid-template-columns:minmax(0,1fr);width:100%;padding:0;margin:0;text-align:left;font:inherit;color:inherit;cursor:pointer;border:1px solid var(--line);border-radius:34px;background:linear-gradient(140deg,#fff 0%,#F6F9FE 55%,#E9F0FD 100%);overflow:hidden;isolation:isolate;box-shadow:0 30px 50px -40px rgba(11,31,58,.55);transition:transform .55s cubic-bezier(.2,.7,.2,1),box-shadow .55s,border-color .4s}
@media(min-width:700px){.wk{grid-template-columns:minmax(0,1.02fr) minmax(0,.98fr);min-height:330px}}
.wk::before{content:"";position:absolute;left:34px;right:34px;top:0;height:2px;border-radius:2px;background:linear-gradient(90deg,transparent,var(--acc2),var(--acc),transparent);opacity:.45;transition:opacity .4s;z-index:2}
.wk::after{content:"";position:absolute;right:-130px;top:-150px;width:440px;height:440px;border-radius:50%;background:radial-gradient(circle,rgba(56,189,248,.2),rgba(36,87,230,0) 68%);z-index:-1;pointer-events:none}
.wk-wm{position:absolute;left:16px;bottom:-64px;z-index:-1;font:italic 400 clamp(130px,17vw,220px)/1 var(--s);color:transparent;-webkit-text-stroke:1.5px rgba(36,87,230,.11);letter-spacing:-.04em;pointer-events:none;user-select:none}
.wk-body{position:relative;display:flex;flex-direction:column;align-items:flex-start;justify-content:center;gap:18px;padding:clamp(24px,3.4vw,42px);min-width:0}
.wk-st{display:inline-flex;align-items:center;gap:9px;padding:6px 14px 6px 11px;border-radius:99px;background:rgba(255,255,255,.88);border:1px solid #C5D2EC;color:#1B46C8;font-size:.88rem;font-weight:500;box-shadow:0 8px 16px -12px rgba(36,87,230,.5)}
.wk-st i{width:8px;height:8px;border-radius:50%;background:var(--acc2);animation:wkp 2.2s ease-out infinite}
@keyframes wkp{0%{box-shadow:0 0 0 0 rgba(56,189,248,.55)}70%{box-shadow:0 0 0 9px rgba(56,189,248,0)}100%{box-shadow:0 0 0 0 rgba(56,189,248,0)}}
.wk-m{display:block}
.wk-t{display:block;font-size:clamp(2rem,4vw,3.1rem);font-weight:500;line-height:1.05;letter-spacing:-.01em;color:var(--acc)}
.wk-d{display:block;margin-top:12px;max-width:26em;color:#33506B;font-size:1.08rem;line-height:1.5}
.wk-tg{display:flex;flex-wrap:wrap;gap:8px}
.wk-p{display:inline-flex;align-items:center;padding:5px 13px;border-radius:99px;border:1px solid var(--line);background:rgba(255,255,255,.8);color:#33506B;font-size:.88rem;line-height:1.3}
.wk-cta{position:relative;overflow:hidden;isolation:isolate;display:inline-flex;align-items:center;gap:18px;height:54px;margin-top:4px;padding:0 8px 0 24px;border-radius:99px;background:#fff;border:1.5px solid #C9D3E3;color:var(--ink);font-weight:500;font-size:1.02rem;--c1:#0B1F3A;--c2:#1B46C8;transition:color .3s .2s,border-color .3s .1s,box-shadow .4s}
.wk-cta::before{content:"";position:absolute;top:0;bottom:0;left:0;width:250%;z-index:-1;background:linear-gradient(100deg,var(--c1) 0,var(--c2) 40%);-webkit-mask-image:linear-gradient(100deg,#000 56%,transparent 100%);mask-image:linear-gradient(100deg,#000 56%,transparent 100%);transform:translateX(-100%);transition:transform .7s cubic-bezier(.22,.7,.2,1)}
.wk-cta i{display:grid;place-items:center;width:38px;height:38px;border-radius:50%;background:var(--ink);color:#fff;transition:background .3s .2s,color .3s .2s,transform .5s cubic-bezier(.2,.7,.2,1)}
.wk-cta i svg{width:18px;height:18px}
.wk-vis{position:relative;display:grid;place-items:center;min-width:0;padding:clamp(18px,3vw,36px)}
@media(max-width:699px){.wk-vis{order:-1;padding:22px 22px 0}}
.wk-mock{position:relative;display:block;width:100%;overflow:hidden;border-radius:20px;background:#fff;box-shadow:0 40px 60px -34px rgba(11,31,58,.6),0 0 0 1px rgba(11,31,58,.07);transform:perspective(1200px) rotateY(-9deg) rotateX(3deg) rotate(-1.2deg);transition:transform .8s cubic-bezier(.2,.7,.2,1),box-shadow .8s}
@media(max-width:699px){.wk-mock{transform:perspective(900px) rotateY(-4deg) rotate(-.8deg)}}
.wk-mock .mock-bar{display:flex;padding:9px 13px}
.wk-mock img{display:block;width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;object-position:top}
.wk:active{transform:scale(.99)}
@media(hover:hover){
.wk:not(.ghost):hover{transform:translateY(-6px);border-color:#C5D2EC;box-shadow:0 46px 70px -44px rgba(27,70,200,.55)}
.wk:not(.ghost):hover::before{opacity:1}
.wk:not(.ghost):hover .wk-mock{transform:perspective(1200px) rotateY(-2deg) rotateX(1deg) translateY(-4px) scale(1.02);box-shadow:0 50px 70px -34px rgba(27,70,200,.55),0 0 0 1px rgba(11,31,58,.07)}
.wk:not(.ghost):hover .wk-cta{color:#fff;border-color:var(--c1);box-shadow:0 18px 30px -14px rgba(27,70,200,.8)}
.wk:not(.ghost):hover .wk-cta::before{transform:translateX(0)}
.wk:not(.ghost):hover .wk-cta i{background:#fff;color:#1B46C8;transform:rotate(45deg)}
}
.wk:focus-visible{outline:2px solid var(--acc);outline-offset:-2px}
.wk.ghost{cursor:default;border-style:dashed;border-color:#C5D2EC;background:linear-gradient(140deg,rgba(255,255,255,.7),rgba(238,243,255,.55));box-shadow:none}
.wk.ghost::before{opacity:.25}
.wk.ghost .wk-t{opacity:.72}
.wk.ghost .wk-st{color:#5B6F82;border-color:#D5DCE8}
.wk.ghost .wk-st i{background:#5F6E83;animation:none}
.wk.ghost .wk-mock{transform:perspective(1200px) rotateY(-9deg) rotateX(3deg) rotate(-1.2deg);box-shadow:0 30px 50px -36px rgba(11,31,58,.35),0 0 0 1px rgba(11,31,58,.06)}
.sk-b{display:grid;gap:12px;align-content:start;padding:20px 18px 24px;aspect-ratio:16/10;background:linear-gradient(180deg,#fff,#F4F7FC)}
.sk-b i{display:block;height:12px;border-radius:7px;background:linear-gradient(90deg,#E3E9F3 0%,#F5F8FD 50%,#E3E9F3 100%);background-size:220% 100%;animation:wksh 2.6s linear infinite}
.sk-b i:nth-child(1){width:46%;height:16px}.sk-b i:nth-child(2){width:78%}.sk-b i:nth-child(3){width:64%}
.sk-b i:nth-child(4){width:100%;height:68px;border-radius:12px;margin-top:6px}
@keyframes wksh{from{background-position:200% 0}to{background-position:-20% 0}}
@media(prefers-reduced-motion:reduce){.wk,.wk-mock,.wk-cta,.wk-cta i,.wk-cta::before{transition:none}.wk-st i,.sk-b i{animation:none}.wk:not(.ghost):hover{transform:none}}
/* tema: boton y modo oscuro */
.th{flex:none;position:relative;overflow:hidden;width:40px;height:40px;padding:0;display:inline-block;border-radius:50%;border:1px solid rgba(11,42,71,.12);background:rgba(255,255,255,.7);color:var(--ink);cursor:pointer;-webkit-tap-highlight-color:transparent;transition:background .3s,border-color .3s,transform .3s cubic-bezier(.2,.7,.2,1)}
.th svg{position:absolute;left:50%;top:50%;width:20px;height:20px;margin:-10px 0 0 -10px;transition:transform .55s cubic-bezier(.2,.7,.2,1),opacity .3s}
.th .sun{opacity:0;transform:rotate(-90deg) scale(.4)}
.th .moon{opacity:1;transform:none}
.th:hover{transform:translateY(-1px)}
.th:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
.th-t{display:none}
.logo-d{display:none!important}
.th-anim,.th-anim *{transition:background-color .45s ease,color .45s ease,border-color .45s ease!important}
html[data-theme=dark]{color-scheme:dark;--ink:#EAF1FF;--muted:#9FB2CF;--line:rgba(255,255,255,.12);--card:#0F1A30;--acc:#5B8DFF;--acc2:#38BDF8;--pastel:linear-gradient(#0F1A30,#0F1A30);--rb:linear-gradient(#2457E6,#2457E6)}
html[data-theme=dark] body{background:#050A16;color:var(--ink)}
html[data-theme=dark] .frame{background:#0A1226;box-shadow:0 0 0 1px rgba(255,255,255,.08),0 30px 60px -40px rgba(0,0,0,.8)}
html[data-theme=dark] .th{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.18);color:#EAF1FF}
html[data-theme=dark] .th .sun{opacity:1;transform:none}
html[data-theme=dark] .th .moon{opacity:0;transform:rotate(90deg) scale(.4)}
html[data-theme=dark] .logo-l{display:none!important}
html[data-theme=dark] .logo-d{display:block!important}
html[data-theme=dark] .hdr{background:rgba(14,24,46,.8);border-color:rgba(255,255,255,.12);box-shadow:0 24px 44px -24px rgba(0,0,0,.8)}
html[data-theme=dark] .hdr.open{background:rgba(14,24,46,.96)}
html[data-theme=dark] .hn a.on{background:rgba(255,255,255,.08)}
html[data-theme=dark] em{background-image:linear-gradient(104deg,transparent 0 42%,rgba(47,107,255,0) 42%,rgba(56,189,248,.9) 46.5%,rgba(125,211,252,1) 48.5%,rgba(56,189,248,.9) 50.5%,rgba(47,107,255,0) 55%,transparent 55% 100%),linear-gradient(95deg,#A9C4FF 0%,#7FA6FF 38%,#5B8DFF 54%,#38BDF8 78%,#A9C4FF 100%)}
html[data-theme=dark] .dk,html[data-theme=dark] .gb,html[data-theme=dark] .cf-send,html[data-theme=dark] .bw-ext,html[data-theme=dark] .mcta,html[data-theme=dark] .b3 .go,html[data-theme=dark] .wk-cta i,html[data-theme=dark] .plc.p3 .gb i,html[data-theme=dark] .cf-chips input:checked+span{background:#2457E6;border-color:#2457E6;color:#fff}
html[data-theme=dark] .up svg{background:#2457E6}
html[data-theme=dark] .gb:hover,html[data-theme=dark] .dk:hover{background:#3A6DF0;border-color:#3A6DF0}
html[data-theme=dark] .og{border-color:rgba(255,255,255,.3);color:#EAF1FF}
html[data-theme=dark] .mq i,html[data-theme=dark] .mc .ico,html[data-theme=dark] .wbl li img{background:#EEF3FB}
html[data-theme=dark] .hero::before{background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px)}
html[data-theme=dark] .hero::after{background:radial-gradient(30% 45% at 6% 30%,rgba(36,87,230,.22),transparent 70%),radial-gradient(30% 45% at 96% 20%,rgba(56,189,248,.18),transparent 70%),radial-gradient(28% 40% at 80% 62%,rgba(36,87,230,.14),transparent 70%)}
html[data-theme=dark] .tb{background:#1B2A47}
html[data-theme=dark] .wk{background:linear-gradient(140deg,#0F1A30 0%,#0E1A33 55%,#12244A 100%);border-color:rgba(255,255,255,.1);box-shadow:0 30px 50px -40px rgba(0,0,0,.9)}
html[data-theme=dark] .wk::after{background:radial-gradient(circle,rgba(56,189,248,.16),rgba(36,87,230,0) 68%)}
html[data-theme=dark] .wk-st{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.16);color:#9DB8FF}
html[data-theme=dark] .wk-p{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);color:#B4C5E0}
html[data-theme=dark] .wk-p.wk-b{background:rgba(91,141,255,.15);border-color:rgba(91,141,255,.35);color:#9DB8FF}
html[data-theme=dark] .wk-cta{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.2);color:#EAF1FF}
html[data-theme=dark] .wk-wm{-webkit-text-stroke:1.5px rgba(125,170,255,.14)}
html[data-theme=dark] .wk.ghost{background:linear-gradient(140deg,rgba(255,255,255,.03),rgba(91,141,255,.06));border-color:rgba(255,255,255,.18)}
html[data-theme=dark] .sk-b{background:linear-gradient(180deg,#101C33,#0C1630)}
html[data-theme=dark] .sk-b i{background:linear-gradient(90deg,#16264A 0%,#1E3160 50%,#16264A 100%);background-size:220% 100%}
html[data-theme=dark] .plc{background:#0F1A30}
html[data-theme=dark] .plc.p3{background:linear-gradient(160deg,#16367F,#0B1F3A 70%)}
html[data-theme=dark] .plc-img{background:#0A1226}
html[data-theme=dark] .cc{background:#0F1A30;outline-color:rgba(255,255,255,.1)}
html[data-theme=dark] .cc:hover,html[data-theme=dark] .cc.lit{outline-color:transparent}
html[data-theme=dark] .cc b{color:#EAF1FF}
html[data-theme=dark] .cf{background:#0F1A30}
html[data-theme=dark] .cf input,html[data-theme=dark] .cf textarea{background:#0A1226;border-color:rgba(255,255,255,.14);color:#EAF1FF}
html[data-theme=dark] .cf input::placeholder,html[data-theme=dark] .cf textarea::placeholder{color:#6F83A3}
html[data-theme=dark] .ctab{background:linear-gradient(135deg,#0F1A30,#101F3C)}
html[data-theme=dark] .bw-win{background:#0F1A30}
html[data-theme=dark] .bw-body,html[data-theme=dark] .bw-load{background:#0F1A30}
html[data-theme=dark] .wk-mock,html[data-theme=dark] .mock{box-shadow:0 40px 60px -34px rgba(0,0,0,.8),0 0 0 1px rgba(255,255,255,.08)}
html[data-theme=dark] .ft-box{box-shadow:0 0 0 1px rgba(255,255,255,.08)}
html[data-theme=dark] .cf-o,html[data-theme=dark] .pr em{background-image:none}
html[data-theme=dark] ::selection{background:#2457E6;color:#fff}
html[data-theme=dark] .wbc{background:#050B18;box-shadow:inset 0 0 0 1px rgba(125,211,252,.24);color:#CFE0F7}
html[data-theme=dark] .b4{background:#050B18;box-shadow:0 0 0 1px rgba(255,255,255,.14)}
html[data-theme=dark] .b4 .ed-bar i:nth-child(1){background:#FF6B6B}
html[data-theme=dark] .b4 .ed-bar i:nth-child(2){background:#FFC857}
html[data-theme=dark] .b4 .ed-bar i:nth-child(3){background:#5BD68A}
html[data-theme=dark] .wb-bar i{background:#3A4A68}
html[data-theme=dark] .wbk li{background:#17294A;box-shadow:inset 0 0 0 1px rgba(255,255,255,.07)}
@media(max-width:380px){.hr .th{display:none}}
@media(max-width:959px){.lang-m .th-m{display:inline-flex;align-items:center;justify-content:center;gap:8px;flex:1;width:auto;height:auto;padding:11px 12px;border-radius:14px;overflow:visible;font-weight:500;transform:none;background:transparent;border:1px solid rgba(11,42,71,.1)}
.lang-m .th-m svg{position:static;margin:0;width:18px;height:18px;transform:none;opacity:1}
.lang-m .th-m .sun{display:none}
.lang-m .th-m .moon{display:block}
.lang-m .th-t{display:inline}}
@media(min-width:381px){.lang-m .th-m{display:none}}
html[data-theme=dark] .lang-m .th-m .moon{display:none}
html[data-theme=dark] .lang-m .th-m .sun{display:block}
html[data-theme=dark] .lang-m .th-m{border-color:rgba(255,255,255,.18);background:transparent}
@media(min-width:960px){.hr .gb.sm{display:none}.hw{gap:6px 28px}.hr{gap:20px}.hn a{padding:7px 13px}.soc{gap:6px;margin-right:4px}.lang button{padding:5px 11px}}
@media(max-width:520px){.hero .pl{white-space:nowrap;max-width:none;padding:9px 14px;font-size:min(.88rem,3.3vw);line-height:1.35;border-radius:99px}}
.ft-lg{flex:1 1 100%;display:flex;flex-wrap:wrap;gap:6px 22px;font-size:.92rem}
.ft-lg a{color:#8FA6C9;text-decoration:none;transition:color .2s}
.ft-lg a:hover{color:#fff}
.cf-pv{color:inherit;text-decoration:underline;text-underline-offset:3px}
.lg{padding-top:clamp(128px,13vw,176px)}
.lg-w{max-width:780px;margin:0 auto;padding:0 clamp(18px,4vw,28px)}
html:not([lang=en]) .lg-en,html[lang=en] .lg-es{display:none}
.lg h1{margin:0 0 14px;font-size:clamp(2.2rem,5.2vw,3.4rem);line-height:1.1;font-weight:600;letter-spacing:-.01em;color:var(--ink)}
.lg-lead{margin:0 0 6px;font-size:1.12rem;line-height:1.6;color:var(--muted)}
.lg-upd{margin:0 0 clamp(26px,4vw,40px);font-size:.9rem;color:var(--muted)}
.lg-s{padding:clamp(20px,3vw,28px) 0;border-top:1px solid var(--line)}
.lg-s h2{margin:0 0 10px;font-size:1.28rem;line-height:1.3;font-weight:600;color:var(--ink)}
.lg-s p{margin:0 0 12px;font-size:1.02rem;line-height:1.7;color:var(--muted)}
.lg-s p:last-child{margin-bottom:0}
.lg-s b{font-weight:600;color:var(--ink)}
.lg-s a{color:var(--acc);text-decoration:underline;text-underline-offset:3px}
.lg-id,.lg-ck{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.lg-id li,.lg-ck li{display:grid;grid-template-columns:minmax(120px,170px) 1fr;gap:4px 18px;padding:14px 18px;border-radius:16px;background:var(--card);border:1px solid var(--line)}
.lg-ck li{grid-template-columns:minmax(150px,210px) 1fr}
.lg-id b,.lg-ck b{color:var(--ink);font-weight:600}
.lg-id span,.lg-ck span{color:var(--muted);line-height:1.6;overflow-wrap:anywhere}
@media(max-width:600px){.lg-id li,.lg-ck li{grid-template-columns:1fr;gap:2px}}
.bw-gate{position:absolute;inset:0;z-index:2;display:grid;place-items:center;padding:24px;background:#F3F6FB}
.bw-gate[hidden]{display:none}
.bw-gate-in{max-width:460px;text-align:center}
.bw-gate-in h4{margin:0 0 10px;font-size:1.35rem;font-weight:600;color:var(--ink)}
.bw-gate-in p{margin:0 0 22px;line-height:1.65;color:var(--muted)}
.bw-gate-in p b{color:var(--ink);font-weight:600}
.bw-gate-act{display:flex;flex-wrap:wrap;gap:12px;justify-content:center}
html[data-theme=dark] .bw-gate{background:#0F1A30}
.lg-act{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}
.lg-act .og span{padding:0 4px}
@media(min-width:960px) and (max-width:1099px){.hw{gap:6px 14px}.hr{gap:12px}.hn a{padding:7px 8px}.lang button span{display:none}.lang button{padding:5px 8px}}
/* la cinta deja sitio a la sombra de las fichas (el recorte del desplazamiento la cortaba) */
button.cc{font:inherit;color:inherit;cursor:pointer;width:100%;-webkit-appearance:none;appearance:none;text-align:left}
.cc-i{position:absolute;top:13px;right:13px;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:rgba(36,87,230,.09);color:var(--acc);transition:background .35s,color .35s}
.cc .cc-i svg{width:14px;height:14px;align-self:auto;color:inherit}
.cc:hover .cc-i,.cc.lit .cc-i{background:rgba(255,255,255,.22);color:#fff}
button.cc:focus-visible{outline:3px solid var(--acc2);outline-offset:3px}
.cdlg .bw-win{width:min(1100px,calc(100vw - 48px));height:auto;max-height:calc(100vh - 48px);max-height:calc(100dvh - 48px);background:#0B0B0B}
.cdlg{--cdp:clamp(18px,3.2vw,40px)}
.cdlg .cd-body{background:#0B0B0B;padding:var(--cdp);display:flex;justify-content:center;align-items:center;min-height:0}
.cdlg .cd-body img{display:block;height:auto;width:min(100%,calc((100vh - 48px - 57px - 2*var(--cdp)) * 1.417));width:min(100%,calc((100dvh - 48px - 57px - 2*var(--cdp)) * 1.417));border-radius:10px;box-shadow:0 18px 40px -18px rgba(0,0,0,.9)}
@media(max-width:760px){.cdlg{--cdp:12px}.cdlg .bw-win{width:100vw;max-height:100vh;max-height:100dvh;border-radius:0}.cdlg .cd-body img{width:min(100%,calc((100dvh - 57px - 2*var(--cdp)) * 1.417));border-radius:8px}.cdlg .bw-ext>span{display:none}}
.cd-ico{display:flex;gap:5px;flex:none}
.cd-ico i{width:24px;height:24px;border-radius:7px;background:#fff;box-shadow:0 0 0 1px rgba(11,31,58,.12);display:grid;place-items:center}
.cd-ico img{width:15px;height:15px;object-fit:contain}
.gb:focus-visible,.dk:focus-visible,.og:focus-visible,a:focus-visible,summary:focus-visible,button:focus-visible{outline:3px solid var(--acc2);outline-offset:3px}
"""


def ico(inner, size=24, sw=1.6):
    return ('<svg viewBox="0 0 24 24" width="%d" height="%d" fill="none" stroke="currentColor" stroke-width="%s" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>') % (size, size, sw, inner)


TXT = '<text x="12" y="%s" text-anchor="middle" font-size="%s" font-weight="700" font-family="Barlow,system-ui,sans-serif" fill="currentColor" stroke="none">%s</text>'
SHIELD = '<path d="M4.5 3h15l-1.4 15.5L12 21l-6.1-2.5z"/>'
DEVICO = dict(
    ivs='<img src="img/icons/vscode.svg" alt="" width="128" height="128">',
    ihtml='<img src="img/icons/html5.svg" alt="" width="128" height="128">',
    icss='<img src="img/icons/css3.svg" alt="" width="128" height="128">',
    ijs='<img src="img/icons/javascript.svg" alt="" width="128" height="128">',
    ijava='<img src="img/icons/java.svg" alt="" width="128" height="128">',
    igh2='<img src="img/icons/github.svg" alt="" width="128" height="128">',
    ibulb=ico('<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>'),
)


def _logo(n):
    return '<img src="img/icons/%s.svg" alt="" width="128" height="128" loading="lazy">' % n


MOD_ICON = {
    'mod1': ic('text', 28), 'mod2': _logo('linux'), 'mod3': _logo('python'), 'mod4': _logo('git'),
    'mod5': '<img src="img/icons/sql.png" alt="" width="256" height="256" loading="lazy">', 'mod6': ic('brain', 28), 'mod7': ic('bot', 28),
}


def mods_html():
    out = ['<div class="mods" id="modulos">']
    for i, m in enumerate(MODS):
        tag = '<span class="tg">%s</span>' % T('tag_cert') if m in CERT_MODS else ''
        op = ''
        out.append(
            '<details class="mc"%s><summary><span class="mi">%s</span><span class="mn">%02d</span>'
            '<span class="mt"><b>%s</b>%s</span>%s</summary><dl>'
            '<div><dt>%s</dt><dd>%s</dd></div><div><dt>%s</dt><dd>%s</dd></div><div><dt>%s</dt><dd>%s</dd></div>'
            '</dl></details>' % (op, MOD_ICON[m], i + 1, T(m), tag, ic('chev', 20), T('m_what'), T('m_pending'),
                                 T('m_learn'), T('m_pending'), T('m_use'), T('m_pending')))
    out.append('<a class="mc mcta" href="#certificados"><b>9</b><span>%s</span><i>%s</i></a>' % (T('n_certs'), ic('ur', 20)))
    out.append('</div>')
    return ''.join(out)


def marquee_html():
    def L(n, t):
        return '<i title="%s">%s</i>' % (t, _logo(n).replace(' loading="lazy"', ''))


    # Lo que uso hoy, repartido en dos cintas (6 iconos cada una; la segunda va en sentido contrario)
    row_a = [L('python', 'Python'), L('claudecode', 'Claude Code'), L('chatgpt', 'ChatGPT'), L('antigravity', 'Google Antigravity'),
             '<i title="SQL"><img src="img/icons/sql.png" alt="" width="256" height="256"></i>', L('linux', 'Linux')]
    row_b = [L('vscode', 'VS Code'), L('github', 'GitHub'), L('git', 'Git'), L('html5', 'HTML5'), L('css3', 'CSS'), L('javascript', 'JavaScript')]

    def row(items, cls=''):
        one = ''.join(items)
        return ('<div class="mq%s"><div class="mq-t"><div class="mq-s">%s</div><div class="mq-s" aria-hidden="true">%s</div>'
                '<div class="mq-s" aria-hidden="true">%s</div></div></div>' % (cls, one, one, one))
    return '<div class="mqs" aria-label="Tecnologías">%s%s</div>' % (row(row_a), row(row_b, ' rev'))


def know_html():
    sk = {
        'tree': ico('<rect x="9" y="3" width="6" height="5" rx="1.2"/><path d="M12 8v4M5.5 12h13M5.5 12v4M18.5 12v4"/><rect x="2.5" y="16" width="6" height="5" rx="1.2"/><rect x="15.5" y="16" width="6" height="5" rx="1.2"/>', 24),
        'klass': ico('<rect x="4" y="3" width="16" height="18" rx="2.5"/><path d="M4 9h16M4 15h16"/>', 24),
        'joins': ico('<circle cx="9" cy="12" r="5.5"/><circle cx="15" cy="12" r="5.5"/>', 24),
        'chain': ic('link', 24),
        'server': ico('<rect x="3" y="4" width="18" height="6" rx="2"/><rect x="3" y="14" width="18" height="6" rx="2"/><path d="M7 7h.01M7 17h.01"/>', 24),
        'agent': ico('<circle cx="12" cy="8" r="3.5"/><path d="M5 20c0-3.9 3.1-7 7-7s7 3.1 7 7"/><path d="M19 3v4M17 5h4"/>', 24),
        'loop': ico('<path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/>', 24),
        'pen': ico('<path d="M4 20l4-1L19 8l-3-3L5 16z"/><path d="M14 6l3 3"/>', 24),
        'sliders': ico('<path d="M4 6h8M18 6h2M4 12h2M12 12h8M4 18h10M20 18h0"/><circle cx="15" cy="6" r="2"/><circle cx="9" cy="12" r="2"/><circle cx="17" cy="18" r="2"/>', 24),
        'winai': ico('<rect x="3" y="4" width="18" height="16" rx="3"/><path d="M3 9h18"/><path d="M12 11.5l.9 2.1 2.1.9-2.1.9-.9 2.1-.9-2.1-2.1-.9 2.1-.9z"/>', 24),
    }

    def icon(spec):
        kind, name = spec.split(':', 1)
        if kind == 'logo':
            return '<img src="img/icons/%s.svg" alt="" width="128" height="128" loading="lazy">' % name
        if kind == 'png':
            return '<img src="img/icons/%s.png" alt="" width="256" height="256" loading="lazy">' % name
        return sk[name]

    tabs, panels = [], []
    for i, a in enumerate(AREAS):
        k = 'w%d' % i
        on = (i == 0)
        tabs.append('<button type="button" role="tab" id="wbt%d" aria-controls="wbp%d" aria-selected="%s" tabindex="%d">'
                    '<small>%02d</small><b>%s</b><span class="ext">.%s</span></button>'
                    % (i, i, 'true' if on else 'false', 0 if on else -1, i + 1, T(k + '_tab'), a['ext']))
        rows = ''.join('<li><i>%s</i><div><b>%s</b><span>%s</span></div></li>'
                       % (icon(spec), T('%si%d_t' % (k, j)), T('%si%d_d' % (k, j))) for j, (spec, _, _) in enumerate(a['items']))
        code = a['code'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        chk = ('<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
               'stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9.5"/><path class="ck" pathLength="1" d="M7.6 12.6l3 3 5.8-6.2"/></svg>')
        learn = ''.join('<li style="--i:%d">%s<span>%s</span></li>' % (j, chk, T('%sl%d' % (k, j))) for j in range(len(a['learn'])))
        panels.append('<section role="tabpanel" id="wbp%d" aria-labelledby="wbt%d"%s><header><h3>%s</h3><p class="wbs">%s</p><p class="wbp">%s</p></header>'
                      '<div><h4 class="wbh">%s</h4><ul class="wbk">%s</ul></div>'
                      '<div><h4 class="wbh">%s</h4><ul class="wbl%s">%s</ul></div>'
                      '<div class="wbc" aria-hidden="true"><code>%s</code><u></u></div></section>'
                      % (i, i, '' if on else ' hidden', T(k + '_t'), T(k + '_d'), T(k + '_lead'),
                         T(k + '_ll' if (k + '_ll') in ES else 'wb_learn'), learn, T(k + '_tl' if (k + '_tl') in ES else 'wb_tools'), ' many' if len(a['items']) > 5 else '', rows, code))
    return ('<div class="wb" data-wb><div class="wb-bar" aria-hidden="true"><i></i><i></i><i></i><span>%s</span></div>'
            '<div class="wb-body"><div class="wb-tabs" role="tablist" aria-orientation="vertical">%s</div>'
            '<div class="wb-panels">%s</div></div></div>' % (T('wb_title'), ''.join(tabs), ''.join(panels)))




# El JavaScript vive en src/js/ (un módulo por función); cada página carga solo su archivo de entrada: home, web o basic.

def page_data(body, entry, meta):
    """Lo que site.py necesita de cada página: el marcado, el archivo JS de entrada (home, web o basic) y los metadatos."""
    return dict(body=body, extra_js=entry, meta=meta)


def faq():
    out = ['<div class="faq">']
    for i, m in enumerate(MODS):
        tag = '<span class="tg">%s</span>' % T('tag_cert') if m in CERT_MODS else ''
        op = ' open' if i == 0 else ''
        out.append(
            '<details class="fq"%s><summary><span>%s</span>%s%s</summary><dl>'
            '<div><dt>%s</dt><dd>%s</dd></div><div><dt>%s</dt><dd>%s</dd></div><div><dt>%s</dt><dd>%s</dd></div>'
            '</dl></details>' % (op, T(m), tag, ic('chev', 22), T('m_what'), T('m_pending'), T('m_learn'), T('m_pending'), T('m_use'), T('m_pending')))
    out.append('</div>')
    return ''.join(out)


WEBP = '1-aire-web-development.html'
HOME = '1-aire.html'


IG_PATH = '<path d="M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077"/>'


def soc_items(size=18):
    def a(n, href, label, ext=True):
        t = ' target="_blank" rel="noopener noreferrer"' if ext else ''
        return '<a href="%s"%s aria-label="%s" title="%s">%s</a>' % (href, t, label, label, ic(n, size))
    ig = ('<a href="https://www.instagram.com/m4rkits.dev/" target="_blank" rel="noopener noreferrer" aria-label="Instagram" title="Instagram @m4rkits.dev">'
          '<svg viewBox="0 0 24 24" width="%d" height="%d" fill="currentColor" aria-hidden="true">%s</svg></a>') % (size, size, IG_PATH)
    return a('gh', GH, 'GitHub') + ig + a('li', LI, 'LinkedIn') + a('wa', WA, 'WhatsApp') + a('mail', MAIL, 'Email', False)


def hsocials():
    return '<div class="soc">' + soc_items() + '</div>'


def header(kind):
    if kind == 'home':
        logo, cta = '#portfolio', WEBP + '#contacto'
        links = ('<a class="on" href="#portfolio">%(n_home)s</a><a href="#master">%(n_master)s</a>'
                 '<a href="#certificados">%(n_certs)s</a><a href="' + WEBP + '">%(n_web)s</a>')
    elif kind == 'legal':
        logo, cta = HOME, WEBP + '#contacto'
        links = '<a href="' + HOME + '">%(n_portfolio)s</a><a href="' + WEBP + '">%(n_web)s</a>'
    else:
        logo, cta = HOME, '#contacto'
        links = ('<a href="' + HOME + '">%(n_portfolio)s</a><a class="on" href="#web">%(n_web)s</a>'
                 '<a href="#planes">%(n_plans)s</a><a href="#proyectos">%(n_projects)s</a><a href="#contacto">%(n_contact)s</a>')
    langb = ('<div class="lang%s" role="group" aria-label="Idioma"><button type="button" data-l="es" aria-pressed="true" aria-label="ES, Español"><img src="img/flags/es.svg" alt="" width="20" height="15"><span>ES</span></button>'
             '<button type="button" data-l="en" aria-pressed="false" aria-label="EN, English"><img src="img/flags/gb.svg" alt="" width="20" height="15"><span>EN</span></button></div>')
    th_btn = '<button type="button" class="th" aria-pressed="false" aria-label="Activar modo oscuro" title="Activar modo oscuro"><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>'
    th_m = '<button type="button" class="th th-m" aria-pressed="false" aria-label="Activar modo oscuro"><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><span class="th-t">Modo oscuro</span></button>'
    return ('<header class="hdr"><div class="hw">'
            '<a class="logo" href="' + logo + '"><img class="lh logo-l" src="img/logo-horizontal-claro.png" alt="M4rKitS.dev, Full Stack Developer" width="792" height="166"><img class="lh logo-d" src="img/logo-horizontal-oscuro.png" alt="" width="792" height="166" aria-hidden="true"></a>'
            '<nav class="hn" id="hn" aria-label="Principal">' + links + (langb % ' lang-m').rsplit('</div>', 1)[0] + th_m + '</div>' + '</nav>'
            '<div class="hr">' + hsocials() + (langb % '') + th_btn +
            '<a class="gb sm" href="' + cta + '">%(cta_talk)s</a></div>'
            '<button type="button" class="hm" aria-expanded="false" aria-controls="hn" aria-label="Abrir menú"><span></span><span></span></button>'
            '</div></header>')


def footer(kind):
    logo = '#portfolio' if kind == 'home' else HOME
    return ('<footer class="ft"><div class="ft-box">'
            '<div class="ft-top"><a class="ft-logo" href="' + logo + '"><img src="img/logo-horizontal-oscuro.png" alt="M4rKitS.dev, Full Stack Developer" width="792" height="166" loading="lazy"></a>'
            '<a class="up" href="#" data-up><span>%(f_top)s</span><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg></a></div>'
            '<div class="ft-mid"><p class="ft-msg">%(f_thanks)s</p><p class="ft-sub"><span class="ft-prompt" aria-hidden="true">&gt;</span> %(h_eyebrow)s</p></div>'
            '<div class="ft-bot"><div class="fs ft-fs">' + soc_items() + '</div>'
            '<p class="ft-cp">&copy; M4rKitS.dev &middot; %(f_rights)s</p>'
            '<nav class="ft-lg" aria-label="Legal"><a href="' + LEGAL_FILES['aviso'] + '">%(f_aviso)s</a><a href="' + LEGAL_FILES['priv'] + '">%(f_priv)s</a><a href="' + LEGAL_FILES['cook'] + '">%(f_cook)s</a></nav></div>'
            '</div></footer>')


def plan_art(n):
    """Ilustraciones propias (sin fotos): cada plan muestra su alcance con ventanas de navegador."""
    def win(x, y, w, h, extra=''):
        return ('<g><rect x="%d" y="%d" width="%d" height="%d" rx="12" fill="#fff" filter="url(#sh)"/>'
                '<rect x="%d" y="%d" width="%d" height="22" rx="12" fill="#EEF2F8"/><rect x="%d" y="%d" width="%d" height="10" fill="#EEF2F8"/>'
                '<circle cx="%d" cy="%d" r="3" fill="#C9D3E3"/><circle cx="%d" cy="%d" r="3" fill="#C9D3E3"/><circle cx="%d" cy="%d" r="3" fill="#C9D3E3"/>%s</g>'
                % (x, y, w, h, x, y, w, x, y + 12, w, x + 14, y + 11, x + 25, y + 11, x + 36, y + 11, extra))
    def page(x, y, w):
        # contenido de una landing: titular, texto, boton, imagen y tres cajas
        return ('<rect x="%d" y="%d" width="%d" height="9" rx="4.5" fill="#2457E6"/><rect x="%d" y="%d" width="%d" height="6" rx="3" fill="#C9D3E3"/>'
                '<rect x="%d" y="%d" width="%d" height="6" rx="3" fill="#DCE3EE"/><rect x="%d" y="%d" width="52" height="15" rx="7.5" fill="#0B1F3A"/>'
                '<rect x="%d" y="%d" width="62" height="46" rx="8" fill="#DCE8FF"/><circle cx="%d" cy="%d" r="9" fill="#A9C3FF"/>'
                '<rect x="%d" y="%d" width="46" height="26" rx="6" fill="#F1F5FB"/><rect x="%d" y="%d" width="46" height="26" rx="6" fill="#F1F5FB"/><rect x="%d" y="%d" width="46" height="26" rx="6" fill="#F1F5FB"/>'
                % (x + 16, y + 36, w * 0.5, x + 16, y + 52, w * 0.42, x + 16, y + 63, w * 0.34, x + 16, y + 77,
                   x + w - 78, y + 34, x + w - 47, y + 57,
                   x + 16, y + 106, x + 16 + 54, y + 106, x + 16 + 108, y + 106))
    defs = ('<defs><linearGradient id="bg%d" x1="0" y1="0" x2="1" y2="1">%s</linearGradient>'
            '<filter id="sh" x="-20%%" y="-20%%" width="140%%" height="150%%"><feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#0B1F3A" flood-opacity=".18"/></filter></defs>')
    if n == 1:
        stops = '<stop offset="0" stop-color="#EAF0FA"/><stop offset="1" stop-color="#D5E1F6"/>'
        body = win(46, 26, 228, 148, page(46, 26, 228))
    elif n == 2:
        stops = '<stop offset="0" stop-color="#DCE8FF"/><stop offset="1" stop-color="#B7CEFF"/>'
        card = ('<g filter="url(#sh)"><rect x="196" y="98" width="98" height="64" rx="14" fill="#fff"/></g>'
                '<circle cx="216" cy="122" r="11" fill="#2457E6"/><path d="M210.5 122.5l4 4 7-8" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
                '<rect x="234" y="115" width="46" height="6" rx="3" fill="#0B1F3A"/><rect x="234" y="127" width="32" height="5" rx="2.5" fill="#C9D3E3"/>'
                '<path d="M208 146h60" stroke="#E3E9F3" stroke-width="5" stroke-linecap="round"/><path d="M208 146h38" stroke="#38BDF8" stroke-width="5" stroke-linecap="round"/>')
        body = win(26, 24, 216, 142, page(26, 24, 216)) + card
    else:
        stops = '<stop offset="0" stop-color="#3B73FF"/><stop offset="1" stop-color="#16367F"/>'
        back1 = win(18, 38, 150, 104, '<rect x="32" y="74" width="70" height="7" rx="3.5" fill="#C9D3E3"/><rect x="32" y="88" width="104" height="30" rx="6" fill="#F1F5FB"/>')
        back2 = win(150, 22, 152, 104, '<rect x="164" y="58" width="74" height="7" rx="3.5" fill="#C9D3E3"/><rect x="164" y="72" width="108" height="34" rx="6" fill="#DCE8FF"/>')
        front = win(78, 52, 168, 118, '<rect x="92" y="84" width="82" height="8" rx="4" fill="#2457E6"/><rect x="92" y="99" width="104" height="5" rx="2.5" fill="#C9D3E3"/><rect x="92" y="109" width="70" height="5" rx="2.5" fill="#DCE3EE"/><rect x="92" y="123" width="44" height="14" rx="7" fill="#0B1F3A"/><rect x="190" y="84" width="40" height="34" rx="7" fill="#DCE8FF"/><rect x="190" y="124" width="40" height="22" rx="6" fill="#F1F5FB"/>')
        seo = ('<g filter="url(#sh)"><circle cx="268" cy="146" r="19" fill="#fff"/></g><circle cx="266" cy="144" r="7" fill="none" stroke="#2457E6" stroke-width="3"/><path d="M271.5 149.5l6 6" stroke="#2457E6" stroke-width="3" stroke-linecap="round"/>')
        bag = ('<g filter="url(#sh)"><circle cx="46" cy="156" r="19" fill="#fff"/></g><path d="M38 150h16l-1.5 13h-13z" fill="none" stroke="#0B1F3A" stroke-width="2.6" stroke-linejoin="round"/><path d="M42 150v-2.5a4 4 0 0 1 8 0V150" fill="none" stroke="#0B1F3A" stroke-width="2.6" stroke-linecap="round"/>')
        body = back1 + back2 + front + seo + bag
    return ('<svg viewBox="0 0 320 190" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
            + defs % (n, stops) + '<rect width="320" height="190" fill="url(#bg%d)"/>' % n + body + '</svg>')


CERT_IMG = {3: 'pseudocodigo', 4: 'linux', 5: 'git', 6: 'python', 7: 'python-avanzado', 8: 'sql', 9: 'solid', 10: 'orm'}
CERT_IC = {'pseudocodigo': ['pseudocodigo.svg'], 'linux': ['linux.svg'], 'git': ['git.svg', 'github.svg'], 'python': ['python.svg'], 'sql': ['sql.png'], 'solid': ['basedatos.svg'], 'python-avanzado': ['python.svg'], 'orm': ['python.svg', 'basedatos.svg']}
_CK = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9.5"/><path class="ck" pathLength="1" d="M7.8 12.4l3 3 5.5-6"/></svg>'
_EXPAND = '<i class="cc-i" aria-hidden="true"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4h6v6M20 4l-7 7M10 20H4v-6M4 20l7-7"/></svg></i>'


def cert_card(k):
    if k in CERT_IMG:
        ic = ' '.join('img/icons/' + f for f in CERT_IC[CERT_IMG[k]])
        return ('<button type="button" class="cc" data-cert="%s" data-ic="%s" aria-haspopup="dialog" aria-label="%s: %s">%s<b>%s</b>%s</button>'
                % (CERT_IMG[k], ic, ES['cert_view'], _re.sub('<[^>]+>', '', ES['c%d' % k]), _CK, T('c%d' % k), _EXPAND))
    return '<div class="cc">%s<b>%s</b></div>' % (_CK, T('c%d' % k))


def values():
    plans = ''
    icons = ['code', 'shield', 'cloud']
    for i, n in enumerate([1, 2, 3]):
        feats = ''.join('<li>%s<span>%s</span></li>' % (ic('check', 18), T('pl%d_f%d' % (n, k))) for k in range(1, 5) if ('pl%d_f%d' % (n, k)) in ES)
        badge = '<span class="plc-badge">%s</span>' % T('pl_badge') if n == 3 else ''
        plans += ('<article class="plc p%d"><figure class="plc-img">%s%s</figure><div class="plc-b"><span class="pt">%s</span><h3>%s</h3><p>%s</p><ul>%s</ul>'
                  '<a class="gb" href="#contacto" data-plan="%d"><span>%s</span><i>%s</i></a></div></article>') % (
            n, '<img src="img/plan-%d.jpg" alt="" width="960" height="600" loading="lazy">' % n, badge, T('pl%d_t' % n), T('pl%d_n' % n), T('pl%d_d' % n), feats, n, T('pl_cta'), ic('ur', 18))
    d = {k: T(k) for k in ES}
    d.update(dict(
        cf_ph_name_v=ES['cf_ph_name'], cf_ph_email_v=ES['cf_ph_email'], cf_ph_msg_v=ES['cf_ph_msg'], cf_ph_biz_v=ES['cf_ph_biz'], ick=ic('check', 18), icwa=ic('wa', 18),
        soc=soc_items(20), soc2=socials('', 18), f1=IMG_FOTO1, f2=IMG_FOTO2, f3='img/foto-3.jpg', f4='img/foto-4.jpg', f5='img/foto-7.webp', a5='Marcos Rodríguez trabajando concentrado ante su portátil', a3='Retrato de Marcos Rodríguez sonriendo', a1=ALT1, a2=ALT2, tbh=IMG_TBH, atbh=ALT_TBH,
        igh=ic('gh', 24), icode=ic('code', 40), ibranch=ic('branch', 40), arr=ic('ur', 18), ur=ic('ur', 18),
        i1=ic('term', 22), i2=ic('code', 22), i3=ic('db', 22), i4=ic('branch', 22), gear=ic('gear', 24),
        gh=GH, mail=MAIL, tel=TEL, wa=WA, wa_q=_quote(ES['cf_wa_text'], safe=''), icmail=ic('mail', 18), icphone=ic('phone', 18), icpin=ic('pin', 18),
        faq=faq(), plans=plans,
        ex=''.join('<span>%s</span>' % T('ex%d' % i) for i in range(1, 5)),
        certs=''.join(cert_card(k) for k in range(1, 11)),
        tags=''.join('<li>%s</li>' % T('tag%d' % i) for i in (1, 2, 3)),
        webp=WEBP, home=HOME))
    d.update(DEVICO)
    d.update(mq=marquee_html(), know=know_html())
    return d


def guard_hover(css):
    """Envuelve las reglas :hover en @media(hover:hover) para que no se queden pegadas en pantallas tactiles."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)

    def blocks(t):
        out, i, n = [], 0, len(t)
        while i < n:
            j = t.find('{', i)
            if j < 0:
                break
            depth, k = 1, j + 1
            while k < n and depth:
                c = t[k]
                if c == '{':
                    depth += 1
                elif c == '}':
                    depth -= 1
                k += 1
            out.append((t[i:j].strip(), t[j + 1:k - 1]))
            i = k
        return out

    def split_sel(p):
        parts, d, cur = [], 0, ''
        for ch in p:
            if ch in '([':
                d += 1
            elif ch in ')]':
                d -= 1
            if ch == ',' and d == 0:
                parts.append(cur.strip())
                cur = ''
            else:
                cur += ch
        parts.append(cur.strip())
        return [x for x in parts if x]

    def proc(t, guarded=False):
        res = ''
        for pre, body in blocks(t):
            if pre.startswith('@'):
                low = pre.replace(' ', '')
                if low.startswith(('@keyframes', '@font-face', '@-webkit-keyframes')):
                    res += pre + '{' + body + '}'
                else:
                    g = guarded or 'hover:hover' in low
                    res += pre + '{' + proc(body, g) + '}'
            else:
                sels = split_sel(pre)
                hov = [x for x in sels if ':hover' in x]
                rest = [x for x in sels if ':hover' not in x]
                if guarded or not hov:
                    res += pre + '{' + body + '}'
                else:
                    if rest:
                        res += ','.join(rest) + '{' + body + '}'
                    res += '@media(hover:hover){' + ','.join(hov) + '{' + body + '}}'
        return res
    return proc(css)


def _blocks(t):
    out, i, n = [], 0, len(t)
    while i < n:
        j = t.find('{', i)
        if j < 0:
            break
        depth, k = 1, j + 1
        while k < n and depth:
            c = t[k]
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
            k += 1
        out.append((t[i:j].strip(), t[j + 1:k - 1]))
        i = k
    return out


def _split(p, sep):
    parts, d, cur = [], 0, ''
    for ch in p:
        if ch in '([':
            d += 1
        elif ch in ')]':
            d -= 1
        if ch == sep and d == 0:
            parts.append(cur)
            cur = ''
        else:
            cur += ch
    parts.append(cur)
    return [x for x in parts if x.strip()]


def _rgb(h):
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _lum(r, g, b):
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255


TXT = {'#33506b': '#B4C5E0', '#5b6f82': '#9FB2CF', '#566579': '#9FB2CF', '#9aa7ba': '#7F92B0', '#8793a6': '#7F92B0',
       '#8a97a9': '#7F92B0', '#4f6177': '#A9BAD6', '#4c5b78': '#A9BAD6', '#3f566b': '#A9BAD6', '#33465e': '#B4C5E0',
       '#25435f': '#B4C5E0', '#2b4a8b': '#9DB8FF', '#1b46c8': '#8FB3FF', '#1b3fa8': '#8FB3FF', '#0b1f3a': '#EAF1FF',
       '#06223f': '#EAF1FF', '#16a34a': '#4ADE80', '#15803d': '#4ADE80', '#b42323': '#FF8A8A', '#3b2b00': '#3b2b00'}


def _bg_hex(c):
    h = c.lower()
    if len(h) == 4:
        h = '#' + ''.join(x * 2 for x in h[1:])
    if h == '#ffffff':
        return '#12203A'
    r, g, b = _rgb(h)
    if _lum(r, g, b) < 0.72:
        return c
    k = 0.06
    base = (8, 16, 34)
    return '#%02X%02X%02X' % tuple(int(base[i] + (v - base[i]) * k) for i, v in enumerate((r, g, b)))


def _bg_rgba(m):
    r, g, b, a = int(m.group(1)), int(m.group(2)), int(m.group(3)), float(m.group(4))
    if min(r, g, b) < 190 or a < 0.35:
        return m.group(0)
    if min(r, g, b) > 232:
        return 'rgba(18,32,58,%s)' % m.group(4)
    return 'rgba(%d,%d,%d,%.2f)' % (int(r * .35), int(g * .38), int(b * .5), a * .45)


def _border_hex(c):
    r, g, b = _rgb(c)
    return 'rgba(255,255,255,.14)' if _lum(r, g, b) > 0.7 else c


def _border_rgba(m):
    r, g, b, a = int(m.group(1)), int(m.group(2)), int(m.group(3)), float(m.group(4))
    return 'rgba(255,255,255,.14)' if min(r, g, b) > 230 and a >= 0.5 else m.group(0)


HEX = r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b'
RGBA = r'rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)'


def _dark_decl(prop, val):
    p = prop.strip().lower()
    v = val.strip()
    if p.startswith('--') or 'var(--ink)' in v:
        return None
    if p in ('background', 'background-color', 'background-image'):
        if re.search(r'#0b1f3a|#101a2e|#16367f', v, re.I):
            return None
        n = re.sub(HEX, lambda m: _bg_hex(m.group(0)), v)
        n = re.sub(RGBA, _bg_rgba, n)
    elif p == 'color':
        n = re.sub(HEX, lambda m: TXT.get(m.group(0).lower(), m.group(0)), v)
    elif p.startswith('border') or p.startswith('outline'):
        n = re.sub(HEX, lambda m: _border_hex(m.group(0)), v)
        n = re.sub(RGBA, _border_rgba, n)
    elif p == 'box-shadow':
        n = re.sub(HEX, lambda m: _border_hex(m.group(0)) if _lum(*_rgb(m.group(0))) > 0.7 else m.group(0), v)
        n = re.sub(RGBA, _border_rgba, n)
    else:
        return None
    return None if n == v else '%s:%s' % (p, n)


def dark_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)

    def proc(t):
        res = ''
        for pre, body in _blocks(t):
            if pre.startswith('@'):
                low = pre.replace(' ', '')
                if low.startswith(('@keyframes', '@font-face', '@-webkit-keyframes')):
                    continue
                inner = proc(body)
                if inner:
                    res += pre + '{' + inner + '}'
            else:
                if re.match(r'^(:root|html\[lang|html\[data-theme)', pre):
                    continue
                decls = []
                for d in _split(body, ';'):
                    if ':' not in d:
                        continue
                    k, v = d.split(':', 1)
                    nd = _dark_decl(k, v)
                    if nd:
                        decls.append(nd)
                if decls:
                    sels = ','.join('html[data-theme=dark] ' + x.strip() for x in _split(pre, ','))
                    res += sels + '{' + ';'.join(decls) + '}'
        return res
    return proc(css)


SIG = '<span class="sg"><img class="logo-l" src="img/logo-horizontal-claro.png" alt="M4rKitS.dev, Full Stack Developer" width="792" height="166" loading="lazy"><img class="logo-d" src="img/logo-horizontal-oscuro.png" alt="" width="792" height="166" loading="lazy" aria-hidden="true"></span>'


def full_css():
    lines = CSS.split('\n')
    manual = [l for l in lines if l.startswith('html[data-theme=dark]')]
    base = '\n'.join(l for l in lines if not l.startswith('html[data-theme=dark]'))
    return guard_hover(base + '\n' + dark_css(base) + '\n' + '\n'.join(manual))


def build_home():
    main = """
<section class="hero" id="portfolio"><div class="wrap">
<h1 class="h1">%(h1)s</h1>
<p class="lead">%(h_lead)s</p>
<div class="cta"><a class="gb" href="#master">%(btn_master)s</a><a class="og" href="%(webp)s">%(btn_web)s</a></div>
</div></section>
<div class="wrap" style="position:relative"><div class="bento">
<div class="tb">%(soc)s</div>
<div class="b1"><img data-prio src="%(f4)s" alt="%(a2)s" width="1024" height="1536"></div>
<div class="b2"><img src="img/helsinki.jpg" alt="Catedral de Helsinki" width="1600" height="740"><span class="chip">%(icpin)s<span>Helsinki <small>· %(chip_fi)s</small></span></span></div>
<a class="b3" href="%(webp)s"><div class="mock-bar" aria-hidden="true"><i></i><i></i><i></i><span>m4rkits.dev/web-development</span></div><img class="cap-es" src="img/web-development-captura.jpg" alt="" width="920" height="613"><img class="cap-en" src="img/web-development-captura-en.jpg" alt="" width="920" height="613"><span class="go"><span>%(btn_web)s</span>%(arr)s</span></a>
<div class="b4" aria-hidden="true"><div class="ed-bar"><i></i><i></i><i></i><span>marcos.js</span></div><pre><span class="l"><span class="k">const</span> <span class="p">marcos</span> <span class="o">=</span> {</span><span class="l">  city: <span class="s">"Vantaa"</span>,</span><span class="l">  langs: [<span class="s">"es"</span>, <span class="s">"en"</span>],</span><span class="l">  path: <span class="s">"full stack"</span>,</span><span class="l">  status: <span class="s">"learning"</span>,</span><span class="l">  next: <span class="s">"your project"</span><span class="cur"></span></span><span class="l">};</span></pre></div>
</div></div>

<section class="sec" id="master"><div class="wrap center"><h2 class="h2">%(mq_title)s</h2></div>
%(mq)s</section>

<section class="sec" id="conocimientos"><div class="wrap center"><h2 class="h2">%(k_title)s</h2></div>
<div class="wrap">%(know)s</div></section>

<section class="sec"><div class="gh"><h2 class="h2">%(g_title)s</h2></div>
<div class="goal"><div class="ph"><img src="%(f3)s" alt="%(a3)s" width="1024" height="1536" loading="lazy"></div><div class="gc"><h3>%(g_card)s</h3><p>%(g_text)s</p><p>%(g_text2)s</p>""" + SIG + """</div></div></section>

<section class="sec center" id="certificados"><div class="wrap"><h2 class="h2" style="margin-top:0">%(c_title)s</h2></div><div class="certs">%(certs)s</div>
<dialog class="bw cdlg" id="cd"><div class="bw-win" tabindex="-1" autofocus>
<div class="bw-bar"><div class="bw-dots" aria-hidden="true"><i></i><i></i><i></i></div><h3 class="bw-url"><span class="cd-ico" id="cd-ico" aria-hidden="true"></span><span id="cd-tt"></span></h3>
<a class="bw-ext" id="cd-ext" target="_blank" rel="noopener noreferrer"><span data-t="cert_open">Abrir imagen</span>%(ur)s</a>
<button type="button" class="bw-x" id="cd-x" aria-label="Cerrar"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
<div class="cd-body"><img id="cd-img" alt="" width="1400" height="988" decoding="async"></div>
</div></dialog></section>
"""
    body = '<div class="frame">' + header('home') + '<main>' + main + '</main>' + footer('home') + '</div>'
    return page_data(body % values(), 'home', meta=dict(t='mt_home', d='md_home', img='https://m4rkits.dev/img/og-portfolio.png', alt='Marcos Rodríguez, desarrollador de software Full Stack'))


def build_web():
    main = """
<section class="hero hero-b" id="web"><div class="wrap">
<h1 class="h1">%(w_h1)s</h1>
<p class="lead">%(w_lead)s</p>
<div class="cta"><a class="gb" href="#planes">%(w_btn1)s</a><a class="og" href="#contacto">%(w_btn2)s</a></div>
</div></section>

<section class="sec" id="planes" style="padding-top:44px"><div class="pbox"><div class="center"><h2 class="h2">%(p_title)s</h2></div>
<div class="plans">%(plans)s</div><p class="note">%(p_note)s</p><p class="exl">%(p_extras)s</p><div class="ex">%(ex)s</div></div></section>

<section class="sec" id="proyectos"><div class="center wrap"><h2 class="h2">%(pr_title)s</h2></div>
<ul class="wl" id="wl">
<li><button type="button" class="wk" data-win="1" data-src="1-aire.html" data-host="m4rkits.dev" data-ext="%(gh)s" data-extk="own_cta" data-desc="own_d"><span class="wk-wm" aria-hidden="true">01</span><span class="wk-body"><span class="wk-st"><i></i>%(own_badge)s</span><span class="wk-m"><span class="wk-t">M4rKitS.dev</span><span class="wk-d">%(w_r2)s</span></span><span class="wk-tg"><span class="wk-p">HTML</span><span class="wk-p">CSS</span><span class="wk-p">JavaScript</span></span><span class="wk-cta"><span>%(w_explore)s</span><i>%(ur)s</i></span></span><span class="wk-vis" aria-hidden="true"><span class="wk-mock"><span class="mock-bar"><i></i><i></i><i></i><span>m4rkits.dev</span></span><img class="cap-es" src="img/portfolio-captura.jpg" alt="" width="1200" height="750" loading="lazy"><img class="cap-en" src="img/portfolio-captura-en.jpg" alt="" width="1200" height="750" loading="lazy"></span></span></button></li>
<li><button type="button" class="wk" data-win="1" data-src="https://tbhstrategy.com/" data-host="tbhstrategy.com" data-ext="https://www.tbhstrategy.com" data-extk="tbh_cta" data-desc="tbh_desc"><span class="wk-wm" aria-hidden="true">02</span><span class="wk-body"><span class="wk-st"><i></i>%(tbh_badge)s</span><span class="wk-m"><span class="wk-t">TBH Strategy</span><span class="wk-d">%(w_r1)s</span></span><span class="wk-tg"><span class="wk-p">%(tag1)s</span><span class="wk-p">%(tag2)s</span><span class="wk-p">%(tag3)s</span></span><span class="wk-cta"><span>%(w_explore)s</span><i>%(ur)s</i></span></span><span class="wk-vis" aria-hidden="true"><span class="wk-mock"><span class="mock-bar"><i></i><i></i><i></i><span>tbhstrategy.com</span></span><img src="img/tbh-inicio.webp" alt="" width="2000" height="919" loading="lazy"></span></span></button></li>
<li><div class="wk ghost" aria-disabled="true"><span class="wk-wm" aria-hidden="true">03</span><span class="wk-body"><span class="wk-st"><i></i>%(ly_badge)s</span><span class="wk-m"><span class="wk-t">Lydia Lillo</span><span class="wk-d">%(ly_sub)s</span></span></span><span class="wk-vis" aria-hidden="true"><span class="wk-mock sk"><span class="mock-bar"><i></i><i></i><i></i><span>&nbsp;</span></span><span class="sk-b"><i></i><i></i><i></i><i></i></span></span></span></div></li>
</ul>
<dialog class="bw" id="bw"><div class="bw-win" tabindex="-1" autofocus>
<div class="bw-bar"><div class="bw-dots" aria-hidden="true"><i></i><i></i><i></i></div><h3 class="bw-url"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg><span id="bw-host"></span></h3><a class="bw-ext" id="bw-ext" target="_blank" rel="noopener noreferrer"><span id="bw-extt" data-t="w_open">Abrir en pestaña nueva</span>%(ur)s</a><button type="button" class="bw-x" id="bw-x"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
<div class="bw-body"><div class="bw-gate" id="bw-gate" hidden><div class="bw-gate-in"><h4 data-t="w_gate_t">Vas a ver un sitio externo</h4><p id="bw-gate-p"></p><div class="bw-gate-act"><button type="button" class="gb" id="bw-go"><span data-t="w_gate_go">Cargar el sitio</span><i>%(ur)s</i></button><a class="og" id="bw-gx" target="_blank" rel="noopener noreferrer"><span data-t="w_gate_ext">Abrir en pestaña nueva</span></a></div></div></div><div class="bw-load" id="bw-load" data-t="w_loading">Cargando…</div><iframe id="bw-f" title="" sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-popups-to-escape-sandbox" referrerpolicy="no-referrer" src="about:blank"></iframe></div>
<div class="bw-ft"><p id="bw-d"></p><span class="bw-nl" data-t="w_noload">¿No carga? Ábrela en una pestaña nueva</span></div>
</div></dialog></section>

<section class="sec"><div class="who"><div class="ph"><img src="img/foto-4.jpg" alt="%(a2)s" width="1024" height="1536" loading="lazy"></div><div class="gc"><h2 class="h2">%(who_title)s</h2><p>%(who_text)s</p><p>%(who_text2)s</p><a class="dk" href="%(home)s">%(who_link)s</a></div></div></section>

<section class="sec" id="contacto"><div class="ctab">
<div class="ct-head"><div><h2 class="h2">%(cta_title)s</h2><p>%(cta_text)s</p></div></div>
<form class="cf" id="contact-form" novalidate>
<label class="cf-f f-name"><span class="cf-l">%(cf_name)s</span><input type="text" id="cf-name" name="name" autocomplete="name" required data-tp="cf_ph_name" placeholder="%(cf_ph_name_v)s"></label>
<label class="cf-f f-email"><span class="cf-l">%(cf_email)s</span><input type="email" id="cf-email" name="email" autocomplete="email" required data-tp="cf_ph_email" placeholder="%(cf_ph_email_v)s"></label>
<label class="cf-f f-biz"><span class="cf-l">%(cf_biz)s <em class="cf-o">(%(cf_opt)s)</em></span><input type="text" id="cf-biz" name="business" autocomplete="organization" data-tp="cf_ph_biz" placeholder="%(cf_ph_biz_v)s"></label>
<label class="cf-f f-msg"><span class="cf-l">%(cf_msg)s</span><textarea id="cf-msg" name="message" rows="4" required data-tp="cf_ph_msg" placeholder="%(cf_ph_msg_v)s"></textarea></label>
<fieldset class="cf-fs f-plan"><legend class="cf-l">%(cf_plan)s</legend><div class="cf-chips">
<label><input type="radio" name="plan" value="1"><span>%(pl1_n)s</span></label>
<label><input type="radio" name="plan" value="2"><span>%(pl2_n)s</span></label>
<label><input type="radio" name="plan" value="3"><span>%(pl3_n)s</span></label>
<label><input type="radio" name="plan" value="0" checked><span>%(cf_idk)s</span></label></div></fieldset>
<input class="cf-hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="cf-bar"><label class="cf-ck"><input type="checkbox" id="cf-consent" name="consent"><span>%(cf_consent)s</span></label>
<div class="cf-act"><a class="cf-wa" id="cf-wa" href="%(wa)s?text=%(wa_q)s" target="_blank" rel="noopener noreferrer">%(icwa)s<span data-t="cf_wa">Contactar por WhatsApp</span></a>
<button class="cf-send" type="submit"><span id="cf-btn" data-t="cf_send">Enviar mensaje</span><i>%(ur)s</i></button></div></div>
<p class="cf-st" id="cf-st" role="status" aria-live="polite"></p></form></div></section>
"""
    body = '<div class="frame">' + header('web') + '<main>' + main + '</main>' + footer('web') + '</div>'
    body += '<script src="vendor/emailjs.min.js"></script>'
    return page_data(body % values(), 'web', meta=dict(t='mt_web', d='md_web', img='https://m4rkits.dev/img/og-web.png', alt='M4rKitS.dev, desarrollo web para pequeños negocios'))


ONLY_LANG = None


def build_legal(kind):
    from legal import LEGAL, UPDATED
    blocks = ''
    for lg in ((ONLY_LANG,) if ONLY_LANG else ('es', 'en')):
        d = LEGAL[kind][lg]
        secs = ''.join('<section class="lg-s"><h2>%d. %s</h2>%s</section>' % (i + 1, h, c) for i, (h, c) in enumerate(d['sec']))
        secs = secs.replace('%(priv)s', LEGAL_FILES['priv']).replace('%(cook)s', LEGAL_FILES['cook'])
        upd = ('Última actualización' if lg == 'es' else 'Last updated') + ': ' + UPDATED[lg]
        blocks += '<div class="lg-%s"><h1>%s</h1><p class="lg-lead">%s</p><p class="lg-upd">%s</p>%s</div>' % (lg, d['h1'], d['lead'], upd, secs)
    assert '%' not in blocks
    main = '<section class="lg"><div class="lg-w">' + blocks + '</div></section>'
    body = '<div class="frame">' + header('legal') + '<main>' + main + '</main>' + footer('legal') + '</div>'
    return page_data(body % values(), 'basic', meta=dict(t='mt_' + kind, d='md_' + kind, img='https://m4rkits.dev/img/og-portfolio.png', alt='M4rKitS.dev'))


def build_gracias():
    es = ('<div class="lg-es"><h1>Mensaje <em>enviado</em></h1><p class="lg-lead">Gracias por escribirme. He recibido tu mensaje y te responderé lo antes posible.</p>'
          '<p class="lg-upd">Te acaba de llegar una confirmación al correo. Si no la ves, mira también en la carpeta de spam.</p>'
          '<div class="lg-act"><a class="dk" href="' + HOME + '">Ir al portfolio</a><a class="og" href="' + WEBP + '"><span>Volver a desarrollo web</span></a></div></div>')
    en = ('<div class="lg-en"><h1>Message <em>sent</em></h1><p class="lg-lead">Thanks for writing to me. I have received your message and will reply as soon as I can.</p>'
          '<p class="lg-upd">A confirmation has just been sent to your email. If you do not see it, check your spam folder too.</p>'
          '<div class="lg-act"><a class="dk" href="' + HOME + '">Go to the portfolio</a><a class="og" href="' + WEBP + '"><span>Back to web development</span></a></div></div>')
    main = '<section class="lg"><div class="lg-w">' + (es if ONLY_LANG != 'en' else '') + (en if ONLY_LANG != 'es' else '') + '</div></section>'
    body = '<div class="frame">' + header('legal') + '<main>' + main + '</main>' + footer('legal') + '</div>'
    return page_data(body % values(), 'basic', meta=dict(t='mt_gracias', d='md_gracias', img='https://m4rkits.dev/img/og-portfolio.png', alt='M4rKitS.dev'))


def build_notfound():
    es = ('<div class="lg-es"><h1>Página <em>no encontrada</em></h1><p class="lg-lead">La dirección que buscas no existe o se ha movido.</p>'
          '<div class="lg-act"><a class="dk" href="/">Ir al inicio</a><a class="og" href="/desarrollo-web/"><span>Ver desarrollo web</span></a></div></div>')
    en = ('<div class="lg-en"><h1>Page <em>not found</em></h1><p class="lg-lead">The address you are looking for does not exist or has moved.</p>'
          '<div class="lg-act"><a class="dk" href="/en/">Go to the homepage</a><a class="og" href="/en/web-development/"><span>See web development</span></a></div></div>')
    main = '<section class="lg"><div class="lg-w">' + (es if ONLY_LANG != 'en' else '') + (en if ONLY_LANG != 'es' else '') + '</div></section>'
    body = '<div class="frame">' + header('legal') + '<main>' + main + '</main>' + footer('legal') + '</div>'
    return page_data(body % values(), 'basic', meta=dict(t='mt_gracias', d='md_gracias', img='https://m4rkits.dev/img/og-portfolio.png', alt='M4rKitS.dev'))


if __name__ == '__main__':
    import sys
    open(sys.argv[1] + '/' + HOME, 'w', encoding='utf-8').write(build_home())
    open(sys.argv[1] + '/' + WEBP, 'w', encoding='utf-8').write(build_web())
    for k in LEGAL_FILES:
        open(sys.argv[1] + '/' + LEGAL_FILES[k], 'w', encoding='utf-8').write(build_legal(k))
    open(sys.argv[1] + '/1-aire-gracias.html', 'w', encoding='utf-8').write(build_gracias())
    print('ok d1 (portfolio, desarrollo web, legales y gracias)')
