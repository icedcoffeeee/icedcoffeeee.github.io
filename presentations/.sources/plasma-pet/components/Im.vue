<script setup lang="ts">
const {
  src,
  "v-click": vc,
  foot,
  adjust,
  left,
} = defineProps({
  src: String,
  "v-click": String,
  foot: String,
  adjust: Boolean,
  left: Boolean,
});
</script>
<template>
  <div
    :v-click="vc"
    class="px-12 flex flex-col items-center justify-center gap-2"
  >
    <span class="text-xs text-center text-slate-400 font-mono">{{ foot }}</span>
    <img
      :un-h="adjust ? 'auto' : left ? 84 : 100"
      class="rounded-lg"
      :src="'./' + src"
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
