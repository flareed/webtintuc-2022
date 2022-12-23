<template>
    <a :href="`/${slugify(this.category)}/${this.id}`" class="row py-3 border-bottom border-dark text-dark">
        <h5 class="mb-3 title-style">{{ title }}</h5>
        <div class="row">
            <div class="col-5">
                <img :src=img class="img-fluid" :alt=title width="200" height="133.33">
            </div>
            <div class="col">
                <p>{{ description }}</p>
            </div>
        </div>
    </a>
</template>

<script>
import myLib from '@/helpers';
export default {
    name: 'NewCardSmaller',
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
        slugify(str) {
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

a:hover {
    color: #1657b9 !important;
}

.title-style{
    font-weight: 600 !important;
    font-family: Playfair Display;
}
</style>