<script>
export default {
    methods: {
        bringNotifications: function() {
            if(!this.notificationsOpen){
                document.querySelector('.notification-container').style.left = "0";
            } else {
                document.querySelector('.notification-container').style.left = "calc(-300px - 0.5rem)";
            }
            this.notificationsOpen=!this.notificationsOpen;
        },
        bringSearch: function() {
            if(!this.searchOpen){
                document.querySelector('.search-container').style.left = "0";
            } else {
                document.querySelector('.search-container').style.left = "calc(-300px - 0.5rem)";
            }
            this.searchOpen=!this.searchOpen;
        }
    },
    data() {
        return {
            notificationsOpen: false,
            searchOpen: false
        };
    }
}
</script>
<script setup>
import { reactive, inject, isProxy, toRaw } from "vue";
import { useRoute } from "vue-router";
import useAuth from "../composables/auth";
import useUsers from "../composables/users";
import useSearch from "../composables/search";

const route = useRoute();
const { logout } = useAuth();
const { user } = useUsers();
const { search, searchUser } = useSearch();

</script>

<template>
    <div class="sidebar">
        <div class="sidebar-container">
            <div class="sidebar-logo">
                <img
                alt="Vue logo"
                class="logo"
                src="@app/assets/logo.svg"
                width="45"
                height="45"
                />
            </div>
            <div class="sidebar-items">
                <header>
                    <div class="wrapper">
                        <nav>
                            <RouterLink :to="{name: 'home'}"><v-icon name="md-home-round" /><span>Home</span></RouterLink>
                            <a href="javascript:;" @click="bringSearch()"><v-icon name="md-search-round" /><span>Search</span></a>
                            <a href="javascript:;" @click="bringNotifications()"><v-icon name="md-notifications-round" /><span>Notifications</span></a>
                            <RouterLink :to="{name:'create'}"><v-icon name="md-create-round" /><span>Create</span></RouterLink>
                            <RouterLink :to="{name: 'profile'}"><v-icon name="md-person-round" /><span>Profile</span></RouterLink>
                            <a href="javascript:;" @click="logout"><v-icon name="md-logout-round" /><span>Logout</span></a>
                        </nav>
                    </div>
            
                    <div class="footer">
                        <footer>
                            <RouterLink to="/about">Contact</RouterLink>
                            <RouterLink to="/about">Contact</RouterLink>
                            <RouterLink to="/about">Contact</RouterLink>
                        </footer>
                    </div>
                </header>
            </div>
        </div>
        <div class="notification-container">
            <div class="back-sidebar">
                <a class="action-btn" href="javascript:;" @click="bringNotifications()"><v-icon name="md-arrowback-round" />back</a>
            </div>
            <div class="notifications">
                <h2 class="notification-title">Notifications</h2>
                <div class="notification-items">
                    <div class="notification-item">
                        <div class="user-image"><v-icon name="md-person-round" /></div>
                        <div class="notification-details"><span>User</span> followed you!</div>
                    </div>
                    <div class="notification-item">
                        <div class="user-image"><v-icon name="md-person-round" /></div>
                        <div class="notification-details"><span>User</span> commented on your photo!</div>
                    </div>
                    <div class="notification-item">
                        <div class="user-image"><v-icon name="md-person-round" /></div>
                        <div class="notification-details"></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="search-container">
            <div class="back-sidebar">
                <a class="action-btn" href="javascript:;" @click="bringSearch()"><v-icon name="md-arrowback-round" />back</a>
            </div>
            <div class="search">
                <h2 class="search-title">Search</h2>
                <div class="search-input">
                    <FormKit type="text" @keyup="searchUser" debounce="1000" label="Search User" :floating-label="true"></FormKit>
                </div>
                <div class="search-items" v-if="search?.results.length > 0">
                    <RouterLink v-for="result in search?.results" :to="{name:'profile-username', params: {username: result.username}}">
                        <div class="search-item">
                            <div class="user-image"><v-icon name="md-person-round" /></div>
                            <div class="search-details"><span>@{{result.username}}</span>{{result.first_name}} {{result.last_name}}</div>
                        </div>
                    </RouterLink>
                </div>
                <div class="search-error" v-else>
                    {{ search?.error }}
                </div>
            </div>
        </div>
    </div>
    
</template>

<style scoped lang="scss">
.sidebar {
    max-height: 100vh;
    width: 300px;
}

.sidebar-container {
    display: flex;
    flex-direction: column;
    border-right: 1px solid var(--color-border);
    height: 100%;
    position: absolute;
    width: 100%;
    top: 0;
    left: 0;
    .sidebar-items {
        height: 100%;
    }
    .sidebar-logo {
        height: 100px;
    }
}

header {
    line-height: 1.5;
    height: 100%;
    div:last-of-type {
        margin-top: auto;
        margin-bottom: 1rem;
    }
}

.logo {
    display: block;
    margin: 0 auto 2rem;
    height: inherit;
    border-bottom: 1px solid var(--color-border);
}

nav {
    width: 100%;
    font-size: 12px;
    text-align: center;
    margin-top: 2rem;
    a.router-link-exact-active {
        color: var(--color-text);
        &:hover {
            background-color: transparent;
        }
    }
    a {
        display: inline-block;
        padding: .75rem 1.5rem;
        border-radius: 30px;
        height: 100%;
        margin-bottom: 0.25rem;
        -webkit-user-select: none;
        -ms-user-select: none;
        user-select: none;
        &:hover{
            background-color: rgba(255, 255, 255, .1);
        }
    }
    a.router-link-active {
        background-color: rgba(255, 255, 255, .1);
        &:hover {
            background-color: rgba(255, 255, 255, .25);
        }
    }
}

.footer {
    display: flex;
    flex-direction: row;
    justify-content: center;
    font-size: small;
    footer {
        a {
            margin: 0 .5rem;
        }
    }
}

.notification-container {
    display: flex;
    flex-direction: column;
    max-height: 100vh;
    height: 100%;
    position: absolute;
    width: 100%;
    top: 0;
    left: calc(-300px - 0.5rem);
    padding-left: 1rem;
    background-color: var(--color-background);
    border-right: 1px solid var(--color-border);
    transition: left ease-in .4s;
    .back-sidebar {
        margin: 2rem 0;
        width: fit-content;
        border-bottom: 1px solid var(--color-border);
        padding-bottom: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .notifications {
        margin-right: 2rem;
    }
    .notification-title {
        border-bottom: 1px solid var(--color-border);
        padding-bottom: 1rem;
    }
    .notification-items {
        margin-top: 1rem;
        margin-right: .75rem;
    }
    .notification-item {
        display: flex;
        flex-direction: row;
        padding: 0.75rem 0.5rem 0;
        border-radius: 15px;
        border-bottom: 0.5rem solid transparent;
        margin-bottom: 1rem;
        &:hover {
            background-color: var(--color-background-mute);
        }
        .user-image {
            flex: 1 0 20%;
            margin-right: 1rem;
            svg {
                height: auto;
                width: 100%;
                padding: .25rem;
                border-radius: 8rem;
                border: .25rem solid
            }
        }
        .notification-details {
            flex: 8 1 80%;
            span {
                font-weight: bold;
            }
        }
    }
    .notification-item:not(:last-of-type):before {
        content: "";
        display: block;
        width: 90%;
        height: 1px;
        background-color: var(--color-border);
        position: absolute;
        bottom: -1rem;
    }
}

.search-container {
    display: flex;
    flex-direction: column;
    max-height: 100vh;
    height: 100%;
    position: absolute;
    width: 100%;
    top: 0;
    left: calc(-300px - 0.5rem);
    padding-left: 1rem;
    background-color: var(--color-background);
    border-right: 1px solid var(--color-border);
    transition: left ease-in .4s;
    .back-sidebar {
        margin: 2rem 0;
        width: fit-content;
        border-bottom: 1px solid var(--color-border);
        padding-bottom: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .search {
        margin-right: 2rem;
    }
    .search-title {
        border-bottom: 1px solid var(--color-border);
        padding-bottom: 1rem;
        margin-bottom: 1rem;
    }
    .search-input {
        border-bottom: 1px solid var(--color-border);
        margin-bottom: 1rem;
        .formkit-outer {
            margin-bottom: 1rem !important;
        }
    }
    .search-items {
        margin-top: 1rem;
        margin-right: .75rem;
    }
    .search-item {
        display: flex;
        flex-direction: row;
        padding: 0.75rem 0.5rem 0;
        border-radius: 15px;
        border-bottom: 0.5rem solid transparent;
        margin-bottom: 1rem;
        &:hover {
            background-color: var(--color-background-mute);
        }
        .user-image {
            flex: 1 0 20%;
            margin-right: 1rem;
            svg {
                height: auto;
                width: 100%;
                padding: .25rem;
                border-radius: 8rem;
                border: .25rem solid
            }
        }
        .search-details {
            flex: 8 1 80%;
            display: flex;
            flex-direction: column;
            span {
                font-weight: bold;
            }
        }
    }
    .search-item:not(:last-of-type):before {
        content: "";
        display: block;
        width: 90%;
        height: 1px;
        background-color: var(--color-border);
        position: absolute;
        bottom: -1rem;
    }
}

@media (min-width: 1024px) {
    .sidebar-logo {
        padding: 0 !important;
    }
    .logo {
        width: 45px !important;
        height: 100px !important;
        margin-left: 2rem !important;
    }
    header {
        padding-right: calc(var(--section-gap)/4) !important;
        nav {
            margin-top: 2rem !important;
            margin-left: 1rem !important;
            a {
                display: flex;
                flex-direction: row !important;
                align-items: center;
                padding: .75rem 1.5rem !important;
                margin: 0 !important;
                margin-bottom: 0.25rem !important;
                svg {
                    height: 19.2px !important;
                    width: 19.2px !important;
                    margin-right: .5rem !important;
                }
                > span {
                    display: block !important;
                }
            }
        }
    }
    .footer {
        display: flex !important;
    }
}

@media (max-width: 1024px) {
    .sidebar {
        flex: 1 0 50px;
        .sidebar-logo {
            padding: 0.5rem;
            height: auto;
            img {
                margin: 0;
                width: 100%;
                height: 60px;
            }
        }
        header {
            padding-right: 0;
            nav {
                margin: 0;
                a {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    margin: 0.75rem 0.25rem 0;
                    padding: 0.5rem 0;
                    svg {
                        height: 30px;
                        width: 30px;
                        margin: 0;
                    }
                    > span {
                        display: none;
                    }
                }
            }
        }
        .notification-container, .search-container {
            z-index: 9999;
            width: 300px;
        }
        .footer {
            display: none;
        }
    }
}

header {
    display: flex;
    flex-direction: column;
    padding-right: calc(var(--section-gap)/4);
    .wrapper {
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
    }
}

.logo {
    margin: 0;
    margin-left: 2rem;
}

nav {
    display: flex;
    flex-direction: column;
    text-align: left;
    margin-left: 1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
}
</style>