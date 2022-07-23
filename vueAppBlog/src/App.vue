<template>
  <div>
    <Navbar></Navbar>
    <router-view></router-view>
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
  *{
    margin:0;
    padding:0;
  }
</style>
