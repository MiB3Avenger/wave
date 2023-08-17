<template>
    <main class="guest">
        <slot />
    </main>
</template>
<style lang="scss">
main.guest {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    overflow: none;
}
</style>