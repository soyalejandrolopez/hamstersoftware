<script setup lang="ts">
import { useRoute } from 'vue-router'

const { t, te } = useI18n()
const route = useRoute()

// State
const activeSectionId = ref<string>('hero')
const isExpanded = ref<boolean>(false)
const hasUserDismissed = ref<boolean>(false)
const isMounted = ref<boolean>(false)
const scrollProgress = ref<number>(0)
const hideTimer = ref<ReturnType<typeof setTimeout> | null>(null)

// Distinguish home vs detail pages
const isHomePage = computed(() => {
  const path = route.path.replace(/^\/(es|en)/, '')
  return path === '' || path === '/'
})

const isDetailPage = computed(() => {
  const path = route.path.replace(/^\/(es|en)/, '')
  return path.startsWith('/servicios/') || path.startsWith('/soluciones/')
})

// Current detail slug and type
const detailInfo = computed(() => {
  const path = route.path.replace(/^\/(es|en)/, '')
  const match = path.match(/^\/(servicios|soluciones)\/([^/]+)/)
  if (!match) return null
  return {
    type: match[1],
    slug: match[2]
  }
})

// Section definition lists
const homeSections = [
  { id: 'hero', icon: 'zap', image: '/images/hero-bg.jpg' },
  { id: 'estadisticas', icon: 'chart-bar', image: '/images/servicios/analitica-datos.jpg' },
  { id: 'servicios', icon: 'puzzle', image: '/images/servicios/desarrollo-web-a-la-medida.jpg' },
  { id: 'soluciones', icon: 'layers', image: '/images/soluciones/erp-crm-pymes.jpg' },
  { id: 'seguridad', icon: 'shield', image: '/images/servicios/auditoria-seguridad-pentesting.jpg' },
  { id: 'casos', icon: 'star', image: '/images/servicios/inteligencia-artificial-aplicada.jpg' },
  { id: 'industrias', icon: 'building', image: '/images/servicios/soluciones-cloud-devops.jpg' },
  { id: 'proceso', icon: 'repeat', image: '/images/servicios/arquitectura-software-microservicios.jpg' },
  { id: 'contacto', icon: 'message-square', image: '/images/servicios/consultoria-ti-estrategica.jpg' }
]

const detailSections = [
  { id: 'detalle-hero', key: 'hero', icon: 'zap' },
  { id: 'detalle-incluye', key: 'incluye', icon: 'check' },
  { id: 'detalle-tecnologias', key: 'tecnologias', icon: 'cpu' },
  { id: 'detalle-faq', key: 'faq', icon: 'message-square' },
  { id: 'detalle-relacionados', key: 'relacionados', icon: 'layers' },
  { id: 'detalle-contacto', key: 'contacto', icon: 'send' }
]

// Determine dynamic current section data
const currentSectionData = computed(() => {
  if (isHomePage.value) {
    const sec = homeSections.find((s) => s.id === activeSectionId.value) || homeSections[0]
    const key = `signalBeacon.home.${sec.id}`
    return {
      id: sec.id,
      tag: te(`${key}.tag`) ? t(`${key}.tag`) : 'Sección',
      title: te(`${key}.title`) ? t(`${key}.title`) : sec.id,
      desc: te(`${key}.desc`) ? t(`${key}.desc`) : '',
      image: sec.image,
      icon: sec.icon
    }
  }

  if (isDetailPage.value && detailInfo.value) {
    const sec = detailSections.find((s) => s.id === activeSectionId.value) || detailSections[0]
    const key = `signalBeacon.detail.${sec.key}`
    const imgUrl = `/images/${detailInfo.value.type}/${detailInfo.value.slug}.jpg`
    return {
      id: sec.id,
      tag: te(`${key}.tag`) ? t(`${key}.tag`) : 'Detalle',
      title: te(`${key}.title`) ? t(`${key}.title`) : sec.key,
      desc: te(`${key}.desc`) ? t(`${key}.desc`) : '',
      image: imgUrl,
      icon: sec.icon
    }
  }

  return null
})

// Calculate list of available dots for navigation
const activeSectionsList = computed(() => {
  if (isHomePage.value) {
    return homeSections.map((s) => ({
      id: s.id,
      label: te(`signalBeacon.home.${s.id}.tag`) ? t(`signalBeacon.home.${s.id}.tag`) : s.id
    }))
  }
  if (isDetailPage.value) {
    return detailSections.map((s) => ({
      id: s.id,
      label: te(`signalBeacon.detail.${s.key}.tag`) ? t(`signalBeacon.detail.${s.key}.tag`) : s.key
    }))
  }
  return []
})

// Smooth scroll to a section
function scrollToSection(id: string) {
  const el = document.getElementById(id)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}

// Temporary card preview on scroll
function triggerScrollPreview() {
  if (hasUserDismissed.value) return
  isExpanded.value = true
  if (hideTimer.value) clearTimeout(hideTimer.value)
  hideTimer.value = setTimeout(() => {
    isExpanded.value = false
  }, 4200)
}

function toggleExpand() {
  isExpanded.value = !isExpanded.value
  if (isExpanded.value) {
    hasUserDismissed.value = false
    if (hideTimer.value) clearTimeout(hideTimer.value)
  }
}

function dismiss() {
  isExpanded.value = false
  hasUserDismissed.value = true
  if (hideTimer.value) clearTimeout(hideTimer.value)
}

// Scroll & IntersectionObserver handling
let observer: IntersectionObserver | null = null

function updateScrollProgress() {
  const totalScroll = document.documentElement.scrollHeight - window.innerHeight
  if (totalScroll > 0) {
    scrollProgress.value = Math.min(100, Math.max(0, Math.round((window.scrollY / totalScroll) * 100)))
  }
}

onMounted(() => {
  isMounted.value = true
  window.addEventListener('scroll', updateScrollProgress, { passive: true })
  updateScrollProgress()

  const targetIds = isHomePage.value
    ? homeSections.map((s) => s.id)
    : detailSections.map((s) => s.id)

  observer = new IntersectionObserver(
    (entries) => {
      // Find the entry that has the highest intersection ratio or is intersecting
      const intersecting = entries.filter((e) => e.isIntersecting)
      if (intersecting.length > 0) {
        // Sort by greatest intersection ratio
        intersecting.sort((a, b) => b.intersectionRatio - a.intersectionRatio)
        const newId = intersecting[0].target.id
        if (newId && newId !== activeSectionId.value) {
          activeSectionId.value = newId
          triggerScrollPreview()
        }
      }
    },
    {
      rootMargin: '-20% 0px -40% 0px',
      threshold: [0.15, 0.4, 0.7]
    }
  )

  targetIds.forEach((id) => {
    const el = document.getElementById(id)
    if (el && observer) observer.observe(el)
  })
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
    observer = null
  }
  if (hideTimer.value) {
    clearTimeout(hideTimer.value)
  }
  if (typeof window !== 'undefined') {
    window.removeEventListener('scroll', updateScrollProgress)
  }
})

// Re-observe when route changes
watch(
  () => route.path,
  () => {
    activeSectionId.value = isHomePage.value ? 'hero' : 'detalle-hero'
    isExpanded.value = false
    hasUserDismissed.value = false

    if (observer) {
      observer.disconnect()
      const targetIds = isHomePage.value
        ? homeSections.map((s) => s.id)
        : detailSections.map((s) => s.id)

      setTimeout(() => {
        targetIds.forEach((id) => {
          const el = document.getElementById(id)
          if (el && observer) observer.observe(el)
        })
      }, 350)
    }
  }
)
</script>

<template>
  <div v-if="isMounted && currentSectionData" class="pointer-events-none fixed left-4 top-1/2 -translate-y-1/2 z-40 sm:left-6">
    <!-- Beacon radar button (always clickable) -->
    <div class="pointer-events-auto flex items-center gap-3">
      <button
        type="button"
        @click="toggleExpand"
        :aria-label="t('signalBeacon.toggle')"
        class="group relative flex h-12 w-12 items-center justify-center rounded-2xl border border-white/20 bg-slate-950/85 text-brand-400 shadow-[0_15px_35px_-5px_rgba(0,0,0,0.6),inset_0_1px_0_rgba(255,255,255,0.2)] backdrop-blur-xl transition-all duration-300 hover:scale-110 hover:border-brand-400/80 hover:text-white"
      >
        <!-- Radar ping pulse waves -->
        <span class="absolute -inset-1 rounded-2xl bg-brand-500/25 animate-ping opacity-60 pointer-events-none" />
        <span class="absolute -inset-2.5 rounded-3xl bg-brand-600/10 animate-pulse pointer-events-none" />

        <!-- Mini radial progress ring around beacon -->
        <svg class="absolute inset-0 h-full w-full -rotate-90 p-1 pointer-events-none" viewBox="0 0 36 36">
          <path
            class="text-white/10"
            stroke-width="2.5"
            stroke="currentColor"
            fill="none"
            d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
          />
          <path
            class="text-brand-400 transition-all duration-300"
            stroke-dasharray="100, 100"
            :stroke-dashoffset="100 - scrollProgress"
            stroke-width="2.5"
            stroke-linecap="round"
            stroke="currentColor"
            fill="none"
            d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
          />
        </svg>

        <!-- Dynamic Icon inside Beacon -->
        <AppIcon :name="currentSectionData.icon || 'zap'" class="relative h-5 w-5 drop-shadow transition-transform duration-300 group-hover:scale-110" />

        <!-- Active signal live dot -->
        <span class="absolute -top-1 -right-1 flex h-3.5 w-3.5">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-3.5 w-3.5 bg-emerald-500 border-2 border-slate-950"></span>
        </span>
      </button>

      <!-- Side dots navigation column (visible when hovering near beacon on desktop) -->
      <div class="hidden lg:flex flex-col gap-1.5 rounded-full border border-white/10 bg-slate-950/70 p-1.5 shadow-relief-dark backdrop-blur-md">
        <button
          v-for="s in activeSectionsList"
          :key="s.id"
          type="button"
          @click="scrollToSection(s.id)"
          :title="s.label"
          class="group relative flex h-2.5 w-2.5 items-center justify-center rounded-full transition-all"
        >
          <span
            class="h-1.5 w-1.5 rounded-full transition-all duration-300"
            :class="activeSectionId === s.id ? 'h-3 w-3 bg-brand-400 shadow-[0_0_8px_rgba(56,189,248,0.9)]' : 'bg-white/20 hover:bg-white/60'"
          />
        </button>
      </div>
    </div>

    <!-- Explanatory Signal Card (Shows preview image and what the section means) -->
    <Transition
      enter-active-class="transition-all duration-400 cubic-bezier(0.16, 1, 0.3, 1)"
      enter-from-class="opacity-0 -translate-x-6 scale-90"
      enter-to-class="opacity-100 translate-x-0 scale-100"
      leave-active-class="transition-all duration-300 ease-in"
      leave-from-class="opacity-100 translate-x-0 scale-100"
      leave-to-class="opacity-0 -translate-x-6 scale-90"
    >
      <div
        v-if="isExpanded && currentSectionData"
        class="pointer-events-auto absolute left-16 top-1/2 -translate-y-1/2 w-[310px] sm:w-[350px] overflow-hidden rounded-3xl border border-white/20 bg-slate-950/90 p-4 shadow-[0_30px_70px_-10px_rgba(0,0,0,0.8),inset_0_1px_0_rgba(255,255,255,0.25)] backdrop-blur-2xl"
      >
        <!-- Top header bar of signal card -->
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
          <div class="flex items-center gap-2">
            <span class="relative flex h-2.5 w-2.5">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
            </span>
            <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-brand-400">
              {{ t('signalBeacon.badge') }}
            </span>
          </div>

          <button
            type="button"
            @click="dismiss"
            :title="t('signalBeacon.close')"
            class="flex h-6 w-6 items-center justify-center rounded-lg border border-white/10 bg-white/5 text-slate-400 transition-colors hover:bg-white/15 hover:text-white"
          >
            <AppIcon name="close" class="h-3 w-3" />
          </button>
        </div>

        <!-- Section Image Showcase -->
        <div class="relative mt-3 aspect-[16/10] w-full overflow-hidden rounded-2xl border border-white/10 bg-slate-900">
          <img
            :src="currentSectionData.image"
            :alt="currentSectionData.title"
            class="h-full w-full object-cover object-center transition-transform duration-700 hover:scale-105"
            loading="lazy"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-950/20 to-transparent pointer-events-none" />

          <!-- Tag overlay on image -->
          <div class="absolute bottom-2.5 left-2.5 right-2.5 flex items-center justify-between">
            <span class="inline-flex items-center gap-1.5 rounded-full border border-white/20 bg-ink-950/80 px-2.5 py-0.5 text-[11px] font-semibold text-white backdrop-blur-md">
              <AppIcon :name="currentSectionData.icon || 'zap'" class="h-3 w-3 text-brand-400" />
              {{ currentSectionData.tag }}
            </span>
            <span class="rounded-md bg-brand-500/20 px-2 py-0.5 text-[10px] font-mono font-bold text-brand-300 border border-brand-500/30">
              {{ scrollProgress }}%
            </span>
          </div>
        </div>

        <!-- Section Meaning / Explanation (Lo que quiere decir) -->
        <div class="mt-3.5 space-y-1.5">
          <h4 class="font-display text-sm font-bold text-white leading-snug">
            {{ currentSectionData.title }}
          </h4>
          <p class="text-xs text-slate-300 leading-relaxed line-clamp-3">
            {{ currentSectionData.desc }}
          </p>
        </div>

        <!-- Action Footer -->
        <div class="mt-3.5 pt-3 border-t border-white/10 flex items-center justify-between">
          <button
            type="button"
            @click="scrollToSection(currentSectionData.id)"
            class="inline-flex items-center gap-1 text-[11px] font-bold text-brand-400 hover:text-brand-300 transition-colors"
          >
            <span>{{ t('signalBeacon.jump') }}</span>
            <AppIcon name="arrow-up-right" class="h-3 w-3" />
          </button>

          <span class="text-[10px] font-mono text-slate-400">
            #{{ currentSectionData.id }}
          </span>
        </div>
      </div>
    </Transition>
  </div>
</template>
