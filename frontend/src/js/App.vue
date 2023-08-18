<template>
    <RouterView v-if="!isLoading" />
</template>

<script>
import { useRoute, useRouter, RouterView } from "vue-router";
import localForage from '@app/js/plugins/localforage'
import { STORAGE_KEY } from '@app/js/store/mutations'
import { ref } from 'vue';
import { useStore } from "vuex";

export default {
    name: 'App',
    components: {
        RouterView
    },
    data() {
        return {
            isLoading: ref(true)
        }
    },
    methods: {
        /**
         * Resets login state.
         */
        resetLoggedIn() {
            this.$store.dispatch("resetToken")
            this.$store.dispatch("resetLoggedIn")
        }
    },
    beforeMount() {
        // Set the application to loading...
        this.isLoading = true

        // Store server data and global variables that are passed to us through the server response.
        let server_data = JSON.parse(document.getElementById('server_data') != null ? document.getElementById('server_data').textContent : "{}")
        this.$store.commit("server_data", server_data)
        
        let global_variables = JSON.parse(document.getElementById('__globalVariables__') != null ? document.getElementById('__globalVariables__').textContent : "{}")
        this.$store.commit("global_variables", global_variables)
    },
    beforeCreate() {
        const router = useRouter()
        const route = useRoute()
        const store = useStore()
        console.log(route.name);

        // Set store values from our local storage.
        localForage.getItem(STORAGE_KEY+"-token").then((value) => {
            let parsed = JSON.parse(value)

            // If the token is not present, we will logout the user.
            if(value == null){
                this.resetLoggedIn()
                this.isLoading = false
            } else {
                this.$store.dispatch("changeToken", parsed)
                
                let interval = setInterval(() => {
                    if(route.name !== undefined) {
                        if(store.getters.loggedIn == true && parse != ''){
                            if(route?.name == 'login')
                                router.push({name: 'home'})

                            clearInterval(interval)
                        }
                    }
                }, 100)
            }
        })
        localForage.getItem(STORAGE_KEY+"-logged-in").then((value) => {
            let parsed = JSON.parse(value)

            // If the logged in state is not present, we will logout the user.
            if(value == null){
                this.resetLoggedIn()
                this.isLoading = false
            } else {
                this.$store.dispatch("changeLoggedIn", parsed)
                
                let interval = setInterval(() => {
                    if(route.name !== undefined) {
                        if(parsed == true && store.getters.token != ''){
                            if(route?.name == 'login')
                                router.push({name: 'home'})

                            clearInterval(interval)
                        }
                        this.isLoading = false
                    }
                    console.log(this.isLoading, route.name, parsed, store.getters.token);
                }, 100)
            }
        })
    },
    computed: {
    },
};
</script>