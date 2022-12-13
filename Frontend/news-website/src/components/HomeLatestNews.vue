<template>
    <div class="row">
        <h5>Tin mới nhất</h5>
    </div>
    <div class="me-3">
        <NewCard :img="this.img" :title="this.title" :description="this.description" />
        <NewCard :img="this.img" :title="this.title" :description="this.description" />
        <NewCard :img="this.img" :title="this.title" :description="this.description" />
        <NewCard :img="this.img" :title="this.title" :description="this.description" />
        <NewCard :img="this.img" :title="this.title" :description="this.description" />
        <NewCard :img="this.img" :title="this.title" :description="this.description" />
        <NewCard :img="this.img" :title="this.title" :description="this.description" />
    </div>


</template>
    
<script>
import NewCard from './NewCard.vue';
export default {
    name: 'HomeLatestNews',
    components: {
        NewCard,
    },
    data() {
        return {
            img: "https://images.unsplash.com/photo-1668405409882-0b3a8b6fc912?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
            title: "Musk dự kiến sa thải gần 4.000 nhân viên Twitter",
            description: "Elon Musk được cho là đang chuẩn bị cho việc sa thải một nửa số nhân viên Twitter ngay trong tuần này."
        }
    }
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>