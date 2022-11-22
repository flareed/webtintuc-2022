import { createRouter, createWebHistory } from "vue-router";

// import LoginPage from './views/LoginPage.vue'
// import SignUpPage from './views/LoginPage.vue'
import HomePage from '../views/HomePage.vue';
import sourceData from '@/data_routes.json'

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
        path: '/signup',
        name: 'SignUp',
        component: () => import('../views/SignUpPage.vue'),
    },
    {
        path: '/:id',
        name: 'Category',
        component: () => import('../views/CategoryPage.vue'),
        props: route=> ({...route.params, id: route.params.id}),
        beforeEnter(to) {
            const exists = sourceData.categories.find(
                destination => destination.slug === to.params.id
            )
            if (!exists) return {
                name: 'not-found',
            }
        }
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