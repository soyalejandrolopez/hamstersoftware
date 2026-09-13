<script setup lang="ts">
import type { Product, Service } from '~/types/content'
import { company } from '~/data/config'
import { useContent } from '~/composables/useContent'

const props = defineProps<{
  item: Product | Service
  kind: 'product' | 'service'
}>()

const { t } = useI18n()
const { products, services } = useContent()
const { public: { siteUrl } } = useRuntimeConfig()
const route = useRoute()

const basePath = computed(() => (props.kind === 'product' ? 'soluciones' : 'servicios'))
const isProduct = computed(() => props.kind === 'product')

const imageSrc = computed(() => {
  return props.item.image || `/images/${basePath.value}/${props.item.slug}.jpg`
})

const title = computed(() => ('name' in props.item ? props.item.name : props.item.title))
const subtitle = computed(() =>
  'subtitle' in props.item ? props.item.subtitle : props.item.description
)

const parentLabel = computed(() => t(isProduct.value ? 'nav.soluciones' : 'nav.servicios'))

const relatedTitle = computed(() =>
  t(isProduct.value ? 'detail.relatedProducts' : 'detail.relatedServices')
)
const viewAllLabel = computed(() =>
  t(isProduct.value ? 'detail.viewAllProducts' : 'detail.viewAllServices')
)

const related = computed(() => {
  const all = isProduct.value ? products.value : services.value
  return all
    .filter((x) => x.slug !== props.item.slug)
    .slice(0, 6)
    .map((x) => ({
      slug: x.slug,
      icon: x.icon,
      name: 'name' in x ? x.name : x.title,
      subtitle: 'subtitle' in x ? x.subtitle : x.description
    }))
})

const whatsappHref = computed(() => {
  const text = `${t('contact.whatsappGreeting', { name: company.name })}\n\n${title.value}`
  return `https://wa.me/${company.whatsappNumber}?text=${encodeURIComponent(text)}`
})

useSeoMeta({
  title: () => `${title.value} — Hamster Software`,
  ogTitle: () => `${title.value} — Hamster Software`,
  description: () => props.item.description,
  ogDescription: () => props.item.description
})

// Datos estructurados: Service/Product + BreadcrumbList + FAQPage
const schema = computed(() => {
  const pageUrl = `${siteUrl}${route.path}`
  const graph: Record<string, unknown>[] = [
    {
      '@type': props.kind === 'product' ? 'Product' : 'Service',
      '@id': `${pageUrl}#item`,
      name: title.value,
      description: props.item.description,
      url: pageUrl,
      image: { '@type': 'ImageObject', url: `${siteUrl}/favicon.svg` },
      provider: {
        '@type': 'Organization',
        name: 'Hamster Software',
        url: siteUrl
      },
      areaServed: 'CO'
    },
    {
      '@type': 'BreadcrumbList',
      '@id': `${pageUrl}#breadcrumb`,
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: t('detail.breadcrumbHome'), item: siteUrl },
        {
          '@type': 'ListItem',
          position: 2,
          name: parentLabel.value,
          item: `${siteUrl}/${basePath.value}`
        },
        { '@type': 'ListItem', position: 3, name: title.value, item: pageUrl }
      ]
    }
  ]

  if (props.item.faq?.length) {
    graph.push({
      '@type': 'FAQPage',
      '@id': `${pageUrl}#faq`,
      mainEntity: props.item.faq.map((f) => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: { '@type': 'Answer', text: f.a }
      }))
    })
  }

  return {
    '@context': 'https://schema.org',
    '@graph': graph
  }
})

useHead(() => ({
  script: [{ type: 'application/ld+json', children: JSON.stringify(schema.value) }]
}))
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden bg-ink-950 pt-24 pb-16 text-white sm:pt-28 sm:pb-20 lg:pt-32">
      <div class="pointer-events-none absolute inset-0 bg-grid-dark opacity-35" />
      <div
        class="pointer-events-none absolute -right-20 -top-20 h-80 w-80 rounded-full bg-brand-600/25 blur-3xl"
      />

      <div class="container-site relative">
        <!-- Breadcrumb -->
        <nav class="flex flex-wrap items-center gap-1.5 text-xs text-slate-400" aria-label="Breadcrumb">
          <NuxtLinkLocale to="/" class="transition-colors hover:text-brand-300">
            {{ t('detail.breadcrumbHome') }}
          </NuxtLinkLocale>
          <AppIcon name="chevron-right" class="h-3 w-3 text-slate-600" />
          <NuxtLinkLocale :to="`/${basePath}`" class="transition-colors hover:text-brand-300">
            {{ parentLabel }}
          </NuxtLinkLocale>
          <AppIcon name="chevron-right" class="h-3 w-3 text-slate-600" />
          <span class="font-medium text-slate-300">{{ title }}</span>
        </nav>

        <div class="mt-8 flex flex-col gap-8 lg:flex-row lg:items-center lg:justify-between">
          <div class="max-w-2xl">
            <span
              class="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-brand-500 to-indigo-700 text-white shadow-relief-btn-primary"
            >
              <AppIcon :name="item.icon" class="h-7 w-7 drop-shadow" />
            </span>
            <h1 class="mt-6 font-display text-3xl font-bold tracking-tight sm:text-4xl lg:text-[2.85rem] lg:leading-[1.1]">
              {{ title }}
            </h1>
            <p class="mt-3 text-base font-semibold text-brand-300 sm:text-lg">{{ subtitle }}</p>
            <p class="mt-4 max-w-xl leading-relaxed text-slate-300">{{ item.overview }}</p>

            <div class="mt-8 flex flex-wrap gap-3.5">
              <a :href="whatsappHref" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
                <AppIcon name="whatsapp" class="h-4 w-4" />
                {{ t('detail.ctaWhatsapp') }}
              </a>
              <NuxtLinkLocale to="/#contacto" class="btn btn-white btn-lg">
                {{ t('detail.ctaPrimary') }}
                <AppIcon name="arrow-up-right" class="h-4 w-4" />
              </NuxtLinkLocale>
            </div>
          </div>

          <!-- Showcase visual with realistic relief & glassmorphism -->
          <div class="relative w-full max-w-lg lg:max-w-md xl:max-w-lg">
            <div
              class="relative overflow-hidden rounded-3xl border border-white/20 bg-slate-900/80 p-2 shadow-[0_25px_60px_-15px_rgba(0,0,0,0.7),inset_0_1px_0_rgba(255,255,255,0.2)] backdrop-blur-xl transition-transform duration-500 hover:scale-[1.02]"
            >
              <!-- Browser / window top header -->
              <div class="flex items-center justify-between border-b border-white/10 bg-slate-950/60 px-4 py-2.5 rounded-t-2xl">
                <div class="flex items-center gap-1.5">
                  <span class="h-2.5 w-2.5 rounded-full bg-rose-500/90 shadow-sm" />
                  <span class="h-2.5 w-2.5 rounded-full bg-amber-500/90 shadow-sm" />
                  <span class="h-2.5 w-2.5 rounded-full bg-emerald-500/90 shadow-sm" />
                </div>
                <div class="flex items-center gap-1.5 rounded-md bg-white/5 px-2.5 py-0.5 text-[10px] font-mono text-slate-400 border border-white/5">
                  <AppIcon name="lock" class="h-2.5 w-2.5 text-emerald-400" />
                  <span>hamstersoftware.com/{{ basePath }}/{{ item.slug }}</span>
                </div>
              </div>

              <!-- Main showcase photo -->
              <div class="relative aspect-[16/10] w-full overflow-hidden rounded-b-2xl bg-slate-950">
                <img
                  :src="imageSrc"
                  :alt="title"
                  class="h-full w-full object-cover object-center transition-transform duration-700 hover:scale-105"
                  loading="eager"
                />
                <div class="pointer-events-none absolute inset-0 bg-gradient-to-t from-slate-950/70 via-transparent to-transparent" />
                
                <!-- Floating badge on the image -->
                <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between gap-2 rounded-xl border border-white/15 bg-ink-950/85 p-2.5 backdrop-blur-md shadow-relief-dark">
                  <div class="flex items-center gap-2">
                    <span class="flex h-7 w-7 items-center justify-center rounded-lg bg-brand-600 text-white shadow-sm">
                      <AppIcon :name="item.icon" class="h-4 w-4" />
                    </span>
                    <span class="font-display text-xs font-bold text-white truncate max-w-[180px] sm:max-w-[220px]">
                      {{ title }}
                    </span>
                  </div>
                  <span class="inline-flex items-center gap-1 rounded-full bg-emerald-500/20 px-2 py-0.5 text-[10px] font-semibold text-emerald-300">
                    <span class="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse" />
                    {{ isProduct ? 'Solución Lista' : 'Servicio Activo' }}
                  </span>
                </div>
              </div>
            </div>

            <!-- Mini stats/benefits overlay pill below image -->
            <div class="mt-4 grid grid-cols-2 gap-3">
              <div
                v-for="(b, i) in item.benefits.slice(0, 2)"
                :key="i"
                class="flex items-center gap-2.5 rounded-2xl border border-white/10 bg-white/[0.04] p-3 shadow-relief-dark backdrop-blur-md"
              >
                <span class="flex h-8 w-8 shrink-0 items-center justify-center rounded-xl bg-brand-500/20 text-brand-400">
                  <AppIcon :name="b.icon" class="h-4 w-4" />
                </span>
                <span class="text-xs font-bold text-slate-200 line-clamp-1">{{ b.title }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Qué incluye -->
    <section class="bg-white py-16 sm:py-20">
      <div class="container-site grid gap-12 lg:grid-cols-2 lg:items-start">
        <div>
          <span class="eyebrow">{{ parentLabel }}</span>
          <h2 class="section-title mt-5">
            {{ t('detail.featuresTitle') }}
          </h2>
          <ul class="mt-8 space-y-3.5">
            <li
              v-for="f in item.features"
              :key="f"
              class="flex items-start gap-3 rounded-2xl border border-slate-200/85 bg-white p-4 shadow-relief-sm transition-all hover:border-brand-200 hover:shadow-relief-card"
            >
              <span
                class="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-gradient-to-r from-brand-600 to-indigo-600 text-white shadow-relief-btn-primary"
              >
                <AppIcon name="check" class="h-3.5 w-3.5" />
              </span>
              <span class="text-sm font-medium leading-relaxed text-slate-700">{{ f }}</span>
            </li>
          </ul>
        </div>

        <!-- Beneficios -->
        <div>
          <span class="eyebrow">{{ t('detail.benefitsTitle') }}</span>
          <div class="mt-8 grid gap-4 sm:grid-cols-2">
            <div
              v-for="b in item.benefits"
              :key="b.title"
              class="group rounded-2xl border border-slate-200/85 bg-white p-6 shadow-relief-card transition-all duration-300 hover:-translate-y-1 hover:border-brand-300 hover:shadow-relief-card-hover"
            >
              <span
                class="flex h-11 w-11 items-center justify-center rounded-xl border border-brand-100 bg-brand-50 text-brand-600 shadow-inner transition-colors duration-300 group-hover:bg-brand-600 group-hover:text-white"
              >
                <AppIcon :name="b.icon" class="h-5 w-5" />
              </span>
              <h3 class="mt-4 font-display text-base font-bold text-slate-900">{{ b.title }}</h3>
              <p class="mt-1.5 text-sm leading-relaxed text-slate-600">{{ b.text }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tecnologías -->
    <section class="bg-gradient-to-b from-slate-50 to-white py-16 sm:py-20 border-y border-slate-200/60">
      <div class="container-site">
        <div class="max-w-2xl">
          <span class="eyebrow">{{ t('detail.techTitle') }}</span>
          <h2 class="section-title mt-5">{{ t('detail.techTitle') }}</h2>
        </div>
        <div class="mt-10 flex flex-wrap gap-3">
          <span
            v-for="tech in item.tech"
            :key="tech"
            class="inline-flex items-center gap-2 rounded-full border border-slate-200/90 bg-white px-4 py-2 text-xs font-semibold uppercase tracking-wide text-slate-700 shadow-relief-sm transition-all hover:border-brand-300 hover:text-brand-700"
          >
            <span class="h-2 w-2 rounded-full bg-brand-500 shadow-[0_0_6px_rgba(37,99,235,0.8)]" />
            {{ tech }}
          </span>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section v-if="item.faq?.length" class="bg-white py-16 sm:py-20">
      <div class="container-site mx-auto max-w-3xl">
        <div class="text-center">
          <span class="eyebrow">FAQ</span>
          <h2 class="section-title mt-5">{{ t('detail.faqTitle') }}</h2>
        </div>
        <div class="mt-10 space-y-3.5">
          <details
            v-for="(f, i) in item.faq"
            :key="i"
            class="group rounded-2xl border border-slate-200/85 bg-white p-2 shadow-relief-sm transition-all open:border-brand-200 open:bg-brand-50/30 open:shadow-relief-card"
          >
            <summary
              class="flex cursor-pointer list-none items-center justify-between gap-4 px-4 py-3 font-display text-[15px] font-bold text-slate-900"
            >
              {{ f.q }}
              <span
                class="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-slate-100 text-slate-500 shadow-inner transition-transform duration-300 group-open:rotate-45 group-open:bg-brand-600 group-open:text-white"
              >
                <AppIcon name="close" class="h-3.5 w-3.5" />
              </span>
            </summary>
            <p class="px-4 pb-4 pt-1 text-sm leading-relaxed text-slate-600">{{ f.a }}</p>
          </details>
        </div>
      </div>
    </section>

    <!-- Relacionados -->
    <section class="bg-slate-50 py-16 sm:py-20 border-t border-slate-200/60">
      <div class="container-site">
        <div class="flex flex-wrap items-end justify-between gap-4">
          <div>
            <span class="eyebrow">{{ parentLabel }}</span>
            <h2 class="section-title mt-5">{{ relatedTitle }}</h2>
          </div>
          <NuxtLinkLocale
            :to="`/${basePath}`"
            class="inline-flex items-center gap-1.5 rounded-full border border-brand-200/80 bg-brand-50 px-4 py-1.5 text-xs font-bold text-brand-700 shadow-relief-sm transition-all hover:bg-brand-100"
          >
            {{ viewAllLabel }}
            <AppIcon name="arrow-right" class="h-3.5 w-3.5" />
          </NuxtLinkLocale>
        </div>

        <div class="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          <NuxtLinkLocale
            v-for="r in related"
            :key="r.slug"
            :to="`/${basePath}/${r.slug}`"
            class="group flex items-start gap-4 rounded-2xl border border-slate-200/85 bg-white p-6 shadow-relief-card transition-all duration-300 hover:-translate-y-1 hover:border-brand-300 hover:shadow-relief-card-hover"
          >
            <span
              class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl border border-brand-100 bg-brand-50 text-brand-600 shadow-inner transition-colors duration-300 group-hover:bg-brand-600 group-hover:text-white"
            >
              <AppIcon :name="r.icon" class="h-5 w-5" />
            </span>
            <span class="min-w-0">
              <span class="block font-display text-[15px] font-bold text-slate-900 group-hover:text-brand-700">
                {{ r.name }}
              </span>
              <span class="mt-0.5 block text-xs text-slate-500">{{ r.subtitle }}</span>
            </span>
            <AppIcon
              name="arrow-up-right"
              class="ml-auto mt-1 h-4 w-4 shrink-0 text-slate-300 transition-all duration-300 group-hover:translate-x-0.5 group-hover:text-brand-600"
            />
          </NuxtLinkLocale>
        </div>
      </div>
    </section>

    <!-- CTA final -->
    <section class="relative overflow-hidden bg-ink-950 py-20 text-white sm:py-24">
      <div class="pointer-events-none absolute inset-0 bg-grid-dark opacity-35" />
      <div
        class="pointer-events-none absolute -bottom-24 left-1/2 h-72 w-[36rem] -translate-x-1/2 rounded-full bg-brand-600/25 blur-3xl"
      />
      <div class="container-site relative mx-auto max-w-3xl text-center">
        <h2 class="font-display text-3xl font-bold tracking-tight sm:text-4xl">{{ t('detail.ctaTitle') }}</h2>
        <p class="mx-auto mt-4 max-w-xl text-slate-300">{{ t('detail.ctaText') }}</p>
        <div class="mt-9 flex flex-wrap items-center justify-center gap-3.5">
          <a :href="whatsappHref" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
            <AppIcon name="whatsapp" class="h-4 w-4" />
            {{ t('detail.ctaWhatsapp') }}
          </a>
          <NuxtLinkLocale to="/#contacto" class="btn btn-white btn-lg">
            {{ t('detail.ctaPrimary') }}
            <AppIcon name="arrow-up-right" class="h-4 w-4" />
          </NuxtLinkLocale>
        </div>
      </div>
    </section>
  </div>
</template>
