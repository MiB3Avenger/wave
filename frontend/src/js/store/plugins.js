/**
 * Plugin actions for our store.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/store/plugins.js
 * @exports function Store Plugin
 */

// Base plugin imports.
import { createLogger } from 'vuex'
import { STORAGE_KEY } from './mutations'
import localForage from '@app/js/plugins/localforage'

/**
 * Creates a localstorage plugin and helps subscribe data into user's browser.
 * 
 * @param {Store} store 
 */
const localStoragePlugin = store => {
    // Subscribe to current module.
    store.subscribe((mutation, { server_data }) => {
        localForage.setItem(STORAGE_KEY+"-server-data", JSON.stringify(server_data))
    })

    store.subscribe((mutation, { token }) => {
        localForage.setItem(STORAGE_KEY+"-token", JSON.stringify(token))
    })

    store.subscribe((mutation, { loggedIn }) => {
        localForage.setItem(STORAGE_KEY+"-logged-in", JSON.stringify(loggedIn))
    })
}

// Decide whether to create a logger or not based on environment.
export default process.env.NODE_ENV !== 'production'
    ? [createLogger(), localStoragePlugin]
    : [localStoragePlugin]