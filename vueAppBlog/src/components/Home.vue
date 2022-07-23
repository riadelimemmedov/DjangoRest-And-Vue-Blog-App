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
                    <a href="#"><h3>{{post.title}}</h3></a>
                    <ul class="post-meta list-inline">
                        <li class="list-inline-item">
                            <i class="fa fa-user-circle-o"></i> <a href="#">{{post.owner}}</a>
                        </li>
                        <li class="list-inline-item">
                            <i class="fa fa-calendar-o"></i> {{formatDate(post.created)}}<a href="#"></a>
                        </li>
                        <li class="list-inline-item">
                            <i class="fa fa-tags"></i> <a href="#">Bootstrap4</a>
                        </li>
                    </ul>
                    <p>
                      {{post.body.split(/[!,?,.]/,5).toString()}}...
                      {{post.blog_category}}
                    </p><br>
                    <a href="#" class="btn btn-outline-secondary btn-sm">Read More</a>
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


  import PostList from '../partials/PostList.vue'
  import { onUpdated } from 'vue'

  export default {
    data() {
      return {
        posts: [],
        pageOfItems:[]
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
      formatDate(value){
        if(value){
          return moment(String(value)).format('MMMM DD, YYYY')
        }
      }
    },
    created(){
        this.getAllPosts()
    }
  }
</script>

<style>
body{
    margin-top:20px;
    background:#f3f3f3;
}
/*
Timeline
*/

.page-timeline {
    margin: 30px auto 0 auto;
    position: relative;
    max-width: 1000px;
}

.page-timeline:before {
    position: absolute;
    content: '';
    top: 0;
    bottom: 0;
    left: 303px;
    right: auto;
    height: 100%;
    width: 3px;
    background: #3498db;
    z-index: 0;

        -webkit-box-shadow: 0 2px 2px 0 rgba(0,0,0,0.2),0 6px 10px 0 rgba(0,0,0,0.3);
    box-shadow: 0 2px 2px 0 rgba(0,0,0,0.2),0 6px 10px 0 rgba(0,0,0,0.3);
}

.page-timeline:after {
    position: absolute;
    content: '';
    width: 3px;
    height: 40px;
    background: #3498db;
    background: -webkit-linear-gradient(top, #4782d3, rgba(52, 152, 219, 0));
    background: linear-gradient(to bottom, #4782d3, rgba(52, 152, 219, 0));
    top: 100%;
    left: 303px;

        -webkit-box-shadow: 0 2px 2px 0 rgba(0,0,0,0.2),0 6px 10px 0 rgba(0,0,0,0.3);
    box-shadow: 0 2px 2px 0 rgba(0,0,0,0.2),0 6px 10px 0 rgba(0,0,0,0.3);
}

.vtimeline-content {
    margin-left: 350px;
    background: #fff;
    border: 1px solid #e6e6e6;
    padding: 35px 20px;
    border-radius: 3px;
    text-align: left;

    -webkit-box-shadow: 0 2px 2px 0 rgba(0,0,0,0.2),0 6px 10px 0 rgba(0,0,0,0.3);
    box-shadow: 0 2px 2px 0 rgba(0,0,0,0.2),0 6px 10px 0 rgba(0,0,0,0.3);
}

.vtimeline-content h3 {
    font-size: 1.5em;
    font-weight: 600;
    display: inline-block;
    margin: 0;
}

.vtimeline-content p {
    font-size: 0.9em;
    margin: 0;
}

.vtimeline-point {
    position: relative;
    display: block;
    vertical-align: top;
    margin-bottom: 30px;
}

.vtimeline-icon {
    position: relative;
    color: #fff;
    width: 50px;
    height: 50px;
    background: #4782d3;
    border-radius: 50%;
    float: left;
    text-align: center;
    line-height: 50px;
    z-index: 99;
    margin-left: 280px;
}

.vtimeline-icon i {
    display: block;
    font-size: 1.5em;
    line-height: 50px;

}

.vtimeline-date {
    width: 260px;
    text-align: right;
    position: absolute;
    left: 0;
    top: 10px;
    font-weight: 400;
    color: #374054;
}
.post-meta {
    padding-top: 15px;
    margin-bottom: 20px;
}
.post-meta li:not(:last-child) {
    margin-right: 10px;
}
h3 {
    font-family: "Montserrat", sans-serif;
    color: #252525;
    font-weight: 700;
    font-variant-ligatures: common-ligatures;
    margin-top: 0;
    letter-spacing: -0.2px;
    line-height: 1.3;
}
.mb20 {
    margin-bottom: 20px !important;
}
</style>
