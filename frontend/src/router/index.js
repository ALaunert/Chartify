import { createRouter, createWebHistory } from 'vue-router'
import ArtistData from '@/components/ArtistData.vue'

const routes = [
  {
    path: '/artist/:id',
    name: 'artist',
    component: ArtistData
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
