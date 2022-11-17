<template>
    <div class="container-fluid">
        <div class="row px-4">
            <div class="col">
                <div class="row">
                    <div class="font-weight-bold">Thứ 5, 17/11/2022</div>
                </div>
                <div class="row">
                    <div>Tin tức hôm nay</div>
                </div>
            </div>
            <div class="col-6 d-flex justify-content-center">
                <img src="../assets/logo1.png" alt="logo">
            </div>
            <div class="col">
                <div class="row py-auto">
                    <div class="col-8">
                        <div class="input-group">
                            <input type="text" class="form-control search-style" placeholder="Tìm kiếm">
                            <div class="input-group-append">
                                <button class="btn btn-outline-dark btn-sm" type="button">
                                    <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                                </button>
                            </div>
                        </div>
                    </div>
                    <div class="mr-2 my-1">
                        <h4>
                            <font-awesome-icon icon="fa-solid fa-circle-user" />
                        </h4>
                    </div>
                        <div class="my-2 float-right">
                            <a class="text-dark" href="">Đăng nhập</a>
                        </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
export default {
    name: 'HomeHeader',
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.search-style {
    font-size: small !important;
}
</style>