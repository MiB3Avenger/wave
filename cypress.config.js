const { defineConfig } = require("cypress");

module.exports = defineConfig({
  projectId: 'u5azh9',
  defaultCommandTimeout: 8000,
  pageLoadTimeout:10000,
  env: {
    NODE_ENV: 'test',
  },
  e2e: {
    specPattern: "./frontend/cypress/e2e/**/*.{cy,spec}.{js,jsx,ts,tsx}",
    supportFile: "./frontend/cypress/support/e2e.js",
    baseUrl: "http://127.0.0.1:8000",
  },
});
