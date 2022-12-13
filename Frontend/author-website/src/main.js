import "bootstrap/dist/css/bootstrap.css"
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from '@/routers'
import CKEditor from '@ckeditor/ckeditor5-vue';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faCircleUser } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faCircleUser)

createApp(App)
.component('font-awesome-icon', FontAwesomeIcon)
.use(router)
.use( CKEditor )
.mount('#app')

import "bootstrap/dist/js/bootstrap.js"