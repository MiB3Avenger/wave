<script setup>
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();

const goBackFn = () => {
    if(window.history.state.back == null){
        let split = route.fullPath.split("/");
        split.pop();
        let next = split.join("/");
        router.push(next);
    } else {
        router.back()
    }
}
</script>
<template>
    <button class="go-back" @click="goBackFn"><v-icon name="md-arrowback-round" />Go Back</button>
</template>
<style lang="scss">
.go-back {
    background-color: var(--color-primary-container);
    color: var(--color-on-primary-container);
    padding: 0.5rem 1.5rem;
    border: 0;
    height: 40px;
    display: flex;
    align-items: center;
    border-radius: 25px;
    width: 150px;
    justify-content: center;
    transition: 0.4s;
    font-weight: bold;
    white-space: nowrap;
    &:hover {
        background-color: var(--color-background-mute);
        color: var(--color-on-primary);
    }
}
</style>