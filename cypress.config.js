const { defineConfig } = require("cypress");

module.exports = defineConfig({
  env: {
    NODE_ENV: 'test',
  },
  e2e: {
    specPattern: "./frontend/cypress/e2e/**/*.{cy,spec}.{js,jsx,ts,tsx}",
    supportFile: "./frontend/cypress/support/e2e.js",
    baseUrl: process.env.APP_ENV == "local" ? "http://127.0.0.1:8000" :"http://localhost:3000",
  },
});
