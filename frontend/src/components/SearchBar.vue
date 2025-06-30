<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import SearchResultsContainer from "./SearchResultsContainer.vue"

const query = ref("")
const results = ref<any[]>([])
const wrapperRef = ref<HTMLElement | null>(null)

const resetResults = () =>
{
  results.value = [];
}

const handleClickOutside = (event: MouseEvent) => {
  if (wrapperRef.value && !wrapperRef.value.contains(event.target as Node)) {
    resetResults()
  }
}

onMounted(() => {
  document.addEventListener("click", handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener("click", handleClickOutside)
})

const getSearchData = async (search: string) => {
  if (!search)
  {
    resetResults()

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
    resetResults()
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
  <div class="search-wrapper" ref="wrapperRef">
    <form @submit="onSubmit" id="search-bar-form">
      <input @keyup="onKeyUp" type="text" v-model="query" name="searchbar" id="search_bar" placeholder="Enter your artist"/>
      <button type="submit" name="search">Find</button>
    </form>

    <div class="results-absolute-wrapper">
      <SearchResultsContainer v-if="results.length" :results="results" @result-selected="resetResults"/>
    </div>
  </div>
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
.search-wrapper {
  position: relative;
}

.results-absolute-wrapper {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 100;
}

</style>