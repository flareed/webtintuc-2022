<template>
        <a :href="`/${slugify(this.category)}/${this.id}`" class="row py-3 border-bottom border-dark text-dark">
            <div class="col-4">
                <img :src="`http://127.0.0.1:8000${img}`" class="img-fluid cropped" :alt=title >
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
        category: String,
        id: Number
    },
    data() {
        return {
            
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
.cropped {
    width: 230px !important; 
    height: 153px !important; 
    overflow: hidden !important;
    object-fit: cover !important;
}
</style>