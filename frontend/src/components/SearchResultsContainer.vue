<script setup lang="ts">
import SearchResult from './SearchResult.vue';
import { computed } from 'vue'

const props = defineProps(['results']);
const emit = defineEmits(['result-selected']);

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
        :id="result.id"
        @selected="$emit('result-selected')"
    />
  </div>
</template>

<style scoped>

#results-container {
  max-height: 300px;
  overflow-y: auto;
  background-color: #535bf2;
  border-radius: 8px;
  padding: 8px;
}

</style>