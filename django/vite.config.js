import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
const { resolve } = require('path');

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue({
    style: 'sass'
  })],
  root: resolve('./static/src'),
  base: '/static/',
  server: {
    host: 'localhost',
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    extensions: ['.js', '.json'],
    alias: {
      "@": fileURLToPath(new URL("./static/src", import.meta.url)),
    },
  },
  build: {
    outDir: resolve('./static/dist'),
    assetsDir: '',
    manifest: true,
    emptyOutDir: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        main: resolve('./static/src/main.js'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
});
