import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/@:username",
      name: "profile-username",
      component: () => import("../views/ProfileView.vue"),
      props: true,
      beforeEnter: (to, from) => {
        to.params.name = "profile-username"
      }
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("../views/ProfileView.vue"),
      props: true,
      beforeEnter: (to, from) => {
        to.params.name = "profile"
      }
    },
    {
      path: "/profile/edit",
      name: "edit-profile",
      component: () => import("../views/EditProfileView.vue"),
    },
  ],
  strict: false,
  sensitive: true,
});

export default router;
