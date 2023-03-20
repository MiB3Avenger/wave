<script>
</script>
<script setup>
import { ref, onMounted } from 'vue'
import Authenticated from '../layouts/Authenticated.vue';

const file = ref(null);
const img = ref(null);

const addMedia = (file) => {
    file.click();
}

const removeMedia = () => {
    img.value = null;
}

const changeMedia = (e) => {
    const file = e.target.files[0];
    img.value = URL.createObjectURL(file);
}

const uploadPost = () => {
    console.log('uploading...');
}
</script>
<template>
    <Authenticated>
        <div class="create-post">
            <div class="actions">
                <input type="file" ref="file" class="media-input" accept="image/png, image/jpeg" @change="changeMedia" />
                <button class="action-btn inverted" @click="addMedia(file)"><v-icon name="md-add-round" />Add media</button>
                <button class="action-btn inverted" @click="removeMedia()" v-if="img != null"><v-icon name="md-close-round" />Remove media</button>
                <div class="bold">Create new post</div>
                <button class="action-btn" @click="uploadPost"><v-icon name="md-share-round" />Share</button>
            </div>
            <div class="create-post-container">
                <div class="media">
                    <img v-if="img != null" :src="img" alt="">
                    <div v-else>
                        Add media to see a preview here.
                    </div>
                </div>
                <div class="description">
                    <div class="caption">
                        <FormKit 
                            type="textarea"
                            placeholder="Write a caption...">
                        </FormKit>
                    </div>
                    <div class="location">
                        <FormKit 
                            type="search"
                            placeholder="Add a location...">
                        </FormKit>
                    </div>
                </div>
            </div>
        </div>
    </Authenticated>
</template>
<style lang="scss">
.create-post {
    display: flex;
    flex-direction: column;
    margin-top: 1rem;
    .actions {
        display: flex;
        flex-direction: row;
        flex: 1 0 100%;
        justify-content: space-between;
        align-items: center;
        input {
            display: none;
        }
        button {
            padding: 1.25rem;
            border-radius: 30px;
        }
    }
    .create-post-container {
        display: flex;
        flex-direction: row;
        flex: 1 0 100%;
        justify-content: space-between;
        margin-top: 2rem;
        > div {
            flex: 0 0 50%;
            width: 50%;
        }
        .media {
            margin-right: .5rem;
            border: 1px solid var(--color-border);
            div {
                padding: 1rem;
            }
            img {
                width: 100%;
            }
        }
        .description {
            margin-left: .5rem;
            .caption {
                height: 40vh;
                &::before {
                    content: "";
                    display: block;
                    width: 100%;
                    height: 1px;
                    background-color: var(--color-border);
                    position: absolute;
                    top: 0;
                }
                &::after {
                    content: "";
                    display: block;
                    width: 100%;
                    height: 1px;
                    background-color: var(--color-border);
                    position: absolute;
                    bottom: 0;
                }
            }
            .formkit-outer {
                margin: 0;
                height: 100%;
                .formkit-wrapper {
                    max-width: 100%;
                    height: 100%;
                    .formkit-inner {
                        box-shadow: none;
                        height: 100%;
                        textarea {
                            height: 100%;
                            resize: none;
                        }
                    }
                }
            }
            .location {
                display: none;
            }
        }
    }
}

@media (max-width: 768px) {
    .create-post {
        .create-post-container {
            flex-direction: column;
        }
    }
}

@media (max-width: 512px) {
    .create-post {
        .actions {
            button {
                padding: .5rem
            }
        }
    }
}
</style>