<template>
  <div class="container mb80"><br><br><br>


    <div class="page-timeline" style="margin-right:150px">

      <div class="vtimeline-point" v-for="(post,index) in pageOfItems" :key="index">
            <div class="vtimeline-icon">
                <i class="fa fa-image"></i>
            </div>
            <div class="vtimeline-block">
                <span class="vtimeline-date">{{formatDate(post.created)}}</span><div class="vtimeline-content">
                    <a href="#"><img :src="post.blog_image" alt="" class="img-fluid mb20" style="width:700px;height:700px"></a>
                    
                    <a href="" @click.prevent="getBlogDetail(post.id)"><h3>{{post.title}}</h3></a>
                    
                    <ul class="post-meta list-inline">
                        <li class="list-inline-item">
                            <i class="fa fa-user-circle-o"></i> <a href="#">{{post.owner}}</a>
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
                          <i class="fa fa-thumbs-o-up" aria-hidden="true"></i><!-- Like modelini yazandan sonra goster burda her posta gelen like sayini -->
                        </li>
                    </ul>
                    <p>
                      {{post.body.split(/[!,?,.]/,5).toString()}}...
                    </p><br>
                    <a href="#" class="btn btn-outline-dark btn-sm">Read More</a>
                    <form @submit.prevent="likeToPost($event)" method="POST" class="d-inline">
                      <input type="hidden" :value="post_id=post.id" name="blog_id">
                      <button id="like-button" class="btn-sm mx-auto text-center" enctype="multipart/form-data">
                        <i class="fa fa-thumbs-up fa-2x" aria-hidden="true" style="color:#2e86de"></i>
                      </button>
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
        post_id:null
      }
    },
    components:{
      PostList
    },
    methods: {
      onChangePage(pageOfItems){
        this.pageOfItems=pageOfItems
        this.$store.commit('renderPaginationPost',pageOfItems)

        console.log('Hal Hazirdaki Paginationdaki Postlar ', this.pageOfItems)
      },
      getAllPosts(){
        axios.get('/')
          .then((response)=>{
            this.posts=response.data
            console.log(response.data)
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
            "title":"Hello",
            "body":"Python",
          },
          headers:{
            "Content-Type": "multipart/form-data",
          }
        })
      },
      getBlogDetail(post_detail_id){
        axios.get(`blog-detail/${post_detail_id}/`)
          .then((response)=>{
            console.log('Returned Detailed Post ', response.data)
          })
          .catch((err)=>{
            console.log('Not found post ', err);
          })
      },
      formatDate(value){
          if(value){
            return moment(String(value)).format('MMMM DD, YYYY')
          }
      },
    },
    created(){
        this.getAllPosts()
    }
  }
</script>

<style>
  @import "../css/components_css/home.css"
</style>
