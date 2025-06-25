import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


export default defineConfig({
      plugins: [
        vue({
            template: {
                transformAssetUrls: {
                    base: null,
                    includeAbsolute: false
                }
            }
        }),
    ],
  server: {
    host: '0.0.0.0',
    port: 5173,
    strictPort: true,
    open: false,
    allowedHosts: ['frontend', 'localhost', 'chartify.test']
  }
});