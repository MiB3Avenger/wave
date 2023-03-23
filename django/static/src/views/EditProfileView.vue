<script>
export default {
    methods: {
        handleFileUpload(){
            this.uploadPicture.file = this.$refs.file.files[0];
            console.log(uploadPicture.file, this.$refs.file);
        }
    }
}
</script>
<script setup>
import { reactive, ref } from "vue";
import { setErrors } from "@formkit/core";
import useAuth from "../composables/auth";
import useProfile from "../composables/profile";

import Authenticated from "../layouts/Authenticated.vue";
import UserDetails from "../components/profile/UserDetails.vue";
import GoBack from "../components/GoBack.vue";
import useUsers from "../composables/users";

const {getUser, user} = useUsers();
const { uploadProfilePicture, updateDetails } = useProfile();

getUser();

const changePassword = reactive({
    oldPassword: '',
    newPassword: '',
    confirmNewPassword: ''
});

const completed = ref(false);

const password = ref('');

</script>
<template>
    <Authenticated>
        <div class="user-profile edit-profile">
            <div class="user-details-with-back">
                <GoBack></GoBack>
                <UserDetails :user="user" :hideEdit="true"></UserDetails>
            </div>
            <div class="change-details flex">
                <div class="flex column change-profile-picture">
                    <div class="upload-file">
                        <FormKit type="form" id="uploadProfilePicture" @submit="uploadProfilePicture">
                            <FormKit :floating-label="true" type="file" name="picture" accept=".png,.jpg,.jpeg,.bmp" help="Upload a new profile picture" multiple="false" validation="required" />
                        </FormKit>
                    </div>
                </div>
            </div>
        </div>
    </Authenticated>
</template>
<style lang="scss">
.user-profile.edit-profile {
    display: flex;
    flex-direction: column;
    .user-details-with-back {
        display: flex;
        flex-direction: row-reverse;
    }
    .user-details {
        margin-right: 0;
        margin-left: 4rem;
        width: 100%;
    }
    .change-details {
        justify-content: space-around;
        margin-bottom: 2rem;
        form {
            flex: 0 1 50%;
            .formkit-wrapper {
                max-width: 100%;
            }
        }
        .change-user-details {
            margin-top: 2rem;
        }
    }
}
.go-back {
    margin-top: 2rem;
}

@media (max-width: 768px) {
    .user-profile.edit-profile {
        .user-details-with-back {
            flex-direction: column-reverse;
            .user-details {
                margin-left: 0;
            }
            .go-back {
                margin-top: 0;
                margin-bottom: 2rem;
            }
        }
    }
}
</style>