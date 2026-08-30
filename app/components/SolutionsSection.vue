<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { products } = useContent()

const items = computed(() =>
  products.value.map((p) => ({
    slug: p.slug,
    icon: p.icon,
    name: p.name,
    subtitle: p.subtitle,
    description: p.description
  }))
)
</script>

<template>
  <section id="soluciones" class="scroll-mt-24 bg-white py-20 sm:py-28">
    <div class="container-site">
      <RevealOnScroll>
        <div class="flex flex-wrap items-end justify-between gap-6">
          <div class="max-w-2xl">
            <span class="eyebrow">{{ t('solutionsSection.eyebrow') }}</span>
            <h2 class="section-title mt-5">
              {{ t('solutionsSection.title') }}
              <span class="text-gradient">{{ t('solutionsSection.titleHighlight') }}</span>
            </h2>
            <p class="section-sub mt-3">{{ t('solutionsSection.description') }}</p>
          </div>
          <NuxtLinkLocale
            to="/soluciones"
            class="inline-flex items-center gap-2 rounded-xl border border-brand-200/90 bg-gradient-to-r from-brand-50/90 to-sky-50/90 px-5 py-3 text-sm font-semibold text-brand-700 shadow-relief-sm transition-all duration-300 hover:-translate-y-0.5 hover:shadow-relief-card"
          >
            {{ t('solutionsSection.viewAll') }}
            <AppIcon name="arrow-right" class="h-4 w-4" />
          </NuxtLinkLocale>
        </div>
      </RevealOnScroll>

      <div class="mt-12">
        <ItemGrid :items="items" base-path="soluciones" />
      </div>
    </div>
  </section>
</template>
