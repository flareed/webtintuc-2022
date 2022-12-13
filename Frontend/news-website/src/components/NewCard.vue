<template>
        <a :href="`/${section}/${slugify(this.title)}`" class="row py-3 border-bottom border-dark text-dark">
            <div class="col-5">
                <img :src=img class="img-fluid" :alt=title width="200" height="133.33">
            </div>
            <div class="col">
                <div class="row">
                    <h5>{{ title }}</h5>
                </div>
                <div class="row">
                    <p>{{ description }}</p>
                </div>
            </div>
        </a>
</template>
    
<script>
import myLib from '@/helpers';
export default {
    name: 'NewCard',
    props: {
        img: String,
        title: String,
        description: String,
    },
    data() {
        return {
            section: 'the-gioi',
        }
    },
    methods: {
        slugify(str){
            return myLib.toSlug(str)
        }
    }
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
    text-decoration: none;
}

a:hover{
    color: #0d6efd !important;
}
</style>