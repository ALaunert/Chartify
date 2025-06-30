<script setup lang="ts">
import { useRouter } from 'vue-router'
const props = defineProps(['image', 'title', 'id'])
const emit = defineEmits(['selected'])
const defaultImage = '/Spotify_Logo.png';
const router = useRouter()

const openArtist = () => {
  emit('selected');
  router.push({ name: 'artist', params: { id: props.id } })
}
</script>

<template>
  <div @click="openArtist" class="search-result">
    <img :src="image ? image : defaultImage" class="cover" alt="noimg">
    <div class="title">
      {{title}}
    </div>
  </div>
</template>

<style scoped>
.search-result {
  display: flex;
  align-content: center;
  background-color: #747bff;
  margin: 8px;
  gap: 8px;
}

.cover {
  width: 36px;
  height: 36px;
}

</style>