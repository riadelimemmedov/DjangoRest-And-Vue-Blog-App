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

        <li class="nav-item" v-if="authenticatedToken">
          <router-link class="nav-link" :to="{name:'profile',params:{username:current_user_profile_slug}}" active-class="active">Profile</router-link>
        </li>

        user token - {{authenticatedToken}}

      </ul>


      <form class="form-inline my-2 my-lg-0" method="POST" @submit.prevent="searchPostFromBackend()">
      <input type="hidden" name="csrfmiddlewaretoken" :value="django_auth_token">
        <template v-if="token_value">
          <span class="nav-item">
              <a class="nav-link" @click="logOut" style="cursor:pointer">Log Out</a>
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

      <input class="form-control mr-sm-2 d-block" v-model="searched_post_text"  type="search" placeholder="Search" aria-label="Search"><!-- v-on:keyup="searchPost($event)" -->
      <div v-if="filteredPosts" class="position-absolute">
          <div v-if="filteredPosts.length > 0">
            <span class="d-block position-relative ml-5 text-center" v-for="post in filteredPosts" :key="post.id" style="left:120px;top:90px;z-index:99999">
                <router-link tag="a" :to="{name:'detail-blog',params:{id:post.id}}" class="post-detail" target="_blank">
                  {{post.title}}
                </router-link>
            </span>
          </div>
          <div v-else>
            <span class="text-danger position-relative font-weight-bold" style="left:200px;top:50px;z-index:99999">Not Found Post</span>
          </div>
      </div>
        <button class="btn btn-outline-success my-2 my-sm-0" id="search-button" type="submit">Search</button>
      </form>

    </div>

  </nav>

</template>

<script>
  import axios from 'axios'
  import bcrypt from 'bcryptjs'
  import Cookies from 'js-cookie'

  export default{
    props:{
      token_value:'',
    },
    data(){
      return{
        isLoggedIn:false,
        authenticatedToken:this.token_value,
        current_user_profile_slug:'',
        django_auth_token:'',
        searched_post_text:'',
        search_results:[],
        allPosts:[],
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
      searchPostFromBackend(){
        if(this.searched_post_text == ''){
          alert('Please Input Data To SearchBar')
        }
        else if(this.searched_post_text != ''){
          // const hashed_input_text = this.searched_post_text
          // const salt = bcrypt.genSaltSync(10)
          // const csrf = bcrypt.hashSync(hashed_input_text,salt)

          // const csrfdata  = Cookies.set('csrftoken',csrf)
          // const csrftoken = Cookies.get('csrftoken')

          // console.log('Csrf Tokendi Nedi Amk Deyeri budur axi ', csrftoken)

          const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
          console.log('Csrf value from input type hidden ', csrf)
          //Sending Post Request
          axios({
            method:'POST',
            url:'search-blog/',
            data:JSON.stringify({
              "csrfmiddlewaretoken" : this.$cookies.get('csrfmiddlewaretoken'),
              "logged_user_token":this.$store.state.token,
              "searched_post_text":this.searched_post_text
            }),
            headers:{
                "X-CSRFToken" : this.$cookies.get('csrfmiddlewaretoken'),
            },
          })
          .then((response)=>{
              let find_blog = response.data
              let profile_serializer = response.data.profile_serializer
              let renderSearchResult_Data = {...find_blog,...profile_serializer}
              console.log('Render Search Data ', renderSearchResult_Data)
              this.$store.commit('renderSearchResult',{find_blog})
              window.location.href = ''
              window.location.href = 'http://localhost:8080/search-result'
          })
        }
      },
      getTokenFromDjango(){
        axios.get('get-token/',{params:{user_authentication_token:this.authenticatedToken}})
          .then((response) => {
            console.log('Returned Token Value ', response.data.token)
            console.log('Current Login Profile slug value ', response.data.profile_serializer.slug)
            this.current_user_profile_slug = response.data.profile_serializer.slug
            this.django_auth_token = response.data.token
            this.$cookies.set('csrfmiddlewaretoken',this.django_auth_token)
          })
          .catch((err)=>{
            console.log('Error Token ', err)
          })
      },
},



      // searchPost(event){
      //   let input_text = event.target.value != '' ? event.target.value : ''
      //   console.log('input text value  ' , input_text)
      //   this.allPosts = this.$store.state.allPosts
      //   this.filteredPosts(input_text)
      // },
      // filteredPosts(input_text){
      //   if(input_text != undefined){
      //     return this.allPosts.filter((post)=>{
      //     if(post.title.toLowerCase().includes(input_text)){
      //       this.search_results.push(post.title)
      //     }
      //   })
      // }
  computed:{
    filteredPosts(){
      if(this.searched_post_text != ''){
        const allPosts = JSON.parse(window.localStorage.getItem('vuex')).allPosts
        return allPosts.filter((post)=>{
            return post.title.toString().toLowerCase().includes(this.searched_post_text.toString().toLowerCase())
        })
      }
    }

  },
  created(){
    //We call getTokenFromDjango methods because we need a token access backend part.
    this.getTokenFromDjango()
    const token = this.$store.state.token ? true : false
    // console.log('isLoggedIn value before token ', this.isLoggedIn)
    // console.log('token', token);
    this.isLoggedIn = token
    // console.log('After token islogged in', this.isLoggedIn)
  },
}


</script>

<style>

</style>


