<template>
    <h5>Ảnh</h5>

    <div id="carouselExampleCaptions" class="carousel slide px-4" data-bs-ride="false">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"
                aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"
                aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"
                aria-label="Slide 3"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3"
                aria-label="Slide 4"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="4"
                aria-label="Slide 5"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="https://i1-thethao.vnecdn.net/2022/12/21/1-hlv-park-hang-seo-viet-nam-lao-aff-cup-2022-jpeg-1671640812.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=3Kg2DsfaR_jnLtvcJgA7xQ"
                    class="d-block w-100 cropped" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <h5>HLV Park không cười dù thắng đậm Lào</h5>
                    <!-- <p>Some representative placeholder content for the first slide.</p> -->
                </div>
            </div>
            <div class="carousel-item">
                <img src="https://i1-vnexpress.vnecdn.net/2022/12/21/30a330c43ebfe6e1bfae-1671606596.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=IFmXt7fTLQg6mIgQz-97eQ"
                    class="d-block w-100 cropped" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Ngày chạy thử của Metro Bến Thành - Suối Tiênl</h5>
                    <!-- <p>Some representative placeholder content for the second slide.</p> -->
                </div>
            </div>
            <div class="carousel-item">
                <img src="https://i1-thethao.vnecdn.net/2022/12/21/argentina-5-1671575905.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=5sRnmXj1eEG1KJuwZr5kzA"
                    class="d-block w-100 cropped" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Gần năm triệu người mừng thành công tuyển Argentina</h5>
                    <!-- <p>Some representative placeholder content for the third slide.</p> -->
                </div>
            </div>
            <div class="carousel-item">
                <img src="https://i1-giaitri.vnecdn.net/2022/12/21/tranh-cua-fed-2-1671577012.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=IzwIYnX5K0_Uv3Fb-wl4FA"
                    class="d-block w-100 cropped" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Cuộc sống mưu sinh của người Việt trong mắt họa sĩ Pháp</h5>
                    <!-- <p>Some representative placeholder content for the third slide.</p> -->
                </div>
            </div>
            <div class="carousel-item">
                <img src="https://i1-thethao.vnecdn.net/2022/12/19/18world-cup-france-argentina-das-1-1b7c-mobileMasterAt3x.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=FeN9oSGXe8JtsxrTsIKKww"
                    class="d-block w-100 cropped" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Ngày buồn của Mbappe</h5>
                    <!-- <p>Some representative placeholder content for the third slide.</p> -->
                </div>
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions"
            data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions"
            data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>

</template>
    
<script>

export default {
    name: 'HomePicsShow',
    components: {
    },
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cropped {
    width: 1200px !important; 
    height: 800px !important; 
    overflow: hidden !important;
    object-fit: cover;
}
</style>