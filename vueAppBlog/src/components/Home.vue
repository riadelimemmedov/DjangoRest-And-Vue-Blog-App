<template>
  <div class="container mb80"><br><br><br>


    <div class="page-timeline" style="margin-right:150px">

      <div class="vtimeline-point" v-for="(post,index) in pageOfItems" :key="index">
            <div class="vtimeline-icon">
                <i class="fa fa-image"></i>
            </div>
            <div class="vtimeline-block">

                <span class="vtimeline-date">{{formatDate(post.created)}}</span><div class="vtimeline-content">
                    <a href="#"><img :src="`http://127.0.0.1:8000${post.blog_image}`" alt="" class="img-fluid mb20" style="width:700px;height:700px"></a>

                    <router-link :to="{name:'detail-blog',params:{id:post.id}}">
                      <h3>{{post.title}}</h3>
                    </router-link>

                    <ul class="post-meta list-inline">
                        <li class="list-inline-item">
                            <i class="fa fa-user-circle-o"></i>
                            <router-link>
                              <a href="">{{post.owner}}</a>
                            </router-link>
                        </li>
                        <li class="list-inline-item">
                            <i class="fa fa-calendar-o"></i> {{formatDate(post.created)}}<a href="#"></a>
                        </li>
                        <li class="list-inline-item">
                            <i class="fa fa-tags"></i> <a href="#">{{post.category}}</a>
                        </li>
                        <li class="list-inline-item">
                          <i class="fa fa-comment" aria-hidden="true"> {{post.blog_comments.length}}</i>
                        </li>
                        <li class="list-inline-item">
                          <i class="fa fa-thumbs-o-up" aria-hidden="true">&nbsp;{{post.liked.length}}</i>
                        </li>
                    </ul>
                    <p>
                      {{post.body.split(/[!,?,.]/,5).toString()}}...
                    </p><br>

                    <router-link tag="a" class="btn btn-outline-dark btn-sm" :to="{name:'detail-blog',params:{id:post.id}}">
                        Read More
                    </router-link>


                    <form @submit.prevent="likeToPost($event)" method="POST" class="d-inline">
                      <input type="hidden" :value="post_id=post.id" name="blog_id">

                      <div v-if="current_user.username != null" class="mx-auto text-left float-right" style="padding-right:250px !important">

                          <button v-if="post.liked.includes(current_user.username)==true" id="like-button" class="btn-sm mx-auto" type="submit">
                              <i class="fa fa-thumbs-down fa-2x" aria-hidden="true" style="color:#2e86de"></i>
                          </button>

                          <button v-else-if="post.liked.includes(current_user.username)==false" id="like-button" class="btn-sm mx-auto" type="submit">
                              <i class="fa fa-thumbs-up fa-2x" aria-hidden="true" style="color:#2e86de"></i>
                          </button>
                      </div>


                    </form>
                </div>
            </div>
        </div>

      </div>
          <div class="card" style="margin-left:350px;width:55%">
            <div class="card-footer pb-0 pt-3">
                <jw-pagination :items="posts" @changePage="onChangePage"></jw-pagination>
            </div>
          </div>
      <br>


</div>
</template>

<script>
  //Thirty Party Packages
  import axios from 'axios'
  import moment from 'moment'
  import bcrypt from 'bcryptjs'

  import PostList from '../partials/PostList.vue'
  import { onUpdated } from 'vue'

  export default {
    data() {
      return {
        posts: [],
        pageOfItems:[],
        post_id:null,
        current_user:'',
        liked_blog_value : null,
        blog_users_like:[],
        liked_post:'',
      }
    },
    components:{
      PostList
    },
    methods: {
      onChangePage(pageOfItems){
        this.pageOfItems=pageOfItems
        this.$store.commit('renderPaginationPost',pageOfItems)
      },
      getAllPosts(){
        axios.get('/',{
          params:{'user_token':this.$store.state.token}
        })
          .then((response)=>{
            this.posts=response.data.serializer_data
            console.log('Posts', response.data.serializer_data)
            console.log('Current User ', response.data.current_user)
            this.current_user = response.data.current_user != null ? response.data.current_user : false
            this.$store.commit('renderAllPosts',this.posts)
          })
      },
      likeToPost(e){
        const blog_id = e.target.firstChild.value
        const salt = bcrypt.genSaltSync(10)
        const csrf = bcrypt.hashSync(blog_id,salt)

        axios({
          method:'POST',
          url:'/',
          data:{
            'csrfmiddlewaretoken':csrf,
            "blog_id":blog_id,
            "user_token":this.$store.state.token
          },
          headers:{
            "Content-Type": "multipart/form-data",
          }
        })
          .then((response) =>{
            console.log('Returned Response Value ', response.data)
            console.log('Like or Unlike Value ', response.data.like_value)
            console.log('liked blog detail', response.data.blog_obj)
            this.like_value = response.data.like_value
            this.liked_blog_value = response.data.blog_obj.is_liked
            this.liked_post = response.data.blog_obj
            this.getAllPosts()
          })
      },
      formatDate(value){
          if(value){
            return moment(String(value)).format('MMMM DD, YYYY')
          }
      },
    },
    computed:{
      likedPostValue(){
        this.getAllPosts()
        return this.liked_blog_value
      }
    },
    created(){
        this.getAllPosts()
    }
  }
</script>

<style>
  @import "../css/components_css/home.css"
</style>
