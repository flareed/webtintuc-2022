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
                <button type="button" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    Tạo tài khoản
                </button>
                <a href="/login" class="btn btn-light border border-dark">
                    <small>Đã có tài khoản, đăng nhập tại đây</small>
                </a>
            </div>


            <!-- Modal -->
            <div ref="myModal" class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Thông báo</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            Đăng kí thành công
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Đóng</button>
                            <!-- <button type="button" class="btn btn-primary">Save changes</button> -->
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
    // mounted() {
    //     const myModalEl = this.$refs.myModal
    //     myModalEl.addEventListener('show.bs.modal', event => {
    //         // do something...
    //         console.log(event)
    //     })
    // }
}

</script>

    