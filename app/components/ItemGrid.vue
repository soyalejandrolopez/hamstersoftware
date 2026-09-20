<script setup lang="ts">
interface GridItem {
  slug: string
  icon: string
  name: string
  subtitle?: string
  description?: string
}

defineProps<{
  items: GridItem[]
  basePath: string
}>()

const { t } = useI18n()

const cardColors = [
  { iconBg: 'bg-brand-50', iconColor: 'text-brand-600', hoverBg: 'group-hover:bg-brand-600' },
  { iconBg: 'bg-slate-50', iconColor: 'text-slate-600', hoverBg: 'group-hover:bg-slate-600' },
  { iconBg: 'bg-sky-50', iconColor: 'text-sky-600', hoverBg: 'group-hover:bg-sky-600' },
  { iconBg: 'bg-emerald-50', iconColor: 'text-emerald-600', hoverBg: 'group-hover:bg-emerald-600' }
]
</script>

<template>
  <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
    <NuxtLinkLocale
      v-for="(item, i) in items"
      :key="item.slug"
      :to="`/${basePath}/${item.slug}`"
      class="group relative flex flex-col overflow-hidden rounded-2xl border border-slate-200/85 bg-white p-7 shadow-relief-card transition-all duration-300 hover:-translate-y-1.5 hover:border-brand-300/80 hover:shadow-relief-card-hover"
    >
      <!-- Top micro gradient border -->
      <div
        class="absolute inset-x-0 top-0 h-1 opacity-0 transition-opacity duration-300 group-hover:opacity-100"
        style="background: linear-gradient(90deg, #2563eb, #06b6d4)"
      />

      <div class="flex items-start justify-between gap-3">
        <div class="flex items-center gap-3.5 min-w-0">
          <span
            class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl border border-slate-100 shadow-inner transition-all duration-300 group-hover:scale-105 group-hover:shadow-md group-hover:!text-white"
            :class="[
              cardColors[i % cardColors.length]!.iconBg,
              cardColors[i % cardColors.length]!.iconColor,
              cardColors[i % cardColors.length]!.hoverBg
            ]"
          >
            <AppIcon :name="item.icon" class="h-6 w-6 transition-colors duration-300 group-hover:text-white" />
          </span>
          <div class="min-w-0">
            <h3 class="font-display text-lg font-bold text-slate-900 transition-colors group-hover:text-brand-700 leading-snug">
              {{ item.name }}
            </h3>
            <p v-if="item.subtitle" class="text-xs font-semibold uppercase tracking-wider text-brand-600 truncate">
              {{ item.subtitle }}
            </p>
          </div>
        </div>
        <span
          class="shrink-0 rounded-lg border border-slate-200/60 bg-slate-50/80 px-2.5 py-1 font-display text-xs font-bold text-slate-400 shadow-inner transition-colors duration-300 group-hover:border-brand-200 group-hover:bg-brand-50 group-hover:text-brand-600"
        >
          {{ String(i + 1).padStart(2, '0') }}
        </span>
      </div>

      <p v-if="item.description" class="mt-4 text-sm leading-relaxed text-slate-600">
        {{ item.description }}
      </p>

      <span
        class="mt-auto inline-flex items-center gap-1.5 border-t border-slate-100 pt-5 text-sm font-semibold text-brand-600"
      >
        <span class="text-slate-400 transition-colors duration-300 group-hover:text-brand-600">
          {{ t('common.viewMore') }}
        </span>
        <AppIcon
          name="arrow-right"
          class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
        />
      </span>
    </NuxtLinkLocale>
  </div>
</template>
