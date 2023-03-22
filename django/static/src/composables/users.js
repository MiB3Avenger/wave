import { ref, reactive } from 'vue';

import useAxios from './axios';
import useAxiosHeader from './axiosHeader';

const user = reactive({
    name: '',
    email: '',
    username: '',
    posts: 0,
    following: 0,
    followers: 0,
})

export default function useUsers() {
    const axios = useAxios();
    const defaultUser = user;

    const getUser = async (callback = false) => {
        await axios.axiosInstance.get('/user/', { headers: useAxiosHeader() })
            .then(response => {
                if(typeof callback == "function"){
                    callback(response)
                }
                console.log(response);
                user.username = response.data.username
                user.name = response.data.name
                user.email = response.data.email
                user.id = response.data.id
            }).catch(error => {
                logout()
            })
    }

    const getUserById = async (id, callback = false) => {
        await axios.axiosInstance.get('/user/'+id, { headers: useAxiosHeader() })
            .then(response => {
                if(typeof callback == "function"){
                    callback(response)
                }
                console.log(response);
                user.username = response.data.username
                user.name = response.data.name
                user.email = response.data.email
                user.id = response.data.id
            }).catch(error => {
                logout()
            })
    }

    const getUserByUserName = async (id, callback = false) => {
        await axios.axiosInstance.get('/user/'+id, { headers: useAxiosHeader() })
            .then(response => {
                if(typeof callback == "function"){
                    callback(response)
                }
                console.log(response);
                user.username = response.data.username
                user.name = response.data.name
                user.email = response.data.email
                user.id = response.data.id
            }).catch(error => {
                logout()
            })
    }

    return { user, defaultUser, getUser, getUserById, getUserByUserName };
}