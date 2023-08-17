import { ref, reactive, shallowReactive } from 'vue';

import instance from '@app/js/plugins/axios';
import useAxiosHeader from '@app/js/composables/axiosHeader';

export default function useSearch() {
    const processing = ref(false)
    const search = reactive({
        results: [],
        error: 'Enter something to search users.'
    })
    const axios = instance

    const searchUser = async (event) => {
        if (processing.value) return

        processing.value = true
        
        search.results = []
        search.error = ''

        let string = event.target.value

        await axios.get('search/user/', {params: {'search':string}, headers: useAxiosHeader()})
        .then(response => {
            if (response.data.success){
                search.results = response.data.users;
            } else {
                search.error = response.data.message;
            }
        }).catch(error => {
            console.log(error)
        })
        .finally(() => {
            processing.value = false
        })
    }

    return {
        search, searchUser
    }
}