import store from "@app/js/store/index"

export default function useAxiosHeader() {
    let token = store.getters.token;

    if(token != '')
        return { Authorization: 'Bearer '+token }
    
    return {}
}