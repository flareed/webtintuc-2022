<template>
    <header>
        <HomeHeader />
    </header>

    <nav>
        <HomeNavBar :slug="category.slug" />
    </nav>

    <main>
        <div class="container">
            <h6 v-if="!this.isAuthenticate" class="mt-4 alert alert-secondary" role="alert" style="text-align: center;">
                Hãy đăng nhập để có thể đăng ký nhận thông báo từ mục {{ category.name }}
            </h6>
            <div class="row input-style mt-4 border-bottom">
                <div class="col">
                    <h1 class="fw-bold display-4" style="font-family: Dosis">{{ category.name }}</h1>
                </div>
                <div class="col-4 position-relative">
                    <div v-if="this.isAuthenticate">
                        <div v-if="isSub">
                            <button type="button" class="btn btn-success position-absolute top-50 end-0 translate-middle-y" @click="onSelect()" disabled>Đã nhận thông báo</button>
                        </div>
                        <div v-else>
                            <button type="button" class="btn btn-primary position-absolute top-50 end-0 translate-middle-y" @click="onSelect()">Nhận thông báo</button>
                        </div>
                    </div>
                    <div v-else>
                        <button type="button" class="btn btn-primary position-absolute top-50 end-0 translate-middle-y" @click="onSelect()" disabled>Nhận thông báo</button>
                    </div>
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
import sourceData from '@/store/data_routes.json'
import { HTTP } from '../api'
import { store } from '@/store/index'
import users from '@/store/users.json'

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
            store,
            isAuthenticate: localStorage.getItem('isAuthenticate'),
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
        },
        currentUser() {
            let id = localStorage.getItem("currentId")
            return users.data.find(
                (user) => user.id === parseInt(id)
            );
        },
        isSub(){
            return this.currentUser.subcribe.includes(this.category.id)
        }
    },
    created() {
        console.log(this.currentUser)
        HTTP.get(`api/categories/` + this.category.id + `/articles/`)
            .then(response => {
                this.news = response.data
                this.isFetching = false
            })
            .catch(e => {
                console.log(e)
            })
    },
    methods: {
        onSelect(){
            if (this.isAuthenticate){
                this.currentUser.subcribe.push(this.category.id)
            }
        }
    }
}
</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.input-style {
    margin-left: 10%;
    margin-right: 10%;
}
</style>
  