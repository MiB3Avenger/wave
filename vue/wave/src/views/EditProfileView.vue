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

const {getUser, user} = useAuth();
const { uploadProfilePicture } = useProfile();

getUser();

const editProfile = reactive({
    username : user.username,
    email: user.email,
    oldPassword: '',
    newPassword: '',
    confirmNewPassword: ''
});

const changePassword = reactive({
    oldPassword: '',
    newPassword: '',
    confirmNewPassword: ''
});

const completed = ref(false);

</script>
<template>
    <Authenticated>
        <div class="user-profile edit-profile">
            <div class="user-details-with-back">
                <GoBack></GoBack>
                <UserDetails :user="user" :hideEdit="true"></UserDetails>
            </div>
            <div class="change-details">
                <FormKit type="form" @submit="uploadProfilePicture">
                    <FormKit type="file" name="picture" accept=".png,.jpg,.jpeg,.bmp" help="Upload a new profile picture" multiple="false" validation="required" />
                </FormKit>
                <FormKit type="form">
                    <FormKit v-model="editProfile.username" type="text" label="Change Username" help="Pick a new username." validation="required|length:4" value="@useFormKit" />
                    <FormKit v-model="editProfile.email" type="text" label="Change Email" help="Update your account's email to another email." validation="required|email" value="@useFormKit" />
                    <FormKit v-model="editProfile.oldPassword" type="text" label="Password" help="For verifying if it's you who's changing your details." validation="required|password" value="@useFormKit" />
                </FormKit>
                <FormKit type="form">
                    <FormKit v-model="changePassword.oldPassword" type="password" label="Old Password" help="For verifying if it's you who's changing your password." validation="required|password" value="@useFormKit" />
                    <FormKit v-model="changePassword.newPassword" type="password" label="New Password" help="Change your account's password." validation="required|password" value="@useFormKit" />
                    <FormKit v-model="changePassword.confirmNewPassword" type="password" label="Confirm New Password" help="Confirming your new password." validation="required|password" value="@useFormKit" />
                </FormKit>
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
}
.go-back {
    margin-top: 2rem;
}
</style>