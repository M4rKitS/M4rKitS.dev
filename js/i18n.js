/* Textos de la página actual.
   El diccionario del idioma viaja en el propio HTML como JSON (<script id="i18n">). */
const data = JSON.parse(document.getElementById('i18n').textContent);

export const lang = data.lang; // 'es' | 'en'
export const cfg = data.cfg; // rutas que dependen del idioma (política de privacidad, gracias)

export function tx(key) {
  return (data.t && data.t[key]) || '';
}
