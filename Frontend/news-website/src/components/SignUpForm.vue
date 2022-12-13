<template>
    <div class="container">
        <h4 class="text-center">Đăng ký</h4>
        <div class="col-5 mt-2 mx-auto">
            <div class="mb-3">
                <label for="username" class="font-weight-bold">Tên người dùng</label>
                <input type="username" name="username" class="form-control" id="username"
                    placeholder="Nhập tên người dùng">
            </div>
            <div class="mb-3">
                <label for="email" class="font-weight-bold">Email</label>
                <input type="email" name="email" class="form-control" id="email" placeholder="Nhập email">
            </div>
            <div class="mb-3">
                <label for="password" class="font-weight-bold">Mật khẩu</label>
                <input type="password" name="password" class="form-control" id="password" placeholder="Nhập mật khẩu">
            </div>

            <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="check">
                <label class="form-check-label" for="remember">
                    You agree to receive updates and offers from The 23 Post. You may opt out anytime.
                </label>
            </div>

            <small>
                By creating an account, you agree to the <u>Terms of Service</u> and acknowledge our <u>Privacy
                    Policy</u>.
            </small>

            <div class="d-grid gap-2 mt-3">
                <button class="btn btn-dark" data-toggle="modal" data-target="#exampleModalCenter">
                    Tạo tài khoản
                </button>
                <a href="/login" class="btn btn-light border border-dark">
                    <small>Đã có tài khoản, đăng nhập tại đây</small>
                </a>
            </div>

            
            <!-- Modal -->
            <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog"
                aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLongTitle">Thông báo</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            Đã đăng ký thành công
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Đóng</button>
                            <button type="button" class="btn btn-primary">Đồng ý</button>
                        </div>
                    </div>
                </div>
            </div>

            
        </div>
    </div>
</template>
    
<script>

export default {
    name: 'SignUpForm',
}

</script>

    