import { ref, reactive } from 'vue'
import { useRouter } from "vue-router";
import { useStore } from 'vuex';
import instance from '@app/js/plugins/axios';
import useAxiosHeader from '@app/js/composables/axiosHeader';
import useUsers from '@app/js/composables/users';

export default function useAuth() {
    const store = useStore()

    const processing = ref(false)
    const validationErrors = ref({})
    const router = useRouter()
    const axios = instance;
    const users = useUsers()

    const loginForm = reactive({
        username: '',
        password: ''
    })

    const submitLogin = async (credentials) => {
        if (processing.value) return

        processing.value = true
        validationErrors.value = {}

        await axios.post('/login/', credentials)
            .then(async response => {
                console.log(response);
                loginUser(response, true)
            })
            .catch(error => {
                if (error?.response.data) {
                    validationErrors.value = error.response.data
                }
            })
            .finally(() => processing.value = false)
    }

    const submitRegister = async (form) => {
        if (processing.value) return

        processing.value = true
        validationErrors.value = {}

        await axios.post('/register/', form)
            .then(async response => {
                loginUser(response, true)
            })
            .catch(error => {
                if (error?.response.data) {
                    validationErrors.value = error.response.data
                }
            })
            .finally(() => processing.value = false)

    }

    const loginUser = (response, redirect = false) => {
        if(response.data){
            store.dispatch('changeLoggedIn', true)
            store.dispatch('changeToken', response.data.token)
            
            users.user.username = response.data.username
            users.user.name = response.data.name
            users.user.email = response.data.email
            users.user.id = response.data.id
            if (redirect)
                router.push({ name: 'home' })
        } else {
            logout()
        }
    }

    const logout = async () => {
        if (processing.value) return

        processing.value = true

        await axios.delete('/logout/', { headers: useAxiosHeader() })
            .then(response => {
                router.push({ name: 'login' })

                store.dispatch('resetLoggedIn', true)
                store.dispatch('resetToken', response.data.token)

                users.user = users.defaultUser;
            })
            .catch(error => {
                
            })
            .finally(() => {
                processing.value = false
            })
    }

    return { loginForm, validationErrors, logout, processing, submitLogin, submitRegister }
}