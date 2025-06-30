<script setup lang="ts">
import { useRoute } from 'vue-router'
import { onMounted, ref, computed, watch } from 'vue'

const route = useRoute()
const artist = ref(null)

const fetchArtist = async (id: string) => {
  const res = await fetch(`/api/artist/${id}`)
  artist.value = await res.json()
}

onMounted(() => {
  fetchArtist(route.params.id as string)
})

watch(() => route.params.id, (newId) => {
  fetchArtist(newId as string)
})

// Optional: computed fallback image
const artistImage = computed(() => {
  return artist.value?.images?.[0]?.url ?? '/fallback.jpg'
})

const genres = computed(() => artist.value?.genres ?? [])
</script>

<template>
  <div class="artist-data" v-if="artist">
    <img class="artist-image" :src="artistImage" alt="Artist image"/>
    <div class="artist-header">
      <h1 class="artist-name">{{ artist.name }}</h1>
      <div class="artists-genres">
        <span v-for="genre in genres" :key="genre"> {{ genre + `\n`}} </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.artist-data{
  margin-top: 36px;
  display: flex;
  gap: 12px;
  justify-content: center;
}
.artist-image{
  height: 240px;
  width: 240px;
}
.artist-header{
  display: flex;
  flex-direction: column;
}
</style>