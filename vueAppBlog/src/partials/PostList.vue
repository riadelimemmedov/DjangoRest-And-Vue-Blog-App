<template>
      <div class="vtimeline-point">
            <div class="vtimeline-icon">
                <i class="fa fa-image"></i>
            </div>
            <div class="vtimeline-block">
                <span class="vtimeline-date">{{formatDate(post.created)}}</span><div class="vtimeline-content">
                    <a href="#"><img :src="post.blog_image" alt="" class="img-fluid mb20" style="width:700px;height:700px"></a>
                    <a href="#"><h3>{{post.title}}</h3></a>
                    <ul class="post-meta list-inline">
                        <li class="list-inline-item">
                            <i class="fa fa-user-circle-o"></i> <a href="#">{{post.owner}}</a>
                        </li>
                        <li class="list-inline-item">
                            <i class="fa fa-calendar-o"></i> <a href="#">{{formatDate(post.created)}}</a>
                        </li>
                        <li class="list-inline-item">
                            <i class="fa fa-tags"></i> <a href="#">Bootstrap4</a><!-- !Not yet exists Category and Tag and Like and Comment Model -->
                        </li>
                    </ul>
                    <p>
                      {{post.body}}<!-- !Add readmore functionality with vue js -->
                    </p><br>
                    <a href="#" class="btn btn-outline-secondary btn-sm">Read More</a>
                </div>
            </div>
        </div>

</template>

<script>
  import moment from 'moment'

  export default{
    props:{
      single_post:Object
    },
    data(){
      return{
        post:this.single_post
      }
    },
    methods:{
      formatDate:function(value){
        if(value){
          return moment(String(value)).format('MMMM DD, YYYY')
        }
      },
    },
  }
</script>

<style>

</style>
