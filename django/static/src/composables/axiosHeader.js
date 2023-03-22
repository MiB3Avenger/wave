export default function useAxiosHeader() {
    let token = JSON.parse(localStorage.getItem('token'));

    if(token)
        return { Authorization: 'Bearer '+token }
    
    return {}
}