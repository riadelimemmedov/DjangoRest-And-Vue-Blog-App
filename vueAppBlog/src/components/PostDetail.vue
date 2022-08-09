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
          <img class="img-fluid rounded w-100 mb-4" :src="post.blog_image" alt="">
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
                        <textarea class="form-control" rows="3"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>

        <!-- Single Comment -->

        <div class="media mb-4">
            <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
            <div class="media-body">
                <h5 class="mt-0">Commenter Name</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus
                odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate
                fringilla. Donec lacinia congue felis in faucibus.
            </div>
        </div>

        <!-- Comment with nested comments -->
        <div class="media mb-4">
            <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
            <div class="media-body">
                <h5 class="mt-0">Commenter Name</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus
                odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate
                fringilla. Donec lacinia congue felis in faucibus.

                <div class="media mt-4">
                    <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
                    <div class="media-body">
                        <h5 class="mt-0">Commenter Name</h5>
                        Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras
                        purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi
                        vulputate fringilla. Donec lacinia congue felis in faucibus.
                    </div>
                </div>

                <div class="media mt-4">
                    <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
                    <div class="media-body">
                        <h5 class="mt-0">Commenter Name</h5>
                        Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras
                        purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi
                        vulputate fringilla. Donec lacinia congue felis in faucibus.
                    </div>
                </div>

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
        token:''
      }
    },
    methods:{
        getBlogDetail(){
          let post_detail_id = this.$route.params.id
          console.log('Post Detail Id ', post_detail_id)
          axios.get(`blog-detail/${post_detail_id}/`)
            .then((response)=>{
              this.post = response.data
              console.log('Returned Detailed Post ', response.data)
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
          axios({
            method:'POST',
            url:'comment-blogs/',
            data:{
              "csrfmiddlewaretoken":this.token,
              "body":'Great .net post',
              "blog_id":this.$route.params.id,
              "user_token":window.localStorage.getItem('token')
            },
            headers:{
              "Content-Type": "multipart/form-data",
            }
          })
          .then((response)=>{
            console.log('Successfully Send Comment')
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
    }
  }
</script>

<style>

</style>
