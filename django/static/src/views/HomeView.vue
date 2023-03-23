<script setup>
import Authenticated from "../layouts/Authenticated.vue";

import usePosts from "../composables/posts";

const { getPosts, posts } = usePosts()

getPosts();

</script>

<template>
    <Authenticated>
        <div class="feed-container">
            <div class="feed">
                <div class="post" v-for="(post, index) in posts?.data" :key="index">
                    <div class="head">
                        <div class="user">
                            <div class="profile-photo">
                                <img :src="post.author?.detail?.photo" :alt="post.author?.username+'\'s profile picture'">
                            </div>
                            <div class="ingo">
                                <RouterLink v-if="post.author?.username != undefined" :to="{name: 'profile-username', params: { username: post.author?.username }}"><h3>{{ post.author?.first_name }}</h3></RouterLink>
                                
                                <RouterLink v-if="post?.id" :to="{name: 'post', params: { id: post?.id }}"><small>{{ post.posted_at }}</small></RouterLink>
                            </div>
                        </div>
                    </div>

                    <div class="photo">
                        <img v-if="post?.image" :src="post?.image" :alt="post?.body">
                    </div>

                    <div class="action-buttons">
                        <div class="interaction-buttons">
                            <button>
                                <v-icon name="md-favorite-twotone" />
                                <v-icon v-if="false" name="md-favorite-round" />
                            </button>
                            <button>
                                <v-icon name="md-chatbubble-round" />
                            </button>
                            <button>
                                <v-icon name="md-share-round" />
                            </button>
                        </div>
                    </div>

                    <div class="liked-by">
                        <p>liked by <span>{{ post.likes_count }} people</span></p>
                    </div>

                    <div class="caption">
                        <p>
                            <RouterLink v-if="post.author?.username" :to="{name: 'profile-username', params: { username: post.author?.username }}"><span>{{ post.author?.first_name.trim() }}</span></RouterLink>
                            {{ post?.body }}
                        </p>
                    </div>
                    <div class="comments text-muted">
                        <RouterLink v-if="post?.id" :to="{name: 'post', params: { id: post?.id }}">
                            View all comments
                        </RouterLink>
                    </div>
                </div>
            </div>
        </div>
    </Authenticated>
</template>

<style lang="scss">
.feed-container {
    display: flex;
    align-items: center;
    flex-direction: column;
}
.feed {
    width: 60%;
    .post {
        margin: 1rem 0;
        border-radius: 1rem;
        font-size: 0.85rem;
        line-height: 1.5;
        border: 1px solid var(--color-border);
        .head {
            display: flex;
            justify-content: space-between;
            padding-bottom: 0.7rem;
            padding: 1rem;
            border-bottom: 1px solid var(--color-border);
            h3 {
                font-weight: bold;
            }
        }
        .profile-photo {
            width: 2.7rem;
            aspect-ratio: 1/1;
            border-radius: 50%;
            overflow: hidden;
            img {
                display: block;
                width: 100%;
            }
        }
        .user {
            display: flex;
            gap: 1rem;
        }
        .photo {
            overflow: hidden;
            margin: 0;
            border-bottom: 1px solid var(--color-border);
            img {
                display: block;
                width: 100%;
            }
        }
        .action-buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.4rem;
            padding: .75rem 1rem;
            border-bottom: 1px solid var(--color-border);
            button {
                background: none;
                color: var(--color-text);
                border: 0;
                &:hover {
                    cursor: pointer;
                }
                svg {
                    height: 2rem;
                    width: 2rem;
                    border-radius: 1rem;
                    padding: .25rem;
                    border: 1px solid transparent;
                    margin: 0 !important;
                    &:hover {
                        border: 1px solid var(--color-border);
                        background-color: var(--color-background-soft);
                    }
                }
            }
        }
        .liked-by {
            display: flex;
            padding: 1rem;
            > span {
                width: 1.4rem;
                height: 1.4rem;
                display: block;
                border-radius: 50%;
                overflow: hidden;
                border: 2px solid #fff;
                margin-left: -0.6rem;
                img {
                    display: block;
                    width: 100%;
                }
                &:first-child {
                    margin: 0;
                }
            }
            p {
                margin-left: 0.5rem;
                span {
                    font-weight: bold;
                }
            }
        }
        .caption {
            padding: 0 1rem;
            span {
                font-weight: bold;
            }
        }
        .comments {
            padding: 0.5rem 1rem;
            &.text-muted {
                color: var(--color-text-mute);
            }
        }
    }
}
@media (max-width: 768px) {
    .feed {
        width: 100%;
    }
}
</style>