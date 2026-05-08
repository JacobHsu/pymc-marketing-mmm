<template>
  <div class="progress-bar" :style="{ width: `${(currentSlideNo / total) * 100}%` }" />
</template>

<script setup>
import { useNav } from '@slidev/client'
const { currentSlideNo, total } = useNav()
</script>

<style scoped>
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: linear-gradient(to right, #6366f1, #38bdf8);
  z-index: 9999;
  transition: width 0.3s ease;
}
</style>
