# Datos del panel "Lo que he visto": un area por pestana, con orden y nombres propios.
# icono: 'logo:<archivo>' (img/icons/<archivo>.svg), 'png:<archivo>' o 'sk:<nombre>' (trazo propio)
AREAS = [
    dict(tab=('Entorno', 'Environment'), ext='sh', code='$ cd mi-proyecto && code .',
         title=('Entorno de trabajo', 'Working environment'),
         desc=('Dónde se trabaja: el sistema, la terminal y el editor.', 'Where the work happens: the system, the terminal and the editor.'),
         items=[
             ('logo:linux', ('Linux y terminal', 'Linux and terminal'), ('Moverse por el sistema y lanzar tareas desde la línea de comandos.', 'Moving around the system and running tasks from the command line.')),
             ('logo:zsh', ('Zsh', 'Zsh'), ('Intérprete de comandos para trabajar cómodo en la terminal.', 'Command interpreter to work comfortably in the terminal.')),
             ('logo:vscode', ('VS Code', 'VS Code'), ('Editor donde se escribe, se prueba y se revisa el código.', 'Editor where code is written, tested and reviewed.')),
         ]),
    dict(tab=('Versiones', 'Versions'), ext='git', code='$ git commit -m "avance"',
         title=('Control de versiones', 'Version control'),
         desc=('Guardar la historia del código y trabajar sin miedo a perder nada.', 'Keeping the history of the code and working without fear of losing anything.'),
         items=[
             ('logo:git', ('Git', 'Git'), ('Registrar cambios y volver atrás cuando haga falta.', 'Recording changes and going back when needed.')),
             ('logo:github', ('GitHub', 'GitHub'), ('Alojar repositorios y dejar el código disponible en la nube.', 'Hosting repositories and keeping the code available in the cloud.')),
             ('logo:github', ('GitHub desde Antigravity', 'GitHub from Antigravity'), ('Manejar el repositorio sin salir del editor con IA.', 'Handling the repository without leaving the AI editor.')),
         ]),
    dict(tab=('Código', 'Code'), ext='py', code='def hola(): print("Hola")',
         title=('Código y lógica', 'Code and logic'),
         desc=('Pensar la solución y escribirla en código.', 'Thinking up the solution and writing it as code.'),
         items=[
             ('sk:tree', ('Lógica y pseudocódigo', 'Logic and pseudocode'), ('Plantear los pasos de un problema antes de programarlos.', 'Laying out the steps of a problem before coding them.')),
             ('logo:python', ('Python', 'Python'), ('Lenguaje para escribir programas y automatizar tareas.', 'Language to write programs and automate tasks.')),
             ('sk:klass', ('Programación orientada a objetos', 'Object-oriented programming'), ('Organizar el código en clases y objetos reutilizables.', 'Organising code into reusable classes and objects.')),
             ('logo:html5', ('HTML', 'HTML'), ('La estructura y el contenido de una página web.', 'The structure and content of a web page.')),
             ('logo:css3', ('CSS', 'CSS'), ('El aspecto de la web: color, tipografía y distribución.', 'The look of the web: colour, type and layout.')),
         ]),
    dict(tab=('Datos', 'Data'), ext='sql', code='SELECT nombre FROM alumnos;',
         title=('Datos', 'Data'),
         desc=('Guardar la información, consultarla y relacionarla.', 'Storing information, querying it and relating it.'),
         items=[
             ('png:sql', ('SQL', 'SQL'), ('Lenguaje para pedir y modificar datos.', 'Language to request and change data.')),
             ('logo:mysql', ('MySQL', 'MySQL'), ('Sistema de bases de datos que guarda la información en tablas.', 'Database system that stores information in tables.')),
             ('sk:joins', ('Consultas con JOIN y subconsultas', 'Queries with JOINs and subqueries'), ('Combinar tablas y filtrar con consultas anidadas.', 'Combining tables and filtering with nested queries.')),
             ('sk:chain', ('Relaciones entre tablas', 'Table relationships'), ('Diseñar cómo se conectan los datos entre sí.', 'Designing how data connects together.')),
             ('logo:sqlalchemy', ('SQLAlchemy y ORM', 'SQLAlchemy and ORM'), ('Trabajar con la base de datos desde Python usando objetos.', 'Working with the database from Python through objects.')),
         ]),
    dict(tab=('IA', 'AI'), ext='md', code='> resume esta documentación',
         title=('Inteligencia artificial', 'Artificial intelligence'),
         desc=('Antigravity: asistentes, agentes y herramientas conectadas.', 'Antigravity: assistants, agents and connected tools.'),
         items=[
             ('logo:antigravity', ('Google Antigravity', 'Google Antigravity'), ('Editor con asistente de IA integrado para montar y revisar proyectos web.', 'Editor with a built-in AI assistant to put together and review web projects.')),
             ('sk:agent', ('Agentes de IA', 'AI agents'), ('Preparar y ajustar agentes que se encargan de tareas de desarrollo.', 'Setting up and tuning agents that take care of development tasks.')),
             ('sk:loop', ('Procesos automatizados', 'Automated processes'), ('Encadenar pasos repetitivos en flujos que se ejecutan solos.', 'Chaining repetitive steps into workflows that run by themselves.')),
             ('logo:notebooklm', ('NotebookLM', 'NotebookLM'), ('Ordenar documentación y consultarla con ayuda de IA.', 'Organising documentation and querying it with AI help.')),
             ('logo:mcp', ('Model Context Protocol', 'Model Context Protocol'), ('Enchufar herramientas externas a los modelos de IA.', 'Plugging external tools into AI models.')),
             ('sk:pen', ('Google Stitch', 'Google Stitch'), ('Generar propuestas de interfaz y diseño a partir de una idea.', 'Generating interface and design proposals from an idea.')),
             ('sk:sliders', ('Open Agent Manager', 'Open Agent Manager'), ('Seguir y coordinar varios agentes desde un mismo sitio.', 'Tracking and coordinating several agents from one place.')),
             ('sk:winai', ('Apps y webs con IA integrada', 'Apps and sites with built-in AI'), ('Funciones de IA en webs y apps.', 'AI features in sites and apps.')),
             ('logo:chatgpt', ('OpenAI', 'OpenAI'), ('Probar sus modelos y herramientas en distintas tareas.', 'Trying its models and tools on different tasks.')),
         ]),
    dict(tab=('Publicar', 'Publish'), ext='yml', code='$ wrangler pages deploy',
         title=('Publicar en internet', 'Publish online'),
         desc=('Sacar un sitio web a internet y mantenerlo en marcha.', 'Getting a website online and keeping it running.'),
         items=[
             ('logo:cloudflare', ('Cloudflare', 'Cloudflare'), ('Manejar lo básico de un proyecto y sus servicios desde el panel.', 'Handling the basics of a project and its services from the dashboard.')),
             ('logo:cloudflarepages', ('Cloudflare Pages', 'Cloudflare Pages'), ('Publicar sitios estáticos enlazados a un repositorio de GitHub.', 'Publishing static sites linked to a GitHub repository.')),
             ('logo:wrangler', ('Wrangler', 'Wrangler'), ('Gestionar y publicar proyectos de Cloudflare desde la línea de comandos.', 'Managing and publishing Cloudflare projects from the command line.')),
             ('sk:server', ('Alojamiento web', 'Web hosting'), ('Tener una web propia alojada, en línea y al día.', 'Having your own site hosted, online and up to date.')),
         ]),
]


# Desarrollo de cada area: parrafo ampliado y aprendizajes (ES, EN)
MORE = [
    dict(lead=('Todo proyecto empieza en un entorno bien montado. Aquí entran el sistema Linux, la terminal con su shell y el editor donde se escribe y se revisa el código: la base sobre la que se apoya el resto del trabajo.',
               'Every project starts in a well-built environment. This covers the Linux system, the terminal with its shell and the editor where code is written and reviewed: the base everything else rests on.'),
         learn=[('Moverme por carpetas y archivos desde la línea de comandos.', 'Moving around folders and files from the command line.'),
                ('Lanzar y encadenar comandos sin depender del ratón.', 'Running and chaining commands without relying on the mouse.'),
                ('Dejar el editor preparado para escribir y revisar código con comodidad.', 'Setting up the editor to write and review code comfortably.')]),
    dict(lead=('El control de versiones guarda cada cambio con su historia, permite probar ideas sin riesgo y volver atrás cuando algo falla. Git hace ese trabajo en local y GitHub lo lleva a la nube para compartirlo.',
               'Version control keeps every change with its history, lets you try ideas without risk and go back when something breaks. Git does that work locally and GitHub takes it to the cloud to share it.'),
         learn=[('Registrar cambios en un repositorio de forma ordenada.', 'Recording changes in a repository in an orderly way.'),
                ('Trabajar con ramas y recuperar una versión anterior.', 'Working with branches and recovering an earlier version.'),
                ('Subir y sincronizar un proyecto con GitHub.', 'Pushing and syncing a project with GitHub.')]),
    dict(lead=('Antes de escribir una línea hay que saber qué pasos resuelven el problema. De ahí se pasa a un lenguaje, Python, a organizar el código con objetos y a dar forma a una página con HTML y CSS.',
               'Before writing a line you need to know which steps solve the problem. From there you move to a language, Python, to organising code with objects and to shaping a page with HTML and CSS.'),
         learn=[('Descomponer un problema en pasos con pseudocódigo.', 'Breaking a problem into steps with pseudocode.'),
                ('Escribir programas en Python con condiciones, bucles y funciones.', 'Writing Python programs with conditions, loops and functions.'),
                ('Organizar el código en clases y objetos.', 'Organising code into classes and objects.'),
                ('Maquetar una página con HTML y darle estilo con CSS.', 'Laying out a page with HTML and styling it with CSS.')]),
    dict(lead=('Casi toda aplicación necesita guardar información y recuperarla. Esta área recorre cómo se diseñan las tablas y sus relaciones, cómo se piden los datos con SQL y cómo se manejan desde Python con un ORM.',
               'Almost every application needs to store information and get it back. This area covers how tables and their relationships are designed, how data is requested with SQL and how it is handled from Python with an ORM.'),
         learn=[('Crear tablas y relacionarlas entre sí.', 'Creating tables and relating them to each other.'),
                ('Consultar datos con SELECT, JOIN y subconsultas.', 'Querying data with SELECT, JOINs and subqueries.'),
                ('Conectar la base de datos con Python mediante SQLAlchemy.', 'Connecting the database to Python through SQLAlchemy.')]),
    dict(lead=('Con Antigravity se trabaja acompañado de asistentes y agentes, se automatizan tareas repetitivas y se conectan herramientas externas con los modelos.',
               'With Antigravity you work alongside assistants and agents, automate repetitive tasks and connect external tools to the models.'),
         learn=[('Usar un editor con asistente de IA para montar proyectos.', 'Using an editor with an AI assistant to put projects together.'),
                ('Configurar agentes y coordinarlos entre sí.', 'Configuring agents and coordinating them.'),
                ('Automatizar procesos y conectar herramientas con MCP.', 'Automating processes and connecting tools with MCP.'),
                ('Explorar los modelos y las herramientas de OpenAI.', 'Exploring OpenAI models and tools.')]),
    dict(lead=('Un sitio no existe hasta que está en internet. Cloudflare Pages publica una web estática desde su repositorio de GitHub, Wrangler permite hacerlo desde la terminal y el alojamiento mantiene la web propia en línea.',
               'A site does not exist until it is online. Cloudflare Pages publishes a static website from its GitHub repository, Wrangler lets you do it from the terminal and hosting keeps your own site online.'),
         learn=[('Conectar un repositorio con Cloudflare Pages y publicar un sitio estático.', 'Connecting a repository to Cloudflare Pages and publishing a static site.'),
                ('Usar Wrangler para desplegar y gestionar proyectos desde la terminal.', 'Using Wrangler to deploy and manage projects from the terminal.'),
                ('Alojar una web propia y mantenerla en línea y actualizada.', 'Hosting your own site and keeping it online and up to date.'),
                ('Manejar lo básico del panel de Cloudflare.', 'Handling the basics of the Cloudflare dashboard.')]),
]
for _a, _m in zip(AREAS, MORE):
    _a.update(_m)

# Pestaña de IA: va la primera. Presenta el trabajo como desarrollo asistido por agentes: especifico, superviso y valido,
# apoyándome en los fundamentos que adquiero en el máster. Todo lo que aparece sale de lo que hago de verdad.
_ia = [a for a in AREAS if a['tab'][0] == 'IA'][0]
_ia['tab'] = ('IA y agentes', 'AI and agents')
_ia['title'] = ('Desarrollo asistido por agentes de IA', 'AI-agent-assisted development')
_ia['desc'] = ('Agentes de IA para acelerar el desarrollo y reducir la carga operativa, apoyados en los fundamentos del máster.',
               'AI agents to speed up development and reduce operational workload, backed by the fundamentals of the master.')
_ia['lead'] = (
    'Mi flujo de trabajo es desarrollo asistido por agentes: defino el objetivo, oriento al agente con especificaciones precisas, reviso el código que genera y valido cada entregable antes de darlo por bueno. Esa supervisión se apoya en mis conocimientos y lenguajes de programación adquiridos, que me permiten leer y entender el resultado. Empecé con Google Antigravity y hoy trabajo con Claude Code.',
    'My workflow is agent-assisted development: I set the goal, steer the agent with precise specifications, review the code it generates and validate every deliverable before accepting it. That oversight rests on the knowledge and programming languages I have acquired, which let me read and understand the result. I started with Google Antigravity and today I work with Claude Code.')
_ia['learn_label'] = ('Metodología', 'Methodology')
_ia['tools_label'] = ('Stack de IA', 'AI stack')
_ia['learn'] = [
    ('Flujo prompt-first con humano en el circuito (human-in-the-loop): defino el objetivo, el agente implementa y yo decido cuándo se avanza al siguiente paso.',
     'Prompt-first workflow with a human in the loop: I define the goal, the agent implements and I decide when to move on to the next step.'),
    ('Ingeniería de prompts: redacto especificaciones precisas con un asistente conversacional (Claude) antes de lanzar el agente de código.',
     'Prompt engineering: I write precise specifications with a conversational assistant (Claude) before launching the coding agent.'),
    ('Gestión del contexto: separo en chats distintos la estrategia y las decisiones de alto nivel de la generación de prompts de código.',
     'Context management: I keep strategy and high-level decisions in separate chats from the generation of code prompts.'),
    ('Revisión y validación: contrasto cada resultado con capturas y pruebas, itero en varias rondas y compruebo si el agente editó un archivo o lo regeneró desde cero, para no perder correcciones previas.',
     'Review and validation: I check every result with screenshots and tests, iterate over several rounds and verify whether the agent edited a file or regenerated it from scratch, so earlier fixes are not lost.'),
    ('Skills: amplío el agente con paquetes de instrucciones especializadas (diseño, animación con GSAP, SEO, vídeo con Remotion) y mantengo una propia con mi proceso de diseño, que aporto al inicio de cada prompt de diseño.',
     'Skills: I extend the agent with specialised instruction packs (design, GSAP animation, SEO, Remotion video) and maintain my own with my design process, which I include at the start of every design prompt.'),
    ('Entradas reales en lugar de descripciones: aporto logotipos, moodboards y capturas en vez de describir colores con texto.',
     'Real inputs instead of descriptions: I provide logos, moodboards and screenshots rather than describing colours in words.'),
    ('Seguridad y control del agente: claves de API fuera del código, confirmación previa de cada comando de terminal y ningún acceso a datos reales de producción.',
     'Security and agent control: API keys kept out of the code, confirmation before every terminal command and no access to real production data.'),
    ('Control de versiones desde el primer día: cada proyecto va a GitHub.',
     'Version control from day one: every project goes to GitHub.'),
]
_ia['items'] = [
    ('logo:claudecode', ('Claude Code', 'Claude Code'), ('Agente de código de mi flujo actual: implementa lo que especifico y yo reviso cada cambio.', 'Coding agent in my current workflow: it implements what I specify and I review every change.')),
    ('logo:antigravity', ('Google Antigravity', 'Google Antigravity'), ('Primer agente de código que utilicé.', 'The first coding agent I used.')),
    ('sk:agent', ('Claude, asistente conversacional', 'Claude, conversational assistant'), ('Redacto y afino los prompts con él antes de ejecutarlos.', 'I write and refine prompts with it before running them.')),
    ('sk:pen', ('Google Stitch', 'Google Stitch'), ('Prototipado de interfaces, conectado al agente mediante MCP.', 'Interface prototyping, connected to the agent through MCP.')),
    ('logo:mcp', ('Model Context Protocol', 'Model Context Protocol'), ('Estándar para que un agente utilice herramientas externas.', 'Standard that lets an agent use external tools.')),
    ('logo:chatgpt', ('ChatGPT', 'ChatGPT'), ('Rediseño de logotipo, favicon y firma de correo con la paleta del sitio.', 'Redesign of logo, favicon and email signature with the site palette.')),
    ('logo:n8n', ('n8n', 'n8n'), ('Plataforma de automatización: une aplicaciones y servicios en flujos de trabajo que se ejecutan solos.', 'Automation platform: it links apps and services into workflows that run by themselves.')),
    ('logo:notebooklm', ('NotebookLM', 'NotebookLM'), ('Ordenar documentación y consultarla con ayuda de IA.', 'Organising documentation and querying it with AI help.')),
    ('sk:sliders', ('Open Agent Manager', 'Open Agent Manager'), ('Seguir y coordinar varios agentes desde un mismo sitio.', 'Tracking and coordinating several agents from one place.')),
    ('sk:winai', ('Apps y webs con IA integrada', 'Apps and sites with built-in AI'), ('Funciones de IA en webs y apps.', 'AI features in sites and apps.')),
]
AREAS.remove(_ia)
AREAS.insert(0, _ia)

KEYS_ES, KEYS_EN = {}, {}
for ai, a in enumerate(AREAS):
    k = 'w%d' % ai
    KEYS_ES[k + '_tab'], KEYS_EN[k + '_tab'] = a['tab']
    KEYS_ES[k + '_t'], KEYS_EN[k + '_t'] = a['title']
    KEYS_ES[k + '_d'], KEYS_EN[k + '_d'] = a['desc']
    KEYS_ES[k + '_lead'], KEYS_EN[k + '_lead'] = a['lead']
    if 'learn_label' in a:
        KEYS_ES[k + '_ll'], KEYS_EN[k + '_ll'] = a['learn_label']
        KEYS_ES[k + '_tl'], KEYS_EN[k + '_tl'] = a['tools_label']
    for jj, lr in enumerate(a['learn']):
        KEYS_ES['%sl%d' % (k, jj)], KEYS_EN['%sl%d' % (k, jj)] = lr
    for ii, (_, name, desc) in enumerate(a['items']):
        KEYS_ES['%si%d_t' % (k, ii)], KEYS_EN['%si%d_t' % (k, ii)] = name
        KEYS_ES['%si%d_d' % (k, ii)], KEYS_EN['%si%d_d' % (k, ii)] = desc
KEYS_ES['wb_title'] = 'conocimientos'
KEYS_EN['wb_title'] = 'knowledge'
KEYS_ES['wb_learn'], KEYS_EN['wb_learn'] = 'Lo que he podido aprender', 'What I have been able to learn'
KEYS_ES['wb_tools'], KEYS_EN['wb_tools'] = 'Herramientas', 'Tools'
