<template>
  <div>
    <Navbar></Navbar>

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
      }
    },
    components:{
      'Navbar':Navbar
    },
    beforeCreate(){
      this.$store.commit('initializeStorage')

      const token = this.$store.state.token

      console.log('Login Token Value ', token);

      if(token){
        axios.defaults.headers.common['Authorization'] = "Token " + token
      }
      else{
        axios.defaults.headers.common['Authorization'] = ''
      }

    }
}
</script>

<style>
  @import "./css/app_css/style.css"
</style>
