import Vue from 'vue'
import App from './App.vue'
import BootstrapVue  from 'bootstrap-vue'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'
import JwPagination from 'jw-vue-pagination'
import router from './routes.js'
import { store } from './store/store.js'
import Vuelidate from 'vuelidate'


//!Utilize BootstrapVue
Vue.use(BootstrapVue)

//!Utilize Vuelidate
Vue.use(Vuelidate)

//!Utilize JwPagination
Vue.component('jw-pagination',JwPagination)

//!Utilize Axios
axios.defaults.baseURL='http://127.0.0.1:8000/'
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
