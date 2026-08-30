<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { products } = useContent()
const { public: { siteUrl } } = useRuntimeConfig()
const route = useRoute()

const items = computed(() =>
  products.value.map((p) => ({
    slug: p.slug,
    icon: p.icon,
    name: p.name,
    subtitle: p.subtitle,
    description: p.description
  }))
)

useSeoMeta({
  title: () => `${t('nav.soluciones')} — Hamster Software`,
  ogTitle: () => `${t('nav.soluciones')} — Hamster Software`,
  description: () => t('solutionsSection.description'),
  ogDescription: () => t('solutionsSection.description')
})

// Datos estructurados: CollectionPage + BreadcrumbList
const indexSchema = computed(() => {
  const pageUrl = `${siteUrl}${route.path}`
  return {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'CollectionPage',
        '@id': `${pageUrl}#page`,
        name: t('nav.soluciones'),
        description: t('solutionsSection.description'),
        url: pageUrl,
        isPartOf: { '@type': 'WebSite', '@id': `${siteUrl}#website` }
      },
      {
        '@type': 'BreadcrumbList',
        '@id': `${pageUrl}#breadcrumb`,
        itemListElement: [
          { '@type': 'ListItem', position: 1, name: t('detail.breadcrumbHome'), item: siteUrl },
          { '@type': 'ListItem', position: 2, name: t('nav.soluciones'), item: pageUrl }
        ]
      }
    ]
  }
})

useHead(() => ({
  script: [{ type: 'application/ld+json', children: JSON.stringify(indexSchema.value) }]
}))
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden bg-ink-950 pt-24 pb-16 text-white sm:pt-28 sm:pb-20 lg:pt-32">
      <div class="pointer-events-none absolute inset-0 bg-grid-dark" />
      <div
        class="pointer-events-none absolute -right-20 -top-20 h-80 w-80 rounded-full bg-brand-600/20 blur-3xl"
      />
      <div class="container-site relative">
        <nav class="flex flex-wrap items-center gap-1.5 text-xs text-slate-400" aria-label="Breadcrumb">
          <NuxtLinkLocale to="/" class="transition-colors hover:text-brand-300">
            {{ t('detail.breadcrumbHome') }}
          </NuxtLinkLocale>
          <AppIcon name="chevron-right" class="h-3 w-3 text-slate-600" />
          <span class="font-medium text-slate-300">{{ t('nav.soluciones') }}</span>
        </nav>
        <div class="mt-8 max-w-2xl">
          <span class="eyebrow">{{ t('solutionsSection.eyebrow') }}</span>
          <h1 class="mt-5 font-display text-3xl font-bold tracking-tight sm:text-4xl lg:text-[2.75rem] lg:leading-[1.1]">
            {{ t('solutionsSection.title') }}
            <span class="text-gradient">{{ t('solutionsSection.titleHighlight') }}</span>
          </h1>
          <p class="mt-4 text-lg leading-relaxed text-slate-400">
            {{ t('solutionsSection.description') }}
          </p>
        </div>
      </div>
    </section>

    <!-- Grid -->
    <section class="bg-white py-16 sm:py-20">
      <div class="container-site">
        <ItemGrid :items="items" base-path="soluciones" />
      </div>
    </section>

    <!-- CTA -->
    <section class="relative overflow-hidden bg-ink-950 py-20 text-white sm:py-24">
      <div class="pointer-events-none absolute inset-0 bg-grid-dark" />
      <div
        class="pointer-events-none absolute -bottom-24 left-1/2 h-72 w-[36rem] -translate-x-1/2 rounded-full bg-brand-600/20 blur-3xl"
      />
      <div class="container-site relative mx-auto max-w-3xl text-center">
        <h2 class="font-display text-3xl font-bold tracking-tight sm:text-4xl">{{ t('detail.ctaTitle') }}</h2>
        <p class="mx-auto mt-4 max-w-xl text-slate-400">{{ t('detail.ctaText') }}</p>
        <div class="mt-9 flex flex-wrap items-center justify-center gap-3">
          <NuxtLinkLocale to="/#contacto" class="btn btn-white btn-lg">
            {{ t('detail.ctaPrimary') }}
            <AppIcon name="arrow-up-right" class="h-4 w-4" />
          </NuxtLinkLocale>
        </div>
      </div>
    </section>
  </div>
</template>
