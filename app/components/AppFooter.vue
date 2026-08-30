<script setup lang="ts">
import { company } from '~/data/config'
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { products, services } = useContent()

const footerServices = computed(() => services.value.slice(0, 8))

const footerProducts = computed(() => products.value.slice(0, 8))
</script>

<template>
  <footer class="relative overflow-hidden bg-ink-950 text-slate-400 border-t border-white/10">
    <div class="pointer-events-none absolute inset-0 bg-grid-dark opacity-30" />
    <div class="pointer-events-none absolute -bottom-32 left-1/3 h-72 w-72 rounded-full bg-brand-600/15 blur-3xl" />
    <div class="absolute inset-x-12 top-0 h-px bg-gradient-to-r from-transparent via-white/25 to-transparent pointer-events-none" />

    <div class="container-site relative py-16">
      <div class="grid gap-12 lg:grid-cols-12">
        <!-- Marca -->
        <div class="lg:col-span-5">
          <div class="flex items-center gap-2.5">
            <AppLogo gid="logo-footer" class="h-9 w-9 drop-shadow" />
            <span class="font-display text-lg font-bold text-white">
              Hamster<span class="text-brand-400">Software</span>
            </span>
          </div>
          <p class="mt-5 max-w-md leading-relaxed text-slate-300">{{ t('footer.tagline') }}</p>
          <div class="mt-5 max-w-md rounded-xl border border-white/10 bg-white/[0.03] p-4 shadow-relief-dark">
            <p class="text-xs leading-relaxed text-slate-400">
              {{ t('footer.legal') }}
            </p>
          </div>
        </div>

        <!-- Navegación -->
        <div class="lg:col-span-2">
          <h4 class="font-display text-xs font-bold uppercase tracking-wider text-white">
            {{ t('footer.navTitle') }}
          </h4>
          <ul class="mt-5 space-y-3 text-sm">
            <li><a href="#servicios" class="transition-colors hover:text-brand-300">{{ t('nav.servicios') }}</a></li>
            <li><a href="#industrias" class="transition-colors hover:text-brand-300">{{ t('nav.industrias') }}</a></li>
            <li><a href="#proceso" class="transition-colors hover:text-brand-300">{{ t('nav.proceso') }}</a></li>
            <li><a href="#contacto" class="transition-colors hover:text-brand-300">{{ t('nav.contacto') }}</a></li>
          </ul>
        </div>

        <!-- Servicios -->
        <div class="lg:col-span-3">
          <h4 class="font-display text-xs font-bold uppercase tracking-wider text-white">
            {{ t('footer.servicesTitle') }}
          </h4>
          <ul class="mt-5 space-y-3 text-sm">
            <li v-for="s in footerServices" :key="s.id">
              <NuxtLinkLocale :to="`/servicios/${s.slug}`" class="transition-colors hover:text-brand-300">
                {{ s.title }}
              </NuxtLinkLocale>
            </li>
            <li class="pt-1">
              <NuxtLinkLocale
                to="/servicios"
                class="inline-flex items-center gap-1 text-xs font-bold text-brand-400 transition-colors hover:text-brand-300"
              >
                {{ t('detail.viewAllServices') }}
                <AppIcon name="arrow-right" class="h-3 w-3" />
              </NuxtLinkLocale>
            </li>
          </ul>
        </div>

        <!-- Soluciones -->
        <div class="lg:col-span-2">
          <h4 class="font-display text-xs font-bold uppercase tracking-wider text-white">
            {{ t('footer.solutionsTitle') }}
          </h4>
          <ul class="mt-5 space-y-3 text-sm">
            <li v-for="p in footerProducts" :key="p.slug">
              <NuxtLinkLocale :to="`/soluciones/${p.slug}`" class="transition-colors hover:text-brand-300">
                {{ p.name }}
              </NuxtLinkLocale>
            </li>
            <li class="pt-1">
              <NuxtLinkLocale
                to="/soluciones"
                class="inline-flex items-center gap-1 text-xs font-bold text-brand-400 transition-colors hover:text-brand-300"
              >
                {{ t('detail.viewAllProducts') }}
                <AppIcon name="arrow-right" class="h-3 w-3" />
              </NuxtLinkLocale>
            </li>
          </ul>
        </div>
      </div>

      <div
        class="mt-14 flex flex-col gap-4 border-t border-white/10 pt-8 text-xs text-slate-400 sm:flex-row sm:items-center sm:justify-between"
      >
        <p>© {{ company.year }} Hamster Software. {{ t('footer.rights') }}</p>
        <div class="flex flex-wrap gap-x-6 gap-y-2">
          <span class="flex items-center gap-2">
            <AppIcon name="map-pin" class="h-3.5 w-3.5 text-brand-400" />
            {{ company.location }}
          </span>
          <a
            :href="`mailto:${company.email}`"
            class="flex items-center gap-2 transition-colors hover:text-brand-300"
          >
            <AppIcon name="mail" class="h-3.5 w-3.5 text-brand-400" />
            {{ company.email }}
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>
