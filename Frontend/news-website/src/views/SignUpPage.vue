<template>
    <header>
        <LoginHeader />
    </header>

    <main>
        <SignUpForm />
    </main>

    <footer class="footer-bs">
        <LoginFooter />
    </footer>

</template>
  
<script>

import LoginHeader from '@/components/LoginHeader.vue';
import SignUpForm from '@/components/SignUpForm.vue';
import LoginFooter from '@/components/LoginFooter.vue';

export default {
    name: 'SignUpPage',
    components: {
        LoginHeader,
        SignUpForm,
        LoginFooter
    },
}
</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.footer-bs {
    position: fixed;
    /* padding: 10px 10px 0px 10px; */
    bottom: 0;
    width: 100%;
    /* Height of the footer*/
    height: 35px;
    background: grey;
}
</style>