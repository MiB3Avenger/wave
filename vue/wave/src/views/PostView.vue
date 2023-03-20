<script setup>
import Authenticated from '../layouts/Authenticated.vue';

const props = defineProps(['id'])
</script>
<template>
    <Authenticated class="post-view">
        <div class="feed-container">
            <div class="feed">
                <div class="post">
                    <div class="head">
                        <div class="user">
                            <div class="profile-photo">
                                <img src="../assets/images/profile-1.png">
                            </div>
                            <div class="ingo">
                                <h3>Amy</h3>
                                <small>15 minutes ago</small>
                            </div>
                        </div>
                        <span class="edit">
                            <i class="uil uil-ellipsis-h"></i>
                        </span>
                    </div>

                    <div class="photo">
                        <img src="../assets/images/profile-1.png">
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
                        <span><img src="../assets/images/profile-1.png"></span>
                        <span><img src="../assets/images/profile-1.png"></span>
                        <span><img src="../assets/images/profile-1.png"></span>
                        <p>liked by <span>3,304 people</span></p>
                    </div>

                    <div class="caption">
                        <p><span>Amy</span> I like to go shopping.</p>
                    </div>
                    <div class="comments text-muted">
                        <FormKit :floating-label="true" label="Add a comment" type="text"></FormKit>
                        <p><span>Amy</span> I like to go shopping.</p>
                        <p><span>Amy</span> I like to go shopping.</p>
                        <p><span>Amy</span> I like to go shopping.</p>
                        <p><span>Amy</span> I like to go shopping.</p>
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
                span {
                    font-weight: bold;
                }
            }
        }
    }
}
</style>