import { createRouter, createWebHistory } from "vue-router";

// import LoginPage from './views/LoginPage.vue'
// import SignUpPage from './views/LoginPage.vue'
// import HomePage from './views/HomePage.vue';

const routes = [
    { 
        path: '/', 
        name: 'Home', 
        component: () => import('../views/HomePage.vue'), 
    },
    { 
        path: '/login', 
        name: 'Login', 
        component: () => import('../views/LoginPage.vue'), 
    },
    { 
        path: '/signup', 
        name: 'SignUp', 
        component: () => import('../views/SignUpPage.vue'), 
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router