import axios from 'redaxios';

export default function useProfile() {
    const uploadProfilePicture = async (data) => {
        const formData = new FormData();

        data.picture.forEach((fileItem) => {
            formData.append('file', fileItem)
        });

        // Upload image...
        
    }


    return { uploadProfilePicture };
}