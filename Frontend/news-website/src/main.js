import "bootstrap/dist/css/bootstrap.css"
import { createApp } from 'vue'
import App from './App.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret, faCircleUser, faMagnifyingGlass, faList } from '@fortawesome/free-solid-svg-icons'
import {faFacebook, faTwitter, faYoutube} from '@fortawesome/free-brands-svg-icons'

/* add icons to the library */
library.add(faUserSecret, faCircleUser, faMagnifyingGlass, faList, faFacebook, faTwitter, faYoutube)

createApp(App).component('font-awesome-icon', FontAwesomeIcon).mount('#app')

import "bootstrap/dist/js/bootstrap.js"