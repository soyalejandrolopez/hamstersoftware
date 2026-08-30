<script setup lang="ts">
withDefaults(defineProps<{ gid?: string }>(), { gid: 'logo-gradient' })
</script>

<template>
  <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" aria-hidden="true">
    <defs>
      <linearGradient :id="gid" x1="0" y1="0" x2="32" y2="32" gradientUnits="userSpaceOnUse">
        <stop stop-color="#2563eb" />
        <stop offset="1" stop-color="#06b6d4" />
      </linearGradient>
    </defs>
    <rect width="32" height="32" rx="9" :fill="`url(#${gid})`" />
    <circle cx="16" cy="16" r="8.5" fill="none" stroke="white" stroke-width="2.2" />
    <circle cx="16" cy="16" r="2.8" fill="none" stroke="white" stroke-width="2.2" />
    <line x1="16" y1="7.5" x2="16" y2="10.5" stroke="white" stroke-width="2.2" stroke-linecap="round" />
    <line x1="16" y1="21.5" x2="16" y2="24.5" stroke="white" stroke-width="2.2" stroke-linecap="round" />
    <line x1="7.5" y1="16" x2="10.5" y2="16" stroke="white" stroke-width="2.2" stroke-linecap="round" />
    <line x1="21.5" y1="16" x2="24.5" y2="16" stroke="white" stroke-width="2.2" stroke-linecap="round" />
  </svg>
</template>
