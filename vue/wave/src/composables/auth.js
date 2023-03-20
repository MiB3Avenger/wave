import { ref, reactive } from 'vue'
import { useRouter } from "vue-router";

const user = reactive({
    name: '',
    email: '',
    username: '',
    posts: 0,
    following: 0,
    followers: 0,
})

export default function useAuth() {
    const processing = ref(false)
    const validationErrors = ref({})
    const router = useRouter()

    const loginForm = reactive({
        email: '',
        password: '',
        remember: false
    })

    const submitLogin = async () => {
        if (processing.value) return

        processing.value = true
        validationErrors.value = {}

        axios.post('/login', loginForm)
            .then(async response => {
                loginUser(response, true)
            })
            .catch(error => {
                if (error.response?.data) {
                    validationErrors.value = error.response.data.errors
                }
            })
            .finally(() => processing.value = false)
    }

    const loginUser = (response, redirect = false) => {
        if(response.data){
            user.name = response.data.name
            user.email = response.data.email
            localStorage.setItem('loggedIn', JSON.stringify(true))
            if (redirect)
                router.push({ name: 'dashboard.index' })
        } else {
            logout()
        }
    }

    const getUser = (callback = false) => {
        user.username = 'test'
        user.name = 'test'
        user.email = 'test@gmail.com'
        user.posts = 7
        user.followers = 1
        user.following = 1
        return
        axios.get('/api/user')
            .then(response => {
                if(typeof callback == "function"){
                    callback(response)
                }
                loginUser(response)
            }).catch(error => {
                logout()
            })
    }

    const getUserById = (id, callback = false) => {
        user.username = id
        user.name = 'default'
        user.email = 'test@gmail.com'
        user.posts = 0
        user.followers = 0
        user.following = 0
    }

    const logout = async () => {
        if (processing.value) return

        processing.value = true

        axios.post('/logout')
            .then(response => router.push({ name: 'login' }))
            .catch(error => {
                swal({
                    icon: 'error',
                    title: error.response.status,
                    text: error.response.statusText
                })
            })
            .finally(() => {
                processing.value = false
            })
    }

    return { user, loginForm, validationErrors, logout, processing, submitLogin, getUser, getUserById }
}