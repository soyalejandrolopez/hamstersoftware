<script setup lang="ts">
import { company } from '~/data/config'

const props = defineProps<{ error: { statusCode?: number } }>()

const { t } = useI18n()

const statusCode = computed(() => props.error?.statusCode || 500)

const title = computed(() => {
  switch (statusCode.value) {
    case 404:
      return t('error.title404')
    case 500:
      return t('error.title500')
    case 403:
      return t('error.title403')
    default:
      return t('error.titleDefault')
  }
})

const description = computed(() => {
  switch (statusCode.value) {
    case 404:
      return t('error.desc404')
    case 500:
      return t('error.desc500')
    case 403:
      return t('error.desc403')
    default:
      return t('error.descDefault')
  }
})

const is404 = computed(() => statusCode.value === 404)

useSeoMeta({
  title: () => `${title.value} — Hamster Software`,
  robots: () => (is404.value ? 'noindex' : 'index')
})
</script>

<template>
  <div class="relative flex min-h-screen flex-col overflow-hidden bg-gradient-to-b from-brand-50/70 via-white to-white">
    <!-- Fondo decorativo -->
    <div class="pointer-events-none absolute inset-0 bg-grid-light [mask-image:linear-gradient(to_bottom,black,transparent_80%)]" />
    <div class="pointer-events-none absolute -right-40 -top-40 h-[30rem] w-[30rem] rounded-full bg-brand-200/40 blur-3xl" />
    <div class="pointer-events-none absolute -bottom-40 -left-40 h-[28rem] w-[28rem] rounded-full bg-amber-200/30 blur-3xl" />

    <!-- Encabezado con logo -->
    <header class="relative">
      <div class="container-site flex h-16 items-center justify-between lg:h-[4.5rem]">
        <NuxtLinkLocale to="/" class="group flex items-center gap-2.5" @click="clearError()">
          <AppLogo gid="logo-error" class="h-9 w-9 transition-transform duration-300 group-hover:scale-105" />
          <span class="font-display text-lg font-bold tracking-tight text-slate-900">
            Hamster<span class="text-brand-600">Software</span>
          </span>
        </NuxtLinkLocale>
        <LangSwitcher />
      </div>
    </header>

    <!-- Contenido del error -->
    <main class="relative flex flex-1 items-center justify-center px-6 py-16">
      <div class="w-full max-w-xl text-center">
        <!-- Código de error -->
        <div class="relative mx-auto flex h-28 w-28 items-center justify-center">
          <div class="absolute inset-0 animate-pulse-dot rounded-3xl bg-brand-100" />
          <div class="absolute inset-2 rounded-2xl bg-white shadow-card ring-1 ring-slate-100" />
          <AppLogo gid="logo-error-code" class="relative h-14 w-14" />
          <span
            class="absolute -right-3 -top-3 flex h-12 w-12 items-center justify-center rounded-full bg-ink-950 font-display text-lg font-bold text-white shadow-lg"
          >
            {{ statusCode }}
          </span>
        </div>

        <h1 class="mt-10 font-display text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
          {{ title }}
        </h1>

        <p class="mx-auto mt-4 max-w-md text-lg leading-relaxed text-slate-600">
          {{ description }}
        </p>

        <p v-if="is404" class="mt-3 flex items-center justify-center gap-2 text-sm text-slate-400">
          <AppIcon name="map-pin" class="h-4 w-4 text-brand-500" />
          {{ t('error.hint404') }}
        </p>

        <div class="mt-10 flex flex-wrap items-center justify-center gap-4">
          <NuxtLinkLocale to="/" class="btn btn-primary btn-lg" @click="clearError()">
            <AppIcon name="arrow-right" class="h-4 w-4" />
            {{ t('error.backHome') }}
          </NuxtLinkLocale>
          <NuxtLinkLocale to="/#contacto" class="btn btn-outline btn-lg" @click="clearError()">
            <AppIcon name="whatsapp" class="h-4 w-4" />
            {{ t('error.contact') }}
          </NuxtLinkLocale>
        </div>

        <p class="mt-12 text-sm text-slate-400">
          {{ company.location }}
        </p>
      </div>
    </main>
  </div>
</template>
