<template>
  <header>
    <HomeHeader />
  </header>

  <nav>
    <HomeNavBar slug="home" />
  </nav>

  <main>
    <div class="container py-2">
      <div class="row">
        <HomeMostView />
      </div>
      <div class="row mt-4">
        <div class="col border-right border-dark">
          <HomeLatestNews />
        </div>
        <div class="col">
          <HomeCategoryNews section="Thể thao" />
          <HomeCategoryNews section="Giải trí" />
          <HomeCategoryNews section="Du lịch" />
          <HomeCategoryNews section="Số hoá" />
        </div>
      </div>
      <div class="mt-4">
        <HomePicsShow />
      </div>
    </div>
  </main>

  <footer>
    <HomeFooter />
  </footer>
</template>

<script>
import HomeHeader from '../components/HomeHeader.vue';
import HomeNavBar from '../components/HomeNavBar.vue';
import HomeMostView from '@/components/HomeMostView.vue';
import HomeLatestNews from '@/components/HomeLatestNews.vue';
import HomeCategoryNews from '@/components/HomeCategoryNews.vue';
import HomePicsShow from '@/components/HomePicsShow.vue';
import HomeFooter from '@/components/HomeFooter.vue';

export default {
  name: 'HomePage',
  components: {
    HomeHeader,
    HomeNavBar,
    HomeMostView,
    HomeLatestNews,
    HomeCategoryNews,
    HomePicsShow,
    HomeFooter
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
