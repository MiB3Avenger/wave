/**
 * All actions for our store.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/store/actions.js
 * @exports Object Actions
 */

export default {
    // state.loggedIn
    changeLoggedIn({ commit }, loggedIn) {
        commit('changeLoggedIn', loggedIn)
    },
    resetLoggedIn({ commit }) {
        commit('resetLoggedIn')
    },
    // state.token
    changeToken({ commit }, token) {
        commit('changeToken', token)
    },
    resetToken({ commit }) {
        commit('resetToken')
    },
}