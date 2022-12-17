<template>
    <div class="container">
        <h4 class="text-center">Đăng nhập vào tài khoản của bạn</h4>
        <form class="col-5 mt-4 mx-auto">
            <div class="mb-3">
                <label for="email" class="fw-bold">Email</label>
                <input type="email" name="email" class="form-control" id="email" placeholder="Nhập email">
            </div>
            <div class="mb-3">
                <label for="password" class="fw-bold">Mật khẩu</label>
                <input type="password" name="password" class="form-control" id="password" placeholder="Nhập mật khẩu">
            </div>

            <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="check">
                <label class="form-check-label" for="remember">Nhớ tên tài khoản</label>
                <a href="" class="text-dark float-end">Quên mật khẩu ?</a>
            </div>
            <div class="d-grid gap-2">
                <button type="submit" class="btn btn-dark">Đăng nhập</button>
            </div>
        </form>
    </div>
</template>
    
<script>

export default {
    name: 'LoginForm',
}
</script>
    