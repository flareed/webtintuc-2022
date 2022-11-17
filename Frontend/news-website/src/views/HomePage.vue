<template>
<header>
  <HomeHeader/>
</header>

<nav>
  <HomeNavBar/>
</nav>

<main>
  <div class="container py-2">
    <div class="row">
      <HomeMostView/>
    </div>
    <div class="row mt-4">
      <div class="col border-right border-dark">
        <HomeLatestNews/>
      </div>
      <div class="col" style="background-color: blue;">

      </div>
    </div>
    
    
  </div>
</main>

<footer>

</footer>
</template>

<script>
import HomeHeader from '../components/HomeHeader.vue'
import HomeNavBar from '../components/HomeNavBar.vue'
import HomeMostView from '@/components/HomeMostView.vue';
import HomeLatestNews from '@/components/HomeLatestNews.vue';

export default {
  name: 'HomePage',
  components: {
    HomeHeader,
    HomeNavBar,
    HomeMostView,
    HomeLatestNews
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
