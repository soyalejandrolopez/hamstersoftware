<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { products, services } = useContent()

const openMenu = ref<string | null>(null)
const mobileOpen = ref(false)
const mobileAccordion = ref<string | null>(null)
const activeServiceCategory = ref<'all' | 'dataAi' | 'software' | 'cloudInfra' | 'automation'>('all')

const serviceCategoryMap: Record<string, 'dataAi' | 'software' | 'cloudInfra' | 'automation'> = {
  // Datos & IA
  'ingenieria-de-datos': 'dataAi',
  'extraccion-de-datos-etl': 'dataAi',
  'visualizacion-de-datos': 'dataAi',
  'mineria-y-gestion-de-datos': 'dataAi',
  'machine-learning': 'dataAi',
  'modelos-de-lenguaje-pequeno-slms': 'dataAi',
  'bases-de-datos-vectoriales': 'dataAi',
  'chatbots-y-asistentes-virtuales': 'dataAi',
  'redes-neuronales-y-deep-learning': 'dataAi',
  'analitica-avanzada-de-negocios': 'dataAi',

  // Desarrollo de Software y Apps
  'software-de-escritorio': 'software',
  'desarrollo-movil': 'software',
  'sistemas-bajo-demanda': 'software',
  'desarrollo-web': 'software',

  // Cloud, Infraestructura y DevOps
  'nube-y-arquitectura-cloud': 'cloudInfra',
  'computacion-y-servidores': 'cloudInfra',
  'devops-y-cicd': 'cloudInfra',

  // Automatización y Gestión de TI
  'automatizacion-empresarial-rpa': 'automation',
  'operaciones-de-negocios-bpm': 'automation',
  'gestion-de-activos-de-ti': 'automation',
  'automatizacion-de-ti': 'automation'
}

const serviceCategories = computed(() => {
  const all = services.value || []

  const dataAiServices = all.filter(
    (s) => serviceCategoryMap[s.id] === 'dataAi' || (!serviceCategoryMap[s.id] && (s.slug.includes('data') || s.slug.includes('learning') || s.slug.includes('ai') || s.slug.includes('analytics') || s.slug.includes('chatbots') || s.slug.includes('etl')))
  )

  const softwareServices = all.filter(
    (s) => serviceCategoryMap[s.id] === 'software' || (s.slug.includes('web') || s.slug.includes('mobile') || s.slug.includes('desktop') || s.slug.includes('on-demand'))
  )

  const cloudServices = all.filter(
    (s) => serviceCategoryMap[s.id] === 'cloudInfra' || (s.slug.includes('cloud') || s.slug.includes('servers') || s.slug.includes('devops'))
  )

  const automationServices = all.filter(
    (s) => serviceCategoryMap[s.id] === 'automation' || (s.slug.includes('automation') || s.slug.includes('bpm') || s.slug.includes('it-assets'))
  )

  return [
    {
      key: 'dataAi' as const,
      label: t('nav.categories.dataAi'),
      icon: 'brain',
      badgeClass: 'border-purple-200/80 bg-purple-50 text-purple-600',
      services: dataAiServices
    },
    {
      key: 'software' as const,
      label: t('nav.categories.software'),
      icon: 'code',
      badgeClass: 'border-blue-200/80 bg-blue-50 text-blue-600',
      services: softwareServices
    },
    {
      key: 'cloudInfra' as const,
      label: t('nav.categories.cloudInfra'),
      icon: 'cloud',
      badgeClass: 'border-sky-200/80 bg-sky-50 text-sky-600',
      services: cloudServices
    },
    {
      key: 'automation' as const,
      label: t('nav.categories.automation'),
      icon: 'zap',
      badgeClass: 'border-amber-200/80 bg-amber-50 text-amber-600',
      services: automationServices
    }
  ]
})

const filteredServices = computed(() => {
  if (activeServiceCategory.value === 'all') return services.value
  const found = serviceCategories.value.find((c) => c.key === activeServiceCategory.value)
  return found ? found.services : services.value
})

const navItems = computed(() => [
  { key: 'soluciones', label: t('nav.soluciones'), children: products.value },
  { key: 'servicios', label: t('nav.servicios'), children: services.value },
  { key: 'industrias', label: t('nav.industrias'), href: '#industrias' },
  { key: 'proceso', label: t('nav.proceso'), href: '#proceso' },
  { key: 'contacto', label: t('nav.contacto'), href: '#contacto' }
])

function closeAll() {
  openMenu.value = null
  mobileOpen.value = false
  mobileAccordion.value = null
}

function toggleMobileMenu() {
  if (mobileOpen.value) {
    closeAll()
  } else {
    openMenu.value = null
    mobileOpen.value = true
  }
}

function onKeydown(e: KeyboardEvent) {
  if (e.key === 'Escape') closeAll()
}

onMounted(() => {
  window.addEventListener('keydown', onKeydown)
})

onBeforeUnmount(() => {
  window.removeEventListener('keydown', onKeydown)
})
</script>

<template>
  <header
    class="fixed inset-x-0 top-0 z-50 border-b border-slate-200/80 bg-white shadow-[0_4px_20px_-4px_rgba(15,23,42,0.06)] transition-all duration-300"
    @mouseleave="openMenu = null"
  >
    <div class="container-site relative flex h-16 items-center justify-between gap-4 lg:h-[4.5rem]">
      <!-- Logo -->
      <NuxtLinkLocale to="/" class="group flex shrink-0 items-center gap-2.5" @click="closeAll">
        <AppLogo gid="logo-header" class="h-9 w-9 drop-shadow-sm transition-transform duration-300 group-hover:scale-105" />
        <span class="font-display text-lg font-bold tracking-tight text-slate-900 transition-colors duration-300">
          Hamster<span class="text-brand-600">Software</span>
        </span>
      </NuxtLinkLocale>

      <!-- Navegación de escritorio -->
      <nav class="hidden items-center gap-1 lg:flex">
        <template v-for="item in navItems" :key="item.key">
          <button
            v-if="'children' in item"
            class="relative flex items-center gap-1.5 rounded-xl px-3.5 py-2 text-sm font-medium transition-all"
            :class="
              openMenu === item.key
                ? 'bg-brand-50 text-brand-700 shadow-relief-sm'
                : 'text-slate-700 hover:bg-slate-100/70 hover:text-slate-900'
            "
            :aria-expanded="openMenu === item.key"
            aria-haspopup="true"
            @mouseenter="openMenu = item.key"
            @click="openMenu = openMenu === item.key ? null : item.key"
          >
            {{ item.label }}
            <AppIcon
              name="chevron-down"
              class="h-4 w-4 transition-transform duration-200"
              :class="openMenu === item.key ? 'rotate-180 text-brand-600' : 'text-slate-400'"
            />
          </button>
          <a
            v-else
            :href="item.href"
            class="rounded-xl px-3.5 py-2 text-sm font-medium text-slate-700 transition-all hover:bg-slate-100/70 hover:text-brand-700"
            @click="closeAll"
          >
            {{ item.label }}
          </a>
        </template>
      </nav>

      <!-- Acciones -->
      <div class="hidden items-center gap-3 lg:flex">
        <LangSwitcher />
        <a href="#contacto" class="btn btn-primary btn-md" @click="closeAll">
          {{ t('nav.contactSales') }}
        </a>
      </div>

      <!-- Toggle móvil -->
      <button
        class="flex h-10 w-10 items-center justify-center rounded-xl text-slate-700 transition-colors hover:bg-slate-100 lg:hidden"
        :aria-label="mobileOpen ? t('nav.closeMenu') : t('nav.openMenu')"
        :aria-expanded="mobileOpen"
        aria-controls="mobile-menu"
        @click="toggleMobileMenu"
      >
        <AppIcon :name="mobileOpen ? 'close' : 'menu'" class="h-6 w-6" />
      </button>
    </div>

    <!-- Mega menú de escritorio con fondo blanco sólido y relieve -->
    <Transition name="dropdown">
      <div
        v-if="openMenu && !mobileOpen"
        class="absolute inset-x-0 top-full hidden border-b border-slate-200/80 bg-white shadow-2xl shadow-slate-900/15 lg:block"
      >
        <div class="container-site py-8">
          <div class="mb-6 flex items-center justify-between gap-4 border-b border-slate-100 pb-3">
            <p class="font-display text-sm font-bold uppercase tracking-wider text-slate-900">
              {{ openMenu === 'soluciones' ? t('nav.soluciones') : t('nav.servicios') }}
            </p>
            <NuxtLinkLocale
              :to="openMenu === 'soluciones' ? '/soluciones' : '/servicios'"
              class="inline-flex items-center gap-1.5 rounded-full border border-brand-200/70 bg-brand-50 px-3 py-1 text-xs font-bold text-brand-700 shadow-relief-sm transition-all hover:bg-brand-100"
              @click="closeAll"
            >
              {{ openMenu === 'soluciones' ? t('detail.viewAllProducts') : t('detail.viewAllServices') }}
              <AppIcon name="arrow-right" class="h-3 w-3" />
            </NuxtLinkLocale>
          </div>
          <!-- Contenido Mega Menú: Soluciones (18 items) -->
          <div v-if="openMenu === 'soluciones'" class="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-4">
            <NuxtLinkLocale
              v-for="p in products"
              :key="p.name"
              :to="`/soluciones/${p.slug}`"
              class="group flex items-start gap-3.5 rounded-2xl border border-slate-100 bg-white/70 p-3 transition-all duration-200 hover:-translate-y-0.5 hover:border-brand-200 hover:bg-slate-50/80 hover:shadow-relief-sm"
              @click="closeAll"
            >
              <span
                class="mt-0.5 flex h-10 w-10 shrink-0 items-center justify-center rounded-xl border border-brand-100/80 bg-brand-50/70 text-brand-600 shadow-inner transition-colors duration-200 group-hover:border-brand-600 group-hover:bg-brand-600 group-hover:text-white"
              >
                <AppIcon :name="p.icon" class="h-5 w-5" />
              </span>
              <span class="min-w-0">
                <span class="block truncate text-sm font-bold text-slate-900 group-hover:text-brand-700">
                  {{ p.name }}
                </span>
                <span class="mt-0.5 block line-clamp-1 text-xs text-slate-500">{{ p.subtitle }}</span>
              </span>
            </NuxtLinkLocale>
          </div>

          <!-- Contenido Mega Menú: Servicios (22 items organizados por categorías de ingeniería) -->
          <div v-else class="space-y-6">
            <!-- Tabs / Selector de categoría rápida -->
            <div class="flex flex-wrap items-center gap-2 border-b border-slate-100 pb-3">
              <button
                type="button"
                class="inline-flex items-center gap-1.5 rounded-xl px-3.5 py-1.5 text-xs font-semibold transition-all duration-200"
                :class="
                  activeServiceCategory === 'all'
                    ? 'bg-brand-600 text-white shadow-relief-sm'
                    : 'bg-slate-100/80 text-slate-600 hover:bg-slate-200/70 hover:text-slate-900'
                "
                @click="activeServiceCategory = 'all'"
              >
                <AppIcon name="layers" class="h-3.5 w-3.5" />
                {{ t('nav.categories.all') }}
                <span
                  class="ml-1 rounded-full px-1.5 py-0.2 text-[10px]"
                  :class="activeServiceCategory === 'all' ? 'bg-white/20 text-white' : 'bg-slate-200 text-slate-700'"
                >
                  {{ services.length }}
                </span>
              </button>

              <button
                v-for="cat in serviceCategories"
                :key="cat.key"
                type="button"
                class="inline-flex items-center gap-1.5 rounded-xl px-3.5 py-1.5 text-xs font-semibold transition-all duration-200"
                :class="
                  activeServiceCategory === cat.key
                    ? 'bg-brand-600 text-white shadow-relief-sm'
                    : 'bg-slate-100/80 text-slate-600 hover:bg-slate-200/70 hover:text-slate-900'
                "
                @click="activeServiceCategory = cat.key"
              >
                <AppIcon :name="cat.icon" class="h-3.5 w-3.5" />
                {{ cat.label }}
                <span
                  class="ml-1 rounded-full px-1.5 py-0.2 text-[10px]"
                  :class="activeServiceCategory === cat.key ? 'bg-white/20 text-white' : 'bg-slate-200 text-slate-700'"
                >
                  {{ cat.services.length }}
                </span>
              </button>
            </div>

            <!-- Vista 1: Todas las categorías en columnas estructuradas -->
            <div
              v-if="activeServiceCategory === 'all'"
              class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4"
            >
              <div
                v-for="cat in serviceCategories"
                :key="cat.key"
                class="flex flex-col rounded-2xl border border-slate-100/80 bg-slate-50/50 p-4 transition-all hover:border-slate-200 hover:bg-slate-50"
              >
                <!-- Cabecera de Categoría -->
                <div class="mb-3.5 flex items-center gap-2.5 border-b border-slate-200/60 pb-2.5">
                  <span
                    class="flex h-7 w-7 items-center justify-center rounded-lg border text-xs shadow-inner"
                    :class="cat.badgeClass"
                  >
                    <AppIcon :name="cat.icon" class="h-4 w-4" />
                  </span>
                  <div>
                    <h4 class="font-display text-xs font-bold uppercase tracking-wider text-slate-900">
                      {{ cat.label }}
                    </h4>
                    <span class="text-[11px] text-slate-500 font-medium">
                      {{ cat.services.length }} servicios especializados
                    </span>
                  </div>
                </div>

                <!-- Lista de Servicios en esta categoría -->
                <div class="space-y-1">
                  <NuxtLinkLocale
                    v-for="s in cat.services"
                    :key="s.id"
                    :to="`/servicios/${s.slug}`"
                    class="group flex items-center justify-between rounded-xl p-2 transition-all duration-200 hover:bg-white hover:shadow-relief-sm"
                    @click="closeAll"
                  >
                    <div class="flex min-w-0 items-center gap-2.5">
                      <span
                        class="flex h-7 w-7 shrink-0 items-center justify-center rounded-lg border border-slate-200/70 bg-white text-slate-500 transition-colors duration-200 group-hover:border-brand-600 group-hover:bg-brand-600 group-hover:text-white"
                      >
                        <AppIcon :name="s.icon" class="h-3.5 w-3.5" />
                      </span>
                      <span class="truncate text-xs font-semibold text-slate-700 group-hover:text-brand-700">
                        {{ s.title }}
                      </span>
                    </div>
                    <AppIcon
                      name="arrow-right"
                      class="h-3 w-3 shrink-0 text-slate-300 opacity-0 transition-all duration-200 group-hover:translate-x-0.5 group-hover:text-brand-600 group-hover:opacity-100"
                    />
                  </NuxtLinkLocale>
                </div>
              </div>
            </div>

            <!-- Vista 2: Filtrado por categoría específica con tarjetas enriquecidas -->
            <div
              v-else
              class="grid grid-cols-1 gap-3.5 sm:grid-cols-2 lg:grid-cols-3"
            >
              <NuxtLinkLocale
                v-for="s in filteredServices"
                :key="s.id"
                :to="`/servicios/${s.slug}`"
                class="group relative flex flex-col justify-between overflow-hidden rounded-2xl border border-slate-200/80 bg-white p-4 shadow-relief-sm transition-all duration-200 hover:-translate-y-0.5 hover:border-brand-300 hover:shadow-relief-card"
                @click="closeAll"
              >
                <div class="flex items-start gap-3.5">
                  <span
                    class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl border border-brand-100 bg-brand-50 text-brand-600 shadow-inner transition-colors duration-200 group-hover:border-brand-600 group-hover:bg-brand-600 group-hover:text-white"
                  >
                    <AppIcon :name="s.icon" class="h-5 w-5" />
                  </span>
                  <div class="min-w-0 flex-1">
                    <div class="flex items-center justify-between gap-2">
                      <span class="font-display text-sm font-bold text-slate-900 group-hover:text-brand-700">
                        {{ s.title }}
                      </span>
                      <AppIcon
                        name="arrow-up-right"
                        class="h-4 w-4 text-slate-300 transition-colors group-hover:text-brand-600"
                      />
                    </div>
                    <p class="mt-1 line-clamp-2 text-xs leading-relaxed text-slate-500">
                      {{ s.description }}
                    </p>
                  </div>
                </div>
              </NuxtLinkLocale>
            </div>
          </div>

          <!-- Banner inferior del mega menú -->
          <div
            class="mt-6 flex items-center justify-between gap-4 rounded-2xl border border-brand-200/90 bg-gradient-to-r from-brand-50/90 to-sky-50/90 px-6 py-3.5 shadow-relief-sm"
          >
            <p class="text-sm text-slate-700">
              <span class="font-bold text-slate-900">{{ t('nav.notFoundTitle') }}</span>
              {{ t('nav.notFoundDesc') }}
            </p>
            <a href="#contacto" class="btn btn-primary btn-md shrink-0" @click="closeAll">
              {{ t('nav.letsTalk') }}
            </a>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Menú móvil -->
    <Transition name="dropdown">
      <div
        id="mobile-menu"
        v-if="mobileOpen"
        class="absolute inset-x-0 top-full max-h-[calc(100vh-4rem)] overflow-y-auto border-t border-slate-100 bg-white shadow-2xl lg:hidden"
      >
        <div class="px-5 py-4">
          <div v-for="item in navItems" :key="item.key" class="border-b border-slate-100 py-1">
            <button
              v-if="'children' in item"
              class="flex w-full items-center justify-between py-3 text-left text-[15px] font-bold text-slate-900"
              @click="mobileAccordion = mobileAccordion === item.key ? null : item.key"
            >
              {{ item.label }}
              <AppIcon
                name="chevron-down"
                class="h-4 w-4 text-slate-400 transition-transform duration-200"
                :class="mobileAccordion === item.key ? 'rotate-180 text-brand-600' : ''"
              />
            </button>
            <div v-if="'children' in item && mobileAccordion === item.key" class="pb-3">
              <NuxtLinkLocale
                v-for="child in item.children"
                :key="child.id || child.name"
                :to="item.key === 'servicios' ? `/servicios/${child.slug}` : `/soluciones/${child.slug}`"
                class="flex items-center gap-2.5 rounded-xl px-3 py-2 text-sm text-slate-600 hover:bg-slate-50 hover:text-brand-700"
                @click="closeAll"
              >
                <AppIcon :name="child.icon" class="h-4 w-4 shrink-0 text-brand-500" />
                <span class="truncate">{{ child.name || child.title }}</span>
              </NuxtLinkLocale>
              <NuxtLinkLocale
                :to="item.key === 'servicios' ? '/servicios' : '/soluciones'"
                class="mt-1 flex items-center gap-2.5 rounded-xl px-3 py-2 text-sm font-bold text-brand-600 hover:bg-brand-50"
                @click="closeAll"
              >
                {{ item.key === 'servicios' ? t('detail.viewAllServices') : t('detail.viewAllProducts') }}
                <AppIcon name="arrow-right" class="h-4 w-4" />
              </NuxtLinkLocale>
            </div>
            <a
              v-else
              :href="item.href"
              class="block py-3 text-[15px] font-bold text-slate-900"
              @click="closeAll"
            >
              {{ item.label }}
            </a>
          </div>
          <div class="mt-4 flex flex-col gap-3 pb-6">
            <LangSwitcher mobile />
            <a href="#contacto" class="btn btn-primary btn-md w-full" @click="closeAll">
              {{ t('nav.contactSales') }}
            </a>
            <a href="#contacto" class="btn btn-outline btn-md w-full" @click="closeAll">
              {{ t('hero.ctaPrimary') }}
            </a>
          </div>
        </div>
      </div>
    </Transition>
  </header>
</template>
