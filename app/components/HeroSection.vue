<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { hero } = useContent()

// Corporate color mapping and relief accents for each service card
const cardStyles = [
  {
    bg: 'bg-white',
    border: 'border-slate-200/85 hover:border-brand-300',
    topBar: 'bg-gradient-to-r from-brand-500 to-sky-500',
    iconBg: 'bg-brand-50 border border-brand-100/80 shadow-inner group-hover:bg-brand-600 group-hover:border-brand-600',
    iconColor: 'text-brand-600 group-hover:text-white',
    titleHover: 'group-hover:text-brand-700'
  },
  {
    bg: 'bg-white',
    border: 'border-slate-200/85 hover:border-sky-300',
    topBar: 'bg-gradient-to-r from-sky-500 to-cyan-500',
    iconBg: 'bg-sky-50 border border-sky-100/80 shadow-inner group-hover:bg-sky-600 group-hover:border-sky-600',
    iconColor: 'text-sky-600 group-hover:text-white',
    titleHover: 'group-hover:text-sky-700'
  },
  {
    bg: 'bg-white',
    border: 'border-slate-200/85 hover:border-emerald-300',
    topBar: 'bg-gradient-to-r from-emerald-500 to-teal-500',
    iconBg: 'bg-emerald-50 border border-emerald-100/80 shadow-inner group-hover:bg-emerald-600 group-hover:border-emerald-600',
    iconColor: 'text-emerald-600 group-hover:text-white',
    titleHover: 'group-hover:text-emerald-700'
  },
  {
    bg: 'bg-white',
    border: 'border-slate-200/85 hover:border-indigo-300',
    topBar: 'bg-gradient-to-r from-indigo-500 to-brand-500',
    iconBg: 'bg-indigo-50 border border-indigo-100/80 shadow-inner group-hover:bg-indigo-600 group-hover:border-indigo-600',
    iconColor: 'text-indigo-600 group-hover:text-white',
    titleHover: 'group-hover:text-indigo-700'
  }
]

const serviceCardsWithStyles = computed(() => {
  return (hero.value.serviceCards || []).map((card, i) => ({
    ...card,
    style: cardStyles[i % cardStyles.length]!
  }))
})
</script>

<template>
  <section class="relative">
    <!-- ===== Top: Hero Banner (Con imagen de fondo) ===== -->
    <div class="relative overflow-hidden bg-slate-950 text-white">
      <!-- ── Hero Background Image ── -->
      <div class="pointer-events-none absolute inset-0 overflow-hidden">
        <img
          src="/images/hero-bg.jpg"
          alt="Dos jóvenes empresarios trabajando juntos en una oficina moderna"
          class="h-full w-full object-cover object-center opacity-80 contrast-[1.05] saturate-[1.1]"
          loading="eager"
          fetchpriority="high"
        />
        <!-- Light translucent vignette for clear text readability while displaying the image -->
        <div class="absolute inset-0 bg-gradient-to-b from-slate-950/55 via-slate-950/30 to-slate-950/90" />
      </div>

      <!-- ── Ambient subtle glows ── -->
      <div
        class="pointer-events-none absolute -right-32 -top-32 h-[38rem] w-[38rem] rounded-full bg-brand-600/15 blur-3xl"
      />
      <div
        class="pointer-events-none absolute -bottom-32 -left-32 h-[38rem] w-[38rem] rounded-full bg-sky-500/10 blur-3xl"
      />

      <!-- ── Hero Main Content ── -->
      <div class="container-site relative z-10 pb-12 pt-20 sm:pb-14 sm:pt-24 lg:pb-16 lg:pt-24">
        <div class="max-w-3xl text-left">
          <!-- Eyebrow with tactile high relief -->
          <RevealOnScroll>
            <span
              class="inline-flex items-center gap-2.5 rounded-full border border-white/25 bg-slate-950/60 px-4 py-1.5 text-xs font-bold uppercase tracking-widest text-brand-200 shadow-xl backdrop-blur-md"
            >
              <span class="relative flex h-2 w-2">
                <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-brand-400 opacity-85" />
                <span class="relative inline-flex h-2 w-2 rounded-full bg-brand-400 shadow-[0_0_8px_rgba(96,165,250,0.9)]" />
              </span>
              {{ hero.eyebrow }}
            </span>
          </RevealOnScroll>

          <!-- Headline -->
          <RevealOnScroll :delay="80">
            <h1
              class="mt-4 font-display text-[2.25rem] font-bold leading-[1.08] tracking-tight text-white drop-shadow-[0_4px_18px_rgba(0,0,0,0.85)] sm:mt-5 sm:text-[3rem] lg:text-[3.75rem]"
            >
              {{ hero.titleA }}
              <span class="text-gradient-light drop-shadow-md">{{ hero.titleHighlight }}</span>
              {{ hero.titleB }}
            </h1>
          </RevealOnScroll>

          <!-- Description — clear and direct -->
          <RevealOnScroll :delay="160">
            <p class="mt-3.5 max-w-2xl text-justify text-base leading-relaxed text-slate-100 drop-shadow-[0_2px_10px_rgba(0,0,0,0.85)] sm:mt-4 sm:text-lg">
              <span class="font-bold text-white">{{ hero.subtitle }}</span>
              {{ ' ' }}{{ hero.description }}
            </p>
          </RevealOnScroll>

          <!-- CTAs with high relief finish -->
          <RevealOnScroll :delay="240">
            <div class="mt-6 flex flex-wrap items-center justify-start gap-3.5 sm:mt-8">
              <a
                href="#contacto"
                class="group btn btn-primary btn-lg shadow-2xl"
              >
                <span>{{ hero.ctaPrimary }}</span>
                <AppIcon
                  name="arrow-right"
                  class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
                />
              </a>
              <a
                href="#servicios"
                class="btn btn-white btn-lg shadow-2xl"
              >
                {{ hero.ctaSecondary }}
              </a>
            </div>
          </RevealOnScroll>

          <!-- Trust badges in micro-relief plaques -->
          <RevealOnScroll :delay="300">
            <div class="mt-6 flex flex-wrap items-center justify-start gap-2.5 sm:mt-8">
              <div
                v-for="badge in hero.badges"
                :key="badge"
                class="flex items-center gap-2 rounded-full border border-white/20 bg-slate-950/65 px-3.5 py-1.5 text-xs font-semibold text-white shadow-xl backdrop-blur-md transition-all hover:border-brand-400 hover:bg-slate-950/80"
              >
                <span class="flex h-4 w-4 items-center justify-center rounded-full bg-emerald-500/25 text-emerald-300 shadow-inner">
                  <AppIcon name="check" class="h-2.5 w-2.5" />
                </span>
                {{ badge }}
              </div>
            </div>
          </RevealOnScroll>
        </div>
      </div>
    </div>

    <!-- ===== Bottom: 4 High-Relief Service Cards & Social Proof (Fondo limpio independiente) ===== -->
    <div class="relative border-b border-slate-200/80 bg-gradient-to-b from-slate-100/90 via-slate-50 to-white py-16 lg:py-20">
      <div class="container-site">
        <!-- 4 High-relief service cards — "¿Qué hacemos?" -->
        <RevealOnScroll :delay="100">
          <div class="mx-auto grid max-w-5xl grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
            <a
              v-for="card in serviceCardsWithStyles"
              :key="card.title"
              href="#servicios"
              class="group relative flex flex-col overflow-hidden rounded-2xl border p-6 shadow-relief-card transition-all duration-300 hover:-translate-y-1.5 hover:shadow-relief-card-hover"
              :class="[card.style.bg, card.style.border]"
            >
              <!-- Top micro accent bar -->
              <div class="absolute inset-x-0 top-0 h-1 opacity-80" :class="card.style.topBar" />

              <!-- Tactile Icon Badge & Title side by side -->
              <div class="flex items-center gap-3.5">
                <span
                  class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl transition-all duration-300 group-hover:scale-110 group-hover:shadow-md"
                  :class="[card.style.iconBg, card.style.iconColor]"
                >
                  <AppIcon :name="card.icon" class="h-6 w-6 transition-colors duration-300 group-hover:text-white" />
                </span>
                <h3
                  class="font-display text-base font-bold text-slate-900 transition-colors leading-snug"
                  :class="card.style.titleHover"
                >
                  {{ card.title }}
                </h3>
              </div>

              <!-- Text -->
              <p class="mt-3 text-sm leading-relaxed text-slate-600">
                {{ card.desc }}
              </p>

              <!-- Arrow hint on hover -->
              <div class="mt-auto flex items-center justify-end pt-4">
                <span class="inline-flex h-6 w-6 items-center justify-center rounded-full bg-slate-50 text-slate-400 transition-all duration-300 group-hover:bg-brand-50 group-hover:text-brand-600 group-hover:translate-x-0.5">
                  <AppIcon name="arrow-right" class="h-3.5 w-3.5" />
                </span>
              </div>
            </a>
          </div>
        </RevealOnScroll>

        <!-- Social proof in floating high-relief plaque -->
        <RevealOnScroll :delay="200">
          <div class="mx-auto mt-14 flex max-w-md items-center justify-center gap-5 rounded-2xl border border-slate-200/85 bg-white/95 px-6 py-4 shadow-relief-sm backdrop-blur-md">
            <!-- Avatar stack -->
            <div class="flex -space-x-2.5">
              <div
                v-for="i in 4"
                :key="i"
                class="flex h-9 w-9 items-center justify-center rounded-full border-2 border-white text-[11px] font-bold text-white shadow-sm ring-1 ring-black/5"
                :style="{ background: ['#2563eb', '#4f46e5', '#7c3aed', '#0891b2'][i - 1] }"
              >
                {{ ['AL', 'MR', 'JC', 'SP'][i - 1] }}
              </div>
            </div>
            <div class="border-l border-slate-200/80 pl-4">
              <p class="text-sm font-bold text-slate-900">+50 proyectos entregados</p>
              <div class="mt-0.5 flex items-center gap-1">
                <div class="flex text-amber-400">
                  <svg
                    v-for="s in 5"
                    :key="s"
                    class="h-3.5 w-3.5"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    />
                  </svg>
                </div>
                <span class="text-xs font-semibold text-slate-700">5.0</span>
                <span class="text-xs text-slate-400">calificación</span>
              </div>
            </div>
          </div>
        </RevealOnScroll>
      </div>
    </div>
  </section>
</template>
