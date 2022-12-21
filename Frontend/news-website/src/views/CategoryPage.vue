<template>
    <header>
        <HomeHeader />
    </header>

    <nav>
        <HomeNavBar :slug="category.slug" />
    </nav>

    <main>
        <div class="container py-2">
            <div class="row input-style mt-4 border-bottom">
                <div class="col">
                    <h1 class="fw-bold">{{ category.name }}</h1>
                </div>
                <div class="col-4">
                    <button type="button" class="btn btn-primary float-end">Nhận thông báo</button>
                </div>
            </div>

            <div class="row mt-4 input-style">
                <div v-if="!isFetching" class="col">
                    <div v-for="item in this.news" :key="item.id">
                        <NewCard :img="`http://127.0.0.1:8000${item.img}`" :title="item.title"
                            :description="item.description" :category="item.category" :id="item.id"
                            :date="item.date_posted" :isInSection="true"/>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <footer>
        <HomeFooter />
    </footer>
</template>
  
<script>
import HomeHeader from '../components/HomeHeader.vue';
import HomeNavBar from '../components/HomeNavBar.vue';
import HomeFooter from '@/components/HomeFooter.vue';
import NewCard from '@/components/NewCard.vue';
import sourceData from '@/components/store/data_routes.json'
import { HTTP } from '../api'

export default {
    name: 'CategoryPage',
    components: {
        HomeHeader,
        HomeNavBar,
        HomeFooter,
        NewCard,
    },
    data() {
        return {
            news: [],
            isFetching: true,
        }
    },
    props: {
        section: { type: String, required: true },
    },
    computed: {
        category() {
            // console.log(this.id)
            return sourceData.categories.find(
                (destination) => destination.slug === this.section
            );
        }
    },
    created() {
        HTTP.get(`api/categories/` + this.category.id + `/articles/`)
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
.input-style {
    margin-left: 10%;
    margin-right: 10%;
}
</style>
  