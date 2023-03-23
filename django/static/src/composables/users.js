import { ref, reactive } from 'vue';

import useAxios from './axios';
import useAxiosHeader from './axiosHeader';

const user = reactive({
    id: '',
    name: '',
    email: '',
    username: '',
    posts: 0,
    following: 0,
    followers: 0,
    auth_user: false,
    profile: ''
});


export default function useUsers() {
    const axios = useAxios();
    const defaultUser = user;

    const getUser = async (callback = false) => {
        await axios.axiosInstance.get('user/', { headers: useAxiosHeader() })
            .then(response => {
                if(typeof callback == "function"){
                    callback(response)
                }
                user.username = response.data.username
                user.name = response.data.name
                user.email = response.data.email
                user.id = response.data.id
                user.posts = response.data.posts
                user.auth_user = response.data.auth_user
                user.profile = response.data.profile
            })
    }

    const getUserById = async (id, callback = false) => {
        await axios.axiosInstance.get('user/'+id, { headers: useAxiosHeader() })
            .then(response => {
                if(typeof callback == "function"){
                    callback(response)
                }
                user.username = response.data.username
                user.name = response.data.name
                user.email = response.data.email
                user.id = response.data.id
                user.posts = response.data.posts
                user.auth_user = response.data.auth_user
                user.profile = response.data.profile
            })
    }

    const getUserByUserName = async (id, callback = false) => {
        await axios.axiosInstance.get('user/'+id, { headers: useAxiosHeader() })
            .then(response => {
                if(typeof callback == "function"){
                    callback(response)
                }
                user.username = response.data.username
                user.name = response.data.name
                user.email = response.data.email
                user.id = response.data.id
                user.posts = response.data.posts
                user.auth_user = response.data.auth_user
                user.profile = response.data.profile
            })
    }

    return { user, defaultUser, getUser, getUserById, getUserByUserName };
}