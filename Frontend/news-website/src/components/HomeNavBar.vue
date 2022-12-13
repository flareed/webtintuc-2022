<template>
    <div class="container-fluid border-top border-bottom border-dark mb-2" ref="navbar"
        style="background-color: white !important;">
        <div class="row h-100">
            <div class="col-1 my-auto ms-2">
                <a href="/"
                    :class="{ 'text-primary': this.slug === 'home', 'text-dark': this.slug !== 'home' }">
                    <font-awesome-icon icon="fa-solid fa-house" />
                </a>
            </div>
            <div class="col">
                <ul class="nav nav-fill">
                    <div v-for="item in categories" :key="item.name">
                        <li class="nav-item">
                            <a :href="`/${item.slug}`" class="fw-bold nav-link"
                                :class="{ 'text-primary': this.slug === item.slug, 'text-dark': this.slug !== item.slug }">{{
                                        item.name
                                }}</a>
                        </li>
                    </div>
                </ul>
            </div>
        </div>

    </div>
</template>
    
<script>
import sourceData from '../components/store/data_routes.json'

export default {
    name: 'HomeNavBar',
    props: {
        slug: String
    },
    data() {
        return {
            categories: sourceData.categories
        }
    },
    methods: {
        handleScroll(event) {
            var sticky = this.$refs.navbar.offsetTop
            // console.log(event.target.documentElement.scrollTop)
            if (event.target.documentElement.scrollTop >= sticky) {
                this.$refs.navbar.classList.add("sticky")
            }
            if (event.target.documentElement.scrollTop < 70) {
                this.$refs.navbar.classList.remove("sticky")
            }
        }
    },
    created() {
        window.addEventListener('scroll', this.handleScroll);
    },
    unmounted() {
        window.removeEventListener('scroll', this.handleScroll);
    },

}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a:hover {
    color: #0275d8 !important;
    text-decoration: none !important;
}

.sticky {
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 100;
}
</style>