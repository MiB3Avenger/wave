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
main {
    height: 100vh;
    overflow: auto;
    padding: 0 3rem;
}
@media (min-width: 1024px) {
    main {
        width: 100%;
    }
}
@media (max-width: 1024px) {
    main {
        flex: 1 0;
        flex-basis: calc(100% - 50px);
        padding: 0 1rem;
    }
}
</style>