import Vue from 'vue'
import Vuex from 'vuex'

//!Utilize Vuex This Vue App
Vue.use(Vuex)

export const store = new Vuex.Store({
  state:{
    paginationPost:[],
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

