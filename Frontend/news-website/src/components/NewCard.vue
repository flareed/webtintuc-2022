<template>
    <div class="row py-3 border-bottom border-dark">
        <div class="col-5">
            <img :src=img class="img-fluid" :alt=title width="200" height="133.33">
        </div>
        <div class="col">
            <div class="row">
                <h5>{{title}}</h5>
            </div>
            <div class="row">
                <p>{{description}}</p>
            </div>
        </div>
    </div>
</template>
    
<script>
export default {
    name: 'NewCard',
    props: {
        img: String,
        title: String,
        description: String,
    }
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>