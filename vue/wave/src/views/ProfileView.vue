<script>
const win = this;
export default {
    methods: {
        alert: (text) => {
            console.log(text);
        }
    }
}
</script>
<script setup>
import { useRoute } from "vue-router";

import useAuth from "../composables/auth";

import Authenticated from "../layouts/Authenticated.vue";
import ProfileMasonry from "../components/ProfileMasonry.vue";
import UserDetails from "../components/profile/UserDetails.vue";


const { getUser, getUserById, user } = useAuth();
const props = defineProps(['username']);
const route = useRoute();

const random = (min, max) => {
  return Math.floor(Math.random() * (max - min) ) + min;
}

getUser();

if(user.username != props.username && route.name != 'profile'){
    getUserById(props.username);
}

const list = [{
    title:"test",
    height: random(150, 300)+'px',
    likes: 10,
    comments: 10,
},
{
    title:"test",
    height: random(150, 300)+'px',
    likes: 10,
    comments: 10,
},
{
    title:"test",
    height: random(150, 300)+'px',
    likes: 10,
    comments: 10,
},
{
    title:"test",
    height: random(150, 300)+'px',
    likes: 10,
    comments: 10,
},
{
    title:"test",
    height: random(150, 300)+'px',
    likes: 10,
    comments: 10,
},
{
    title:"test",
    height: random(150, 300)+'px',
    likes: 10,
    comments: 10,
},
{
    title:"test",
    height: random(150, 300)+'px',
    likes: 10,
    comments: 10,
},
{
    title:"test",
    height: random(150, 300)+'px',
    likes: 10,
    comments: 10,
}]
</script>
<template>
    <Authenticated>
        <div class="user-profile">
            <UserDetails :user="user" :hideEdit="false"></UserDetails>
            <div class="user-posts">
                <ProfileMasonry :list="list"></ProfileMasonry>
            </div>
        </div>
    </Authenticated>
</template>

<style lang="scss">
.user-posts {
    display: flex;
    flex-wrap: wrap;
    margin-bottom: 2rem;
    // padding: 0 1rem;
    .masonry-wall {
        width: 100%;
    }
}
</style>