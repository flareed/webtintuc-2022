<template>
    <div class="container">
        <h4 class="text-center">Đăng ký</h4>
        <form class="col-5 mt-2 mx-auto">
            <div class="form-group">
                <label for="username" class="font-weight-bold">Tên người dùng</label>
                <input type="username" name="username" class="form-control" id="username" placeholder="Nhập tên người dùng">
            </div>
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
                <label class="form-check-label" for="remember">
                    You agree to receive updates and offers from The 23 Post. You may opt out anytime.
                </label>
            </div>

            <small>
                By creating an account, you agree to the <u>Terms of Service</u> and acknowledge our <u>Privacy Policy</u>.
            </small>


            <button type="submit" class="btn btn-dark btn-block mt-2">Tạo tài khoản</button>
            <button type="button" class="btn btn-light btn-block border border-dark">
                <small>Đã có tài khoản, đăng nhập tại đây</small>
            </button>
        </form>

        

    </div>
</template>
    
<script>

export default {
    name: 'SignUpForm',
}
</script>
    