<template>
    <a :href="`/${slugify(this.category)}/${this.id}`" class="row py-4 border-bottom border-dark text-dark">
        <div class="col-2">
            <small>{{ handleDate(date) }}</small>
        </div>
        
        <div class="col">
            <div v-if="!isInSection" class="row">
                <h6 class="fw-bold text-uppercase">{{ category }}</h6>
            </div>
            <div class="row">
                <h5>{{ title }}</h5>
            </div>
            <div class="row">
                <p>{{ description }}</p>
            </div>
        </div>
        <div class="col-4">
            <img :src=img class="img-fluid cropped float-end" :alt=title >
        </div>
    </a>
</template>

<script>
    import myLib from '@/helpers';
    export default {
    name: 'SearchCard',
    props: {
        img: String,
        title: String,
        description: String,
        category: String,
        id: Number,
        date: String,
        isInSection: Boolean
    },
    data() {
        return {
            
        }
    },
    methods: {
        slugify(str){
            return myLib.toSlug(str)
        },
        handleDate(str) {
            return myLib.parseDateSmaller(str)
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
    object-fit: cover;
}
</style>