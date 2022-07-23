import Vue from 'vue'
import Vuex from 'vuex'

//!Utilize Vuex This Vue App
Vue.use(Vuex)

export const store = new Vuex.Store({
  state:{
    paginationPost:[]
  },
  getters:{
    getPaginationPost(state){
      return state.perPagePost
    }
  },
  mutations:{
    renderPaginationPost(state,paginatepost){
      state.paginationPost = paginatepost
    }
  }
})

