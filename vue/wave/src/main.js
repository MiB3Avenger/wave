import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import { OhVueIcon, addIcons } from "oh-vue-icons";
import * as MdIcons from "oh-vue-icons/icons/md";

import MasonryWall from '@yeger/vue-masonry-wall';

import { plugin, defaultConfig } from '@formkit/vue';
import { createFloatingLabelsPlugin } from '@formkit/addons';
import '@formkit/addons/css/floatingLabels';

import "@formkit/themes/genesis";
import "./assets/main.scss";

const Md = Object.values({ ...MdIcons });
addIcons(...Md);

const app = createApp(App);

const formkitConfig = defaultConfig({
    plugins: [createFloatingLabelsPlugin()]
})

app.use(router);
app.use(MasonryWall);
app.use(plugin, formkitConfig);
app.component("v-icon", OhVueIcon);
app.mount("#app");
