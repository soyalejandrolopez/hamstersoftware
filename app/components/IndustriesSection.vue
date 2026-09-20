<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { industries } = useContent()

const colors = [
  { topBar: 'bg-gradient-to-r from-brand-500 to-sky-500', iconBg: 'bg-brand-50 border border-brand-100/80 shadow-inner group-hover:bg-brand-600 group-hover:border-brand-600', iconColor: 'text-brand-600 group-hover:text-white' },
  { topBar: 'bg-gradient-to-r from-slate-500 to-indigo-500', iconBg: 'bg-slate-50 border border-slate-200/80 shadow-inner group-hover:bg-slate-700 group-hover:border-slate-700', iconColor: 'text-slate-700 group-hover:text-white' },
  { topBar: 'bg-gradient-to-r from-sky-500 to-cyan-500', iconBg: 'bg-sky-50 border border-sky-100/80 shadow-inner group-hover:bg-sky-600 group-hover:border-sky-600', iconColor: 'text-sky-600 group-hover:text-white' },
  { topBar: 'bg-gradient-to-r from-emerald-500 to-teal-500', iconBg: 'bg-emerald-50 border border-emerald-100/80 shadow-inner group-hover:bg-emerald-600 group-hover:border-emerald-600', iconColor: 'text-emerald-600 group-hover:text-white' }
]
</script>

<template>
  <section id="industrias" class="scroll-mt-24 bg-white py-20 sm:py-28">
    <div class="container-site">
      <RevealOnScroll>
        <div class="mx-auto max-w-2xl text-center">
          <span class="eyebrow">{{ t('industriesSection.eyebrow') }}</span>
          <h2 class="section-title mt-5">
            {{ t('industriesSection.title') }}
            <span class="text-gradient">{{ t('industriesSection.titleHighlight') }}</span>
          </h2>
          <p class="section-sub">{{ t('industriesSection.description') }}</p>
        </div>
      </RevealOnScroll>

      <RevealOnScroll :delay="100">
        <div class="mt-14 grid grid-cols-2 gap-5 sm:grid-cols-3 lg:grid-cols-4">
          <div
            v-for="(industry, i) in industries"
            :key="industry.name"
            class="group relative flex items-center gap-3.5 overflow-hidden rounded-2xl border border-slate-200/85 bg-white p-5 shadow-relief-card transition-all duration-300 hover:-translate-y-1.5 hover:border-brand-300/80 hover:shadow-relief-card-hover"
          >
            <!-- Top micro gradient border -->
            <div class="absolute inset-x-0 top-0 h-1 opacity-70" :class="colors[i % colors.length]!.topBar" />

            <span
              class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl transition-all duration-300 group-hover:scale-110 group-hover:shadow-md"
              :class="[colors[i % colors.length]!.iconBg, colors[i % colors.length]!.iconColor]"
            >
              <AppIcon :name="industry.icon" class="h-6 w-6 transition-colors duration-300 group-hover:text-white" />
            </span>
            <span
              class="font-display text-sm font-bold leading-snug text-slate-800 transition-colors group-hover:text-brand-700"
            >
              {{ industry.name }}
            </span>
          </div>
        </div>
      </RevealOnScroll>
    </div>
  </section>
</template>
