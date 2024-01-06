<script setup lang="ts">
let {
  src,
  "v-click": vc,
  left,
  adjust,
  foot,
} = defineProps({
  src: String,
  left: Boolean,
  adjust: Boolean,
  "v-click": String,
  foot: String,
});
</script>

<template>
  <div
    v-bind:v-click="vc"
    class="px-12 flex flex-col items-center justify-center gap-2"
  >
    <span class="text-xs text-center text-slate-400 font-mono">{{ foot }}</span>
    <img
      v-bind:un-h="adjust ? 'auto' : left ? 84 : 100"
      class="rounded-lg"
      :src
    />
  </div>
</template>

<style scoped>
.slidev-vclick-target {
  @apply transition-all max-h-fit duration-500;
}
.slidev-vclick-hidden {
  @apply max-h-[0];
}
</style>
