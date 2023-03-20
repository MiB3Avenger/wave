import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

function auth(to, from, next) {
  if (JSON.parse(localStorage.getItem('loggedIn'))) {
      next()
  } else {
      next('/login')
  }
}

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
      path: "/create",
      name: "create",
      component: () => import("../views/CreateView.vue"),
    },
    {
      path: "/post/:id",
      name: "post",
      component: () => import("../views/PostView.vue"),
      props: true,
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
  scrollBehavior(to, from, savedPosition) {
      if (savedPosition) {
          return savedPosition
      } else {
          return { top: 0 }
      }
  },
});

export default router;
