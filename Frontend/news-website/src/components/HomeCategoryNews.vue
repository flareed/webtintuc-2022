<template>
    <h5>{{category}}</h5>
    <div class="row">

    </div>
</template>
    
<script>
import NewCard from './NewCard.vue';
export default {
    name: 'HomeCategoryNews',
    components: {
        NewCard,
    },
    props: {
        category: String,
        content: [
            {
                
            }
        ]
    }
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>