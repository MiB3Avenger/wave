<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
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
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">Search</RouterLink>
        <RouterLink to="/about">Notifications</RouterLink>
        <RouterLink to="/about">Create</RouterLink>
        <RouterLink to="/about">Profile</RouterLink>
        <RouterLink to="/about">Logout</RouterLink>
      </nav>
    </div>
  </header>

  
  <main>
    <RouterView />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  border-right: 1px solid var(--color-border);
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

  main {
    height: 100vh;
    width: 100%;
    margin-top: 1rem;
    padding: 0 3rem;
    overflow: auto;
  }
}
</style>
