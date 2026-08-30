// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@nuxtjs/i18n'],
  nitro: {
    preset: 'cloudflare-pages'
  },
  css: ['~/assets/css/main.css'],
  tailwindcss: {
    cssPath: '~/assets/css/main.css'
  },
  routeRules: {
    // Google Cloud CDN: solo se cachean assets estáticos. El HTML queda
    // dinámico (SSR) para conservar el nonce CSP por petición.
    //
    // Los archivos bajo /_nuxt/ llevan hash de contenido: TTL máximo e inmutable.
    '/_nuxt/**': { headers: { 'Cache-Control': 'public, max-age=31536000, immutable' } },
    '/images/**': { headers: { 'Cache-Control': 'public, max-age=31536000, immutable' } },
    '/favicon.svg': { headers: { 'Cache-Control': 'public, max-age=31536000, immutable' } },
    '/favicon.ico': { headers: { 'Cache-Control': 'public, max-age=31536000, immutable' } },
    // Archivos que cambian con poca frecuencia: un día en la CDN (s-maxage).
    '/robots.txt': { headers: { 'Cache-Control': 'public, max-age=3600, s-maxage=86400' } },
    '/sitemap.xml': { headers: { 'Cache-Control': 'public, max-age=3600, s-maxage=86400' } },
    // El chat es POST (Cloud CDN nunca cachea POST); no-store como red de seguridad.
    '/api/chat': { headers: { 'Cache-Control': 'no-store' } }
  },
  runtimeConfig: {
    // Cloudflare Workers AI — privado, solo se usa en el servidor (Nitro)
    // En Cloudflare Pages los secrets se inyectan como env vars del Worker
    cloudflareApiToken: process.env.CLOUDFLARE_API_TOKEN || '',
    cloudflareAccountId: process.env.CLOUDFLARE_ACCOUNT_ID || '',
    public: {
      // URL base del sitio en producción (para canonical y hreflang absolutos)
      siteUrl: process.env.NUXT_PUBLIC_SITE_URL || 'https://hamstersoftware.com'
    }
  },
  i18n: {
    strategy: 'prefix_except_default',
    defaultLocale: 'es',
    detectBrowserLanguage: false,
    // baseUrl: genera canonical y hreflang absolutos con el dominio propio
    baseUrl: process.env.NUXT_PUBLIC_SITE_URL || 'https://hamstersoftware.com',
    // Desactivar el caché de respuestas SSR: podía servir HTML de un idioma
    // cuando se pedía el otro, mezclando idiomas en la misma página.
    experimental: {
      httpCacheDuration: 0
    },
    langDir: 'locales',
    locales: [
      { code: 'es', language: 'es-CO', file: 'es.json', name: 'Español' },
      { code: 'en', language: 'en-US', file: 'en.json', name: 'English' }
    ]
  },
  app: {
    head: {
      title: 'Hamster Software — Soluciones de datos a tu medida | Popayán, Colombia',
      meta: [
        {
          name: 'description',
          content:
            'En Popayán transformamos datos en decisiones inteligentes: pipelines de datos, machine learning, desarrollo web y móvil, ciberseguridad y más. +50 proyectos entregados.'
        },
        { name: 'theme-color', content: '#2563eb' }
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap'
        }
      ]
    }
  }
})
