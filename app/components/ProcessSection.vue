<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { processSteps } = useContent()
</script>

<template>
  <section id="proceso" class="scroll-mt-24 bg-gradient-to-b from-slate-50 via-slate-100/40 to-slate-50 py-20 sm:py-28">
    <div class="container-site">
      <RevealOnScroll>
        <div class="mx-auto max-w-2xl text-center">
          <span class="eyebrow">{{ t('processSection.eyebrow') }}</span>
          <h2 class="section-title mt-5">
            {{ t('processSection.title') }}
            <span class="text-gradient">{{ t('processSection.titleHighlight') }}</span>
          </h2>
          <p class="section-sub">{{ t('processSection.description') }}</p>
        </div>
      </RevealOnScroll>

      <div class="relative mt-14 grid gap-8 lg:grid-cols-3">
        <div class="absolute left-0 right-0 top-12 hidden border-t-2 border-dashed border-brand-300/60 lg:block" />

        <RevealOnScroll v-for="(step, i) in processSteps" :key="step.number" :delay="i * 130">
          <div class="relative flex flex-col items-center text-center lg:items-start lg:text-left">
            <!-- Step node in high relief -->
            <div
              class="relative z-10 flex h-24 w-24 flex-col items-center justify-center gap-1 rounded-2xl border border-slate-200/90 bg-gradient-to-b from-white via-slate-50 to-slate-100 shadow-relief-card ring-4 ring-white"
            >
              <AppIcon :name="step.icon" class="h-7 w-7 text-brand-600 drop-shadow-sm" />
              <span class="font-display text-xs font-bold uppercase tracking-wider text-brand-700">{{ step.number }}</span>
            </div>

            <!-- Description card in high relief -->
            <div
              class="group relative mt-6 w-full overflow-hidden rounded-2xl border border-slate-200/85 bg-white p-7 shadow-relief-card transition-all duration-300 hover:-translate-y-1.5 hover:border-brand-300/80 hover:shadow-relief-card-hover"
            >
              <div
                class="absolute inset-x-0 top-0 h-1 opacity-0 transition-opacity duration-300 group-hover:opacity-100"
                style="background: linear-gradient(90deg, #2563eb, #06b6d4)"
              />
              <h3 class="font-display text-xl font-bold text-slate-900 transition-colors group-hover:text-brand-700">{{ step.title }}</h3>
              <p class="mt-3 leading-relaxed text-slate-600">{{ step.description }}</p>
            </div>
          </div>
        </RevealOnScroll>
      </div>
    </div>
  </section>
</template>
