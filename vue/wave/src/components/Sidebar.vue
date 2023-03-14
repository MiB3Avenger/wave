<script setup>
import { reactive, inject } from "vue";
import { useRoute } from "vue-router";
import useAuth from "../composables/auth";

const route = useRoute();
const { getUser, user } = useAuth();

getUser();
</script>

<template>
    <header>
        <img
        alt="Vue logo"
        class="logo"
        src="@/assets/logo.svg"
        width="45"
        height="45"
        />

        <div class="wrapper">
            <nav>
                <RouterLink :to="{name: 'home'}"><v-icon name="md-home-round" />Home</RouterLink>
                <RouterLink to="/about"><v-icon name="md-search-round" />Search</RouterLink>
                <RouterLink to="/about"><v-icon name="md-notifications-round" />Notifications</RouterLink>
                <RouterLink to="/about"><v-icon name="md-create-round" />Create</RouterLink>
                <RouterLink v-if="route.params.username == undefined || user.username != route.params.username" :to="{name: 'profile'}"><v-icon name="md-person-round" />Profile</RouterLink>
                <RouterLink v-if="route.params.username != undefined && user.username == route.params.username" :to="{name: 'profile-username', params: {username: route.params.username}}"><v-icon name="md-person-round" />Profile</RouterLink>
                <RouterLink to="/about"><v-icon name="md-logout-round" />Logout</RouterLink>
            </nav>
        </div>

        <div class="footer">
            <footer>
                <RouterLink to="/about">Contact</RouterLink>
                <RouterLink to="/about">Contact</RouterLink>
                <RouterLink to="/about">Contact</RouterLink>
            </footer>
        </div>
    </header>
</template>

<style scoped>
header {
    line-height: 1.5;
    max-height: 100vh;
    border-right: 1px solid var(--color-border);
}

header div:last-of-type {
        margin-top: auto;
        margin-bottom: 1rem;
}

.logo {
    display: block;
    margin: 0 auto 2rem;
}

nav {
    width: 100%;
    font-size: 12px;
    text-align: center;
    margin-top: 2rem;
}

nav a.router-link-exact-active {
    color: var(--color-text);
}

nav a.router-link-exact-active:hover {
    background-color: transparent;
}

    nav a {
    display: inline-block;
    padding: .75rem 1.5rem;
    border-radius: 30px;
    height: 100%;
    margin-bottom: 0.25rem;
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

nav a.router-link-active {
    background-color: rgba(255, 255, 255, .1);
}

nav a:hover{
    background-color: rgba(255, 255, 255, .1);
}

nav a.router-link-active:hover {
    background-color: rgba(255, 255, 255, .25);
}

.footer {
    display: flex;
    flex-direction: row;
    justify-content: center;
    font-size: small;
}

.footer footer a {
    margin: 0 .5rem;
}

@media (min-width: 1024px) {
    header {
        display: flex;
        flex-direction: column;
        padding-right: calc(var(--section-gap)/4);
        max-width: calc(100vw/4);
    }

    .logo {
        margin: 2rem 2rem .75rem;
    }

    header .wrapper {
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
    }

    nav {
        display: flex;
        flex-direction: column;
        text-align: left;
        margin-left: 1rem;
        font-size: 1rem;

        padding: 1rem 0;
        margin-top: 1rem;
    }
}
</style>