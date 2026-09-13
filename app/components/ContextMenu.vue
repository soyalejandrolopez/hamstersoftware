<script setup lang="ts">
import { company } from '~/data/config'

const { t } = useI18n()
const localePath = useLocalePath()
const router = useRouter()

const visible = ref(false)
const x = ref(0)
const y = ref(0)
const showCodeModal = ref(false)
const copied = ref(false)
const codeCopied = ref(false)
const menuRef = ref<HTMLElement | null>(null)

const asciiArt = `██╗  ██╗ █████╗ ███╗   ███╗███████╗████████╗███████╗██████╗     ███████╗ ██████╗ ███████╗████████╗██╗    ██╗ █████╗ ██████╗ ███████╗
██║  ██║██╔══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██╔════╝╚══██╔══╝██║    ██║██╔══██╗██╔══██╗██╔════╝
███████║███████║██╔████╔██║███████╗   ██║   █████╗  ██████╔╝    ███████╗██║   ██║█████╗     ██║   ██║ █╗ ██║███████║██████╔╝█████╗  
██╔══██║██╔══██║██║╚██╔╝██║╚════██║   ██║   ██╔══╝  ██╔══██╗    ╚════██║██║   ██║██╔══╝     ██║   ██║███╗██║██╔══██║██╔══██╗██╔══╝  
██║  ██║██║  ██║██║ ╚═╝ ██║███████║   ██║   ███████╗██║  ██║    ███████║╚██████╔╝██║        ██║   ╚███╔███╔╝██║  ██║██║  ██║███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝        ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝`

function onContextMenu(e: MouseEvent) {
  // Evitar menú nativo
  e.preventDefault()

  const menuWidth = 240
  const menuHeight = 280
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

function handleViewCode() {
  closeMenu()
  showCodeModal.value = true
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

async function handleCopyAscii() {
  try {
    await navigator.clipboard.writeText(asciiArt)
    codeCopied.value = true
    setTimeout(() => {
      codeCopied.value = false
    }, 1800)
  } catch {}
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
    showCodeModal.value = false
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
  <div>
    <!-- Menú Contextual Personalizado -->
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
          class="fixed z-[9999] w-64 overflow-hidden rounded-2xl border border-slate-700/60 bg-ink-950/95 p-1.5 text-slate-200 shadow-2xl backdrop-blur-xl"
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

          <!-- Opciones principales -->
          <div class="space-y-0.5 text-xs font-medium">
            <button
              type="button"
              class="flex w-full items-center gap-2.5 rounded-xl px-3 py-2 text-left transition-colors hover:bg-white/10 hover:text-white"
              @click="handleViewCode"
            >
              <AppIcon name="code" class="h-4 w-4 text-brand-400" />
              <span class="flex-1">{{ t('contextMenu.viewCode') }}</span>
              <span class="rounded bg-brand-500/20 px-1.5 py-0.5 text-[10px] font-mono text-brand-300">ASCII</span>
            </button>

            <button
              type="button"
              class="flex w-full items-center gap-2.5 rounded-xl px-3 py-2 text-left transition-colors hover:bg-white/10 hover:text-white"
              @click="handleGoTo('/servicios')"
            >
              <AppIcon name="layers" class="h-4 w-4 text-slate-400" />
              <span>{{ t('contextMenu.services') }}</span>
            </button>

            <button
              type="button"
              class="flex w-full items-center gap-2.5 rounded-xl px-3 py-2 text-left transition-colors hover:bg-white/10 hover:text-white"
              @click="handleGoTo('/soluciones')"
            >
              <AppIcon name="puzzle" class="h-4 w-4 text-slate-400" />
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

      <!-- Modal Visor de Código ASCII -->
      <Transition
        enter-active-class="transition duration-200 ease-out"
        enter-from-class="opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="transition duration-150 ease-in"
        leave-from-class="opacity-100"
        leave-to-class="opacity-0"
      >
        <div
          v-if="showCodeModal"
          class="fixed inset-0 z-[10000] flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm"
          @click.self="showCodeModal = false"
        >
          <div
            class="relative w-full max-w-3xl overflow-hidden rounded-2xl border border-slate-800 bg-ink-950 shadow-2xl"
          >
            <!-- Barra superior estilo terminal -->
            <div class="flex items-center justify-between border-b border-white/10 bg-slate-900/90 px-4 py-3">
              <div class="flex items-center gap-2">
                <span class="h-3 w-3 rounded-full bg-rose-500/80 inline-block" />
                <span class="h-3 w-3 rounded-full bg-amber-500/80 inline-block" />
                <span class="h-3 w-3 rounded-full bg-emerald-500/80 inline-block" />
                <span class="ml-2 font-mono text-xs text-slate-400">
                  {{ t('contextMenu.codeModalTitle') }}
                </span>
              </div>
              <div class="flex items-center gap-2">
                <button
                  type="button"
                  class="inline-flex items-center gap-1.5 rounded-lg border border-white/10 bg-white/5 px-2.5 py-1 text-xs font-medium text-slate-300 transition-colors hover:bg-white/10 hover:text-white"
                  @click="handleCopyAscii"
                >
                  <AppIcon :name="codeCopied ? 'check' : 'copy'" class="h-3.5 w-3.5 text-brand-400" />
                  {{ codeCopied ? t('contextMenu.copied') : t('contextMenu.codeModalCopy') }}
                </button>
                <button
                  type="button"
                  class="rounded-lg p-1 text-slate-400 hover:bg-white/10 hover:text-white transition-colors"
                  :aria-label="t('contextMenu.codeModalClose')"
                  @click="showCodeModal = false"
                >
                  <AppIcon name="close" class="h-4 w-4" />
                </button>
              </div>
            </div>

            <!-- Contenido ASCII -->
            <div class="overflow-x-auto p-6">
              <pre
                class="font-mono text-[11px] sm:text-xs md:text-sm font-bold leading-tight text-brand-400 selection:bg-brand-500 selection:text-white"
              >{{ asciiArt }}</pre>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>
