/**
 * Content Security Policy con nonces por request.
 *
 * Nuxt renderiza scripts inline (importmap, payload __NUXT__, data-nuxt-data).
 * En lugar de usar 'unsafe-inline' (que desactiva la protección) generamos un
 * nonce criptográfico por cada petición, lo inyectamos en esos scripts inline
 * y lo referenciamos en el header CSP. Nunca se usa 'unsafe-eval'.
 *
 * Fuentes permitidas:
 *  - script-src:  self + nonce (no unsafe-eval)
 *  - style-src:   self + unsafe-inline (estilos inline de Tailwind/atributos) + Google Fonts CSS
 *  - font-src:    self + fonts.gstatic.com (archivos de fuentes de Google)
 *  - img-src:     self + data: (favicon SVG inline / data URIs)
 *  - connect-src: self
 *
 * Nota: usamos Web Crypto API nativa (crypto.getRandomValues) en lugar de
 * node:crypto para compatibilidad directa con el runtime de Cloudflare Workers.
 */
export default defineNitroPlugin((nitroApp) => {
  nitroApp.hooks.hook('render:html', (htmlContext, { event }) => {
    if (import.meta.prerender) {
      return
    }

    // Web Crypto API — disponible de forma nativa en Cloudflare Workers
    const nonceBytes = new Uint8Array(16)
    crypto.getRandomValues(nonceBytes)
    const nonce = btoa(String.fromCharCode(...nonceBytes))

    const applyNonce = (chunks: string[]): string[] =>
      chunks.map((chunk) =>
        chunk.replace(/<script(?![^>]*\ssrc\s*=)(?![^>]*\snonce\s*=)/g, (m) => `${m} nonce="${nonce}"`)
      )

    htmlContext.head = applyNonce(htmlContext.head)
    htmlContext.bodyPrepend = applyNonce(htmlContext.bodyPrepend)
    htmlContext.body = applyNonce(htmlContext.body)
    htmlContext.bodyAppend = applyNonce(htmlContext.bodyAppend)



    setHeader(
      event,
      'Content-Security-Policy',
      [
        "default-src 'self'",
        `script-src 'self' 'nonce-${nonce}'`,
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
        "font-src 'self' https://fonts.gstatic.com data:",
        "img-src 'self' data:",
        "media-src 'self'",
        "connect-src 'self'",
        "object-src 'none'",
        "base-uri 'self'",
        "form-action 'self'",
        "frame-ancestors 'self'"
      ].join('; ')
    )
  })

  nitroApp.hooks.hook('render:response', (response) => {
    if (typeof response.body === 'string' && response.body.includes('<!DOCTYPE html>')) {
      const asciiBanner = `<!--
██╗  ██╗ █████╗ ███╗   ███╗███████╗████████╗███████╗██████╗     ███████╗ ██████╗ ███████╗████████╗██╗    ██╗ █████╗ ██████╗ ███████╗
██║  ██║██╔══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██╔════╝╚══██╔══╝██║    ██║██╔══██╗██╔══██╗██╔════╝
███████║███████║██╔████╔██║███████╗   ██║   █████╗  ██████╔╝    ███████╗██║   ██║█████╗     ██║   ██║ █╗ ██║███████║██████╔╝█████╗  
██╔══██║██╔══██║██║╚██╔╝██║╚════██║   ██║   ██╔══╝  ██╔══██╗    ╚════██║██║   ██║██╔══╝     ██║   ██║███╗██║██╔══██║██╔══██╗██╔══╝  
██║  ██║██║  ██║██║ ╚═╝ ██║███████║   ██║   ███████╗██║  ██║    ███████║╚██████╔╝██║        ██║   ╚███╔███╔╝██║  ██║██║  ██║███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝        ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
-->\n`
      response.body = asciiBanner + response.body
    }
  })
})
