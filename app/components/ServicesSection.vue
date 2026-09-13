<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { services } = useContent()

// Different accent per service card for visual variety
const accents = [
  { iconBg: 'bg-brand-50', iconColor: 'text-brand-600', hoverBg: 'group-hover:bg-brand-600', hoverShadow: 'group-hover:shadow-brand-600/30' },
  { iconBg: 'bg-slate-50', iconColor: 'text-slate-600', hoverBg: 'group-hover:bg-slate-600', hoverShadow: 'group-hover:shadow-slate-600/30' },
  { iconBg: 'bg-sky-50', iconColor: 'text-sky-600', hoverBg: 'group-hover:bg-sky-600', hoverShadow: 'group-hover:shadow-sky-600/30' },
  { iconBg: 'bg-emerald-50', iconColor: 'text-emerald-600', hoverBg: 'group-hover:bg-emerald-600', hoverShadow: 'group-hover:shadow-emerald-600/30' }
]
</script>

<template>
  <section id="servicios" class="scroll-mt-24 bg-gradient-to-b from-slate-50 via-slate-100/40 to-slate-50 py-20 sm:py-28">
    <div class="container-site">
      <RevealOnScroll>
        <div class="mx-auto max-w-2xl text-center">
          <span class="eyebrow">{{ t('servicesSection.eyebrow') }}</span>
          <h2 class="section-title mt-5">
            {{ t('servicesSection.title') }}
            <span class="text-gradient">{{ t('servicesSection.titleHighlight') }}</span>
          </h2>
          <p class="section-sub">{{ t('servicesSection.description') }}</p>
        </div>
      </RevealOnScroll>

      <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <RevealOnScroll
          v-for="(service, i) in services"
          :key="service.id"
          :delay="(i % 3) * 90"
        >
          <article
            class="group relative flex h-full flex-col overflow-hidden rounded-2xl border border-slate-200/85 bg-white p-7 shadow-relief-card transition-all duration-300 hover:-translate-y-1.5 hover:border-brand-300/80 hover:shadow-relief-card-hover"
          >
            <!-- Top micro gradient border -->
            <div
              class="absolute inset-x-0 top-0 h-1 opacity-0 transition-opacity duration-300 group-hover:opacity-100"
              style="background: linear-gradient(90deg, #2563eb, #06b6d4)"
            />

            <div class="flex items-start justify-between gap-3">
              <div class="flex items-center gap-3.5 min-w-0">
                <span
                  class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl border border-slate-100 shadow-inner transition-all duration-300 group-hover:scale-105 group-hover:shadow-md group-hover:!text-white"
                  :class="[
                    accents[i % accents.length].iconBg,
                    accents[i % accents.length].iconColor,
                    accents[i % accents.length].hoverBg,
                    accents[i % accents.length].hoverShadow
                  ]"
                >
                  <AppIcon :name="service.icon" class="h-6 w-6 transition-colors duration-300 group-hover:text-white" />
                </span>
                <h3 class="font-display text-lg font-bold text-slate-900 transition-colors group-hover:text-brand-700 leading-snug">
                  {{ service.title }}
                </h3>
              </div>
              <span
                class="shrink-0 rounded-lg border border-slate-200/60 bg-slate-50/80 px-2.5 py-1 font-display text-xs font-bold text-slate-400 shadow-inner transition-colors duration-300 group-hover:border-brand-200 group-hover:bg-brand-50 group-hover:text-brand-600"
              >
                {{ String(i + 1).padStart(2, '0') }}
              </span>
            </div>

            <p class="mt-4 text-sm leading-relaxed text-slate-600">{{ service.description }}</p>

            <ul class="mt-5 space-y-2.5">
              <li
                v-for="feature in service.features"
                :key="feature"
                class="flex items-start gap-2.5 text-sm text-slate-600"
              >
                <span class="mt-0.5 flex h-4 w-4 shrink-0 items-center justify-center rounded-full bg-emerald-50 text-emerald-500 shadow-inner">
                  <AppIcon name="check" class="h-2.5 w-2.5" />
                </span>
                <span>{{ feature }}</span>
              </li>
            </ul>

            <div class="mt-auto flex flex-wrap items-center justify-between gap-2 border-t border-slate-100 pt-6">
              <NuxtLinkLocale
                :to="`/servicios/${service.slug}`"
                class="inline-flex items-center gap-1.5 text-sm font-semibold text-brand-600 transition-colors hover:text-brand-700"
              >
                {{ t('servicesSection.viewMore') }}
                <AppIcon
                  name="arrow-right"
                  class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
                />
              </NuxtLinkLocale>
              <a
                href="#contacto"
                class="inline-flex items-center gap-1 text-xs font-medium text-slate-400 transition-colors hover:text-brand-600"
              >
                {{ t('servicesSection.cta') }}
              </a>
            </div>
          </article>
        </RevealOnScroll>
      </div>
    </div>
  </section>
</template>
