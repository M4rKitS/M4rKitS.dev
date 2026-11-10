# Código fuente de la web

Las páginas HTML de la raíz del repositorio **se generan desde aquí**. Esta carpeta es la fuente; el resultado
(HTML, CSS y JS ya construidos) es lo que se sube a Cloudflare Pages.

## Qué hay

| Archivo | Para qué sirve |
| --- | --- |
| `site.py` | Construye la web completa: páginas en español y en inglés, `hreflang`, canónicas, sitemap, `robots.txt`, `_headers` y `_redirects`. |
| `d1.py` | Diseño: CSS y marcado de cada sección. |
| `common.py` | Textos en español e inglés (`ES` y `EN`), iconos y utilidades. |
| `legal.py` | Aviso legal, política de privacidad y de cookies, en los dos idiomas. |
| `wbdata.py` | Contenido de la ventana de conocimientos. |
| `motion.py` | CSS de la capa de movimiento. |
| `fonts.css` | `@font-face` de las tipografías, que se sirven desde la propia web. |
| `js/` | JavaScript, un módulo por función (ver abajo). |

## JavaScript

Cada página carga **un solo archivo de entrada** como módulo ES (`<script type="module">`), y ese archivo importa
solo lo que la página necesita:

- `home.js`: portfolio.
- `web.js`: desarrollo web (formulario, proyectos, planes).
- `basic.js`: avisos legales, gracias y 404.

Cada módulo exporta una función `init…()` que solo actúa si encuentra su elemento en la página:
`nav.js` (menú, sección activa y enlaces ancla), `theme.js` (modo claro y oscuro), `lang-switch.js`,
`workbench.js`, `certs.js`, `projects.js`, `contact-form.js` (EmailJS y WhatsApp), `cards.js`, `plans.js`,
`shine.js`, `scroll-top.js` y `motion.js` (GSAP, que se carga después de `load`).

`i18n.js` lee del HTML el diccionario del idioma (un bloque JSON con `id="i18n"`) y ofrece `tx(clave)`.
Los textos no están en el JS: viajan como datos en cada página.

Al construir, la versión del JS (un hash de su contenido) se añade a la URL de cada módulo
(`/js/home.js?v=…`), por eso `_headers` puede darles caché de un año: cuando cambian, cambia la URL.

## Construir

Hace falta Python 3 (sin dependencias). Los recursos (`img/`, `fonts/`, `vendor/`) se leen de la raíz del repositorio.

```bash
python3 src/site.py /ruta/de/salida
```

La carpeta de salida se **vacía y se vuelve a crear**, así que no uses la raíz del repositorio como destino.
Para publicar, se copia la salida sobre la raíz y se hace commit.

## Lo que no está aquí

Las fotos originales y los PDF de los certificados no se suben. Las versiones ya optimizadas que usa la web
están en `img/`.
