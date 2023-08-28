import { createApp } from 'vue'
import router from './router'
import store from './store'
import { loadFonts } from './plugins/webfontloader'
import App from './App'

import { OhVueIcon, addIcons } from "oh-vue-icons"
import * as MdIcons from "oh-vue-icons/icons/md"

import MasonryWall from '@yeger/vue-masonry-wall'

import { plugin, defaultConfig } from '@formkit/vue'
import { createFloatingLabelsPlugin } from '@formkit/addons'
import '@formkit/addons/css/floatingLabels';

import "@formkit/themes/genesis";

import "@app/css/style.scss"
import "@app/assets/favicon.ico"

const Md = Object.values({ ...MdIcons })
addIcons(...Md)

const formkitConfig = defaultConfig({
  plugins: [createFloatingLabelsPlugin()]
})

loadFonts()

createApp(App)
  .use(router)
  .use(MasonryWall)
  .use(plugin, formkitConfig)
  .use(store)
  .component("v-icon", OhVueIcon)
  .mount('#app')
