# Base común: textos ES/EN, iconos, imágenes optimizadas y helpers.
import json

ES = {
 'n_home': 'Inicio', 'n_master': 'Máster', 'n_certs': 'Certificados', 'n_web': 'Desarrollo web',
 'n_plans': 'Planes', 'n_projects': 'Proyectos', 'n_contact': 'Contacto', 'n_portfolio': 'Portfolio',
 'cta_talk': 'Hablemos', 'cta_write': 'Escríbeme',
 'h_eyebrow': 'Desarrollador de software Full&nbsp;Stack en formación',
 'h_hello': '¡Hola! Soy Marcos Rodríguez',
 'h1': '¡Hola! Soy <em>Marcos Rodríguez</em>',
 'h_lead': 'Cuando un proyecto llega a mis manos, lo llevo hasta su mejor versión. Detalle, energía y una meta: que al verlo pienses «esto es justo lo que quería».',
 'h_short': 'Estudio el máster Full Stack de Conquer Blocks y cuento cada módulo con mis palabras.',
 'role_a': 'Full stack', 'role_b': 'en formación', 'role_c': 'Developer',
 'btn_master': 'Esta es mi formación', 'btn_web': 'Webs para tu negocio',
 'chip_loc': 'Vantaa, Finlandia', 'chip_fi': 'Finlandia', 'chip_lang': 'Español e inglés',
 'follow': 'Sígueme', 'hire': 'ESCRÍBEME · ESCRÍBEME · ',
 'st_certs': 'Certificados', 'st_mods': 'Módulos', 'st_langs': 'Idiomas', 'st_plans': 'Planes',
  'k_kicker': 'Conocimientos técnicos y herramientas', 'k_title': 'Lo que he visto, <em>por áreas</em>',
 'k_intro': 'Los conocimientos del máster hasta ahora, clasificados por el tipo de trabajo al que sirven.',
 'a1_t': 'Lógica y programación', 'a1_d': 'Plantear un problema, resolverlo con código y darle forma en una página web.',
 'a2_t': 'Datos', 'a2_d': 'Guardar la información, consultarla y relacionarla entre tablas.',
 'a3_t': 'Herramientas de trabajo', 'a3_d': 'El entorno de cada día para escribir, versionar y ordenar el código.',
 'a4_t': 'Inteligencia artificial', 'a4_d': 'Módulo de IA con Antigravity: trabajar con asistentes, agentes y herramientas conectadas.',
 'a5_t': 'Publicación en la nube', 'a5_d': 'Sacar un sitio web a internet a partir de su repositorio.',
 'k_logic': 'Lógica y pseudocódigo', 'k_oop': 'Programación orientada a objetos', 'k_joins': 'Consultas con JOIN y subconsultas',
 'k_rel': 'Relaciones entre tablas', 'k_orm': 'SQLAlchemy y ORM', 'k_linux': 'Linux y terminal', 'k_gha': 'GitHub desde Antigravity',
 'ai1_t': 'Google Antigravity', 'ai1_d': 'Editor con asistente de IA integrado para montar y revisar proyectos web.',
 'ai2_t': 'Agentes de IA', 'ai2_d': 'Preparar y ajustar agentes que se encargan de tareas de desarrollo.',
 'ai3_t': 'Procesos automatizados', 'ai3_d': 'Encadenar pasos repetitivos en flujos que se ejecutan solos.',
 'ai4_t': 'NotebookLM', 'ai4_d': 'Ordenar documentación y consultarla con ayuda de IA.',
 'ai5_t': 'Model Context Protocol', 'ai5_d': 'Enchufar herramientas externas a los modelos de IA.',
 'ai6_t': 'Google Stitch', 'ai6_d': 'Generar propuestas de interfaz y diseño a partir de una idea.',
 'ai7_t': 'Open Agent Manager', 'ai7_d': 'Seguir y coordinar varios agentes desde un mismo sitio.',
 'ai8_t': 'Apps y webs con IA integrada', 'ai8_d': 'Dar a una web o una app funciones que usan IA.',
 'ai9_t': 'OpenAI', 'ai9_d': 'Probar sus modelos y herramientas en distintas tareas.',
 'cl1_t': 'Cloudflare', 'cl1_d': 'Manejar lo básico de un proyecto y sus servicios desde el panel.',
 'cl2_t': 'Cloudflare Pages', 'cl2_d': 'Publicar sitios estáticos enlazados a un repositorio de GitHub.',
 'm_kicker': 'Máster Full Stack en Conquer Blocks', 'mq_title': 'Todo lo que cubre el máster, <em>de un vistazo</em>', 'mq_intro': 'Lenguajes, frameworks y herramientas del temario Full Stack.', 'm_title': 'Módulo a módulo, <em>con mis palabras</em>',
 'm_intro': 'De cada módulo cuento tres cosas: qué era, qué he aprendido y cómo lo uso hoy.',
 'm_what': 'Qué era', 'm_learn': 'Qué aprendí', 'm_use': 'Cómo lo uso hoy',
 'm_pending': 'Pendiente: lo escribo con el índice del módulo.',
 'm_view': 'Ver módulos', 'tag_cert': 'Con certificado',
 'mod1': 'Pseudocódigo', 'mod2': 'Linux y la Terminal', 'mod3': 'Python, básico y avanzado',
 'mod4': 'Git y GitHub', 'mod5': 'SQL', 'mod6': 'IA', 'mod7': 'Agentes de IA y automatizaciones',
 'g_kicker': 'Hacia dónde voy', 'g_title': 'Hacia dónde <em>voy</em>',
 'g_text': 'Quiero trabajar como freelance o en una buena empresa que me permita hacerlo en remoto. Sigo estudiando y los módulos que me faltan irán apareciendo aquí.',
 'g_pending': 'Pendiente: lista de módulos que me faltan.',
 'c_kicker': 'Certificados', 'c_title': 'Lo que ya tengo <em>en papel</em>', 'c_sub': 'Ocho certificados, cada uno de un módulo o curso que he terminado.',
 'c1': 'AWS Educate · Generative AI', 'c2': 'IA y Logística', 'c3': 'Pseudocódigo', 'c4': 'Linux y la Terminal',
 'c5': 'Git y GitHub', 'c6': 'Python', 'c7': 'Python Avanzado', 'c8': 'SQL',
 'w_eyebrow': 'Disponible para nuevos proyectos',
 'w_h1': 'Webs claras para <em>pequeños negocios</em>',
 'w_lead': 'Diseño y desarrollo web mientras sigo estudiando. Hablamos de lo que necesitas, te doy una cifra concreta y recibes una web lista para compartir.',
 'w_btn1': 'Ver planes', 'w_btn2': 'Escríbeme',
 'w_chip1': 'Español e inglés', 'w_chip2': 'Horario de España',
 'p_kicker': 'Planes', 'p_title': 'Tres formas de <em>empezar</em>',
 'p_note': 'Estos precios marcan el punto de partida. Hablamos de tu proyecto, lo ajustamos y entonces te doy una cifra concreta.',
 'p_from': 'Desde', 'pl_cta': 'Lo hablamos',
 'pl1_n': 'Landing sencilla', 'pl1_d': 'Diseño y textos de una web de una página, lista para compartir.',
 'pl1_p': '700 €', 'pl1_m': 'pago único',
 'pl1_f1': 'Diseño de una página', 'pl1_f2': 'Textos incluidos', 'pl1_f3': 'Lista para compartir',
 'pl2_n': 'Landing + mantenimiento', 'pl2_d': 'La landing, más cambios de contenido, actualizaciones técnicas y copias de seguridad cada mes.',
 'pl2_p': '700 €', 'pl2_m': 'y desde 30 €/mes',
 'pl2_f1': 'Landing completa', 'pl2_f2': 'Cambios de contenido', 'pl2_f3': 'Actualizaciones técnicas', 'pl2_f4': 'Copias de seguridad',
 'pl3_n': 'Web completa con SEO y mantenimiento', 'pl3_d': 'Una web de varias páginas con SEO y mantenimiento mensual. También tiendas online o apps.',
 'pl3_p': 'A medida', 'pl3_m': 'Presupuesto tras hablar',
 'pl3_f1': 'Web de varias páginas', 'pl3_f2': 'SEO incluido', 'pl3_f3': 'Mantenimiento mensual', 'pl3_f4': 'Tiendas online o apps',
 'ex_title': 'Extras sueltos',
 'ex1': 'SEO técnica', 'ex1p': 'desde 150 €', 'ex2': 'Contenido optimizado', 'ex2p': 'desde 150 €',
 'ex3': 'Seguimiento SEO', 'ex3p': 'desde 60 €/mes', 'ex4': 'Mantenimiento + SEO', 'ex4p': 'desde 80 €/mes',
 'pr_kicker': 'Proyectos', 'pr_title': 'Trabajo <em>real</em>',
 'tbh_badge': 'Cliente real',
 'tbh_desc': 'Rediseño completo de la web de TBH Strategy, la consultora de redes sociales de Tamara en Tralee: identidad en verde salvia, blog para posicionar en Google, formulario de contacto y migración de dominio sin perder el correo ni la analítica.',
 'tag1': 'Migración de dominio', 'tag2': 'SEO / Blog', 'tag3': 'Google Analytics',
 'tbh_cta': 'Visitar tbhstrategy.com',
 'ly_sub': 'Gestión de redes sociales', 'ly_badge': 'Próximamente',
 'own_t': 'Esta web y su repositorio', 'own_badge': 'Proyecto propio',
 'own_d': 'El código de esta web está en GitHub, abierto para que lo veas.', 'own_cta': 'Ver repositorio',
 'who_kicker': 'Quién lo hace', 'who_title': 'Hola, soy <em>Marcos</em>',
 'who_text': 'Vivo en Vantaa, Finlandia, y estudio el máster Full Stack en Conquer Blocks mientras hago webs para pequeños negocios. Atiendo en español e inglés y trabajo con horario de España.',
 'who_link': 'Conoce mi portfolio',
 'cta_title': '¿Hablamos de <em>tu web</em>?', 'cta_text': 'Cuéntame qué necesitas y te respondo con una cifra concreta.',
 'f_loc': 'Vantaa, Finlandia', 'f_rights': 'Todos los derechos reservados', 'f_nav': 'Navegación', 'f_contact': 'Contacto', 'f_top': 'Volver arriba', 'f_thanks': 'Gracias por llegar hasta aquí.',
}

EN = {
 'n_home': 'Home', 'n_master': 'Master', 'n_certs': 'Certificates', 'n_web': 'Web development',
 'n_plans': 'Plans', 'n_projects': 'Projects', 'n_contact': 'Contact', 'n_portfolio': 'Portfolio',
 'cta_talk': "Let's talk", 'cta_write': 'Write to me',
 'h_eyebrow': 'Full Stack software developer in training',
 'h_hello': "Hi! I'm Marcos Rodriguez",
 'h1': "Hi! I'm <em>Marcos Rodriguez</em>",
 'h_lead': 'When a project lands in my hands, I take it to its best version. Detail, energy and one goal: that when you see it you think “this is exactly what I wanted”.',
 'h_short': "I'm studying the Full Stack master at Conquer Blocks and I tell each module in my own words.",
 'role_a': 'Full stack', 'role_b': 'in training', 'role_c': 'Developer',
 'btn_master': 'This is my training', 'btn_web': 'Websites for your business',
 'chip_loc': 'Vantaa, Finland', 'chip_fi': 'Finland', 'chip_lang': 'Spanish and English',
 'follow': 'Follow me', 'hire': 'WRITE TO ME · WRITE TO ME · ',
 'st_certs': 'Certificates', 'st_mods': 'Modules', 'st_langs': 'Languages', 'st_plans': 'Plans',
  'k_kicker': 'Technical knowledge and tools', 'k_title': 'What I have covered, <em>by area</em>',
 'k_intro': 'What the master has covered so far, sorted by the kind of work it serves.',
 'a1_t': 'Logic and programming', 'a1_d': 'Framing a problem, solving it in code and shaping it into a web page.',
 'a2_t': 'Data', 'a2_d': 'Storing information, querying it and relating it across tables.',
 'a3_t': 'Working tools', 'a3_d': 'The everyday environment to write, version and organise code.',
 'a4_t': 'Artificial intelligence', 'a4_d': 'AI module with Antigravity: working with assistants, agents and connected tools.',
 'a5_t': 'Cloud publishing', 'a5_d': 'Getting a website online from its repository.',
 'k_logic': 'Logic and pseudocode', 'k_oop': 'Object-oriented programming', 'k_joins': 'Queries with JOINs and subqueries',
 'k_rel': 'Table relationships', 'k_orm': 'SQLAlchemy and ORM', 'k_linux': 'Linux and terminal', 'k_gha': 'GitHub from Antigravity',
 'ai1_t': 'Google Antigravity', 'ai1_d': 'Editor with a built-in AI assistant to put together and review web projects.',
 'ai2_t': 'AI agents', 'ai2_d': 'Setting up and tuning agents that take care of development tasks.',
 'ai3_t': 'Automated processes', 'ai3_d': 'Chaining repetitive steps into workflows that run by themselves.',
 'ai4_t': 'NotebookLM', 'ai4_d': 'Organising documentation and querying it with AI help.',
 'ai5_t': 'Model Context Protocol', 'ai5_d': 'Plugging external tools into AI models.',
 'ai6_t': 'Google Stitch', 'ai6_d': 'Generating interface and design proposals from an idea.',
 'ai7_t': 'Open Agent Manager', 'ai7_d': 'Tracking and coordinating several agents from one place.',
 'ai8_t': 'Apps and sites with built-in AI', 'ai8_d': 'Giving a site or an app features that use AI.',
 'ai9_t': 'OpenAI', 'ai9_d': 'Trying its models and tools on different tasks.',
 'cl1_t': 'Cloudflare', 'cl1_d': 'Handling the basics of a project and its services from the dashboard.',
 'cl2_t': 'Cloudflare Pages', 'cl2_d': 'Publishing static sites linked to a GitHub repository.',
 'm_kicker': 'Full Stack Master at Conquer Blocks', 'mq_title': 'Everything the master covers, <em>at a glance</em>', 'mq_intro': 'Languages, frameworks and tools from the Full Stack syllabus.', 'm_title': 'Module by module, <em>in my own words</em>',
 'm_intro': 'For each module I tell three things: what it was, what I learned and how I use it today.',
 'm_what': 'What it was', 'm_learn': 'What I learned', 'm_use': 'How I use it today',
 'm_pending': "Pending: I'll write this from the module's index.",
 'm_view': 'See modules', 'tag_cert': 'Certified',
 'mod1': 'Pseudocode', 'mod2': 'Linux and the Terminal', 'mod3': 'Python, basic and advanced',
 'mod4': 'Git and GitHub', 'mod5': 'SQL', 'mod6': 'AI', 'mod7': 'AI agents and automation',
 'g_kicker': 'Where I am heading', 'g_title': 'Where I am <em>heading</em>',
 'g_text': "I want to work as a freelancer or for a good company that lets me do it remotely. I keep studying, and the modules I still have to take will show up here.",
 'g_pending': 'Pending: list of the modules I still have to take.',
 'c_kicker': 'Certificates', 'c_title': 'What I already have <em>on paper</em>', 'c_sub': 'Eight certificates, each from a module or course I have finished.',
 'c1': 'AWS Educate · Generative AI', 'c2': 'AI and Logistics', 'c3': 'Pseudocode', 'c4': 'Linux and the Terminal',
 'c5': 'Git and GitHub', 'c6': 'Python', 'c7': 'Advanced Python', 'c8': 'SQL',
 'w_eyebrow': 'Available for new projects',
 'w_h1': 'Clear websites for <em>small businesses</em>',
 'w_lead': 'Web design and development while I keep studying. We talk about what you need, I give you a concrete figure and you get a website ready to share.',
 'w_btn1': 'See plans', 'w_btn2': 'Write to me',
 'w_chip1': 'Spanish and English', 'w_chip2': 'Spanish time zone',
 'p_kicker': 'Plans', 'p_title': 'Three ways to <em>start</em>',
 'p_note': 'These prices are the starting point. We talk about your project, adjust it, and then I give you a concrete figure.',
 'p_from': 'From', 'pl_cta': "Let's talk",
 'pl1_n': 'Simple landing', 'pl1_d': 'Design and copy for a one-page website, ready to share.',
 'pl1_p': '€700', 'pl1_m': 'one-off payment',
 'pl1_f1': 'One-page design', 'pl1_f2': 'Copy included', 'pl1_f3': 'Ready to share',
 'pl2_n': 'Landing + maintenance', 'pl2_d': 'The landing, plus content changes, technical updates and backups every month.',
 'pl2_p': '€700', 'pl2_m': 'plus from €30/month',
 'pl2_f1': 'Complete landing', 'pl2_f2': 'Content changes', 'pl2_f3': 'Technical updates', 'pl2_f4': 'Backups',
 'pl3_n': 'Full website with SEO and maintenance', 'pl3_d': 'A multi-page website with SEO and monthly maintenance. Online stores and apps too.',
 'pl3_p': 'Custom quote', 'pl3_m': 'Quote after we talk',
 'pl3_f1': 'Multi-page website', 'pl3_f2': 'SEO included', 'pl3_f3': 'Monthly maintenance', 'pl3_f4': 'Online stores or apps',
 'ex_title': 'Add-ons',
 'ex1': 'Technical SEO', 'ex1p': 'from €150', 'ex2': 'Keyword-optimized content', 'ex2p': 'from €150',
 'ex3': 'Monthly SEO follow-up', 'ex3p': 'from €60/month', 'ex4': 'Maintenance + SEO', 'ex4p': 'from €80/month',
 'pr_kicker': 'Projects', 'pr_title': 'Real <em>work</em>',
 'tbh_badge': 'Real client',
 'tbh_desc': "Full redesign of the TBH Strategy website, Tamara's social media consultancy in Tralee: a sage-green identity, a blog to rank on Google, a contact form and a domain migration that kept her email and analytics intact.",
 'tag1': 'Domain migration', 'tag2': 'SEO / Blog', 'tag3': 'Google Analytics',
 'tbh_cta': 'Visit tbhstrategy.com',
 'ly_sub': 'Social media management', 'ly_badge': 'Coming soon',
 'own_t': 'This website and its repository', 'own_badge': 'Own project',
 'own_d': 'The code of this website is on GitHub, open for you to read.', 'own_cta': 'See repository',
 'who_kicker': 'Who is behind it', 'who_title': "Hi, I'm <em>Marcos</em>",
 'who_text': "I live in Vantaa, Finland, and I'm studying the Full Stack master at Conquer Blocks while I build websites for small businesses. I work in Spanish and English, on Spanish hours.",
 'who_link': 'See my portfolio',
 'cta_title': "Shall we talk about <em>your website</em>?", 'cta_text': 'Tell me what you need and I will answer with a concrete figure.',
 'f_loc': 'Vantaa, Finland', 'f_rights': 'All rights reserved', 'f_nav': 'Navigation', 'f_contact': 'Contact', 'f_top': 'Back to top', 'f_thanks': 'Thanks for making it this far.',
}

from wbdata import KEYS_ES, KEYS_EN
ES.update(KEYS_ES)
EN.update(KEYS_EN)

MODS = ['mod1', 'mod2', 'mod3', 'mod4', 'mod5', 'mod6', 'mod7']
CERT_MODS = {'mod1', 'mod2', 'mod3', 'mod4', 'mod5'}

IMG_FOTO1 = 'img/foto-1.webp'
IMG_FOTO2 = 'img/foto-2.webp'
IMG_CUT1 = 'img/foto-1-recorte.png'
IMG_CUT2 = 'img/foto-2-recorte.png'
IMG_TBH = 'img/tbh-inicio.webp'
ALT1 = 'Marcos Rodríguez sentado ante su portátil en su escritorio'
ALT2 = 'Retrato de Marcos Rodríguez con los brazos cruzados'
ALT_TBH = 'Captura de la página de inicio de tbhstrategy.com'

GH = 'https://github.com/M4rKitS'
LI = 'https://www.linkedin.com/in/mrodriguezhdz'
MAIL = 'mailto:contact@m4rkits.dev'
TEL = 'tel:+358413193036'
WA = 'https://wa.me/358413193036'

P = {
 'gh': '<path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>',
 'li': '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>',
 'wa': '<path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>',
 'spark': '<path d="M12 1.5c.7 5.6 4.9 9.8 10.5 10.5-5.6.7-9.8 4.9-10.5 10.5-.7-5.6-4.9-9.8-10.5-10.5C7.1 11.3 11.3 7.1 12 1.5z"/>',
 'sun': '<path d="M12 1l1.9 6.1L19.5 3.6l-2.2 6.1 6.2 1.3-6.2 1.3 2.2 6.1-5.6-3.5L12 23l-1.9-6.1-5.6 3.5 2.2-6.1L.5 11l6.2-1.3-2.2-6.1 5.6 3.5z"/>',
}
STROKE = {
 'ur': '<path d="M7 17 17 7M8 7h9v9"/>',
 'r': '<path d="M5 12h14M13 6l6 6-6 6"/>',
 'l': '<path d="M19 12H5M11 6l-6 6 6 6"/>',
 'check': '<path d="M5 12.5 10 17l9-10"/>',
 'chev': '<path d="m6 9 6 6 6-6"/>',
 'mail': '<path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/><path d="m3 7 9 6 9-6"/>',
 'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.9.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 'pin': '<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 'shield': '<path d="M12 3 5 6v5c0 4.5 3 8.2 7 10 4-1.8 7-5.5 7-10V6z"/><path d="m9 12 2 2 4-4"/>',
 'badge': '<circle cx="12" cy="9" r="6"/><path d="m9 14-1.5 7L12 18.5 16.5 21 15 14"/>',
 'code': '<path d="m8 8-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>',
 'term': '<path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/><path d="m7 10 3 2-3 2M12 15h4"/>',
 'db': '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3.1 3 7 3s7-1.3 7-3V6M5 12v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6"/>',
 'branch': '<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="8" r="2.5"/><path d="M6 8.5v7M18 10.5c0 4-5 3-10.5 6"/>',
 'bot': '<rect x="4" y="8" width="16" height="11" rx="3"/><path d="M12 4v4M9 13h.01M15 13h.01M9 16h6"/>',
 'brain': '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 5 1V4a3 3 0 0 0-2 0zM15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-5 1V4a3 3 0 0 1 2 0z"/>',
 'cloud': '<path d="M17.5 19H9a7 7 0 1 1 6.7-9h1.8a4.5 4.5 0 1 1 0 9z"/>',
 'play': '<path d="m8 5 11 7-11 7z"/>',
 'img': '<rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-8 9"/>',
 'link': '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3A4 4 0 0 0 11 18.7l1-1"/>',
 'text': '<path d="M4 7V5h16v2M9 19h6M12 5v14"/>',
 'gear': '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
}


def ic(name, size=20, cls=''):
    c = ' class="%s"' % cls if cls else ''
    if name in P:
        return '<svg%s viewBox="0 0 24 24" width="%d" height="%d" fill="currentColor" aria-hidden="true">%s</svg>' % (c, size, size, P[name])
    return ('<svg%s viewBox="0 0 24 24" width="%d" height="%d" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>') % (c, size, size, STROKE[name])


def T(k):
    return '<span data-t="%s">%s</span>' % (k, ES[k])


def socials(cls='', size=20):
    items = [('gh', GH, 'GitHub'), ('li', LI, 'LinkedIn'), ('mail', MAIL, 'Email'), ('wa', WA, 'WhatsApp')]
    out = []
    for n, h, label in items:
        ext = '' if n == 'mail' else ' target="_blank" rel="noopener noreferrer"'
        out.append('<a class="%s" href="%s"%s aria-label="%s">%s</a>' % (cls, h, ext, label, ic(n, size)))
    return ''.join(out)


COMMON_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;overflow-x:clip}
body{overflow-x:clip;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
img{display:block;max-width:100%}
a{color:inherit}
ul,ol{list-style:none}
button{font:inherit;color:inherit}
summary{list-style:none;cursor:pointer}
summary::-webkit-details-marker{display:none}
:focus-visible{outline:3px solid currentColor;outline-offset:3px}
.pgdiv{display:flex;align-items:center;gap:14px;max-width:1180px;margin:0 auto;padding:36px 20px;font:600 11px/1.2 system-ui,-apple-system,sans-serif;letter-spacing:.12em;text-transform:uppercase;opacity:.55}
.pgdiv::before,.pgdiv::after{content:"";flex:1;border-top:1px dashed currentColor}
.mock{margin:0;border-radius:14px;overflow:hidden;background:#fff;box-shadow:0 30px 60px -30px rgba(0,0,0,.45);border:1px solid rgba(0,0,0,.08)}
.mock-bar{display:flex;align-items:center;gap:6px;padding:9px 12px;background:#ECECEC;border-bottom:1px solid rgba(0,0,0,.08)}
.mock-bar i{width:10px;height:10px;border-radius:50%;background:#C9C9C9}
.mock-bar span{margin-left:8px;flex:1;max-width:260px;font:500 .74rem/1.6 system-ui,sans-serif;padding:1px 10px;border-radius:99px;background:#fff;color:#555}
.mock img{width:100%;height:auto}
.lang{display:inline-flex;gap:2px}
.lang button{border:0;background:none;cursor:pointer;font-weight:600;font-size:.82rem;padding:5px 9px;border-radius:99px}
@keyframes marq{to{transform:translateX(-50%)}}
@keyframes spin{to{transform:rotate(360deg)}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;scroll-behavior:auto!important;transition:none!important}}
"""



import re as _re
_SRCSET = {
    'img/foto-1.webp': ('img/foto-1-1024.webp', [('img/foto-1-640.webp', 640), ('img/foto-1-1024.webp', 1024)], '(max-width:700px) 90vw, 420px'),
    'img/foto-3.jpg': ('img/foto-3-1024.webp', [('img/foto-3-640.webp', 640), ('img/foto-3-1024.webp', 1024)], '(max-width:700px) 90vw, 520px'),
    'img/foto-4.jpg': ('img/foto-4-1024.webp', [('img/foto-4-640.webp', 640), ('img/foto-4-1024.webp', 1024)], '(max-width:700px) 90vw, 520px'),
    'img/foto-7.webp': ('img/foto-7-1448.webp', [('img/foto-7-800.webp', 800), ('img/foto-7-1448.webp', 1448)], '(max-width:859px) 90vw, 560px'),
    'img/helsinki.jpg': ('img/helsinki-1600.webp', [('img/helsinki-800.webp', 800), ('img/helsinki-1600.webp', 1600)], '(max-width:700px) 90vw, 700px'),
}
_SWAP = {
    'img/tbh-inicio.webp': 'img/tbh-inicio-1000.webp',
    'img/web-development-captura.jpg': 'img/web-development-captura-4.webp',
    'img/web-development-captura-en.jpg': 'img/web-development-captura-en-4.webp',
    'img/portfolio-captura.jpg': 'img/portfolio-captura-3.webp',
    'img/portfolio-captura-en.jpg': 'img/portfolio-captura-en-3.webp',
    'img/plan-1.jpg': 'img/plan-1.webp', 'img/plan-2.jpg': 'img/plan-2.webp', 'img/plan-3.jpg': 'img/plan-3.webp',
    'img/logo-horizontal-claro.png': 'img/logo-horizontal-claro.webp',
    'img/logo-horizontal-oscuro.png': 'img/logo-horizontal-oscuro.webp',
}


def optimize_imgs(h):
    """Imagenes ligeras: WebP, tamanos adaptados (srcset) y prioridad para la foto principal."""
    def fix(m):
        tag = m.group(0)
        s = _re.search(r'src="([^"]+)"', tag)
        if not s:
            return tag
        src = s.group(1)
        if src in _SRCSET:
            main, sets, sizes = _SRCSET[src]
            tag = tag.replace('src="%s"' % src, 'src="%s" srcset="%s" sizes="%s"' % (main, ', '.join('%s %dw' % (u, w) for u, w in sets), sizes))
            if 'data-prio' in tag:
                tag = tag.replace(' data-prio', '').replace(' loading="lazy"', '').replace('<img ', '<img fetchpriority="high" decoding="async" ', 1)
            elif 'loading=' not in tag:
                tag = tag.replace('<img ', '<img loading="lazy" decoding="async" ', 1)
        elif src in _SWAP:
            tag = tag.replace('src="%s"' % src, 'src="%s"' % _SWAP[src])
        return tag
    return _re.sub(r'<img [^>]*>', fix, h)
