<template>
    <div class="mt-2 border-bottom px-2">
        <h6 class="font-weight-bold">{{ username }}</h6>
        <p class="mt-2">{{ content }}</p>
        <div class="row mb-2 pl-1">
            <div class="col">
                <div><font-awesome-icon icon="fa-solid fa-thumbs-up" />  {{ like }}</div>
            </div>
        </div>
    </div>
</template>
    
<script>
export default {
    name: 'CommentCard',
    props: {
        username: String,
        content: String,
        like: Number,
    },
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>