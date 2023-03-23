<script setup>
import { ref, onMounted } from 'vue'
import Authenticated from '../layouts/Authenticated.vue';
import usePosts from '../composables/posts';
import useUsers from '../composables/users';

const { user } = useUsers();

const file = ref(null);
const caption = ref('');
const error = ref('');
const img = ref(null);
let fileInputKey = 0

const { uploadPost } = usePosts();

const addMedia = (file) => {
    error.value = ''
    file.click();
}

const removeMedia = () => {
    fileInputKey++
    img.value = null;
}

const changeMedia = (e) => {
    const fileObject = e.target.files[0];
    img.value = URL.createObjectURL(fileObject);
}

const upload = () => {
    console.log(file.value.files, caption);
    console.log('uploading...');
    error.value = ''
    if(file.value.files.length == 0 || file.value == null){
        error.value = 'Please select a file!'
    } else if(caption.value == '') {
        error.value = 'Please enter a caption!'
    } else {
        const body = new FormData()
        body.append('body', caption.value)
        body.append('image', file.value.files[0])

        const data = {'body': caption.value, 'image': file.value.files[0], 'user': user.id}

        console.log(data);

        // uploadPost(body)
        uploadPost(data)
    }

    console.log(error.value);
}
</script>
<template>
    <Authenticated>
        <div class="create-post">
            <div class="actions">
                <input type="file" ref="file" class="media-input" accept="image/png, image/jpeg" @change="changeMedia" :key="fileInputKey" />
                <button class="action-btn inverted" @click="addMedia(file)"><v-icon name="md-add-round" />Add media</button>
                <button class="action-btn inverted" @click="removeMedia()" v-if="img != null"><v-icon name="md-close-round" />Remove media</button>
                <div class="bold">Create new post</div>
                <button class="action-btn" @click="upload"><v-icon name="md-share-round" />Share</button>
            </div>
            <div class="custom-error formkit-message" v-if="error.value != ''">{{ error }}</div>
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
                            v-model="caption"
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
            cursor: pointer;
        }
    }
    .custom-error {
        margin-top: 1rem;
    }
    .create-post-container {
        display: flex;
        flex-direction: row;
        flex: 1 0 100%;
        justify-content: space-between;
        margin-top: 1rem;
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