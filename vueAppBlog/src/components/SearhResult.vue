<template>
    <div class="container">
        <div class="row" v-if="searchResults['find_blog'].length > 0 && searchResults['profile_serializer'].length > 0">
            <div class="col-sm-8 col-sm-offset-2 offset-2 mt-5" v-for="searchResult in searchResults['find_blog']" :key="searchResult.id">
                  <div class="row">
                    <div class="col-sm-12">
                        <div class="panel panel-white post">
                            <div class="post-heading">
                                  <div class="pull-left image" v-for="profile in searchResults['profile_serializer']" :key="profile.id">
                                      <router-link :to="{name:'profile',params:{username:profile.user}}">
                                        <img v-if="searchResult.owner == profile.user" :src="`http://127.0.0.1:8000${profile.profile_picture}`" class="img-circle avatar" alt="user profile image">
                                      </router-link>
                                    <div class="pull-left meta">
                                        <div class="title h5" v-if="searchResult.owner == profile.user">
                                          <router-link :to="{name:'profile',params:{username:profile.user}}">
                                              <b>{{searchResult.owner}}</b>
                                          </router-link>
                                        </div>
                                        <!-- <h6 class="text-muted time">{{searchResult.created}}</h6> -->
                                    </div>
                                  </div>
                            </div>
                            <div class="post-image">
                                <router-link :to="{name:'detail-blog',params:{id:searchResult.id}}">
                                  <img src=""><img :src="`http://127.0.0.1:8000${searchResult.blog_image}`" class="image" alt="image post">
                                </router-link>
                            </div>
                            <div class="post-description">
                                <router-link :to="{name:'detail-blog',params:{id:searchResult.id}}" class="text-secondary">
                                  <h4>{{searchResult.title}}</h4>
                                </router-link>
                                <p>{{searchResult.body.split(/[!,?,.]/,5).toString()}}...</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row" v-else>
            <div class="col-sm-10 col-sm-offset-2 offset-1 text-center mt-5">
                <div class="alert alert-danger font-weight-bold text-secondary">Not Found Posts</div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    data(){
      return{
        searchResults:[]
      }
    },
    created(){
        this.searchResults = this.$store.state.searchResults
    },
    mounted(){

    }
  }
</script>

<style>
  body{margin-top:20px;
  background:#eee;
  }

  .profile-widget {
    position: relative;
  }
  .profile-widget .image-container {
    background-size: cover;
    background-position: center;
    padding: 190px 0 10px;
  }
  .profile-widget .image-container .profile-background {
    width: 100%;
    height: auto;
  }
  .profile-widget .image-container .avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    margin: 0 auto -60px;
    display: block;
  }
  .profile-widget .details {
    padding: 50px 15px 15px;
    text-align: center;
  }
  /* End Component: Profile Widget */
  /********************************************************************
  *********************************************************************
  *********************************************************************/
  /* Component: Mini Profile Widget */
  .mini-profile-widget .image-container .avatar {
    width: 180px;
    height: 180px;
    display: block;
    margin: 0 auto;
    border-radius: 50%;
    background: white;
    padding: 4px;
    border: 1px solid #dddddd;
  }
  .mini-profile-widget .details {
    text-align: center;
  }



  /* Component: Panel */
  .panel {
    border-radius: 0;
    margin-bottom: 30px;
  }
  .panel.solid-color {
    color: white;
  }
  .panel .panel-heading {
    border-radius: 0;
    position: relative;
  }
  .panel .panel-heading > .controls {
    position: absolute;
    right: 10px;
    top: 12px;
  }
  .panel .panel-heading > .controls .nav.nav-pills {
    margin: -8px 0 0 0;
  }
  .panel .panel-heading > .controls .nav.nav-pills li a {
    padding: 5px 8px;
  }
  .panel .panel-heading .clickable {
    margin-top: 0px;
    font-size: 12px;
    cursor: pointer;
  }
  .panel .panel-heading.no-heading-border {
    border-bottom-color: transparent;
  }
  .panel .panel-heading .left {
    float: left;
  }
  .panel .panel-heading .right {
    float: right;
  }
  .panel .panel-title {
    font-size: 16px;
    line-height: 20px;
  }
  .panel .panel-title.panel-title-sm {
    font-size: 18px;
    line-height: 28px;
  }
  .panel .panel-title.panel-title-lg {
    font-size: 24px;
    line-height: 34px;
  }
  .panel .panel-body {
    font-size: 13px;
  }
  .panel .panel-body > .body-section {
    margin: 0px 0px 20px;
  }
  .panel .panel-body > .body-section > .section-heading {
    margin: 0px 0px 5px;
    font-weight: bold;
  }
  .panel .panel-body > .body-section > .section-content {
    margin: 0px 0px 10px;
  }
  .panel-white {
    border: 1px solid #dddddd;
  }
  .panel-white > .panel-heading {
    color: #333;
    background-color: #fff;
    border-color: #ddd;
  }
  .panel-primary {
    border: 1px solid #dddddd;
  }
  .panel-purple {
    border: 1px solid #dddddd;
  }
  .panel-purple > .panel-heading {
    color: #fff;
    background-color: #8e44ad;
    border: none;
  }
  .panel-purple > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-light-purple {
    border: 1px solid #dddddd;
  }
  .panel-light-purple > .panel-heading {
    color: #fff;
    background-color: #9b59b6;
    border: none;
  }
  .panel-light-purple > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-blue,
  .panel-info {
    border: 1px solid #dddddd;
  }
  .panel-blue > .panel-heading,
  .panel-info > .panel-heading {
    color: #fff;
    background-color: #2980b9;
    border: none;
  }
  .panel-blue > .panel-heading .panel-title a:hover,
  .panel-info > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-light-blue {
    border: 1px solid #dddddd;
  }
  .panel-light-blue > .panel-heading {
    color: #fff;
    background-color: #3498db;
    border: none;
  }
  .panel-light-blue > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-green,
  .panel-success {
    border: 1px solid #dddddd;
  }
  .panel-green > .panel-heading,
  .panel-success > .panel-heading {
    color: #fff;
    background-color: #27ae60;
    border: none;
  }
  .panel-green > .panel-heading .panel-title a:hover,
  .panel-success > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-light-green {
    border: 1px solid #dddddd;
  }
  .panel-light-green > .panel-heading {
    color: #fff;
    background-color: #2ecc71;
    border: none;
  }
  .panel-light-green > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-orange,
  .panel-warning {
    border: 1px solid #dddddd;
  }
  .panel-orange > .panel-heading,
  .panel-warning > .panel-heading {
    color: #fff;
    background-color: #e82c0c;
    border: none;
  }
  .panel-orange > .panel-heading .panel-title a:hover,
  .panel-warning > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-light-orange {
    border: 1px solid #dddddd;
  }
  .panel-light-orange > .panel-heading {
    color: #fff;
    background-color: #ff530d;
    border: none;
  }
  .panel-light-orange > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-red,
  .panel-danger {
    border: 1px solid #dddddd;
  }
  .panel-red > .panel-heading,
  .panel-danger > .panel-heading {
    color: #fff;
    background-color: #d40d12;
    border: none;
  }
  .panel-red > .panel-heading .panel-title a:hover,
  .panel-danger > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-light-red {
    border: 1px solid #dddddd;
  }
  .panel-light-red > .panel-heading {
    color: #fff;
    background-color: #ff1d23;
    border: none;
  }
  .panel-light-red > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-pink {
    border: 1px solid #dddddd;
  }
  .panel-pink > .panel-heading {
    color: #fff;
    background-color: #fe31ab;
    border: none;
  }
  .panel-pink > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-light-pink {
    border: 1px solid #dddddd;
  }
  .panel-light-pink > .panel-heading {
    color: #fff;
    background-color: #fd32c0;
    border: none;
  }
  .panel-light-pink > .panel-heading .panel-title a:hover {
    color: #f0f0f0;
  }
  .panel-group .panel {
    border-radius: 0;
  }
  .panel-group .panel + .panel {
    margin-top: 0;
    border-top: 0;
  }

  /* Component: Posts */
  .post .post-heading {
    height: 95px;
    padding: 20px 15px;
  }
  .post .post-heading .avatar {
    width: 60px;
    height: 60px;
    display: block;
    margin-right: 15px;
  }
  .post .post-heading .meta .title {
    margin-bottom: 0;
  }
  .post .post-heading .meta .title a {
    color: black;
  }
  .post .post-heading .meta .title a:hover {
    color: #aaaaaa;
  }
  .post .post-heading .meta .time {
    margin-top: 8px;
    color: #999;
  }
  .post .post-image .image {
    width: 100%;
    height: auto;
  }
  .post .post-description {
    padding: 15px;
  }
  .post .post-description p {
    font-size: 14px;
  }
  .post .post-description .stats {
    margin-top: 20px;
  }
  .post .post-description .stats .stat-item {
    display: inline-block;
    margin-right: 15px;
  }
  .post .post-description .stats .stat-item .icon {
    margin-right: 8px;
  }


  .fluid-width-video-wrapper {
      width: 100%;
      position: relative;
      padding: 0;
  }

  .fluid-width-video-wrapper iframe, .fluid-width-video-wrapper object, .fluid-width-video-wrapper embed {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
  }
</style>
