<script setup lang="ts">
import SearchResult from './SearchResult.vue';
import { computed } from 'vue'

const props = defineProps(['results']);

const sortedResults = computed(() =>
  [...props.results].sort((a, b) => b.followers.total - a.followers.total)
);
</script>

<template>
  <div id="results-container">
    <SearchResult
        v-for="result in sortedResults"
        :key="result.id"
        :image="result.images[2] ? result.images[2].url : null"
        :title="result.name"
    />
  </div>
</template>

<style scoped>

#results-container {
  background-color: #535bf2;
  display: flex;
  flex-direction: column;
}
</style>