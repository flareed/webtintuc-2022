<template>
    <div class="container">
        <h4 class="text-center">Đăng nhập vào tài khoản của bạn</h4>
        <div class="col-5 mt-4 mx-auto">
            <div class="mb-3">
                <label for="email" class="fw-bold">Email</label>
                <input type="email" class="form-control" id="email" v-model="email" placeholder="Nhập email">
            </div>
            <div class="mb-3">
                <label for="password" class="fw-bold">Mật khẩu</label>
                <input type="password" class="form-control" id="password" v-model="password"
                    placeholder="Nhập mật khẩu">
            </div>

            <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="check">
                <label class="form-check-label" for="remember">Nhớ tên tài khoản</label>
                <a href="" class="text-dark float-end">Quên mật khẩu ?</a>
            </div>
            <div class="d-grid gap-2">
                <button type="button" class="btn btn-dark" @click="onLogin()">Đăng nhập</button>
                <a href="/signup" class="btn btn-light border border-dark">
                    <small>Không có tài khoản, đăng ký tại đây</small>
                </a>
            </div>


            <h6 v-if="!success" class="mt-4 alert alert-warning" role="alert" style="text-align: center;">
                Email hoặc mật khẩu không chính xác
            </h6>

        </div>
    </div>
</template>
    
<script>
import users from '@/store/users.json'
import { store } from '../store/index'

export default {
    name: 'LoginForm',
    data() {
        return {
            email: '',
            password: '',
            success: true,
            store
        }
    },
    methods: {
        onLogin() {
            let current_user = users.data.find(
                (user) => user.email === this.email
            );

            if (typeof current_user == 'undefined') {
                this.success = false
            } else {
                if (current_user.password == this.password) {
                    store.login(current_user)
                    localStorage.setItem('currentId', current_user.id)
                    localStorage.setItem('isAuthenticate', true)
                    this.$router.push({ name: 'Home' })
                } else {
                    this.success = false
                }
            }


        }
    }
}
</script>
    