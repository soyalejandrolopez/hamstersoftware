<script setup lang="ts">
const props = withDefaults(
  defineProps<{ delay?: number; direction?: 'up' | 'left' | 'right' }>(),
  { delay: 0, direction: 'up' }
)

const visible = ref(false)
const el = ref<HTMLElement | null>(null)
let observer: IntersectionObserver | undefined

const hiddenClass = computed(() => {
  if (props.direction === 'left') return 'opacity-0 translate-x-8'
  if (props.direction === 'right') return 'opacity-0 -translate-x-8'
  return 'opacity-0 translate-y-7'
})

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          visible.value = true
          observer?.disconnect()
        }
      }
    },
    { threshold: 0.12, rootMargin: '0px 0px -48px 0px' }
  )
  if (el.value) observer.observe(el.value)
})

onBeforeUnmount(() => observer?.disconnect())
</script>

<template>
  <div
    ref="el"
    data-reveal
    :class="[
      'transition-all duration-700 ease-out will-change-transform',
      'motion-reduce:!translate-x-0 motion-reduce:!translate-y-0 motion-reduce:!opacity-100 motion-reduce:!transition-none',
      visible ? 'translate-x-0 translate-y-0 opacity-100' : hiddenClass
    ]"
    :style="{ transitionDelay: `${delay}ms` }"
  >
    <slot />
  </div>
</template>
