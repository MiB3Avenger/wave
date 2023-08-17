import { ref, reactive } from 'vue';
import { reset } from "@formkit/core";

import instance from '@app/js/plugins/axios';
import useAxiosHeader from '@app/js/composables/axiosHeader';
import { useRouter, useRoute } from 'vue-router';


export default function usePosts() {
    const axios = instance;
    const post = ref(null);
    const responsePost = reactive({
        id: 0,
        author: {},
        body: '',
        image: '',
        likes_count: 0,
        posted_at: 'just now'
    })
    const router = useRouter();

    const posts = reactive({
        data: {}
    })

    const uploadPost = async (form) => {
        let headers = useAxiosHeader()

        const posts = {body: form['body'], author_id: form['user']}

        await axios.post('posts/', 
            posts,
            {headers:headers}
        ).then(response => {
            post.value = response.data.post;
        })

        const data = new FormData()
        data.append('image', form['image'])
        
        await axios.put('posts/create/'+post.value, data, {
            headers: headers
        }).then(response => {
        }).catch(error => {
        })
    }

    const getPostById = async (data) => {
        await axios.get('posts/'+data, {
            headers: useAxiosHeader()
        }).then(response => {
            let data = response.data

            responsePost.id = data.id
            responsePost.author = data.author
            responsePost.body = data.body
            responsePost.image = data.image
            responsePost.likes_count = data.likes_count
            responsePost.posted_at = data.posted_at
            responsePost.comments = data.comments
        })
    }

    const addCommentByPostId = async (data) => {
        let comment = {
            'post': responsePost.id,
            'author': responsePost.author.id,
            'body': data
        }

        await axios.post('posts/'+responsePost.id+'/comments/', comment, {
            headers: useAxiosHeader()
        }).then(response => {
            reset('comment')
            router.push({ name: 'post', params: {id: responsePost.id} })
        })
    }

    const getPosts = async () => {
        await axios.get('posts/', {
            headers: useAxiosHeader()
        }).then(response => {
            posts.data = response.data
        })
    }

    return {uploadPost, getPosts, getPostById, addCommentByPostId, responsePost, posts}
}