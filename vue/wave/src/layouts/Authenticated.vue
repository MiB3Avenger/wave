<script setup>
import Sidebar from "../components/Sidebar.vue";
</script>
<template>
    <Sidebar />

    <main>
        <slot />
    </main>
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