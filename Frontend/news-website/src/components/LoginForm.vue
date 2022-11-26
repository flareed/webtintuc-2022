<template>
    <div class="container">
        <h4 class="text-center">Đăng nhập vào tài khoản của bạn</h4>
        <form class="col-5 mt-4 mx-auto">
            <div class="form-group">
                <label for="email" class="font-weight-bold">Email</label>
                <input type="email" name="email" class="form-control" id="email" placeholder="Nhập email">
            </div>
            <div class="form-group">
                <label for="password" class="font-weight-bold">Mật khẩu</label>
                <input type="password" name="password" class="form-control" id="password" placeholder="Nhập mật khẩu">
            </div>

            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="check">
                <label class="form-check-label" for="remember">Nhớ tên tài khoản</label>
                <a href="" class="text-dark float-right">Quên mật khẩu ?</a>
            </div>


            <button type="submit" class="btn btn-dark btn-block">Đăng nhập</button>
            <a href="/signup" class="btn btn-light btn-block border border-dark">
                <small>Không có tài khoản, đăng ký tại đây</small>
            </a>
            <!-- <button type="button" class="btn btn-light btn-block border border-dark">
                <small>Không có tài khoản, đăng ký tại đây</small>
            </button> -->
        </form>

        

    </div>
</template>
    
<script>

export default {
    name: 'LoginForm',
}
</script>
    