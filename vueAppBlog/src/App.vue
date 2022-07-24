<template>
  <div>
    <Navbar></Navbar>

    <transition name="transitionUrl" mode="out-in" appear>
      <router-view></router-view>
    </transition>

  </div>
</template>

<script>
  import Navbar from './partials/Navbar.vue'

  export default {
    data () {
      return {
      }
    },
    components:{
      'Navbar':Navbar
    }
}
</script>

<style>
  @import "./css/app_css/style.css"
</style>
