/**
 * Local Forage plugin. Helper plugin to store data into localstorage.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/plugis/localforage.js
 * @exports LocalForage Instance
 */

import localforage from "localforage/src/localforage"

localforage.config({
    name: 'wave web app',
    driver: localforage.LOCALSTORAGE
})

const localForage = localforage

export default localForage