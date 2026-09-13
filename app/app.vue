<script setup lang="ts">
const { locale } = useI18n()

// Head reactivo al idioma: canonical, og:locale y enlaces alternates
const localeHead = useLocaleHead({ addDirAttribute: true, addSeoAttributes: true })
const switchLocalePath = useSwitchLocalePath()

const { public: { siteUrl } } = useRuntimeConfig()

const localeOptions = [
  { code: 'es', iso: 'es-CO' },
  { code: 'en', iso: 'en-US' }
]

useHead(() => ({
  // `lang` se toma del locale actual directamente (robusto ante SSR/caché)
  htmlAttrs: { lang: locale.value, dir: 'ltr' },
  link: [
    ...(localeHead.value.link ?? []),
    // Alternates hreflang absolutos con el dominio propio (SEO multi-idioma)
    ...localeOptions.map((l) => ({
      rel: 'alternate',
      hreflang: l.code,
      href: `${siteUrl}${switchLocalePath(l.code) ?? ''}`
    }))
  ],
  meta: [...(localeHead.value.meta ?? [])]
}))

// Fallback sin JavaScript: muestra el contenido aunque IntersectionObserver no esté disponible
useHead({
  noscript: [{ innerHTML: '[data-reveal]{opacity:1!important;transform:none!important}' }]
})
</script>

<template>
  <div class="min-h-screen bg-white">
    <NuxtRouteAnnouncer />
    <AppHeader />
    <main>
      <NuxtPage />
    </main>
    <AppFooter />
    <ChatWidget />
    <ClientOnly>
      <ContextMenu />
    </ClientOnly>
  </div>
</template>
