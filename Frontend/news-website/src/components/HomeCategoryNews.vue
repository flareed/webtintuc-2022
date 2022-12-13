<template>
    <h5>{{ section }}</h5>
    <div class="row ms-3 mb-4 ">
        <a :href="`/${sectionSlug}/${slugify(content[0].title)}`" class="text-dark">
            <div class="row py-3 border-bottom">
            <div class="col-5">
                <img :src="content[0].img" class="img-fluid" :alt="content[0].title" width="200" height="133.33">
            </div>
            <div class="col">
                <div class="row">
                    <h5>{{ content[0].title }}</h5>
                </div>
                <div class="row">
                    <p>{{ content[0].description }}</p>
                </div>
            </div>
        </div>
        </a>
        
        <div class="row h-100 py-3 border-bottom border-dark">
            <a :href="`/${sectionSlug}/${slugify(content[1].title)}`" class="col text-dark">
                <h6>{{ content[1].title }}</h6>
            </a>
            <a :href="`/${sectionSlug}/${slugify(content[2].title)}`" class="col border-start border-end text-dark">
                <h6>{{ content[2].title }}</h6>
            </a>
            <a :href="`/${sectionSlug}/${slugify(content[3].title)}`" class="col text-dark">
                <h6>{{ content[3].title }}</h6>
            </a>
        </div>

    </div>
</template>
    
<script>
import sourceData from '@/components/store/data_routes.json'
import myLib from '@/helpers';

export default {
    name: 'HomeCategoryNews',
    components: {
    },
    props: {
        section: String
    },
    data() {
        return {
            content: [
                {
                    img: "https://images.unsplash.com/photo-1664575196412-ed801e8333a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
                    title: "Rủi ro của Man Utd ở vòng play-off Europa League",
                    description: "Do chỉ đứng nhì bảng, Man Utd vào vòng play-off nhưng có nguy cơ gặp Barca hay Juventus từ Champions League xuống.",
                },
                {
                    img: "https://images.unsplash.com/photo-1664575196412-ed801e8333a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
                    title: "Ngoại hạng Anh được khuyên tạm nghỉ sớm vì World Cup",
                    description: "Do chỉ đứng nhì bảng, Man Utd vào vòng play-off nhưng có nguy cơ gặp Barca hay Juventus từ Champions League xuống.",
                },
                {
                    img: "https://images.unsplash.com/photo-1664575196412-ed801e8333a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
                    title: "Bốn đội cùng bảng bằng điểm ở Europa League",
                    description: "Do chỉ đứng nhì bảng, Man Utd vào vòng play-off nhưng có nguy cơ gặp Barca hay Juventus từ Champions League xuống.",
                },
                {
                    img: "https://images.unsplash.com/photo-1664575196412-ed801e8333a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
                    title: "Ten Hag xếp Harry Maguire đá tiền đạo",
                    description: "Do chỉ đứng nhì bảng, Man Utd vào vòng play-off nhưng có nguy cơ gặp Barca hay Juventus từ Champions League xuống.",
                }
            ]
        }
    },
    computed: {
        sectionSlug() {
            return sourceData.categories.find(
                (destination) => destination.name === this.section
            ).slug;
        }
    },
    methods: {
        slugify(str){
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

a:hover{
    color: #0d6efd !important
}
</style>