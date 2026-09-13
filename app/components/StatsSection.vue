<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { stats } = useContent()

const cardAccents = [
  {
    topBar: 'bg-gradient-to-r from-brand-500 to-blue-600',
    iconBg: 'bg-brand-50 border border-brand-100/80 shadow-inner',
    iconColor: 'text-brand-600',
    numGradient: 'from-brand-700 via-brand-600 to-blue-700'
  },
  {
    topBar: 'bg-gradient-to-r from-sky-500 to-cyan-500',
    iconBg: 'bg-sky-50 border border-sky-100/80 shadow-inner',
    iconColor: 'text-sky-600',
    numGradient: 'from-sky-700 via-sky-600 to-cyan-700'
  },
  {
    topBar: 'bg-gradient-to-r from-emerald-500 to-teal-500',
    iconBg: 'bg-emerald-50 border border-emerald-100/80 shadow-inner',
    iconColor: 'text-emerald-600',
    numGradient: 'from-emerald-700 via-emerald-600 to-teal-700'
  },
  {
    topBar: 'bg-gradient-to-r from-indigo-500 to-violet-500',
    iconBg: 'bg-indigo-50 border border-indigo-100/80 shadow-inner',
    iconColor: 'text-indigo-600',
    numGradient: 'from-indigo-700 via-indigo-600 to-slate-800'
  }
]
</script>

<template>
  <section id="estadisticas" class="relative scroll-mt-24 border-y border-slate-200/70 bg-gradient-to-b from-white via-slate-50/50 to-white py-16 lg:py-20">
    <div class="container-site">
      <div class="grid grid-cols-2 gap-5 lg:grid-cols-4">
        <div v-for="(s, i) in stats" :key="s.label">
          <RevealOnScroll :delay="i * 90">
            <div
              class="group relative flex flex-col overflow-hidden rounded-2xl border border-slate-200/85 bg-white p-6 shadow-relief-card transition-all duration-300 hover:-translate-y-1.5 hover:shadow-relief-card-hover"
            >
              <!-- Top micro accent bar -->
              <div class="absolute inset-x-0 top-0 h-1 opacity-75" :class="cardAccents[i % 4].topBar" />

              <div class="flex items-center justify-between">
                <span
                  class="flex h-11 w-11 items-center justify-center rounded-xl transition-transform duration-300 group-hover:scale-110 group-hover:shadow-md"
                  :class="[cardAccents[i % 4].iconBg, cardAccents[i % 4].iconColor]"
                >
                  <AppIcon :name="s.icon" class="h-5 w-5" />
                </span>
                <span class="h-2 w-2 rounded-full bg-slate-200 opacity-60 transition-colors group-hover:bg-brand-500" />
              </div>

              <p
                class="mt-5 bg-gradient-to-r bg-clip-text font-display text-4xl font-extrabold tracking-tight text-transparent sm:text-5xl"
                :class="cardAccents[i % 4].numGradient"
              >
                <AnimatedNumber :value="s.value" />{{ s.suffix }}
              </p>
              <p class="mt-2 text-xs font-bold uppercase tracking-wider text-slate-500">
                {{ s.label }}
              </p>
            </div>
          </RevealOnScroll>
        </div>
      </div>
    </div>
  </section>
</template>
