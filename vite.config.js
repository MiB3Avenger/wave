const { resolve } = require("path")
import { fileURLToPath, URL } from "url"
import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"

export default defineConfig({
  plugins: [vue()],
  root: resolve("./frontend/src"),
  base:
    process.env.APP_ENV == "prod"
      ? "https://wave.mib3avenger.com/static/vite/"
      : "http://localhost:3000/",
  server: {
    host: "0.0.0.0",
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
    origin:
      process.env.APP_ENV == "prod"
        ? "https://wave.mib3avenger.com/static/vite"
        : "http://localhost:3000",
  },
  resolve: {
    extensions: [".js", ".json", ".vue", ".less", ".scss"],
    alias: [
      { find: '@app', replacement: fileURLToPath(new URL('./frontend/src', import.meta.url)) },
      { find: 'tailwind-config', replacement: fileURLToPath(new URL('./tailwind.config.js', import.meta.url)) },
    ],
    // alias: {
    //   "@app": resolve(__dirname, "./frontend/src"),
    //   "@app/js": resolve(__dirname, "./frontend/src/js"),
    //   "@app/css": resolve(__dirname, "./frontend/src/css"),
    //   "@app/icons": resolve(__dirname, "./frontend/src/icons"),
    //   "@app/assets": resolve(__dirname, "./frontend/src/assets"),
    //   "tailwind-config": resolve(__dirname, "./tailwind.config.js"),
    // },
  },
  optimizeDeps: {
    include: ["tailwind-config"],
  },
  build: {
    outDir: resolve("./frontend/dist/vite"),
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    target: "esnext",
    rollupOptions: {
      input: {
        main: resolve("./frontend/src/js/main.js"),
        test: resolve("./frontend/src/js/test.js"),
      },
      output: {
        chunkFileNames: undefined,
      },
      external: [/^\/static\/.*/],
    },
    commonjsOptions: {
      include: ["tailwind.config.js", "node_modules/**"],
    },
  },
});
