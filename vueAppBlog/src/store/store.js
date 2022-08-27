import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

//!Utilize Vuex This Vue App
Vue.use(Vuex)

export const store = new Vuex.Store({
  plugins: [createPersistedState()],
  state:{
    paginationPost:[],
    allPosts:[],
    searchResults:null,
    isAuthenticated:false,
    token:''
  },
  getters:{
    getPaginationPost(state){
      return state.perPagePost
    }
  },
  mutations:{
    renderPaginationPost(state,paginatepost){
      state.paginationPost = paginatepost
    },
    renderAllPosts(state,posts){
      state.allPosts = posts
    },
    initializeStorage(state){
      if(window.localStorage.getItem('token')){
        state.token = window.localStorage.getItem('token')
        state.isAuthenticated = true
      }
      else{
        state.token = ''
        state.isAuthenticated = false
      }
    },
    renderSearchResult(state,result_posts){
      state.searchResults=result_posts
    },
    setToken(state,token){
      state.token=token
      state.isAuthenticated=true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    }
  }
})

