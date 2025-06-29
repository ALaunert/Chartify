<script setup lang="ts">
import { ref } from "vue"
import SearchResultsContainer from "./SearchResultsContainer.vue"

const query = ref("")
const results = ref([])

const getSearchData = async (search: string) => {
  const url = `/api/artist/search/artist:${search}`
  try {
    const response = await fetch(url)
    if (!response.ok) throw new Error(`Response status: ${response.status}`)

    const data = await response.json()
    results.value = data.artists.items
  }
  catch (error) {
    console.error(error)
    results.value = []
  }
}

const onSubmit = (e: Event) => {
  e.preventDefault()
  getSearchData(query.value)
}
</script>

<template>
  <form @submit="onSubmit" id="search-bar-form">
    <input type="text" v-model="query" name="searchbar" id="search_bar" />
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
</style>