<script setup lang="ts">
import { company } from '~/data/config'
import { getOfflineChatReply } from '~/utils/offlineChat'

const { t, tm, rt, locale } = useI18n()

interface UiMessage {
  role: 'user' | 'bot'
  text: string
}

const open = ref(false)
const input = ref('')
const messages = ref<UiMessage[]>([])
const loading = ref(false)
const scrollEl = ref<HTMLElement | null>(null)

const quickQuestions = computed(() => {
  // `tm` devuelve el array crudo (compilado como nodos AST en el cliente);
  // se resuelve cada elemento con `rt` para obtener strings.
  const q = tm('chat.quickQuestions')
  return Array.isArray(q) ? q.map((item) => rt(item)) : []
})

const greeting = computed(() => t('chat.greeting'))

function openChat() {
  open.value = true
  if (messages.value.length === 0) {
    messages.value.push({ role: 'bot', text: greeting.value })
  }
}

function closeChat() {
  open.value = false
}

async function scrollToBottom() {
  await nextTick()
  if (scrollEl.value) {
    scrollEl.value.scrollTop = scrollEl.value.scrollHeight
  }
}

async function send(text?: string) {
  const content = (text ?? input.value).trim()
  if (!content || loading.value) return

  messages.value.push({ role: 'user', text: content })
  input.value = ''
  loading.value = true
  await scrollToBottom()

  // Simulación fluida de respuesta offline
  await new Promise((resolve) => setTimeout(resolve, 400))

  try {
    const reply = getOfflineChatReply(content, locale.value)
    messages.value.push({ role: 'bot', text: reply })
  } catch {
    messages.value.push({ role: 'bot', text: t('chat.error') })
  } finally {
    loading.value = false
    await scrollToBottom()
  }
}

function onKeydown(e: KeyboardEvent) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    send()
  }
}
</script>

<template>
  <div class="fixed bottom-5 right-5 z-[60] sm:bottom-6 sm:right-6">
    <!-- Panel de chat con alto relieve -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 translate-y-4 scale-95"
      enter-to-class="opacity-100 translate-y-0 scale-100"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0 scale-100"
      leave-to-class="opacity-0 translate-y-4 scale-95"
    >
      <div
        v-if="open"
        class="mb-4 flex h-[490px] w-[min(92vw,390px)] flex-col overflow-hidden rounded-3xl border border-slate-200/90 bg-white shadow-[0_25px_60px_-15px_rgba(0,0,0,0.35),inset_0_1px_0_rgba(255,255,255,1)]"
        role="dialog"
        aria-label="Chat de Hamster Software"
      >
        <!-- Encabezado oscuro con relieve -->
        <div class="relative flex items-center gap-3 bg-gradient-to-r from-ink-950 via-slate-900 to-ink-950 px-5 py-4 border-b border-white/10">
          <div class="pointer-events-none absolute inset-0 bg-grid-dark opacity-35" />
          <AppLogo gid="logo-chat" class="relative h-9 w-9 drop-shadow" />
          <div class="relative min-w-0 flex-1">
            <p class="font-display text-sm font-bold text-white">Hamster<span class="text-brand-400">Software</span></p>
            <p class="flex items-center gap-1.5 text-[11px] font-semibold text-emerald-400">
              <span class="h-2 w-2 animate-pulse-dot rounded-full bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.9)]" />
              {{ t('chat.online') }}
            </p>
          </div>
          <button
            class="relative flex h-8 w-8 items-center justify-center rounded-xl text-slate-300 transition-colors hover:bg-white/10 hover:text-white"
            aria-label="Cerrar chat"
            @click="closeChat"
          >
            <AppIcon name="close" class="h-5 w-5" />
          </button>
        </div>

        <!-- Mensajes -->
        <div ref="scrollEl" class="flex-1 space-y-3 overflow-y-auto bg-slate-50/70 p-4">
          <div
            v-for="(m, i) in messages"
            :key="i"
            class="flex"
            :class="m.role === 'user' ? 'justify-end' : 'justify-start'"
          >
            <div
              v-if="m.role === 'bot'"
              class="mr-2 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-brand-100 shadow-inner"
            >
              <AppLogo gid="logo-msg" class="h-4.5 w-4.5" />
            </div>
            <div
              class="max-w-[80%] whitespace-pre-line rounded-2xl px-4 py-2.5 text-sm leading-relaxed"
              :class="
                m.role === 'user'
                  ? 'rounded-br-sm bg-gradient-to-r from-brand-600 to-indigo-700 text-white shadow-relief-btn-primary'
                  : 'rounded-bl-sm border border-slate-200/80 bg-white text-slate-700 shadow-relief-sm'
              "
            >
              {{ m.text }}
            </div>
          </div>

          <!-- Sugerencias rápidas -->
          <div v-if="messages.length === 1" class="flex flex-wrap gap-2 pt-1">
            <button
              v-for="q in quickQuestions"
              :key="q"
              class="rounded-full border border-brand-200/90 bg-white px-3.5 py-1.5 text-xs font-semibold text-brand-700 shadow-relief-sm transition-all hover:bg-brand-50 hover:shadow-md"
              @click="send(q)"
            >
              {{ q }}
            </button>
          </div>

          <!-- Escribiendo... -->
          <div v-if="loading" class="flex justify-start">
            <div class="mr-2 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-brand-100 shadow-inner">
              <AppLogo gid="logo-typing" class="h-4.5 w-4.5" />
            </div>
            <div class="flex items-center gap-1.5 rounded-2xl rounded-bl-sm border border-slate-200/80 bg-white px-4 py-3 shadow-relief-sm">
              <span class="h-2 w-2 animate-pulse-dot rounded-full bg-slate-400" />
              <span class="h-2 w-2 animate-pulse-dot rounded-full bg-slate-400" style="animation-delay: 200ms" />
              <span class="h-2 w-2 animate-pulse-dot rounded-full bg-slate-400" style="animation-delay: 400ms" />
            </div>
          </div>
        </div>

        <!-- Input -->
        <div class="border-t border-slate-200/80 bg-white p-3.5">
          <div class="flex items-end gap-2">
            <textarea
              v-model="input"
              rows="1"
              class="input min-h-[44px] max-h-28 flex-1 resize-none !py-2.5"
              :placeholder="t('chat.placeholder')"
              @keydown="onKeydown"
            />
            <button
              class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-gradient-to-r from-brand-600 to-indigo-700 text-white shadow-relief-btn-primary transition-transform hover:scale-105 disabled:cursor-not-allowed disabled:opacity-50"
              :disabled="loading || !input.trim()"
              aria-label="Enviar mensaje"
              @click="send()"
            >
              <AppIcon name="send" class="h-5 w-5" />
            </button>
          </div>
          <p class="mt-2 text-center text-[10px] text-slate-400">{{ t('chat.poweredBy') }}</p>
        </div>
      </div>
    </Transition>

    <!-- Botón flotante en alto relieve -->
    <button
      class="group relative flex h-14 w-14 items-center justify-center rounded-full bg-gradient-to-br from-brand-500 via-brand-600 to-indigo-700 text-white shadow-relief-btn-primary transition-all duration-300 hover:scale-105 hover:shadow-relief-btn-primary-hover"
      :aria-label="open ? 'Cerrar chat' : 'Abrir chat de Hamster Software'"
      @click="open ? closeChat() : openChat()"
    >
      <span
        v-if="!open"
        class="absolute inset-0 -z-10 animate-ping rounded-full bg-brand-500/40"
        style="animation-duration: 2.5s"
      />
      <AppIcon v-if="open" name="close" class="h-6 w-6" />
      <AppLogo v-else gid="logo-float" class="h-8 w-8 drop-shadow transition-transform duration-300 group-hover:rotate-6" />
    </button>
  </div>
</template>
