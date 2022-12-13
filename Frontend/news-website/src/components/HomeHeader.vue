<template>
    <div class="container-fluid pb-2">
        <div class="row px-4">
            <div class="col">
                <div class="row">
                    <div class="fw-bold">{{ getDate }}</div>
                </div>
                <div class="row">
                    <div>Tin tức hôm nay</div>
                </div>
            </div>
            <div class="col-5 text-center">
                <img src="../assets/logo_header.png" class="img-fluid" alt="logo">
            </div>
            <div class="col">
                <div class="row">
                    <div class="col-8">
                        <div class="input-group">
                            <input type="text" class="form-control search-style" placeholder="Tìm kiếm">
                            <button class="btn btn-outline-secondary" type="button">
                                <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                            </button>
                        </div>
                    </div>
                    <div class="col-1">
                        <h4 class="my-1">
                            <font-awesome-icon icon="fa-solid fa-circle-user" />
                        </h4>
                    </div>
                    <div class="col my-auto">
                        <a class="text-dark" href="/login">Đăng nhập</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>

export default {
    name: 'HomeHeader',
    computed: {
        getDate() {
            const date = new Date();

            let day = date.getDate();
            let month = date.getMonth() + 1;
            let year = date.getFullYear();

            const weekday = ["Chủ nhật", "Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy"];
            let dayOfWeek = weekday[date.getDay()];

            let currentDate = `${dayOfWeek}, ${day}/${month}/${year}`
            return currentDate
        }
    }
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.search-style {
    font-size: small !important;
}
</style>