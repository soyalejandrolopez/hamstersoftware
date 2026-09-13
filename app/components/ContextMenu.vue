<script setup lang="ts">
import { company } from '~/data/config'

const { t } = useI18n()
const localePath = useLocalePath()
const router = useRouter()

const visible = ref(false)
const x = ref(0)
const y = ref(0)
const copied = ref(false)
const menuRef = ref<HTMLElement | null>(null)

function onContextMenu(e: MouseEvent) {
  // Evitar menú nativo
  e.preventDefault()

  const menuWidth = 230
  const menuHeight = 240
  const padding = 12

  let posX = e.clientX
  let posY = e.clientY

  if (posX + menuWidth > window.innerWidth - padding) {
    posX = window.innerWidth - menuWidth - padding
  }
  if (posY + menuHeight > window.innerHeight - padding) {
    posY = window.innerHeight - menuHeight - padding
  }

  x.value = Math.max(padding, posX)
  y.value = Math.max(padding, posY)
  visible.value = true
}

function closeMenu() {
  visible.value = false
}

function handleGoTo(path: string) {
  closeMenu()
  router.push(localePath(path))
}

function handleScrollTop() {
  closeMenu()
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

async function handleCopyUrl() {
  try {
    await navigator.clipboard.writeText(window.location.href)
    copied.value = true
    setTimeout(() => {
      copied.value = false
      closeMenu()
    }, 1200)
  } catch {
    closeMenu()
  }
}

const whatsappUrl = computed(() => {
  return `https://wa.me/${company.whatsappNumber}?text=${encodeURIComponent(
    t('contact.whatsappGreeting', { name: company.name })
  )}`
})

function onGlobalClick(e: MouseEvent) {
  if (menuRef.value && !menuRef.value.contains(e.target as Node)) {
    closeMenu()
  }
}

function onKeyDown(e: KeyboardEvent) {
  if (e.key === 'Escape') {
    closeMenu()
  }
}

onMounted(() => {
  window.addEventListener('contextmenu', onContextMenu)
  window.addEventListener('click', onGlobalClick)
  window.addEventListener('scroll', closeMenu, { passive: true })
  window.addEventListener('keydown', onKeyDown)
})

onUnmounted(() => {
  window.removeEventListener('contextmenu', onContextMenu)
  window.removeEventListener('click', onGlobalClick)
  window.removeEventListener('scroll', closeMenu)
  window.removeEventListener('keydown', onKeyDown)
})
</script>

<template>
  <Teleport to="body">
    <Transition
      enter-active-class="transition duration-150 ease-out"
      enter-from-class="scale-95 opacity-0"
      enter-to-class="scale-100 opacity-100"
      leave-active-class="transition duration-100 ease-in"
      leave-from-class="scale-100 opacity-100"
      leave-to-class="scale-95 opacity-0"
    >
      <div
        v-if="visible"
        ref="menuRef"
        class="fixed z-[9999] w-60 overflow-hidden rounded-2xl border border-slate-700/60 bg-ink-950/95 p-1.5 text-slate-200 shadow-2xl backdrop-blur-xl"
        :style="{ left: `${x}px`, top: `${y}px` }"
        @click.stop
      >
        <!-- Cabecera de marca -->
        <div class="flex items-center gap-2.5 px-3 py-2 border-b border-white/10 mb-1">
          <AppLogo gid="logo-context" class="h-5 w-5 drop-shadow" />
          <span class="font-display text-xs font-bold text-white tracking-wide">
            Hamster<span class="text-brand-400">Software</span>
          </span>
        </div>

        <!-- Opciones del menú -->
        <div class="space-y-0.5 text-xs font-medium">
          <button
            type="button"
            class="flex w-full items-center gap-2.5 rounded-xl px-3 py-2 text-left transition-colors hover:bg-white/10 hover:text-white"
            @click="handleGoTo('/servicios')"
          >
            <AppIcon name="layers" class="h-4 w-4 text-brand-400" />
            <span>{{ t('contextMenu.services') }}</span>
          </button>

          <button
            type="button"
            class="flex w-full items-center gap-2.5 rounded-xl px-3 py-2 text-left transition-colors hover:bg-white/10 hover:text-white"
            @click="handleGoTo('/soluciones')"
          >
            <AppIcon name="puzzle" class="h-4 w-4 text-indigo-400" />
            <span>{{ t('contextMenu.solutions') }}</span>
          </button>

          <div class="my-1 border-t border-white/10" />

          <button
            type="button"
            class="flex w-full items-center gap-2.5 rounded-xl px-3 py-2 text-left transition-colors hover:bg-white/10 hover:text-white"
            @click="handleCopyUrl"
          >
            <AppIcon :name="copied ? 'check' : 'copy'" class="h-4 w-4 text-slate-400" />
            <span>{{ copied ? t('contextMenu.copied') : t('contextMenu.copyUrl') }}</span>
          </button>

          <a
            :href="whatsappUrl"
            target="_blank"
            rel="noopener noreferrer"
            class="flex w-full items-center gap-2.5 rounded-xl px-3 py-2 text-left transition-colors hover:bg-white/10 hover:text-white"
            @click="closeMenu"
          >
            <AppIcon name="whatsapp" class="h-4 w-4 text-emerald-400" />
            <span>{{ t('contextMenu.contact') }}</span>
          </a>

          <button
            type="button"
            class="flex w-full items-center gap-2.5 rounded-xl px-3 py-2 text-left transition-colors hover:bg-white/10 hover:text-white"
            @click="handleScrollTop"
          >
            <AppIcon name="arrow-up" class="h-4 w-4 text-slate-400" />
            <span>{{ t('contextMenu.scrollTop') }}</span>
          </button>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>
