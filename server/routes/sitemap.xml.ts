import es from '~~/i18n/locales/es.json'

export default defineEventHandler((event) => {
  setHeader(event, 'content-type', 'application/xml; charset=utf-8')

  const base = process.env.NUXT_PUBLIC_SITE_URL || 'https://hamstersoftware.com'

  const urls = new Set<string>()

  // Páginas raíz por idioma
  urls.add('/')
  urls.add('/en')

  // Índices de soluciones y servicios
  urls.add('/soluciones')
  urls.add('/en/soluciones')
  urls.add('/servicios')
  urls.add('/en/servicios')

  // Subpáginas de soluciones (slug común ES/EN)
  for (const p of es.products) {
    urls.add(`/soluciones/${p.slug}`)
    urls.add(`/en/soluciones/${p.slug}`)
  }

  // Subpáginas de servicios
  for (const s of es.services) {
    urls.add(`/servicios/${s.slug}`)
    urls.add(`/en/servicios/${s.slug}`)
  }

  const now = new Date().toISOString().slice(0, 10)

  const items = [...urls]
    .map(
      (path) =>
        `  <url><loc>${base}${path}</loc><lastmod>${now}</lastmod><changefreq>monthly</changefreq><priority>${path === '/' ? '1.0' : '0.8'}</priority></url>`
    )
    .join('\n')

  return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${items}\n</urlset>`
})
