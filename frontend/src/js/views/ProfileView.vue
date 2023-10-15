<script setup>
import { useRoute, onBeforeRouteLeave, onBeforeRouteUpdate } from "vue-router";

import useAuth from "../composables/auth";

import Authenticated from "../layouts/Authenticated.vue";
import ProfileMasonry from "../components/ProfileMasonry.vue";
import UserDetails from "../components/profile/UserDetails.vue";
import useUsers from "../composables/users";


const { user, getUser, getUserByUserName } = useUsers();
const props = defineProps(['username']);
const route = useRoute();

const random = (min, max) => {
  return Math.floor(Math.random() * (max - min) ) + min;
}

if(props.username != ''){
    if(props.username != user.username && route.params?.name == 'profile-username'){
        getUserByUserName(props.username);
    }
} else {
    getUser();
}

if(route.params.name == 'profile'){
    getUser();
}

if(route.params.name == 'profile-username') {
    getUserByUserName(props.username);
}

onBeforeRouteLeave(async (to, from) => {
    if(to.name == 'profile'){
        getUser();
    }

    if(to.name == 'profile-username') {
        getUserByUserName(to.params.username);
    }
})

onBeforeRouteUpdate(async (to, from) => {
    if(from.params.username == undefined){
        await getUserByUserName(to.params.username);
    } else {
        if(to.params.username != from.params.username){
            await getUserByUserName(to.params.username);
        } else {
            await getUser();
        }
    }
})

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
            <UserDetails :user="user"></UserDetails>
            <div class="user-posts" v-if="user.posts.length > 0">
                <ProfileMasonry :list="user.posts"></ProfileMasonry>
            </div>
            <div class="user-error" v-else>
                No posts found.
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