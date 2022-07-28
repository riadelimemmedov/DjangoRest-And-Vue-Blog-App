import Vue from "vue"
import VueRouter from "vue-router"
import Router from 'vue-router'

//Imported components created after//
import Home from './components/Home.vue'
import Signup from './components/Signup.vue'
import Login from './components/Login.vue'

//!Utilize VueRouter
Vue.use(VueRouter)

export default new Router({
  mode:'history',
  base:process.env.BASE_URL,
  routes:[
    {path:'/',component:Home,name:'home'},
    {path:'/sign-up',component:Signup,name:'sign-up'},
    {path:'/login',component:Login,name:'login'}
  ]
})

