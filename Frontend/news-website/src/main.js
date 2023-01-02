import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import { createApp } from 'vue'
import App from './App.vue'
import router from '@/routers'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret, faCircleUser, faMagnifyingGlass, faList, faHouse, faFeather, faThumbsUp } from '@fortawesome/free-solid-svg-icons'
import {faFacebook, faTwitter, faYoutube} from '@fortawesome/free-brands-svg-icons'
import {faShareFromSquare, faBookmark, faComment} from '@fortawesome/free-regular-svg-icons'

/* add icons to the library */
library.add(faUserSecret, faCircleUser, faMagnifyingGlass, faList, faFacebook, faTwitter, faYoutube, faHouse, faShareFromSquare, faBookmark, faComment, faFeather, faThumbsUp)

let app = createApp(App)

app
.component('font-awesome-icon', FontAwesomeIcon)
.use(router)
.mount('#app')


// import "bootstrap/dist/js/bootstrap.js"