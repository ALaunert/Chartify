<script setup lang="ts">
defineProps(['image','title'])
const defaultImage = '/Spotify_Logo.png';
</script>

<template>
  <div class="search-result">
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