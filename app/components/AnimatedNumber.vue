<script setup lang="ts">
const props = defineProps<{ value: number }>()

const display = ref(0)
const el = ref<HTMLElement | null>(null)
let started = false

function animate() {
  const duration = 1600
  const start = performance.now()
  const tick = (now: number) => {
    const progress = Math.min((now - start) / duration, 1)
    const eased = 1 - Math.pow(1 - progress, 3)
    display.value = Math.round(eased * props.value)
    if (progress < 1) requestAnimationFrame(tick)
  }
  requestAnimationFrame(tick)
}

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting && !started) {
          started = true
          animate()
          observer.disconnect()
        }
      }
    },
    { threshold: 0.4 }
  )
  if (el.value) observer.observe(el.value)
})
</script>

<template>
  <span ref="el">{{ display }}</span>
</template>
