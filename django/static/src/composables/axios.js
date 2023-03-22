import axios from 'redaxios';

export default function useAxios() {
    let axiosInstance = axios.create({
        baseURL: 'http://127.0.0.1:8000/api',
        headers: {
            'Access-Control-Allow-Origin': '*'
        },
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
    })

    return {axiosInstance};
}