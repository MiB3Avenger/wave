<script setup>
import Sidebar from "../components/Sidebar.vue";
</script>
<template>
    <div class="app-container">
        <Sidebar />

        <main>
            <slot />
        </main>
    </div>
</template>
<style>
@media (min-width: 1024px) {
  main {
    height: 100vh;
    width: 100%;
    padding: 0 3rem;
    overflow: auto;
  }
}
</style>