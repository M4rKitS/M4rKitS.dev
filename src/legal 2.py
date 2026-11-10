# -*- coding: utf-8 -*-
"""Textos legales (ES/EN) de m4rkits.dev. Cada bloque va en su idioma y se muestra segun html[lang]."""

UPDATED = {'es': '5 de noviembre de 2026', 'en': '5 November 2026'}
MAIL = 'contact@m4rkits.dev'
EP = '<a href="mailto:%s">%s</a>' % (MAIL, MAIL)

LEGAL = {
 'aviso': {
  'es': {
   'h1': 'Aviso <em>legal</em>',
   'lead': 'Quién está detrás de esta web y bajo qué condiciones puedes usarla.',
   'sec': [
    ('Titular del sitio web', '<ul class="lg-id"><li><b>Titular</b><span>Marcos Rodríguez, persona física</span></li><li><b>Dirección</b><span>Asola, 01400 Vantaa, Finlandia</span></li><li><b>Correo</b><span>' + EP + '</span></li><li><b>Sitio web</b><span>m4rkits.dev</span></li><li><b>Actividad</b><span>Portfolio profesional y servicios de diseño y desarrollo web</span></li></ul>'),
    ('Objeto y uso del sitio', '<p>Esta web presenta mi formación como desarrollador de software Full&nbsp;Stack, mis proyectos y los servicios de desarrollo web que ofrezco a pequeños negocios. Al navegar por ella aceptas usarla de forma lícita, sin dañar el sitio ni a terceros.</p>'),
    ('Propiedad intelectual', '<p>Los textos, el diseño, el código y la marca M4rKitS.dev son de su titular. No se pueden copiar ni reutilizar sin permiso, salvo la cita breve de fragmentos con mención de la fuente.</p><p>Los nombres, logotipos y capturas de proyectos de terceros (por ejemplo, de clientes o de entidades que emiten certificados) pertenecen a sus titulares y se muestran solo como referencia de trabajo y formación.</p>'),
    ('Información orientativa', '<p>La descripción de los planes y servicios es orientativa y no constituye una oferta vinculante. Cualquier presupuesto o acuerdo se confirma por escrito antes de empezar.</p>'),
    ('Enlaces y contenido de terceros', '<p>La web enlaza a páginas externas (redes sociales, proyectos de clientes, entidades formativas) y puede mostrar un sitio externo en una ventana cuando tú lo eliges. No controlo esos sitios ni respondo de su contenido ni de sus políticas.</p>'),
    ('Responsabilidad', '<p>Procuro que la información sea correcta y esté al día, pero no garantizo que esté libre de errores ni que el sitio esté siempre disponible. No respondo de los daños derivados de un uso indebido de la web.</p>'),
    ('Protección de datos y cookies', '<p>Cómo trato tus datos está en la <a href="%(priv)s">Política de privacidad</a>, y qué almacena la web en tu navegador, en la <a href="%(cook)s">Política de cookies</a>.</p>'),
    ('Ley aplicable', '<p>Este sitio se rige por la legislación de Finlandia y por la normativa de la Unión Europea que le sea aplicable. Si eres consumidor, conservas los derechos que te reconoce la ley imperativa de tu país de residencia.</p>'),
   ]},
  'en': {
   'h1': 'Legal <em>notice</em>',
   'lead': 'Who is behind this website and the terms under which you can use it.',
   'sec': [
    ('Website owner', '<ul class="lg-id"><li><b>Owner</b><span>Marcos Rodríguez, natural person</span></li><li><b>Address</b><span>Asola, 01400 Vantaa, Finland</span></li><li><b>Email</b><span>' + EP + '</span></li><li><b>Website</b><span>m4rkits.dev</span></li><li><b>Activity</b><span>Professional portfolio and web design and development services</span></li></ul>'),
    ('Purpose and use of the site', '<p>This website presents my training as a Full&nbsp;Stack software developer, my projects and the web development services I offer to small businesses. By browsing it you agree to use it lawfully, without harming the site or third parties.</p>'),
    ('Intellectual property', '<p>The texts, design, code and the M4rKitS.dev brand belong to the site owner. They may not be copied or reused without permission, except for short quotations that credit the source.</p><p>Names, logos and screenshots of third-party projects (for example clients or the bodies that issue certificates) belong to their owners and are shown only as a reference to my work and training.</p>'),
    ('Informational content', '<p>The description of plans and services is indicative and is not a binding offer. Any quote or agreement is confirmed in writing before work starts.</p>'),
    ('Links and third-party content', '<p>The site links to external pages (social networks, client projects, training providers) and can display an external site in a window when you choose to. I do not control those sites and am not responsible for their content or policies.</p>'),
    ('Liability', '<p>I do my best to keep the information correct and up to date, but I do not guarantee that it is free of errors or that the site is always available. I am not liable for damage arising from misuse of the site.</p>'),
    ('Data protection and cookies', '<p>How I handle your data is described in the <a href="%(priv)s">Privacy policy</a>, and what the site stores in your browser in the <a href="%(cook)s">Cookie policy</a>.</p>'),
    ('Governing law', '<p>This site is governed by the law of Finland and by the European Union rules that apply to it. If you are a consumer, you keep the rights granted by the mandatory law of your country of residence.</p>'),
   ]},
 },
 'priv': {
  'es': {
   'h1': 'Política de <em>privacidad</em>',
   'lead': 'Qué datos recojo, para qué los uso y qué derechos tienes sobre ellos.',
   'sec': [
    ('Responsable del tratamiento', '<p>Marcos Rodríguez, Asola, 01400 Vantaa (Finlandia). Contacto: ' + EP + '.</p>'),
    ('Qué datos trato y para qué', '<p><b>Formulario de contacto.</b> Si me escribes desde el formulario trato tu nombre, tu correo, el nombre de tu negocio o web (opcional), tu mensaje y el tipo de servicio que marcas. Los uso solo para responder a tu consulta o preparar un presupuesto. Base legal: tu consentimiento, que das al marcar la casilla, y, si pides un presupuesto, las medidas previas a un posible contrato.</p><p><b>WhatsApp.</b> El botón abre WhatsApp con un mensaje ya escrito. Hasta que lo envías no recibo ningún dato. Después, la conversación se rige por la política de WhatsApp.</p><p><b>Estadísticas de visitas.</b> Uso Cloudflare Web Analytics, que mide visitas de forma agregada, sin cookies y sin identificarte.</p><p><b>Datos técnicos.</b> El servidor que aloja la web (Cloudflare) puede registrar datos técnicos como la dirección IP para garantizar la seguridad y el funcionamiento del servicio.</p><p><b>Datos obligatorios y decisiones automatizadas.</b> Nombre, correo y mensaje son necesarios para poder responderte: sin ellos no puedo atender tu consulta. No tomo decisiones automatizadas ni elaboro perfiles con tus datos.</p>'),
    ('Quién más recibe tus datos', '<p>Los mensajes del formulario pasan por <b>EmailJS</b>, el servicio que los envía a mi correo y te manda la confirmación automática. La web se aloja en <b>Cloudflare</b>. No vendo tus datos ni los uso para publicidad.</p>'),
    ('Transferencias fuera del Espacio Económico Europeo', '<p>EmailJS está operado por una empresa de Singapur y sus servidores están en Estados Unidos. Según su política de privacidad, para usuarios europeos aplica garantías como las cláusulas contractuales tipo. Cloudflare también puede tratar datos fuera del Espacio Económico Europeo con garantías equivalentes.</p>'),
    ('Cuánto tiempo los conservo', '<p>Guardo tu consulta mientras la atiendo y, si no llegamos a trabajar juntos, hasta 12 meses después por si retomas la conversación. Si hay relación de trabajo, conservo lo necesario durante los plazos que exija la ley. Las estadísticas no contienen datos personales.</p>'),
    ('Tus derechos', '<p>Puedes pedirme acceso, rectificación, supresión, limitación, portabilidad u oposición, y retirar tu consentimiento cuando quieras, escribiendo a ' + EP + '. Retirarlo no afecta a lo que ya se hizo antes.</p><p>Si crees que no he tratado bien tus datos, puedes reclamar ante la autoridad de protección de datos de Finlandia (<a href="https://tietosuoja.fi" target="_blank" rel="noopener noreferrer">Tietosuojavaltuutetun toimisto</a>) o ante la de tu país.</p>'),
    ('Menores y seguridad', '<p>Esta web no está dirigida a menores de edad. Aplico medidas razonables para proteger los datos, como conexión cifrada (HTTPS) y acceso solo desde mi cuenta.</p>'),
    ('Cambios', '<p>Si cambio algo importante de esta política, actualizaré la fecha de arriba.</p>'),
   ]},
  'en': {
   'h1': 'Privacy <em>policy</em>',
   'lead': 'What data I collect, what I use it for and what rights you have over it.',
   'sec': [
    ('Data controller', '<p>Marcos Rodríguez, Asola, 01400 Vantaa (Finland). Contact: ' + EP + '.</p>'),
    ('What data I process and why', '<p><b>Contact form.</b> If you write to me through the form I process your name, your email, your business or website name (optional), your message and the type of service you select. I use them only to reply to your enquiry or prepare a quote. Legal basis: your consent, which you give by ticking the box, and, if you ask for a quote, steps taken before a possible contract.</p><p><b>WhatsApp.</b> The button opens WhatsApp with a ready-made message. I receive no data until you send it. After that, the conversation is governed by WhatsApp\'s policy.</p><p><b>Visit statistics.</b> I use Cloudflare Web Analytics, which measures visits in aggregate, without cookies and without identifying you.</p><p><b>Technical data.</b> The server that hosts the site (Cloudflare) may log technical data such as your IP address to keep the service secure and working.</p><p><b>Required data and automated decisions.</b> Name, email and message are needed so I can reply: without them I cannot handle your enquiry. I make no automated decisions and build no profiles from your data.</p>'),
    ('Who else receives your data', '<p>Form messages go through <b>EmailJS</b>, the service that delivers them to my inbox and sends you the automatic confirmation. The site is hosted on <b>Cloudflare</b>. I do not sell your data or use it for advertising.</p>'),
    ('Transfers outside the European Economic Area', '<p>EmailJS is operated by a company in Singapore and its servers are in the United States. According to its privacy policy, for European users it applies safeguards such as standard contractual clauses. Cloudflare may also process data outside the European Economic Area with equivalent safeguards.</p>'),
    ('How long I keep it', '<p>I keep your enquiry while I deal with it and, if we do not end up working together, for up to 12 months in case you pick the conversation back up. If we work together, I keep what the law requires for the legal periods. Statistics contain no personal data.</p>'),
    ('Your rights', '<p>You can ask me for access, rectification, erasure, restriction, portability or objection, and withdraw your consent at any time, by writing to ' + EP + '. Withdrawing it does not affect what was done before.</p><p>If you think I have not handled your data properly, you can complain to the Finnish data protection authority (<a href="https://tietosuoja.fi/en" target="_blank" rel="noopener noreferrer">Office of the Data Protection Ombudsman</a>) or to the one in your country.</p>'),
    ('Minors and security', '<p>This site is not aimed at minors. I apply reasonable measures to protect data, such as an encrypted connection (HTTPS) and access only from my own account.</p>'),
    ('Changes', '<p>If I change something important in this policy, I will update the date above.</p>'),
   ]},
 },
 'cook': {
  'es': {
   'h1': 'Política de <em>cookies</em>',
   'lead': 'Qué guarda esta web en tu navegador y por qué no necesita un banner de cookies.',
   'sec': [
    ('Resumen', '<p>Esta web no usa cookies de publicidad ni de seguimiento. Solo guarda en tu navegador una preferencia que eliges tú (el modo claro u oscuro), y mide las visitas con una herramienta que no instala cookies.</p>'),
    ('Qué se guarda y qué se carga', '<ul class="lg-ck"><li><b>prop_theme</b><span>Almacenamiento local del navegador. Recuerda si prefieres el modo claro u oscuro. Propio, funcional. Se queda hasta que lo borres.</span></li><li><b>Cloudflare Web Analytics</b><span>Mide visitas de forma agregada. No instala cookies ni guarda nada en tu dispositivo, y no te identifica.</span></li><li><b>Formulario de contacto (EmailJS)</b><span>No instala cookies en esta web. Al enviar el formulario, tu mensaje viaja a sus servidores (ver la política de privacidad).</span></li><li><b>Ventana de proyectos</b><span>Solo se carga el sitio externo (por ejemplo, tbhstrategy.com) cuando pulsas para verlo. Ese sitio puede usar sus propias cookies, que no controlo.</span></li><li><b>Tipografías</b><span>Se sirven desde esta misma web, no desde Google.</span></li></ul>'),
    ('Por qué no hay banner', '<p>La ley exige tu consentimiento para guardar o leer información en tu dispositivo, salvo que sea imprescindible para algo que tú pides, como recordar el modo claro u oscuro que has elegido. Como esta web no usa cookies de análisis ni de publicidad, no hay nada que pedirte aceptar. Si algún día los añado, te lo preguntaré antes, con la opción de rechazar tan visible como la de aceptar.</p>'),
    ('Cómo borrar lo guardado', '<p>Puedes borrar los datos del sitio desde los ajustes de tu navegador. La web volverá al modo claro.</p>'),
    ('Cambios', '<p>Si cambia algo de lo que se guarda, actualizaré esta página y su fecha.</p>'),
   ]},
  'en': {
   'h1': 'Cookie <em>policy</em>',
   'lead': 'What this site stores in your browser and why it does not need a cookie banner.',
   'sec': [
    ('Summary', '<p>This site uses no advertising or tracking cookies. It only stores in your browser one preference you choose yourself (light or dark mode), and measures visits with a tool that sets no cookies.</p>'),
    ('What is stored and what is loaded', '<ul class="lg-ck"><li><b>prop_theme</b><span>Browser local storage. Remembers whether you prefer light or dark mode. First-party, functional. It stays until you clear it.</span></li><li><b>Cloudflare Web Analytics</b><span>Measures visits in aggregate. It sets no cookies, stores nothing on your device and does not identify you.</span></li><li><b>Contact form (EmailJS)</b><span>Sets no cookies on this site. When you send the form, your message travels to its servers (see the privacy policy).</span></li><li><b>Projects window</b><span>The external site (for example, tbhstrategy.com) loads only when you press to view it. That site may use its own cookies, which I do not control.</span></li><li><b>Fonts</b><span>Served from this same site, not from Google.</span></li></ul>'),
    ('Why there is no banner', '<p>The law requires your consent to store or read information on your device, unless it is essential for something you ask for, such as remembering the light or dark mode you chose. Since this site uses no analytics or advertising cookies, there is nothing to ask you to accept. If I ever add them, I will ask first, with the option to refuse as visible as the option to accept.</p>'),
    ('How to delete what is stored', '<p>You can clear the site data from your browser settings. The site will then go back to light mode.</p>'),
    ('Changes', '<p>If anything that is stored changes, I will update this page and its date.</p>'),
   ]},
 },
}
