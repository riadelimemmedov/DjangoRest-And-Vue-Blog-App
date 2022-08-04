<template>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color:#ced6e0;margin-top:-5px">
    <a class="navbar-brand" href="/">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item"><!-- !Bura router-link yazmalinsan yaddsa saxla active classsida orde duzeldersen ele indi router-link tagi icincde deyil deye islemir -->
          <router-link class="nav-link" :to="{name:'home'}" active-class="active">Posts</router-link>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="#">Profile</a>
        </li>
      </ul>

      <form class="form-inline my-2 my-lg-0">

        <template v-if="token_value">

          <span class="nav-item">
              <a class="nav-link" @click="logOut" style="cursor:pointer">Log Out</a>
              <!-- <router-link class="nav-link" :to="{name:'login'}" active-class="active">Log Out</router-link> -->
              <!-- LogOut funstion writinf after -->
          </span>
        </template>

        <template v-else>
            <span class="nav-item">
                <router-link class="nav-link" :to="{name:'sign-up'}" active-class="active">Sign Up</router-link>
            </span>
            <span class="nav-item">
              <router-link class="nav-link" :to="{name:'login'}" active-class="active">Log In</router-link>
            </span>
        </template>

        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
</template>

<script>
  import axios from 'axios'

  export default{
    props:{
      token_value:''
    },
    data(){
      return{
        isLoggedIn:false,
        authenticatedToken:this.token_value
      }
    },
    methods:{
      logOut(){
        this.$swal.fire({
          title: 'Are you sure logout?',
          icon: 'warning',
          showCancelButton: true,
          focusCancel:true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Yes!'
        }).then((result) => {
          //?Logout Functionality
          axios.defaults.headers.common['Authorization'] = ''
          window.localStorage.removeItem('token')
          this.$store.commit('removeToken')
          if (result.isConfirmed) {
            this.$swal.fire(
              'Successfully LogOut',
              '',
              'success',
              setTimeout(() => {
                console.log('ay blet');
                console.log(document.querySelector('.swal2-confirm').textContent)
                document.querySelector('.swal2-confirm').addEventListener('click',()=>{
                  window.location.href = '/'
                })
              },100)
            )
          }
      })

    },
    created(){
      const token = this.$store.state.token ? true : false
      console.log('isLoggedIn value before token ', this.isLoggedIn)
      console.log('token', token);
      this.isLoggedIn = token
      console.log('After token islogged in', this.isLoggedIn)
    },

  }


}
</script>

<style>

</style>


