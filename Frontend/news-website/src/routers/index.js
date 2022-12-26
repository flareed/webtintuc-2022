import { createRouter, createWebHistory } from "vue-router";

import HomePage from '../views/HomePage.vue';
import sourceData from '../store/data_routes.json'
// import { HTTP } from '../api'

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
        path: '/search',
        name: 'Search',
        component: () => import('../views/SearchPage.vue'),
        props: route => ({ query: route.query.q, category: route.query.category })
    },
    {
        path: '/:section/:id',
        name: 'article',
        component: () => import('../views/DetailPage.vue'),
        props: route=> ({...route.params, section: route.params.section, id: route.params.id}),
        beforeEnter(to) {
            const exists = sourceData.categories.find(
                destination => destination.slug === to.params.section
            )
            if (!exists) return {
                name: 'not-found',
            }
        },
    },
    {
        path: '/:section',
        name: 'Category',
        component: () => import('../views/CategoryPage.vue'),
        props: route=> ({...route.params, section: route.params.section}),
        beforeEnter(to) {
            const exists = sourceData.categories.find(
                destination => destination.slug === to.params.section
            )
            if (!exists) return {
                name: 'not-found',
            }
        },
        // children: [
        //     {
        //         path: ':name',
        //         name: 'article',
        //         component: () => import('../views/DetailPage.vue'),
        //         props: route=> ({...route.params, section: route.params.id, name: route.params.name}),
        //     }
        // ]
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