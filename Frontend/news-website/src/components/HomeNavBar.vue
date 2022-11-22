<template>
    <div class="container-fluid border-top border-bottom border-dark my-2">
        <div class="row h-100 py-1 px-4">
            <div class="col-1">
                <h6 class="my-auto">
                  <a href="/" :class="{ 'text-primary': this.slug === 'home', 'text-dark': this.slug !== 'home'}">
                    <font-awesome-icon icon="fa-solid fa-house" />
                  </a>
                  
                </h6>
            </div>
            <div class="col">
                <div class="row h-100">
                    <div v-for="item in categories" :key="item.name" class="my-auto mr-auto"> 
                        <a class="font-weight-bold" :href=item.slug :class="{ 'text-primary': this.slug === item.slug, 'text-dark': this.slug !== item.slug}">{{ item.name }}</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import sourceData from '@/data_routes.json'
export default {
    name: 'HomeNavBar',
    props:{
      slug: String
    },
    data() {
        return {
            categories: sourceData.categories
        }
    }
}
</script>
    
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a:hover{
  color: #0275d8 !important;
  text-decoration: none;
}
</style>