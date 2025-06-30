<script setup lang="ts">
import { ref } from "vue"
import SearchResultsContainer from "./SearchResultsContainer.vue"

const query = ref("")
const results = ref([])

const getSearchData = async (search: string) => {
  if (!search)
  {
    results.value = []

    return;
  }

  const url = `/api/artist/search/artist:${search}`
  try {
    const response = await fetch(url)
    if (!response.ok) throw new Error(`Response status: ${response.status}`)

    const data = await response.json()
    results.value = data.artists?.items || []
  }
  catch (error) {
    console.error(error)
    results.value = []
  }
}

const onSubmit = (e: Event) => {
  e.preventDefault();

  if (debounceTimer) {
    clearTimeout(debounceTimer);
    debounceTimer = null;
  }

  getSearchData(query.value);
};

let debounceTimer: ReturnType<typeof setTimeout> | null = null;

const ignoredKeys = new Set([
  "Shift", "Control", "Alt", "Meta",
  "ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown",
  "CapsLock", "Tab", "Enter", "Escape"
]);

const onKeyUp = (e: KeyboardEvent) => {
  if (ignoredKeys.has(e.key)) return;

  if (debounceTimer) clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    getSearchData(query.value);
    debounceTimer = null;
  }, 1500);
};
</script>

<template>
  <form @submit="onSubmit" id="search-bar-form">
    <input  @keyup="onKeyUp" type="text" v-model="query" name="searchbar" id="search_bar" placeholder="Enter your artist"/>
    <button type="submit" name="search">Find</button>
  </form>

  <SearchResultsContainer v-if="results" :results="results" />
</template>

<style scoped>
#search-bar-form{
  background: #888888;
  padding: 8px 16px;
  border-radius: 12px;
  display: flex;
  gap: 8px;
}
#search_bar{
  padding-left: 8px;
}
</style>