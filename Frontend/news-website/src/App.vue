<template>
  <!-- <HomePage /> -->
  <LoginPage />
  <!-- <SignUpPage /> -->
</template>

<script>
// import HomePage from './views/HomePage.vue'
import LoginPage from "./views/LoginPage.vue";
// import SignUpPage from "./views/SignUpPage.vue";

export default {
  name: 'App',
  components: {
    // HomePage,
    LoginPage,
    // SignUpPage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 15px;
  font-size: small;
}
</style>
