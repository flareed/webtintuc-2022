<template>
    <div class="container-fluid pb-2 border-bottom border-dark">
        <div class="row px-4">
            <div class="col">
                <div class="row">
                    <div class="fw-bold">{{ getDate }}</div>
                </div>
                <div class="row">
                    <div>Tin tức hôm nay</div>
                </div>
            </div>
            <a href="/" class="col-5 text-center">
                <img src="../assets/logo_header.png" class="img-fluid" alt="logo">
            </a>
            <div class="col">
                <div class="row">
                    <div class="col-8">
                        <form action="/search" method="get">
                            <div class="input-group">
                                <input type="text" name="q" class="form-control search-style" placeholder="Tìm kiếm">
                                <button class="btn btn-outline-secondary" type="submit">
                                    <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                                </button>
                            </div>
                        </form>
                    </div>
                    <div class="col-1">
                        <h4 class="my-1">
                            <font-awesome-icon icon="fa-solid fa-circle-user" />
                        </h4>
                    </div>
                    <div class="col my-auto">
                        <div v-if="this.isAuthenticate" data-bs-toggle="offcanvas"
                            data-bs-target="#offcanvasRight">
                            {{ currentUser.username }}
                        </div>
                        <div v-else>
                            <a class="text-dark" href="/login">Đăng nhập</a>
                        </div>
                    </div>

                    <div v-if="this.isAuthenticate" class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight"
                        aria-labelledby="offcanvasRightLabel">
                        <div class="offcanvas-header">
                            <h5 class="offcanvas-title" id="offcanvasRightLabel">Thông tin cá nhân</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="offcanvas"
                                aria-label="Close"></button>
                        </div>
                        <div class="offcanvas-body">
                            <div class="border-bottom">
                                Email
                            </div>
                            <h6 class="fw-bold mt-2 mb-4">{{ currentUser.email }}</h6>
                            <div class="border-bottom">
                                Tên người dùng
                            </div>
                            <h6 class="fw-bold mt-2">{{ currentUser.username }}</h6>
                            <a href="/" type="button" class="btn btn-dark mt-5" @click="onLogout()">Logout</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import { store } from '../store/index'
import users from '@/store/users.json'

export default {
    name: 'HomeHeader',
    data() {
        return {
            store,
            isAuthenticate: localStorage.getItem('isAuthenticate'),
        }
    },
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
        },
        currentUser() {
            let id = localStorage.getItem("currentId")
            return users.data.find(
                (user) => user.id === parseInt(id)
            );
        }
    },
    methods: {
        onLogout(){
            // store.logout()
            localStorage.clear();
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