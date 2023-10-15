import path from 'path'
import vue from '@vitejs/plugin-vue'

export default {
  plugins: [vue()],
  test: {
    server: {
      deps: {
        inline: ["localforage"],
      },
    },
  },
  resolve: {
    extensions: [".js", ".json", ".vue", ".less", ".scss"],
    alias: {
      "@app": path.resolve(__dirname, "./frontend/src"),
      "@app/js": path.resolve(__dirname, "./frontend/src/js"),
      "@app/css": path.resolve(__dirname, "./frontend/src/css"),
      "@app/icons": path.resolve(__dirname, "./frontend/src/icons"),
      "@app/assets": path.resolve(__dirname, "./frontend/src/assets"),
      "tailwind-config": path.resolve(__dirname, "./tailwind.config.js"),
    },
  },
};
