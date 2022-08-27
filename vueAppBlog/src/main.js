import Vue from 'vue'
import App from './App.vue'
import BootstrapVue  from 'bootstrap-vue'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'
import JwPagination from 'jw-vue-pagination'
import router from './routes.js'
import { store } from './store/store.js'
import Vuelidate from 'vuelidate'
import VueSweetalert2 from 'vue-sweetalert2'
import VueCookies from 'vue-cookies'
import 'sweetalert2/dist/sweetalert2.min.css'

//!Utilize VueSweetalert2
Vue.use(VueSweetalert2)

//!Utilize BootstrapVue
Vue.use(BootstrapVue)

//!Utilize Vuelidate
Vue.use(Vuelidate)

//!Utilize JwPagination
Vue.component('jw-pagination',JwPagination)

//!Utilize VueCokkies
Vue.use(VueCookies,{expire:'1s'})

//!Utilize Axios
axios.defaults.baseURL='http://127.0.0.1:8000/'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
