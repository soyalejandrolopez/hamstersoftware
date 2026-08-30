<script setup lang="ts">
import { useContent } from '~/composables/useContent'

const { services } = useContent()

const route = useRoute()
const slug = computed(() => String(route.params.slug ?? ''))

const item = computed(() => services.value.find((s) => s.slug === slug.value))

// 404 en SSR / carga inicial
if (!item.value) {
  throw createError({ statusCode: 404, statusMessage: 'Not Found' })
}

// 404 robusto en navegación client-side entre slugs
watch(item, (val) => {
  if (!val) {
    showError({ statusCode: 404, statusMessage: 'Not Found' })
  }
})
</script>

<template>
  <DetailPage v-if="item" :item="item" kind="service" />
</template>
