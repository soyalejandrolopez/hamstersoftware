<script setup lang="ts">
import type { SeverityKey } from '~/types/content'
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { security } = useContent()

const severityStyles: Record<SeverityKey, string> = {
  critical: 'bg-rose-500/15 text-rose-400 ring-1 ring-rose-500/20',
  high: 'bg-orange-500/15 text-orange-400 ring-1 ring-orange-500/20',
  medium: 'bg-amber-500/15 text-amber-400 ring-1 ring-amber-500/20',
  low: 'bg-emerald-500/15 text-emerald-400 ring-1 ring-emerald-500/20'
}
</script>

<template>
  <section id="seguridad" class="relative scroll-mt-24 overflow-hidden bg-ink-950 py-20 text-white sm:py-28">
    <div class="pointer-events-none absolute inset-0 bg-grid-dark" />
    <div
      class="pointer-events-none absolute right-0 top-0 h-[32rem] w-[32rem] -translate-y-1/3 translate-x-1/3 rounded-full bg-brand-600/25 blur-3xl"
    />
    <div
      class="pointer-events-none absolute -bottom-24 -left-24 h-80 w-80 rounded-full bg-indigo-600/15 blur-3xl"
    />

    <div class="container-site relative grid items-center gap-14 lg:grid-cols-2">
      <!-- Copy -->
      <RevealOnScroll>
        <span
          class="inline-flex items-center gap-2.5 rounded-full border border-white/15 bg-white/5 px-4 py-2 text-xs font-semibold uppercase tracking-widest text-brand-300 shadow-relief-sm backdrop-blur-md"
        >
          <AppIcon name="shield" class="h-3.5 w-3.5 text-brand-400" />
          {{ security.eyebrow }}
        </span>
        <h2 class="mt-6 font-display text-3xl font-bold tracking-tight sm:text-4xl lg:text-[2.85rem] lg:leading-[1.14]">
          {{ security.title }}
        </h2>
        <p class="mt-5 max-w-xl text-lg leading-relaxed text-slate-300">{{ security.description }}</p>

        <ul class="mt-8 space-y-4">
          <li v-for="f in security.features" :key="f" class="flex items-start gap-3">
            <span class="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-emerald-400/20 text-emerald-400 shadow-inner ring-1 ring-emerald-400/30">
              <AppIcon name="check" class="h-3.5 w-3.5" />
            </span>
            <span class="text-slate-200 font-medium">{{ f }}</span>
          </li>
        </ul>

        <div class="mt-10 flex flex-wrap items-center gap-4">
          <a href="#contacto" class="btn btn-white btn-lg">
            {{ security.cta }}
            <AppIcon name="arrow-up-right" class="h-4 w-4" />
          </a>
          <span class="inline-flex items-center gap-2 text-xs font-semibold text-slate-400">
            <AppIcon name="clock" class="h-4 w-4 text-brand-400" />
            {{ security.updatedNote }}
          </span>
        </div>
      </RevealOnScroll>

      <!-- Feed de CVEs en alto relieve oscuro -->
      <RevealOnScroll :delay="150" direction="left">
        <div class="relative mx-auto max-w-md">
          <div
            class="relative overflow-hidden rounded-3xl p-6 sm:p-7 shadow-relief-dark"
            style="
              background: linear-gradient(135deg, rgba(15,23,42,0.88) 0%, rgba(11,18,32,0.96) 100%);
              border: 1px solid rgba(255,255,255,0.12);
              backdrop-filter: blur(28px);
              box-shadow: inset 0 1px 0 0 rgba(255,255,255,0.2), 0 25px 50px -12px rgba(0,0,0,0.7), 0 0 0 1px rgba(37,99,235,0.15);
            "
          >
            <!-- Top rim highlight -->
            <div class="absolute inset-x-8 top-0 h-px bg-gradient-to-r from-transparent via-white/40 to-transparent" />

            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <span
                  class="flex h-10 w-10 items-center justify-center rounded-xl shadow-relief-sm"
                  style="background: linear-gradient(135deg, #2563eb, #4f46e5); border: 1px solid rgba(255,255,255,0.2);"
                >
                  <AppIcon name="shield-alert" class="h-5 w-5 text-white" />
                </span>
                <div>
                  <p class="text-sm font-bold text-white">{{ security.feedTitle }}</p>
                  <p class="text-[11px] font-medium text-slate-400">{{ security.feedSource }}</p>
                </div>
              </div>
              <span
                class="flex items-center gap-1.5 rounded-full px-3 py-1 text-[11px] font-semibold text-emerald-300 shadow-inner"
                style="background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.3)"
              >
                <span class="h-2 w-2 animate-pulse-dot rounded-full bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.8)]" />
                {{ security.live }}
              </span>
            </div>

            <div class="mt-6 space-y-3">
              <div
                v-for="cve in security.feed"
                :key="cve.id"
                class="group flex items-center justify-between gap-3 rounded-xl px-4 py-3.5 transition-all duration-200 hover:border-white/20 hover:bg-white/[0.06]"
                style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);"
              >
                <div class="flex min-w-0 items-center gap-3">
                  <span
                    class="shrink-0 rounded-lg px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider shadow-sm"
                    :class="severityStyles[cve.severity]"
                  >
                    {{ t(`severity.${cve.severity}`) }}
                  </span>
                  <div class="min-w-0">
                    <p class="font-mono text-xs font-bold text-white">{{ cve.id }}</p>
                    <p class="truncate text-[11px] text-slate-300">{{ cve.title }}</p>
                  </div>
                </div>
                <span class="shrink-0 text-[10px] font-medium text-slate-500">{{ cve.time }}</span>
              </div>
            </div>
          </div>

          <!-- Floating high-relief badge -->
          <div
            class="absolute -bottom-5 -right-5 hidden animate-float-slow sm:block"
            style="
              background: rgba(11,18,32,0.94);
              border: 1px solid rgba(16,185,129,0.35);
              border-radius: 16px;
              padding: 12px 18px;
              box-shadow: inset 0 1px 0 rgba(255,255,255,0.15), 0 20px 35px rgba(0,0,0,0.5);
              backdrop-filter: blur(20px);
            "
          >
            <div class="flex items-center gap-2">
              <span class="h-2 w-2 rounded-full bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.9)]" />
              <p class="text-xs font-bold text-emerald-300">
                {{ security.monitoredToday }}
              </p>
            </div>
          </div>
        </div>
      </RevealOnScroll>
    </div>
  </section>
</template>
