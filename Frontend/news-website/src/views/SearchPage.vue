<template>
    <header>
        <HomeHeader />
    </header>

    <main>
        <div class="input-style">
            <form action="/search" method="get">
                <div class="input-group input-group-lg">
                    <input type="text" name="q" class="form-control search-style" placeholder="Tìm kiếm"
                        :value="this.query">
                    <button class="btn btn-outline-secondary" type="submit">
                        <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                    </button>
                </div>
            </form>
        </div>
        <div class="input-style">
            <div class="row mt-4">
                <div v-if="!isFetching" class="col">
                    <div v-for="item in this.news" :key="item.id">
                        <SearchCard :img="item.img" :title="item.title" :description="item.description"
                            :category="item.category" :id="item.id" :date="item.date_posted" />
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
import HomeFooter from '@/components/HomeFooter.vue';
import SearchCard from '@/components/SearchCard.vue';
import { HTTP } from '../api'

export default {
    name: 'SearchPage',
    components: {
        HomeHeader,
        HomeFooter,
        SearchCard,
    },
    data() {
        return {
            news: [],
            isFetching: true,
        }
    },
    props: {
        query: { type: String, required: true },
    },
    created() {
        console.log(this.query)
        HTTP.get(`api/articles/?q=${this.query}`)
            .then(response => {
                this.news = response.data.results
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
    margin-top: 20px;
    margin-left: 20%;
    margin-right: 20%;
}
</style>
  