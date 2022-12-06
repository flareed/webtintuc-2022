import { createRouter, createWebHistory } from "vue-router";

import HomePage from '../views/HomePage.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePage,
        alias: "/home"
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('../views/LoginPage.vue'),
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'not-found',
        component: () => import('../views/PageNotFound.vue'),
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router