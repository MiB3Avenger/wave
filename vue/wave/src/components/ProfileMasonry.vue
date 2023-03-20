<script setup>
import {OhVueIcon as VIcon} from "oh-vue-icons";

const props = defineProps(['list']);

</script>
<template>
    <MasonryWall :items="props.list" :column-width="250" :gap="10">
        <template #default="{ item, index }">
        <div
            :style="{ height: `${item.height}` }"
            class="post flex items-center justify-center"
        >
            <div class="post-details">
                <span class="likes"><VIcon name="md-favorite-round"/>{{ item.likes }}</span>
                <span class="comments"><VIcon name="md-chatbubble-round"/>{{ item.comments }}</span>
            </div>
            <div class="post-image">
                {{ index }}
            </div>
        </div>
        </template>
    </MasonryWall>
</template>
<style lang="scss">
.user-posts {
    .post {
        min-height: 150px;
        width: 100%;
        line-height: 150px;
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
            line-height: 100%;
            padding: 0.5rem;
            font-size: small;
            -webkit-user-select: none;
            -ms-user-select: none;
            user-select: none;
            span {
                display: flex;
                align-items: center;
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
    }
}
</style>