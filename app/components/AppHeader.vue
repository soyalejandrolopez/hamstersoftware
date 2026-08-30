<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { products, services } = useContent()

const openMenu = ref<string | null>(null)
const mobileOpen = ref(false)
const mobileAccordion = ref<string | null>(null)

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
          <div v-if="openMenu === 'soluciones'" class="grid grid-cols-4 gap-x-6 gap-y-2">
            <NuxtLinkLocale
              v-for="p in products"
              :key="p.name"
              :to="`/soluciones/${p.slug}`"
              class="group flex items-start gap-3 rounded-2xl border border-transparent p-3.5 transition-all hover:border-slate-200/80 hover:bg-slate-50/80 hover:shadow-relief-sm"
              @click="closeAll"
            >
              <span
                class="mt-0.5 flex h-10 w-10 shrink-0 items-center justify-center rounded-xl border border-brand-100 bg-brand-50 text-brand-600 shadow-inner transition-colors duration-200 group-hover:border-brand-600 group-hover:bg-brand-600 group-hover:text-white"
              >
                <AppIcon :name="p.icon" class="h-5 w-5" />
              </span>
              <span>
                <span class="block text-sm font-bold text-slate-900 group-hover:text-brand-700">
                  {{ p.name }}
                </span>
                <span class="mt-0.5 block text-xs text-slate-500">{{ p.subtitle }}</span>
              </span>
            </NuxtLinkLocale>
          </div>
          <div v-else class="grid grid-cols-3 gap-x-6 gap-y-2">
            <NuxtLinkLocale
              v-for="s in services"
              :key="s.id"
              :to="`/servicios/${s.slug}`"
              class="group flex items-start gap-3 rounded-2xl border border-transparent p-3.5 transition-all hover:border-slate-200/80 hover:bg-slate-50/80 hover:shadow-relief-sm"
              @click="closeAll"
            >
              <span
                class="mt-0.5 flex h-10 w-10 shrink-0 items-center justify-center rounded-xl border border-brand-100 bg-brand-50 text-brand-600 shadow-inner transition-colors duration-200 group-hover:border-brand-600 group-hover:bg-brand-600 group-hover:text-white"
              >
                <AppIcon :name="s.icon" class="h-5 w-5" />
              </span>
              <span class="block text-sm font-bold text-slate-900 group-hover:text-brand-700">
                {{ s.title }}
              </span>
            </NuxtLinkLocale>
          </div>
          <div
            class="mt-6 flex items-center justify-between gap-4 rounded-2xl border border-brand-200/90 bg-gradient-to-r from-brand-50/90 to-sky-50/90 px-6 py-4 shadow-relief-sm"
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
