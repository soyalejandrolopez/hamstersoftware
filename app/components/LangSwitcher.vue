<script setup lang="ts">
withDefaults(defineProps<{ mobile?: boolean }>(), { mobile: false })

const { locale, setLocale, t } = useI18n()
const open = ref(false)
const root = ref<HTMLElement | null>(null)

const options: { code: 'es' | 'en'; label: string; short: string }[] = [
  { code: 'es', label: 'Español', short: 'ES' },
  { code: 'en', label: 'English', short: 'EN' }
]

async function switchTo(code: 'es' | 'en') {
  open.value = false
  if (code !== locale.value) {
    await setLocale(code)
  }
}

function onDocumentClick(e: MouseEvent) {
  if (root.value && !root.value.contains(e.target as Node)) {
    open.value = false
  }
}

onMounted(() => document.addEventListener('click', onDocumentClick))
onBeforeUnmount(() => document.removeEventListener('click', onDocumentClick))
</script>

<template>
  <!-- Variante móvil: dos botones -->
  <div v-if="mobile" class="flex items-center gap-2">
    <button
      v-for="opt in options"
      :key="opt.code"
      class="flex-1 rounded-lg px-4 py-2.5 text-sm font-semibold transition-colors"
      :class="
        locale === opt.code
          ? 'bg-brand-600 text-white shadow-lg shadow-brand-600/25'
          : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
      "
      @click="switchTo(opt.code)"
    >
      {{ opt.label }}
    </button>
  </div>

  <!-- Variante escritorio: dropdown -->
  <div v-else ref="root" class="relative">
    <button
      class="flex items-center gap-1.5 rounded-full border border-slate-200 bg-slate-50 px-3 py-1.5 text-xs font-bold text-slate-800 transition-colors hover:border-brand-500 hover:text-brand-600"
      :aria-expanded="open"
      aria-haspopup="true"
      :aria-label="t('nav.changeLanguage')"
      @click.stop="open = !open"
    >
      <AppIcon name="globe" class="h-3.5 w-3.5 text-brand-600" />
      {{ locale === 'es' ? 'ES' : 'EN' }}
      <AppIcon
        name="chevron-down"
        class="h-3.5 w-3.5 text-slate-500 transition-transform duration-200"
        :class="open ? 'rotate-180 text-brand-600' : ''"
      />
    </button>

    <Transition name="dropdown">
      <div
        v-if="open"
        class="absolute right-0 top-full z-50 mt-2 w-40 overflow-hidden rounded-xl border border-slate-200 bg-white py-1.5 shadow-xl"
      >
        <button
          v-for="opt in options"
          :key="opt.code"
          class="flex w-full items-center justify-between px-4 py-2 text-left text-sm font-bold transition-colors hover:bg-slate-50"
          :class="locale === opt.code ? 'text-brand-600' : 'text-slate-800'"
          @click="switchTo(opt.code)"
        >
          {{ opt.label }}
          <AppIcon v-if="locale === opt.code" name="check" class="h-4 w-4" />
        </button>
      </div>
    </Transition>
  </div>
</template>
