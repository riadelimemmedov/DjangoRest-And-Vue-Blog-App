<template>
  <div>
    <Navbar :token_value="token"></Navbar>

    <transition name="transitionUrl" mode="out-in" appear>
      <router-view></router-view>
    </transition>

  </div>
</template>

<script>
  import axios from 'axios'

  import Navbar from './partials/Navbar.vue'

  export default {
    data () {
      return {
        token:'',
        allPosts:[]
      }
    },
    components:{
      'Navbar':Navbar
    },
    created(){
      this.$store.commit('initializeStorage')

      const token = this.$store.state.token
      this.token = token

      console.log('Login Token Value ', token);

      if(token){
        axios.defaults.headers.common['Authorization'] = "Token " + token
      }
      else{
        axios.defaults.headers.common['Authorization'] = ''
      }
    },
    mounted(){
      console.log('all posts return vuex state ', this.$store.state.allPosts)
    }
}
</script>

<style>
  @import "./css/app_css/style.css"
</style>
