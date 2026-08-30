<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { cases } = useContent()
</script>

<template>
  <section id="casos" class="scroll-mt-24 bg-gradient-to-b from-slate-50 via-slate-100/50 to-white py-20 sm:py-28">
    <div class="container-site">
      <RevealOnScroll>
        <div class="mx-auto max-w-2xl text-center">
          <span class="eyebrow">{{ t('casesSection.eyebrow') }}</span>
          <h2 class="section-title mt-5">
            {{ t('casesSection.title') }}
            <span class="text-gradient">{{ t('casesSection.titleHighlight') }}</span>
          </h2>
          <p class="section-sub">{{ t('casesSection.description') }}</p>
        </div>
      </RevealOnScroll>

      <div class="mt-14 grid gap-8 lg:grid-cols-2">
        <RevealOnScroll v-for="(item, i) in cases" :key="item.id" :delay="i * 120">
          <article
            class="group flex h-full flex-col overflow-hidden rounded-2xl border border-slate-200/85 bg-white shadow-relief-card transition-all duration-300 hover:-translate-y-1.5 hover:border-brand-300/80 hover:shadow-relief-card-hover"
          >
            <!-- Visual with realistic relief & lighting -->
            <div
              class="relative aspect-[16/10] overflow-hidden shadow-inner"
              :class="item.visualType === 'app' || item.visualType === 'salon' ? 'bg-gradient-to-br from-slate-950 via-indigo-950/80 to-slate-900' : 'bg-gradient-to-br from-slate-950 via-slate-900 to-brand-950'"
            >
              <div class="absolute inset-0 bg-grid-dark opacity-30" />
              <!-- Specular top reflection -->
              <div class="absolute inset-x-0 top-0 h-20 bg-gradient-to-b from-white/15 to-transparent pointer-events-none" />

              <!-- Web Browser Mockup -->
              <div v-if="item.visualType === 'web' || item.visualType === 'spa'" class="absolute inset-0 flex items-center justify-center p-4 sm:p-7">
                <div
                  class="relative w-full max-w-md overflow-hidden rounded-xl border border-white/15 bg-slate-900/90 shadow-[0_20px_50px_rgba(0,0,0,0.6),inset_0_1px_0_rgba(255,255,255,0.2)] backdrop-blur-md transition-transform duration-500 group-hover:scale-[1.03]"
                >
                  <!-- Browser top bar -->
                  <div class="flex items-center gap-2 border-b border-white/10 bg-slate-800/90 px-3.5 py-2">
                    <div class="flex items-center gap-1.5">
                      <span class="h-2.5 w-2.5 rounded-full bg-rose-500/90 shadow-sm" />
                      <span class="h-2.5 w-2.5 rounded-full bg-amber-500/90 shadow-sm" />
                      <span class="h-2.5 w-2.5 rounded-full bg-emerald-500/90 shadow-sm" />
                    </div>
                    <div class="mx-auto flex w-3/5 items-center justify-center gap-1.5 rounded-md bg-slate-950/70 px-2.5 py-0.5 text-[10px] text-slate-300 border border-white/5">
                      <AppIcon name="lock" class="h-2.5 w-2.5 text-emerald-400" />
                      <span class="font-mono text-[10px] text-slate-300">rentaya.com.co</span>
                    </div>
                  </div>
                  <!-- Web screenshot -->
                  <div class="relative aspect-[16/9] w-full overflow-hidden bg-slate-950">
                    <img
                      :src="item.image || '/images/rentaya-web.png'"
                      :alt="item.title"
                      class="h-full w-full object-cover object-top transition-transform duration-700 group-hover:scale-105"
                      loading="lazy"
                    />
                    <div class="pointer-events-none absolute inset-0 bg-gradient-to-t from-slate-950/30 via-transparent to-transparent" />
                  </div>
                </div>
              </div>

              <!-- Mobile Phone Mockup -->
              <div v-else class="absolute inset-0 flex items-center justify-center p-3 sm:p-5">
                <div
                  class="relative h-[210px] w-[115px] sm:h-[235px] sm:w-[130px] rounded-[2rem] border-[3.5px] border-slate-700/90 bg-slate-900 shadow-[0_20px_50px_rgba(0,0,0,0.65),inset_0_1px_0_rgba(255,255,255,0.3)] transition-transform duration-500 group-hover:scale-105"
                >
                  <!-- Speaker notch -->
                  <div class="absolute left-1/2 top-1.5 z-10 h-1.5 w-8 -translate-x-1/2 rounded-full bg-slate-700" />
                  <!-- Mobile screen -->
                  <div class="relative flex h-full flex-col overflow-hidden rounded-[1.65rem] bg-slate-950">
                    <img
                      :src="item.image || '/images/rentaya-app.png'"
                      :alt="item.title"
                      class="h-full w-full object-cover object-top transition-transform duration-700 group-hover:scale-105"
                      loading="lazy"
                    />
                    <div class="pointer-events-none absolute inset-0 bg-gradient-to-t from-slate-950/25 via-transparent to-transparent" />
                  </div>
                </div>

                <!-- Floating badge for mobile -->
                <div
                  class="absolute right-6 top-1/2 -translate-y-1/2 hidden sm:flex items-center gap-2 rounded-xl border border-white/15 bg-slate-900/90 px-3 py-2 shadow-relief-dark backdrop-blur-md transition-transform duration-500 group-hover:translate-x-1"
                >
                  <span class="flex h-6 w-6 items-center justify-center rounded-lg bg-emerald-500/20 text-emerald-400">
                    <AppIcon name="whatsapp" class="h-3.5 w-3.5" />
                  </span>
                  <div class="text-left">
                    <p class="text-[10px] font-bold text-white leading-tight">WhatsApp Direct</p>
                    <p class="text-[9px] text-slate-400 leading-tight">Sin intermediarios</p>
                  </div>
                </div>
              </div>

              <!-- Category badge in high relief -->
              <span
                class="absolute left-4 top-4 rounded-full border border-white/80 bg-white/95 px-3.5 py-1.5 text-[11px] font-bold text-slate-800 shadow-relief-sm backdrop-blur-md"
              >
                {{ item.category }}
              </span>
            </div>

            <!-- Content -->
            <div class="flex flex-1 flex-col p-7 sm:p-8">
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="tag in item.tags"
                  :key="tag"
                  class="rounded-full border border-brand-200/80 bg-brand-50/90 px-3 py-1 text-xs font-semibold text-brand-700 shadow-relief-sm"
                >
                  {{ tag }}
                </span>
              </div>
              <h3 class="mt-4 font-display text-2xl font-bold text-slate-900 transition-colors group-hover:text-brand-700">
                {{ item.title }}
              </h3>
              <p class="mt-3 leading-relaxed text-slate-600">{{ item.description }}</p>

              <div class="mt-6 flex items-center justify-between gap-4 border-t border-slate-100 pt-5">
                <a
                  href="#contacto"
                  class="inline-flex items-center gap-2 text-sm font-semibold text-brand-600 transition-colors hover:text-brand-700"
                >
                  {{ t('casesSection.cta') }}
                  <AppIcon
                    name="arrow-right"
                    class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
                  />
                </a>
                <span
                  v-if="item.stat"
                  class="inline-flex items-center gap-1.5 rounded-full border border-emerald-200/80 bg-emerald-50 px-3.5 py-1.5 text-xs font-bold text-emerald-700 shadow-relief-sm"
                >
                  <AppIcon name="trending-up" class="h-4 w-4 text-emerald-600" />
                  {{ item.stat }}
                </span>
              </div>
            </div>
          </article>
        </RevealOnScroll>
      </div>
    </div>
  </section>
</template>
