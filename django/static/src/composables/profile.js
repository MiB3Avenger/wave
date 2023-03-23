import { ref, reactive } from 'vue';
import { reset } from "@formkit/core";

import useAxios from './axios';
import useAxiosHeader from './axiosHeader';
import useUsers from './users';

export default function useProfile() {
    const axios = useAxios();
    const { user } = useUsers();

    const uploadProfilePicture = async (data) => {

        const formData = new FormData()

        data.picture.forEach((fileItem) => {
            formData.append('photo', fileItem.file)
        });

        // Upload image...
        await axios.axiosInstance.put('profile/picture', formData, {
            headers: useAxiosHeader()
        }).then(response => {
            reset('uploadProfilePicture')
            user.profile.photo = response.data.photo;
        }).catch(errors => {
            console.log(errors);
        })
    }


    return { uploadProfilePicture };
}