import { ref, reactive } from 'vue';
import { reset } from "@formkit/core";

import instance from '@app/js/plugins/axios';
import useAxiosHeader from '@app/js/composables/axiosHeader';
import useUsers from './users';

export default function useProfile() {
    const axios = instance;
    const { user } = useUsers();

    const uploadProfilePicture = async (data) => {

        const formData = new FormData()

        data.picture.forEach((fileItem) => {
            formData.append('photo', fileItem.file)
        });

        // Upload image...
        await axios.put('profile/picture/', formData, {
            headers: useAxiosHeader()
        }).then(response => {
            reset('uploadProfilePicture')
            user.profile.photo = response.data.photo;
        }).catch(errors => {
            console.log(errors);
        })
    }

    const updateDetails = async (data) => {
        await axios.post('profile/details/', data, {
            headers: useAxiosHeader()
        }).then(response => {
            reset('updateDetailsForm')
            user.username = response.data.username
            user.email = response.data.email
        })
    }

    return { uploadProfilePicture, updateDetails };
}