<script setup>
import {OhVueIcon as VIcon} from "oh-vue-icons";

const props = defineProps(['list']);

</script>
<template>
    <MasonryWall :items="props.list" :column-width="250" :gap="10">
        <template #default="{ item, index }">
        <RouterLink :to="{name: 'post', params: {id: item.id}}">
        <div
            :style="{ height: `${item.height}` }"
            class="post flex items-center justify-center"
        >
            <div class="post-details">
                <span class="likes"><VIcon name="md-favorite-round"/>{{ item.likes_count }}</span>
                <!-- <span class="comments"><VIcon name="md-chatbubble-round"/>{{ item.comments }}</span> -->
            </div>
            <div class="post-image">
                <img :src="item.image" :alt="item.body">
            </div>
        </div>
        </RouterLink>
        </template>
    </MasonryWall>
</template>
<style lang="scss">
.user-posts {
    .post {
        width: 100%;
        background: #EC985A;
        color: white;
        margin-bottom: 1%;
        text-align: center;
        font-family: system-ui;
        font-weight: 900;
        font-size: 2rem;
        &:hover {
            cursor: pointer;
            &::before {
                opacity: .4;
            }
            .post-details {
                opacity: 1;
            }
        }
        .post-details {
            display: flex;
            position: absolute;
            width: 100%;
            height: 100%;
            opacity: 0;
            z-index: 9999;
            justify-content: flex-end;
            align-items: flex-end;
            // line-height: 100%;
            font-size: small;
            -webkit-user-select: none;
            -ms-user-select: none;
            user-select: none;
            span {
                display: flex;
                align-items: center;
                padding: 0.5rem;
                &:not(:first-child) {
                    margin-left: .25rem;
                }
            }
            .ov-icon {
                margin-right: 0.1rem;
            }
        }
        &::before {
            content: '';
            display: block;
            position: absolute;
            width: 100%;
            height: 100%;
            background-color: var(--color-background-mute);
            opacity: 0;
            z-index: 9998;
        }
        .post-image {
            img {
                width: 100%;
                height: 100%;
            }
        }
    }
}
</style>