<template>
  <div class="container">

    <!-- Post Content Column -->
    <div class="col-lg-10">

        <!-- Title -->
        <h1 class="mt-5">{{post.title}}</h1>

        <!-- Author -->
        <p class="lead">
            by
            <a href="#">{{post.owner}}</a>
        </p>

        <hr>

        <!-- Preview Image -->
        <div v-if="post.blog_image">
          <img class="img-fluid rounded w-100 mb-4" :src="`http://127.0.0.1:8000${post.blog_image}`" alt="not found picture">
        </div>

        <div v-else>
          <h1 class="text-muted">Not Found Picture</h1>
        </div>

        <!-- Post Content -->
        <p class="lead">{{post.body}}</p>

        <hr>

        <!-- Comments Form -->
        <div class="card my-4">
            <h5 class="card-header">Leave a Comment:</h5>
            <div class="card-body">
              <!-- !Comment Form -->
                <form @submit.prevent="createComment" method="POST">
                    <div class="form-group">
                        <textarea class="form-control" rows="3" v-model="comment_text"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>

        <!-- Single Comment -->

        <div class="media mb-4" v-for="comment in comments" :key="comment.id">
            <div class="media-body">
                <h5 class="mt-0">{{comment.owner}}</h5>
                {{comment.body}}
                <hr>
            </div>
        </div>

    </div>

</div>
</template>

<script>
  import axios from 'axios'

  export default {
    data(){
      return{
        post:[],
        comments:[],
        token:'',
        comment_text:''
      }
    },
    methods:{
        getBlogDetail(){
          let post_detail_id = this.$route.params.id
          console.log('Post Detail Id ', post_detail_id)
          axios.get(`blog-detail/${post_detail_id}/`)
            .then((response)=>{
              this.post = response.data.serializer
              this.comments = response.data.commentserialize
              console.log('Returned Detailed Post ', response.data)
              console.log('Each post comment serializer list data ', this.comments)
            })
            .catch((err)=>{
              console.log('Not found post ', err);
            })
        },
        postComment(){
          axios.get('get-token/')
            .then((response)=>{
              this.token = response.data.token
              console.log('Returned Token Value Is ', response.data.token)
            })
        },
        createComment(){
          console.log('user id' ,this.$store.state.token)
          axios({
            method:'POST',
            url:'comment-blogs/',
            data:{
              "csrfmiddlewaretoken":this.token,
              "body":this.comment_text,
              "blog":this.$route.params.id,
              "token":this.$store.state.token
            },
            headers:{
              "Content-Type": "multipart/form-data",
            }
          })
          .then((response)=>{
            this.comments.push(response.data)
          })
          .catch((err)=>{
            console.log(err)
            console.log('Err Comment Send')
          })
        }
    },
    created(){
      this.getBlogDetail()
      this.postComment()
    },
    mounted(){
      console.log('Mounted Work Post Detail')
    },
    watch:{
      comments:function(){
        console.log('Comment lIst Updated')
        console.log(this.comments)
      }
    }
  }
</script>

<style>

</style>
