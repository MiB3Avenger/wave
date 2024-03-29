import { createRouter, createWebHistory} from 'vue-router'
import { useStore } from 'vuex'

function auth(to, from, next) {
    const store = useStore()

    let loggedIn = store.getters.loggedIn
    let token = store.getters.token

    if (loggedIn != false && token != '') {
        next()
    } else {
        next('/login')
    }
}

const routes = [
    {
        path: "/",
        name: "home",
        component: () => import("../views/HomeView.vue"),
        beforeEnter: auth
    },
    {
        path: "/login",
        name: "login",
        component: () => import("../views/LoginView.vue"),
        beforeEnter: (to, from, next) => {
            if (localStorage.getItem('loggedIn') != null && localStorage.getItem('token') != null) {
                next('/')
            } else {
                next()
            }
        }
    },
    {
        path: "/about",
        name: "about",
        component: () => import("../views/AboutView.vue"),
        beforeEnter: auth
    },
    {
        path: "/create",
        name: "create",
        component: () => import("../views/CreateView.vue"),
        beforeEnter: auth
    },
    {
        path: "/post/:id",
        name: "post",
        component: () => import("../views/PostView.vue"),
        props: true,
        beforeEnter: auth
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
    {
        path: "/:pathMatch(.*)*",
        name: "404",
        redirect: {name: 'home'}
    }
]

export { routes }

const router = createRouter({
    // In case we want to create url history
    // history: createWebHistory(),
    // base: "/",
    history: createWebHistory(),
    routes,
    strict: false,
    sensitive: true,
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        } else {
            return { top: 0 }
        }
    },
})

export default router