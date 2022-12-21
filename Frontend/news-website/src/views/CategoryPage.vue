<template>
    <header>
        <HomeHeader />
    </header>

    <nav>
        <HomeNavBar :slug="category.slug"/>
    </nav>

    <main>
        <div class="container py-2">
            <div class="row">
                <div class="col">
                    <h3>{{ category.name }}</h3>
                </div>
                <div class="col">
                    <button type="button" class="btn btn-primary">Đăng ký nhận thông báo</button>
                </div>
            </div>
            
            <div class="row mt-4">
                <div v-if="!isFetching" class="col-8">
                    <div v-for="item in this.news" :key="item.id">
                        <NewCard :img="item.img" :title="item.title" :description="item.description" :category="item.category" :id="item.id" />
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
            // img: "https://images.unsplash.com/photo-1668405409882-0b3a8b6fc912?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
            // title: "Musk dự kiến sa thải gần 4.000 nhân viên Twitter",
            // description: "Elon Musk được cho là đang chuẩn bị cho việc sa thải một nửa số nhân viên Twitter ngay trong tuần này."
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

</style>
  