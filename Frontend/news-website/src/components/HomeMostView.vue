<template>
        <h5>Nhiều lượt xem</h5>
        <div class="row">
            <a :href="`/${sectionSlug(this.articles[0].category)}/${this.articles[0].title}`" class="col pe-4 border-end border-dark text-dark">
                <div class="row">
                    <div class="col">
                        <img :src=this.articles[0].imageTitle class="img-fluid" alt="Girl in a jacket" width="400" height="267">
                    </div>
                    <div class="col">
                        <div class="row">
                            <h4>
                                {{ this.articles[0].title }}
                            </h4>
                        </div>
                        <div class="row">
                            <p>
                                {{ this.articles[0].desciption }}
                            </p>
                        </div>
                        <div class="row">
                            <b>{{ this.articles[0].category }}</b>
                        </div>
                    </div>
                </div>
            </a>
            <div class="col-4">
                <a :href="`/${sectionSlug(this.articles[1].category)}/${this.articles[1].title}`" class="row ps-2 ms-2 border-bottom border-dark text-dark">
                    <div class="row">
                        <h5>{{ this.articles[1].title }}</h5>
                    </div>
                    <div class="row">
                        <p>
                            {{ this.articles[1].desciption }} 
                        </p>
                    </div>
                </a>
                <a :href="`/${sectionSlug(this.articles[2].category)}/${this.articles[2].title}`" class="row ps-2 ms-2 mt-3 text-dark">
                    <div class="row">
                        <h5>{{ this.articles[2].title }}</h5>
                    </div>
                    <div class="row">
                        <p>
                            {{ this.articles[2].desciption }} 
                        </p>
                    </div>
                </a>
            </div>
        </div>
</template>
    
<script>
import sourceData from '@/components/store/data_routes.json'

export default {
    name: 'HomeMostView',
    data() {
        return {
            articles: [
                {
                    "imageTitle": "https://images.unsplash.com/photo-1668613964763-90d0bd6559f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
                    "title": "Lịch trình gợi ý cho người lần đầu đi Hà Giang",
                    "desciption": "Vũ Phương Anh, 23 tuổi, chia sẻ kinh nghiệm sau khi kết thúc chuyến đi Hà Giang 4 ngày 3 đêm, cuối tháng 10.",
                    "category": "Du lịch",
                },
                {
                    "imageTitle": "https://images.unsplash.com/photo-1668613964763-90d0bd6559f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
                    "title": "Lý do Musk muốn nhanh kiếm tiền từ Twitter",
                    "desciption": "Tỷ phú Elon Musk áp dụng một loạt thay đổi sau khi trở thành ông chủ Twitter nhằm thúc đẩy hoạt động kiếm tiền của mạng xã hội.",
                    "category": "Số hoá",
                },
                {
                    "imageTitle": "https://images.unsplash.com/photo-1668613964763-90d0bd6559f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
                    "title": "Đánh giá iPhone 14 Pro Max",
                    "desciption": "iPhone 14 Pro Max có thiết kế cao cấp, thời lượng pin, màn hình và camera tốt, nhưng Dynamic Island và màn hình luôn bật còn nhiều bất tiện.",
                    "category": "Số hoá",
                }
            ],
        }
    },
    methods: {
        sectionSlug(name) {
            console.log(name)
            return sourceData.categories.find(
                (destination) => destination.name === name
            ).slug;
        }
    }
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
    text-decoration: none;
}
</style>