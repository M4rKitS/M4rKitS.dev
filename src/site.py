# -*- coding: utf-8 -*-
"""Genera la web real (ES en / y EN en /en/) a partir de los mismos bloques de las propuestas.
Uso: python3 site.py <carpeta_de_salida>"""
import sys, os, re, json, hashlib, shutil, html as _h

import common
import d1
import legal
import motion
from common import ES, EN

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # raíz del repositorio: de aquí salen img/, fonts/ y vendor/
SRC = ROOT
SITE = 'https://m4rkits.dev'

URLS = {
    'home': ('/', '/en/'),
    'web': ('/desarrollo-web/', '/en/web-development/'),
    'aviso': ('/aviso-legal/', '/en/legal-notice/'),
    'priv': ('/privacidad/', '/en/privacy/'),
    'cook': ('/cookies/', '/en/cookies/'),
    'gracias': ('/gracias/', '/en/thanks/'),
}
TOKENS = [('web', '1-aire-web-development.html'), ('aviso', '1-aire-aviso-legal.html'), ('priv', '1-aire-privacidad.html'),
          ('cook', '1-aire-cookies.html'), ('gracias', '1-aire-gracias.html'), ('home', '1-aire.html')]

# Textos que las propuestas llevan solo en castellano dentro del marcado (se traducen en las paginas en ingles)
EN_LITERALS = [
    ('aria-label="Principal"', 'aria-label="Main"'), ('aria-label="Idioma"', 'aria-label="Language"'),
    ('aria-label="Abrir menú"', 'aria-label="Open menu"'), ('aria-label="Activar modo oscuro"', 'aria-label="Switch to dark mode"'),
    ('title="Activar modo oscuro"', 'title="Switch to dark mode"'), ('<span class="th-t">Modo oscuro</span>', '<span class="th-t">Dark mode</span>'),
    ('aria-label="Legal"', 'aria-label="Legal"'), ('aria-label="Español"', 'aria-label="Español"'),
    ('alt="Retrato de Marcos Rodríguez sonriendo"', 'alt="Portrait of Marcos Rodríguez smiling"'),
    ('alt="Catedral de Helsinki"', 'alt="Helsinki Cathedral"'),
    ('alt="Marcos Rodríguez sentado ante su portátil en su escritorio"', 'alt="Marcos Rodríguez sitting at his laptop on his desk"'),
    ('aria-label="Tecnologías"', 'aria-label="Technologies"'),
    ('alt="Marcos Rodríguez trabajando concentrado ante su portátil"', 'alt="Marcos Rodríguez working, focused at his laptop"'),
    ('alt="Retrato de Marcos Rodríguez con los brazos cruzados"', 'alt="Portrait of Marcos Rodríguez with his arms crossed"'),
    ('$ cd mi-proyecto &amp;&amp; code .', '$ cd my-project &amp;&amp; code .'), ('$ cd mi-proyecto && code .', '$ cd my-project && code .'),
    ('def hola(): print(&quot;Hola&quot;)', 'def hello(): print(&quot;Hello&quot;)'), ('def hola(): print("Hola")', 'def hello(): print("Hello")'),
    ('SELECT nombre FROM alumnos;', 'SELECT name FROM students;'),
    ('&gt; resume esta documentación', '&gt; summarize this documentation'), ('> resume esta documentación', '> summarize this documentation'),
]
OG_ALT = {'home': ('Marcos Rodríguez, desarrollador de software Full Stack', 'Marcos Rodríguez, Full Stack software developer'),
          'web': ('M4rKitS.dev, desarrollo web para pequeños negocios', 'M4rKitS.dev, web development for small businesses')}

JSONLD = {
    'home': lambda lang: {
        '@context': 'https://schema.org', '@type': 'ProfilePage', 'url': SITE + URLS['home'][lang == 'en'], 'inLanguage': lang,
        'mainEntity': {
            '@type': 'Person', 'name': 'Marcos Rodríguez', 'alternateName': 'M4rKitS',
            'jobTitle': 'Full Stack software developer (in training)' if lang == 'en' else 'Desarrollador de software Full Stack en formación',
            'url': SITE + '/', 'email': 'contact@m4rkits.dev',
            'address': {'@type': 'PostalAddress', 'addressLocality': 'Vantaa', 'addressCountry': 'FI'},
            'knowsLanguage': ['es', 'en'],
            'knowsAbout': ['Python', 'SQL', 'Git', 'GitHub', 'Linux', 'Web development', 'AI agents and automation', 'n8n'],
            'sameAs': ['https://github.com/M4rKitS', 'https://www.linkedin.com/in/mrodriguezhdz', 'https://www.instagram.com/m4rkits.dev/']}},
    'web': lambda lang: {
        '@context': 'https://schema.org', '@type': 'ProfessionalService', 'name': 'M4rKitS.dev',
        'url': SITE + URLS['web'][lang == 'en'], 'inLanguage': lang, 'email': 'contact@m4rkits.dev',
        'description': 'Web design and development for small businesses.' if lang == 'en' else 'Diseño y desarrollo web para pequeños negocios.',
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Vantaa', 'addressCountry': 'FI'},
        'availableLanguage': ['es', 'en'], 'serviceType': 'Web design and development',
        'founder': {'@type': 'Person', 'name': 'Marcos Rodríguez'},
        'sameAs': ['https://github.com/M4rKitS', 'https://www.linkedin.com/in/mrodriguezhdz', 'https://www.instagram.com/m4rkits.dev/']},
}

def absolutize(h):
    h = re.sub(r'(?<![\w/.\-])(img|fonts|vendor)/', r'/\1/', h)
    return h


def url_tokens(h, lang):
    i = 1 if lang == 'en' else 0
    for k, tok in TOKENS:
        h = h.replace(tok, URLS[k][i])
    return h


JS_V = ''
JS_DEPS = {}


def build_js(outdir):
    """Copia src/js a la salida. La versión (hash del contenido) va en la URL de cada módulo,
    así el navegador puede guardarlos para siempre y se renuevan solos cuando cambian."""
    global JS_V
    jsdir = HERE + '/js'
    files = sorted(f for f in os.listdir(jsdir) if f.endswith('.js'))
    h = hashlib.sha1()
    for f in files:
        h.update(open(jsdir + '/' + f, 'rb').read())
    JS_V = h.hexdigest()[:8]
    JS_DEPS.clear()
    for f in files:
        # módulos que necesita cada archivo (también los de segundo nivel), para precargarlos todos a la vez
        seen, todo = [], [f]
        while todo:
            cur = todo.pop(0)
            for m in re.findall(r"from '\./([\w\-]+\.js)'", open(jsdir + '/' + cur, encoding='utf-8').read()):
                if m not in seen:
                    seen.append(m); todo.append(m)
        JS_DEPS[f] = seen
    os.makedirs(outdir + '/js')
    for f in files:
        code = open(jsdir + '/' + f, encoding='utf-8').read()
        code = re.sub(r"(from '\./[\w\-]+\.js)'", r"\1?v=%s'" % JS_V, code)
        open(outdir + '/js/' + f, 'w', encoding='utf-8').write(code)


def build_css():
    fonts = open(HERE + '/fonts.css', encoding='utf-8').read().replace('url(', 'url(/fonts/')
    css = fonts + common.COMMON_CSS + d1.full_css()
    css = re.sub(r'(?<![\w/.\-])(img)/', r'/\1/', css)
    return css


def head(lang, key, meta, noindex=False):
    d = ES  # el diccionario activo (ya intercambiado para EN)
    t = _h.escape(d[meta['t']], quote=True)
    ds = _h.escape(d[meta['d']], quote=True)
    es_u, en_u = SITE + URLS[key][0], SITE + URLS[key][1]
    self_u = en_u if lang == 'en' else es_u
    img = meta['img']
    alt = _h.escape(OG_ALT[key][1] if (lang == 'en' and key in OG_ALT) else meta['alt'], quote=True)
    loc, loc_alt = ('en_GB', 'es_ES') if lang == 'en' else ('es_ES', 'en_GB')
    hl = ''
    if not noindex:
        hl = ('<link rel="alternate" hreflang="es" href="%s">\n<link rel="alternate" hreflang="en" href="%s">\n'
              '<link rel="alternate" hreflang="x-default" href="%s">\n') % (es_u, en_u, es_u)
    ld = ''
    if key in JSONLD:
        ld = '<script type="application/ld+json">' + json.dumps(JSONLD[key](lang), ensure_ascii=False, separators=(',', ':')) + '</script>\n'
    return ('<title>%s</title>\n<meta name="description" content="%s">\n'
            '<meta name="robots" content="%s">\n<link rel="canonical" href="%s">\n%s'
            '<meta property="og:type" content="website">\n<meta property="og:site_name" content="M4rKitS.dev">\n'
            '<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n'
            '<meta property="og:image" content="%s">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
            '<meta property="og:image:alt" content="%s">\n<meta property="og:locale" content="%s">\n<meta property="og:locale:alternate" content="%s">\n'
            '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="%s">\n'
            '<meta name="twitter:description" content="%s">\n<meta name="twitter:image" content="%s">\n%s') % (
        t, ds, 'noindex, follow' if noindex else 'index, follow', self_u, hl, t, ds, self_u, img, alt, loc, loc_alt, t, ds, img, ld)


def render(lang, key, cap, css_name, noindex=False):
    meta = cap['meta']
    i = 1 if lang == 'en' else 0
    hd = head(lang, key, meta, noindex)
    alt_url = URLS[key][1 - i]
    dict_now = dict(ES)
    # Diccionario del idioma y rutas que dependen del idioma: datos en JSON, no código
    data = {'lang': lang, 'cfg': {'priv': URLS['priv'][i].lstrip('/'), 'thanks': URLS['gracias'][i]}, 't': dict_now}
    i18n = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    entry = cap['extra_js']
    preload = ''.join('<link rel="modulepreload" href="/js/%s?v=%s">\n' % (m, JS_V) for m in JS_DEPS[entry + '.js'])
    scripts = ('<script type="application/json" id="i18n">%s</script>\n'
               '<script type="module" src="/js/%s.js?v=%s"></script>') % (i18n, entry, JS_V)
    body = common.optimize_imgs(cap['body'])
    body = re.sub(r'(data-t="(\w+)"[^>]*>)([^<]*)(<)', lambda m: m.group(1) + (ES[m.group(2)] if (m.group(2) in ES and '<' not in ES[m.group(2)]) else m.group(3)) + m.group(4), body)
    es_href, en_href = URLS[key][0], URLS[key][1]
    body = body.replace('data-l="es"', 'data-l="es" data-href="%s"' % es_href).replace('data-l="en"', 'data-l="en" data-href="%s"' % en_href)
    body = body.replace('<span>m4rkits.dev/web-development</span>', '<span>m4rkits.dev/%s</span>' % ('en/web-development' if lang == 'en' else 'desarrollo-web'))
    if lang == 'en':
        for a, b in EN_LITERALS:
            body = body.replace(a, b)
    motion_head = ''
    if key in ('home', 'web'):
        motion_head = '<style>' + motion.MOTION_CSS + '</style>\n'
    out = ('<!DOCTYPE html>\n<html lang="%s">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n%s'
           '<link rel="icon" href="/img/favicon.ico" sizes="any">\n<link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48.png">\n'
           '<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">\n<link rel="icon" type="image/png" sizes="192x192" href="/img/icon-192.png">\n'
           '<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">\n<meta name="theme-color" content="#DAE1EB">\n'
           "<script>try{if(localStorage.getItem('prop_theme')==='dark'){document.documentElement.setAttribute('data-theme','dark')}}catch(e){}</script>\n"
           '<link rel="preload" href="/fonts/barlow-normal-latin-400.woff2" as="font" type="font/woff2" crossorigin>\n'
           '<link rel="preload" href="/fonts/barlow-normal-latin-600.woff2" as="font" type="font/woff2" crossorigin>\n'
           '<link rel="stylesheet" href="/css/%s">\n%s%s</head>\n<body>\n%s\n%s\n</body>\n</html>\n') % (
        lang, hd, css_name, preload, motion_head, body, scripts)
    out = out.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">', 1)
    out = url_tokens(out, lang)
    out = absolutize(out)
    return out


def static_files(outdir, css_name, pages):
    # 1) copiar solo los recursos que usan las paginas
    used = set()
    texts = [open(p, encoding='utf-8').read() for _, _, p in pages] + [open(outdir + '/css/' + css_name, encoding='utf-8').read()]
    texts += [open(outdir + '/js/' + f, encoding='utf-8').read() for f in os.listdir(outdir + '/js')]
    for t in texts:
        for m in re.finditer(r'/(img|fonts|vendor)/[A-Za-z0-9_./\-]+\.(?:png|jpg|jpeg|webp|svg|ico|avif|woff2|js)', t):
            used.add(m.group(0))
    used.add('/img/og-portfolio.png'); used.add('/img/og-web.png')
    for f in os.listdir(SRC + '/img'):
        if f.startswith('cert-') and f.endswith('.webp'):
            used.add('/img/' + f)  # se piden por JavaScript al abrir un certificado
    missing = []
    for u in sorted(used):
        src = SRC + u
        if not os.path.exists(src):
            missing.append(u); continue
        dst = outdir + u
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(src, dst)
    shutil.copy(SRC + '/img/favicon.ico', outdir + '/favicon.ico')
    # 2) sitemap con alternativas de idioma
    idx = [k for k in ('home', 'web', 'aviso', 'priv', 'cook')]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for k in idx:
        es_u, en_u = SITE + URLS[k][0], SITE + URLS[k][1]
        for loc in (es_u, en_u):
            pr = '1.0' if k == 'home' and loc == es_u else ('0.9' if k == 'home' else ('0.8' if k == 'web' else '0.3'))
            xml.append('  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority>'
                       '<xhtml:link rel="alternate" hreflang="es" href="%s"/><xhtml:link rel="alternate" hreflang="en" href="%s"/>'
                       '<xhtml:link rel="alternate" hreflang="x-default" href="%s"/></url>' % (loc, LASTMOD.get(k, LASTMOD_DEFAULT), pr, es_u, en_u, es_u))
    xml.append('</urlset>')
    open(outdir + '/sitemap.xml', 'w', encoding='utf-8').write('\n'.join(xml) + '\n')
    open(outdir + '/robots.txt', 'w', encoding='utf-8').write('User-agent: *\nAllow: /\nDisallow: /cdn-cgi/\n\nSitemap: https://m4rkits.dev/sitemap.xml\n')
    open(outdir + '/llms.txt', 'w', encoding='utf-8').write(LLMS)
    open(outdir + '/_headers', 'w', encoding='utf-8').write(HEADERS)
    open(outdir + '/_redirects', 'w', encoding='utf-8').write(REDIRECTS)
    return missing


LLMS = """# M4rKitS.dev

> Marcos Rodríguez (M4rKitS) is a Full Stack software developer in training based in Vantaa, Finland. He studies the Full Stack master at Conquer Blocks and builds clear, fast websites for small businesses in Spanish and English.

The site has two sections, each available in Spanish and in English:

- [Portfolio](https://m4rkits.dev/): his training (master modules, certificates) and where he is heading.
- [Web development](https://m4rkits.dev/desarrollo-web/): the website service for small businesses, project examples and a contact form.
- [Portfolio in English](https://m4rkits.dev/en/) and [web development in English](https://m4rkits.dev/en/web-development/).

## Links

- [GitHub](https://github.com/M4rKitS)
- [LinkedIn](https://www.linkedin.com/in/mrodriguezhdz)
- Email: contact@m4rkits.dev
- Languages: Spanish and English

## Legal

- [Legal notice](https://m4rkits.dev/en/legal-notice/), [Privacy policy](https://m4rkits.dev/en/privacy/), [Cookie policy](https://m4rkits.dev/en/cookies/)
"""

HEADERS = """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()
  Content-Security-Policy: frame-ancestors 'self'

/css/*
  Cache-Control: public, max-age=31536000, immutable

/js/*
  Cache-Control: public, max-age=31536000, immutable

/fonts/*
  Cache-Control: public, max-age=31536000, immutable

/img/*
  Cache-Control: public, max-age=2592000

/vendor/*
  Cache-Control: public, max-age=2592000
"""

# Fecha de la última modificación de cada página (formato AAAA-MM-DD). Se actualiza al cambiar el contenido de esa página.
LASTMOD_DEFAULT = '2026-11-05'
LASTMOD = {'home': '2026-11-10', 'web': '2026-11-10'}

REDIRECTS = """https://m4rkits.pages.dev/* https://m4rkits.dev/:splat 301
/index.html / 301
/gracias.html /gracias/ 301
/web-development /desarrollo-web/ 301
/web-development/ /desarrollo-web/ 301
/web-development/index.html /desarrollo-web/ 301
/tbh /desarrollo-web/ 301
/tbh/ /desarrollo-web/ 301
/tbh.html /desarrollo-web/ 301
"""


def main(outdir):
    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir)
    build_js(outdir)
    css = build_css()
    css_name = 'site.%s.css' % hashlib.sha1(css.encode('utf-8')).hexdigest()[:8]
    os.makedirs(outdir + '/css')
    open(outdir + '/css/' + css_name, 'w', encoding='utf-8').write(css)
    for dct in (ES, common.EN):
        for k in ('m_kicker', 'k_kicker', 'p_kicker', 'w_eyebrow'):
            dct.pop(k, None)
    es_orig = dict(ES)
    pages = []
    for lang in ('es', 'en'):
        ES.clear(); ES.update(es_orig)
        d1.ONLY_LANG = lang
        if lang == 'en':
            ES.update(common.EN)
        builders = [('home', d1.build_home), ('web', d1.build_web), ('aviso', lambda: d1.build_legal('aviso')),
                    ('priv', lambda: d1.build_legal('priv')), ('cook', lambda: d1.build_legal('cook')), ('gracias', d1.build_gracias)]
        for key, fn in builders:
            cap = fn()
            if lang == 'en' and key in ('aviso', 'priv', 'cook'):
                pass
            noindex = key == 'gracias'
            out = render(lang, key, cap, css_name, noindex)
            p = URLS[key][1 if lang == 'en' else 0]
            path = outdir + p + 'index.html'
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, 'w', encoding='utf-8').write(out)
            pages.append((lang, key, path))
    # pagina 404 real (evita que Pages sirva index.html con 200 para rutas inexistentes)
    ES.clear(); ES.update(es_orig); d1.ONLY_LANG = None
    cap = d1.build_notfound()
    h404 = render('es', 'gracias', cap, css_name, True)
    h404 = re.sub(r'<link rel="canonical"[^>]*>\n', '', h404)
    h404 = re.sub(r'<meta property="og:url"[^>]*>\n', '', h404)
    h404 = h404.replace('data-href="/gracias/"', 'data-href="/"').replace('data-href="/en/thanks/"', 'data-href="/en/"')
    open(outdir + '/404.html', 'w', encoding='utf-8').write(h404)
    pages.append(('es', '404', outdir + '/404.html'))
    ES.clear(); ES.update(es_orig)
    miss = static_files(outdir, css_name, pages)
    if miss:
        print('FALTAN', miss)
    return css_name, pages


if __name__ == '__main__':
    css_name, pages = main(sys.argv[1])
    print('ok', css_name, len(pages), 'paginas')
