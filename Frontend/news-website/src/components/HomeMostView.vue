<template>
    <h5>Nhiều lượt xem</h5>
    <div v-if="!isFetching">
        <div class="row">
            <a :href="`/${sectionSlug(this.news[0].category)}/${this.news[0].id}`"
                class="col pe-4 border-end border-dark text-dark">
                <div class="row">
                    <div class="col">
                        <img :src="`http://127.0.0.1:8000${this.news[0].img}`" class="img-fluid" :alt="this.news[0].title" width="400"
                            height="267">
                    </div>
                    <div class="col">
                        <div class="row">
                            <h4 class="title-style">
                                {{ this.news[0].title }}
                            </h4>
                        </div>
                        <div class="row">
                            <p>
                                {{ this.news[0].description }}
                            </p>
                        </div>
                        <div class="row">
                            <b>{{ this.news[0].category }}</b>
                        </div>
                    </div>
                </div>
            </a>
            <div class="col-4">
                <a :href="`/${sectionSlug(this.news[1].category)}/${this.news[1].id}`"
                    class="row ps-2 ms-2 border-bottom border-dark text-dark">
                    <div class="row">
                        <h5 class="title-style">{{ this.news[1].title }}</h5>
                    </div>
                    <div class="row">
                        <p>
                            {{ this.news[1].description }}
                        </p>
                    </div>
                </a>
                <a :href="`/${sectionSlug(this.news[2].category)}/${this.news[2].id}`"
                    class="row ps-2 ms-2 mt-3 text-dark">
                    <div class="row">
                        <h5 class="title-style">{{ this.news[2].title }}</h5>
                    </div>
                    <div class="row">
                        <p>
                            {{ this.news[2].description }}
                        </p>
                    </div>
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
    name: 'HomeMostView',
    data() {
        return {
            news: [],
            isFetching: true
        }
    },
    methods: {
        sectionSlug(name) {
            return sourceData.categories.find(
                (destination) => destination.name === name
            ).slug;
        },
        slugify(str) {
            return myLib.toSlug(str)
        }
    },
    created() {
        HTTP.get(`api/categories/11/articles/`)
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
</style>