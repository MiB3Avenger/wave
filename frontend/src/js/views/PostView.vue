<script setup>
import { ref } from 'vue';
import Authenticated from '../layouts/Authenticated.vue';
import usePosts from '../composables/posts';

const props = defineProps(['id'])
const { getPostById, addCommentByPostId, responsePost, refresh } = usePosts();

getPostById(props.id);

const comment = ref('')

console.log(responsePost);

</script>
<template>
    <Authenticated class="post-view">
        <div class="feed-container">
            <div class="feed">
                <div class="post">
                    <div class="head">
                        <div class="user">
                            <div class="profile-photo">
                                <img :src="responsePost.author?.detail?.photo" :alt="responsePost.author?.username+'\'s profile picture'">
                            </div>
                            <div class="ingo">
                                <RouterLink v-if="responsePost.author?.username != undefined" :to="{name: 'profile-username', params: { username: responsePost.author?.username }}"><h3>{{ responsePost.author?.first_name }}</h3></RouterLink>
                                
                                <RouterLink v-if="responsePost?.id" :to="{name: 'post', params: { id: responsePost?.id }}"><small>{{ responsePost?.posted_at }}</small></RouterLink>
                            </div>
                        </div>
                    </div>

                    <div class="photo">
                        <img v-if="responsePost?.image" :src="responsePost?.image" :alt="responsePost?.body">
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
                        <p>Liked by <span>{{ responsePost.likes_count }} people</span></p>
                    </div>

                    <div class="caption">
                        <p>
                            <RouterLink v-if="responsePost.author?.username" :to="{name: 'profile-username', params: { username: responsePost.author?.username }}"><span>{{ responsePost.author?.first_name.trim() }}</span></RouterLink>
                            {{ responsePost?.body }}
                        </p>
                    </div>
                    <div class="comments text-muted">
                        <FormKit :floating-label="true" id="comment" label="Add a comment" type="text" v-model="comment" @keyup.enter="addCommentByPostId(comment)"></FormKit>
                        <div v-if="responsePost?.comments">
                            <p v-for="(item,index) in responsePost?.comments" :key="index">
                                <RouterLink :to="{name: 'profile-username', params: { username: item?.author.username }}"><span>{{ item.author.first_name }}</span></RouterLink> {{ item.body }}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </Authenticated>
</template>
<style lang="scss">
.post-view {
    .feed {
        .caption {
            margin-bottom: .5rem;
        }
        .comments {
            .formkit-wrapper {
                max-width: 100% !important;
                .formkit-input {
                    padding: .75rem !important;
                }
            }
            p {
                margin-bottom: .25rem;
                span {
                    font-weight: bold;
                    color: var(--color-text-mute);
                }
            }
        }
    }
}
</style>