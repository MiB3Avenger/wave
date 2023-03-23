import { ref, reactive } from 'vue';

import useAxios from './axios';
import useAxiosHeader from './axiosHeader';

export default function usePosts() {
    const axios = useAxios();
    const post = ref(null);

    const uploadPost = async (form) => {
        let headers = useAxiosHeader()

        const posts = {body: form['body'], author_id: form['user']}

        await axios.axiosInstance.post('posts/', 
            posts,
            {headers:headers}
        ).then(response => {
            post.value = response.data.post;
        })

        const data = new FormData()
        data.append('image', form['image'])
        
        await axios.axiosInstance.put('posts/create/'+post.value, data, {
            headers: headers
        }).then(response => {
        }).catch(error => {
        })
    }

    return {uploadPost}
}