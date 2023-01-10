<template>
    <header>
        <HomeHeader />
    </header>

    <main>
        <div class="input-style">
            <form action="/search" method="get">
                <div class="row">
                    <div class="col-4">
                        <div class="input-group">
                            <label class="input-group-text" for="inputGroupSelect">Chuyên đề</label>
                            <select class="form-select" name="category" id="inputGroupSelect">
                                <option value="0" :selected="store.selectedCategory == 0">Tất cả</option>
                                <option v-for="item in categories_data" :key="item.name" :value="item.id"
                                    :selected="store.selectedCategory == item.id">{{
                                        item.name
                                    }}</option>
                            </select>
                        </div>
                    </div>
                    <div class="col">
                        <div class="input-group">
                            <input type="text" name="q" class="form-control search-style" placeholder="Tìm kiếm"
                                :value="this.query">
                            <button class="btn btn-outline-secondary" type="submit">
                                <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                            </button>
                        </div>
                    </div>
                </div>
            </form>
        </div>

        <div class="input-style">
            <div class="row mt-4">
                <div v-if="!isFetching" class="col">
                    <div v-if="!isEmpty">
                        <div v-if="this.change">
                            <div v-for="item in this.news" :key="item.id">
                                <NewCard :img="`http://127.0.0.1:8000${item.img}`" :title="item.title" :description="item.description"
                                    :category="item.category" :id="item.id" :date="item.date_posted" />
                            </div>
                        </div>
                        <div v-else>
                            <div v-for="item in this.news" :key="item.id">
                                <NewCard :img="item.img" :title="item.title" :description="item.description"
                                    :category="item.category" :id="item.id" :date="item.date_posted" />
                            </div>
                        </div>

                    </div>
                    <div v-else>
                        <h5>Không tìm thấy kết quả phù hợp</h5>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
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
import NewCard from '@/components/NewCard.vue';
import sourceData from '@/store/data_routes.json'
import { HTTP } from '../api'
import { store } from '../store/index'

export default {
    name: 'SearchPage',
    components: {
        HomeHeader,
        HomeFooter,
        NewCard,
    },
    data() {
        return {
            news: [],
            isFetching: true,
            categories_data: sourceData.categories,
            isEmpty: false,
            store,
            change: false
        }
    },
    props: {
        query: { type: String, required: true },
        category: String,
    },
    created() {
        store.selectedCategory = parseInt(this.category)
        console.log(typeof this.categories_data[0].id)
        console.log(store.selectedCategory)
        if (typeof this.category !== 'undefined') {
            if (this.category == '0') {
                this.change = false
                HTTP.get(`api/articles/?q=${this.query}`)
                    .then(response => {
                        this.news = response.data.results
                        this.isFetching = false
                        if (this.news.length == 0) {
                            this.isEmpty = true
                        }
                    })
                    .catch(e => {
                        console.log(e)
                    })
            } else {
                this.change = true
                HTTP.get(`api/categories/${this.category}/articles/?q=${this.query}`)
                    .then(response => {
                        this.news = response.data
                        this.isFetching = false
                        if (this.news.length == 0) {
                            this.isEmpty = true
                        }
                    })
                    .catch(e => {
                        console.log(e)
                    })
            }
        } else {
            this.change = false
            HTTP.get(`api/articles/?q=${this.query}`)
                .then(response => {
                    this.news = response.data.results
                    this.isFetching = false
                    if (this.news.length == 0) {
                        this.isEmpty = true
                    }
                })
                .catch(e => {
                    console.log(e)
                })
        }

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
