import Vue from "vue"
import VueRouter from "vue-router"
import Router from 'vue-router'

//Imported components created after//
import Home from './components/Home.vue'

//!Utilize VueRouter
Vue.use(VueRouter)

export default new Router({
  mode:'history',
  base:process.env.BASE_URL,
  routes:[
    {path:'/',component:Home,name:'home'}
  ]
})

