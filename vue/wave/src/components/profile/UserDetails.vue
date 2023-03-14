<script setup>
const props = defineProps(['user', 'hideEdit']);
</script>
<template>
    <div class="user-details">
        <div class="user-profile-picture">
            <v-icon name="md-person-round" />
        </div>
        <div class="user-information">
            <RouterLink v-if="!hideEdit" :to="{name: 'edit-profile'}" class="action-btn">Edit Profile</RouterLink>
            <div class="user-information-data">
                <div class="posts"><span>{{ user.posts }}</span>posts</div>
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
    padding: 1rem 6rem 2rem;
    margin: 1rem 8rem 2rem;
    border-bottom: 1px solid var(--color-border);;
    
    .user-profile-picture {
        flex: 1 0 auto;
        width: 20%;
        margin-right: 2rem;
        svg {
            height: auto;
            width: 100%;
            padding: .75rem;
            border-radius: 8rem;
            border: .25rem solid
        }
    }

    .user-information {
        flex: 4 0 auto;
        width: max-content;
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
</style>