<template>
    <section class="section-conten padding-y" style="min-height:84vh">

      <div class="card mx-auto" style="max-width: 380px; margin-top:100px;">
          <div class="card-body">
            <h4 class="card-title mb-4">Login</h4>
              <div class="alert alert-danger" v-for="error in errors" :key="error">
                  <strong v-if="errors.length>0">{{error}}</strong>
              </div>
              <form @submit.prevent="submitLoginForm" method="POST" autocomplete="off">
                  <div class="form-group">
                      <input type="text" ref="username" v-model="username" class="form-control" placeholder="Username" required>
                  </div>
                  <div class="form-group">
                      <input type="password" v-model="password" class="form-control" placeholder="Password"  required>
                  </div>

                  <div class="form-group">
                      <button type="submit" class="btn btn-primary btn-block"> Login  </button>
                  </div>
              </form>
          </div>
        </div>

        <p class="text-center mt-4">Don't have account?
          <router-link :to="{name:'sign-up'}">Sign In</router-link>
        </p>
        <br><br>



  </section>

</template>

<script>
  import axios from 'axios'

  export default{
    data(){
      return{
        username:'',
        password:'',
        errors:[]
      }
    },
    methods: {
      async submitLoginForm(){
          //When user login one more time refresh axios.defaults.headers.common Authorization token refresh
          axios.defaults.headers.common['Authorization'] = ''
          window.localStorage.removeItem('token')

          const formData = {
            username:this.username,
            password:this.password
          }

          await axios.post('api/v1/token/login',formData)
            .then((response)=>{
              console.log('Response data value ', response)
              const token = response.data.auth_token
              console.log('Login Token Value ', token)

              //Send token Vuex When Login
              this.$store.commit('setToken',token)
              axios.defaults.headers.common['Authorization'] = "Token " + token
              window.localStorage.setItem('token',token)

              //After login redirect home page
              // this.$router.replace({name:'home'})
              window.location.href = '/'
            })
            .catch((err)=>{
              console.log('error value in login ', err.data);
              this.errors.push('Something Went Wrong.Please Check Out')
            })

      },
    },
    mounted(){
      window.document.title = 'Log In'
      this.$refs.username.focus()
    },
    created() {
    },
  }
</script>

<style>

</style>
