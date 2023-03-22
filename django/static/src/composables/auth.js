import { ref, reactive } from 'vue'
import { useRouter } from "vue-router";
import useAxios from './axios';
import useAxiosHeader from './axiosHeader';
import useUsers from './users';

export default function useAuth() {
    const processing = ref(false)
    const validationErrors = ref({})
    const router = useRouter()
    const axios = useAxios();
    const users = useUsers();

    const loginForm = reactive({
        username: '',
        password: ''
    })

    const submitLogin = async (credentials) => {
        if (processing.value) return

        processing.value = true
        validationErrors.value = {}

        await axios.axiosInstance.post('/login/', credentials)
            .then(async response => {
                loginUser(response, true)
            })
            .catch(error => {
                console.log(error?.data);
                if (error?.data) {
                    validationErrors.value = error.data
                }
            })
            .finally(() => processing.value = false)
    }

    const submitRegister = async (form) => {
        if (processing.value) return

        processing.value = true
        validationErrors.value = {}

        await axios.axiosInstance.post('/register/', form)
            .then(async response => {
                loginUser(response, true)
            })
            .catch(error => {
                console.log(error?.data);
                if (error?.data) {
                    validationErrors.value = error.data
                }
            })
            .finally(() => processing.value = false)

    }

    const loginUser = (response, redirect = false) => {
        if(response.data){
            localStorage.setItem('loggedIn', JSON.stringify(true))
            localStorage.setItem('token', JSON.stringify(response.data.token))
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

        console.log(axios);

        await axios.axiosInstance.delete('/logout/', { headers: useAxiosHeader() })
            .then(response => {
                router.push({ name: 'login' })
                localStorage.removeItem('loggedIn')
                localStorage.removeItem('token')
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