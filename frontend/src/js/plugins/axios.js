/**
 * An extended axios instance with progress bar hooked.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/plugis/axios.js
 * @exports AxiosInstance Instance
 */

// Base import.
import axios from "axios"

// Fetch global variables from document.
// We cannot wait until store is ready and populated, so to make instance quickly, we use this method.
let global_variables = JSON.parse(document.getElementById('__globalVariables__') != null ? document.getElementById('__globalVariables__').textContent : "{}")
const api =  global_variables.urls?.api ?? '/' // If there's no url for API, just use base url.

// Create instance...
const instance = axios.create({
    baseURL: api,
    headers: {
        'Access-Control-Allow-Origin': '*',
    },
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
});

// Extend functionality to handle progress bar...
instance.interceptors.request.use((config) => {
    return config
});
instance.interceptors.response.use((response) => {
    return response
});

// Export the instance...
export default instance