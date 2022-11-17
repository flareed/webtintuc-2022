<template>
    <div class="container-fluid border-top border-bottom border-dark my-2">
        <div class="row h-100 py-1 px-4">
            <div class="col-1">
                <h5 class="my-auto">
                    <font-awesome-icon icon="fa-solid fa-list" />
                </h5>
            </div>
            <div class="col">
                <div class="row h-100">
                    <div v-for="(item, index) in categories" :key="index" class="my-auto mr-auto">
                        {{ item }}
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
    
<script>
export default {
    name: 'HomeNavBar',
    data() {
        return {
            categories: [
                'Thời sự',
                'Thế giới',
                'Góc nhìn',
                'Kinh doanh',
                'Khoa học',
                'Giải trí',
                'Thể thao',
                'Pháp luật',
                'Sức khoẻ',
                'Du lịch',
                'Số hoá',
                'Xe',
                'Ý kiến',
            ]
        }
    }
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>