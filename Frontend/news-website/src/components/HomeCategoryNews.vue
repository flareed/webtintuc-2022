<template>
    <h5>{{ section }}</h5>
    <div v-if="!isFetching" >
        <div class="row ms-3 mb-4 ">
            <a :href="`/${sectionSlug}/${this.news[0].id}`" class="text-dark">
                <div class="row py-3 border-bottom">
                    <div class="col-5">
                        <img :src="`http://127.0.0.1:8000${this.news[0].img}`" class="img-fluid"
                            :alt="this.news[0].title" width="200" height="133.33">
                    </div>
                    <div class="col">
                        <div class="row">
                            <h6 class="title-style">{{ this.news[0].title }}</h6>
                        </div>
                        <div class="row">
                            <p>{{ this.news[0].description }}</p>
                        </div>
                    </div>
                </div>
            </a>

            <div class="row h-100 py-3 border-bottom border-dark">
                <a :href="`/${sectionSlug}/${this.news[1].id}`" class="col text-dark subtitle-style">
                    <h6>{{ this.news[1].title }}</h6>
                </a>
                <a :href="`/${sectionSlug}/${this.news[2].id}`" class="col border-start border-end text-dark subtitle-style">
                    <h6>{{ this.news[2].title }}</h6>
                </a>
                <a :href="`/${sectionSlug}/${this.news[3].id}`" class="col text-dark subtitle-style">
                    <h6>{{ this.news[3].title }}</h6>
                </a>
            </div>

        </div>
    </div>
</template>
    
<script>
import sourceData from '@/store/data_routes.json'
import myLib from '@/helpers';
import { HTTP } from '../api'

export default {
    name: 'HomeCategoryNews',
    components: {
    },
    props: {
        section: String,
        id: String
    },
    data() {
        return {
            news: [],
            isFetching: true
        }
    },
    computed: {
        sectionSlug() {
            return sourceData.categories.find(
                (destination) => destination.name === this.section
            ).slug;
        },
    },
    methods: {
        slugify(str) {
            return myLib.toSlug(str)
        }
    },
    created() {
        HTTP.get(`api/categories/` + this.id + `/articles/`)
            .then(response => {
                this.news = response.data
                this.isFetching = false
            })
            .catch(e => {
                console.log(e)
            })
    },
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

.subtitle-style{
    font-family: Playfair Display;
}
</style>