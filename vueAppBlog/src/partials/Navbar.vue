<template>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color:#ced6e0;margin-top:-20px !important">
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
        
        <template v-if="isLoggedIn">
    
          <span class="nav-item">
              <a href="" class="nav-link">Log Out</a>
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
  export default{
    data(){
      return{
        isLoggedIn:false,
        authenticatedToken:'',
      }
    },
    mounted(){
      const token = this.$store.state.token ? true : false
      console.log('isLoggedIn value before token ', this.isLoggedIn)
      this.isLoggedIn = token
      console.log('After token islogged in', this.isLoggedIn)
    }

  }
</script>

<style>

</style>


