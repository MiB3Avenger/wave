export const STORAGE_KEY = 'wave-vuejs'

// for testing
if (navigator.webdriver) {
    window.localStorage.clear()
}

export const mutations = {
    server_data(state, server_data) {
        state.server_data = server_data
    },
    global_variables(state, global_variables) {
        state.global_variables = global_variables
    },
    changeLoggedIn(state, loggedIn) {
        state.loggedIn = loggedIn
    },
    resetLoggedIn(state) {
        state.loggedIn = false
    },
    changeToken(state, token) {
        state.token = token
    },
    resetToken(state) {
        state.token = ''
    },
}