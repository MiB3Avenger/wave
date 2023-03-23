<script setup>
const props = defineProps(['user']);
</script>
<template>
    <div class="user-details">
        <div class="user-profile-picture">
            <v-icon name="md-person-round" v-if="user?.profile.photo == null" />
            <div v-else>
                <img :src="user?.profile.photo" :alt="user?.username+'\'s profile picture'">
            </div>
        </div>
        <div class="user-information">
            <RouterLink v-if="user?.auth_user" :to="{name: 'edit-profile'}" class="action-btn">Edit Profile</RouterLink>
            <div class="user-information-data">
                <div class="posts"><span>{{ user.posts.length }}</span>posts</div>
                <div class="followers clickable" @click="alert('clicked!')"><span>{{ user.followers }}</span>followers</div>
                <div class="following clickable" @click="alert('clicked!')"><span>{{ user.following }}</span>following</div>
            </div>
            <div class="user-username">
                <span class="name">{{ user?.name }}</span>
                <span class="username">
                    @{{ user?.username }}
                </span>
            </div>
        </div>
    </div>
</template>
<style lang="scss">
.user-details {
    display: flex;
    flex-direction: row;
    padding: 1rem 6rem 2rem 2rem;
    margin: 0 8rem 2rem 4rem;
    border-bottom: 1px solid var(--color-border);;
    
    .user-profile-picture {
        flex: 1 0 20%;
        margin-right: 2rem;
        svg, div > img {
            height: auto;
            width: 100%;
            padding: .75rem;
            border-radius: 8rem;
            border: .25rem solid
        }
        div > img {
            height: 100%;
            aspect-ratio: 1 / 1;
            object-fit: cover;
        }
    }

    .user-information {
        flex: 4 1 80%;
        display: flex;
        flex-direction: column;
        > *:not(:last-child){
            margin: 0 0 .75rem;
        }
        a {
            width: max-content;
        }
        .user-information-data {
            display: flex;
            flex-direction: row;
            div:not(:first-child) {
                margin-left: 2rem;
            }
            span {
                margin-right: 0.25rem;
                font-weight: bold;
            }
            .followers, .following {
                -webkit-user-select: none;
                -ms-user-select: none;
                user-select: none;
            }
        }
        .user-username {
            display: flex;
            flex-direction: column;
            font-size: small;
            .name {
                font-weight: bold;
                font-size: large;
                text-transform: capitalize;
            }
        }
    }
}

@media (max-width: 1024px) {
    .user-details {
        padding-left: 0rem;
        margin-left: 0rem;
        margin-right: 3rem;
    }
}

@media (max-width: 768px) {
    .user-profile-picture {
        flex-basis: 30%;
    }
}

@media (max-width: 512px) {
    .user-details {
        margin-right: 0rem;
        align-items: end;
        .user-profile-picture {
            flex-basis: 30%;
            margin-right: .5rem;
        }
    }
}
</style>