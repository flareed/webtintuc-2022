<template>
    <header>
        <HomeHeader />
    </header>

    <nav>
        <HomeNavBar :slug=this.section />
    </nav>

    <main>
        <div class="container py-2 px-4 mt-4" style="max-width: 65%">
            <div class="row">
                <div class="col">
                    <h6>{{ article.tag }}</h6>
                </div>
                <div class="col">
                    <h6 class="float-right">{{ article.date }}</h6>
                </div>
            </div>
            <div class="row mt-4">
                <h2>{{ article.title }}</h2>
            </div>
            <div class="row mt-4">
                <span>
                    <p>{{ article.description }}</p>
                </span>

            </div>
            <div class="row">
                <span class="content-style" v-html="article.content"></span>
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
// import NewCard from '@/components/NewCard.vue';
import articleData from '@/components/store/data_article.json';

export default {
    name: 'DetailPage',
    components: {
        HomeHeader,
        HomeNavBar,
        HomeFooter,
        // NewCard,
    },
    data() {
        return {
            img: "https://images.unsplash.com/photo-1668405409882-0b3a8b6fc912?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
            title: "Musk dự kiến sa thải gần 4.000 nhân viên Twitter",
            description: "Elon Musk được cho là đang chuẩn bị cho việc sa thải một nửa số nhân viên Twitter ngay trong tuần này."
        }
    },
    props: {
        section: { type: String, required: true },
        name: { type: String, required: true },
    },
    computed: {
        // category() {
        //     console.log(this.section)
        //     console.log(this.id)
        // }
        article() {
            console.log(this.section)
            return articleData
        }
    }
}
</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
span :deep(img) {
    width: 80%;
    /* height: 70%; */
    display: block;
    margin-left: auto;
    margin-right: auto;
}

span :deep p {
    font-size: 18px;
}
</style>
  