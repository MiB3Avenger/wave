/**
 * Helps keeping state in one single place without increasing scroll length in the createStore file.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/store/state.js
 * @exports Object Store Default State
 */

// Base imports. We create tailwind config, incase we want to specify how our graph should be colored.
import resolveConfig from 'tailwindcss/resolveConfig'
import tailwindConfig from 'tailwind-config'

const fullConfig = resolveConfig(tailwindConfig)

export default {
    // Any server data we get from server.
    server_data: {},
    // Any global variables we get from server. Mostly API endpoints.
    global_variables: {},
    loggedIn: false,
    token: '',
}