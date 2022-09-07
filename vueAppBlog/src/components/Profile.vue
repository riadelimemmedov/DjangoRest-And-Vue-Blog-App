<template>
    <div class="container-xl px-4 mt-5">
      <hr class="mt-0 mb-4">
        <div class="alert alert-dismissible fade show" :class="isAlert ? 'alert-success' : 'alert-danger'" role="alert" id="alert-box" v-if="isAlert">
            <strong v-if="isAlert">Successfully Update Profile Information</strong>
            <strong v-else>Failed to Update Profile Information</strong>
            <button type="button" class="close" data-dismiss="alert" aria-label="Close" @click="closeAlert()">
              <span aria-hidden="true">&times;</span>
            </button>
        </div>
      <div class="row">
          <div class="col-xl-4">
              <!-- Profile picture card-->
              <div class="card mb-4 mb-xl-0">
                  <div class="card-header">Profile Picture</div>
                  <div class="card-body text-center">
                      <img class="img-account-profile rounded border shadow mb-2" :src="`http://127.0.0.1:8000${image_url}`" alt="">
                  </div>
              </div>
          </div>
          <div class="col-xl-8">
              <!-- Account details card-->
              <div class="card mb-4">
                  <div class="card-header">Account Details</div>
                  <div class="card-body">
                      <form method="POST" @submit.prevent="updateProfile">
                          <!-- Form Group (username)-->
                          <div class="mb-3">
                              <label class="small mb-1" for="inputUsername">Username</label>
                              <input class="form-control read only" v-model="username" id="inputUsername" type="text" placeholder="Enter your username" :readonly="isDisabled" disabled>
                          </div>
                          <!-- Form Row-->
                          <div class="row gx-3 mb-3">
                              <!-- Form Group (first name)-->
                              <div class="col-md-6">
                                  <label class="small mb-1" for="inputFirstName">First name</label>
                                  <input class="form-control" v-model="first_name" id="inputFirstName" @keyup="changeEventTrigger" type="text" placeholder="Enter your first name">
                              </div>
                              <!-- Form Group (last name)-->
                              <div class="col-md-6">
                                  <label class="small mb-1" for="inputLastName">Last name</label>
                                  <input class="form-control" id="inputLastName" @keyup="changeEventTrigger" v-model="last_name" type="text" placeholder="Enter your last name">
                              </div>
                          </div>
                          <!-- Form Row        -->
                          <div class="row gx-3 mb-3">
                              <!-- Form Group (organization name)-->
                              <div class="col-md-6">
                                  <label class="small mb-1" for="inputOrgName">Organization name</label>
                                  <input class="form-control" id="inputOrgName" @keyup="changeEventTrigger" v-model="organization_name" type="text" placeholder="Enter your organization name">
                              </div>
                              <!-- Form Group (location)-->
                              <div class="col-md-6">
                                  <label class="small mb-1" for="inputLocation">Location</label>
                                  <input class="form-control" v-model="location" @keyup="changeEventTrigger" id="inputLocation" type="text" placeholder="Enter your location">
                              </div>
                          </div>
                          <!-- Form Group (email address)-->
                          <div class="mb-3">
                              <label class="small mb-1" for="inputEmailAddress">Email address</label>
                              <input class="form-control" v-model="email" @keyup="changeEventTrigger" id="inputEmailAddress" type="email" placeholder="Enter your email address">
                          </div>
                          <!-- Form Row-->
                          <div class="row gx-3 mb-3">
                              <!-- Form Group (phone number)-->
                              <!-- Form Group (birthday)-->
                              <div class="col-md-12">
                                  <label class="small mb-1" for="inputBio">Bio</label>
                                  <textarea class="form-control" v-model="bio" @keyup="changeEventTrigger" id="inputBio" rows="4" placeholder="Enter Your Bio"></textarea>
                              </div>
                          </div>
                          <!-- Save changes button-->
                          <button class="btn btn-primary disabled" id="updateButton" type="button">Save changes</button>
                      </form>
                  </div>
              </div>
          </div>
      </div>
  </div>
</template>

<script>

    import PictureInput from 'vue-picture-input'
    import axios from 'axios'

    export default{
      name: 'app',
        data () {
          return {
            isDisabled:false,
            isAlert:false,
            user_slug:'',
            username:'',
            first_name:'',
            last_name:'',
            organization_name:'',
            location:'',
            email:'',
            bio:'',
            image_url:''
          }
        },
        components: {
          PictureInput
        },
        methods: {
          getProfileData(){
            axios({
              method:'GET',
              url:`update/profile/${this.user_slug}`,
            })
            .then((response) => {
              console.log('respose value from profile ', response.data)
              this.username = response.data.user
              this.first_name = response.data.firstname
              this.last_name = response.data.lastname
              this.organization_name = response.data.organization_name
              this.location = response.data.location
              this.email = response.data.email_address
              this.bio = response.data.bio
              this.image_url = response.data.profile_picture
              console.log('Successfully return profile','nice')
            })
            .catch((err)=>{
              console.log('Error return user ', err)
            })
          },
          updateProfile(){
            this.isDisabled = true
            axios({
              method:'POST',
              url:`update/profile/${this.user_slug}/`,
              data:JSON.stringify({
                "firstname":this.first_name,
                "lastname":this.last_name,
                "email_address":this.email,
                "organization_name":this.organization_name,
                "location":this.location,
                "bio":this.bio,
              }),
              headers:{
                  'Content-Type': 'application/json'
              }
            }).
            then((response)=>{
              this.isAlert = null
              this.isAlert = response.data.success
              document.querySelector('#updateButton').classList.add('disabled')
            })
            .catch((err)=>{
              console.log('When updated profile encount error ', err)
              this.isAlert = false
            })
          },
          closeAlert(){
            document.getElementById('alert-box').hidden = true
            this.isAlert = false
          },
          changeEventTrigger(){
            document.querySelector('#updateButton').classList.remove('disabled')
            document.querySelector('#updateButton').type='submit'
            console.log('changed input value ')
          },
        },
        created(){
          this.user_slug = window.location.href.split('/')[4]
          this.getProfileData()
        },
      }

</script>

<style>
  body{
    margin-top:20px;
    background-color:#f2f6fc;
    color:#69707a;
  }
  .img-account-profile {
      height: 10rem;
  }
  .rounded-circle {
      border-radius: 50% !important;
  }
  .card {
      box-shadow: 0 0.15rem 1.75rem 0 rgb(33 40 50 / 15%);
  }
  .card .card-header {
      font-weight: 500;
  }
  .card-header:first-child {
      border-radius: 0.35rem 0.35rem 0 0;
  }
  .card-header {
      padding: 1rem 1.35rem;
      margin-bottom: 0;
      background-color: rgba(33, 40, 50, 0.03);
      border-bottom: 1px solid rgba(33, 40, 50, 0.125);
  }
  .form-control, .dataTable-input {
      display: block;
      width: 100%;
      padding: 0.875rem 1.125rem;
      font-size: 0.875rem;
      font-weight: 400;
      line-height: 1;
      color: #69707a;
      background-color: #fff;
      background-clip: padding-box;
      border: 1px solid #c5ccd6;
      -webkit-appearance: none;
      -moz-appearance: none;
      appearance: none;
      border-radius: 0.35rem;
      transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  }

  .nav-borders .nav-link.active {
      color: #0061f2;
      border-bottom-color: #0061f2;
  }
  .nav-borders .nav-link {
      color: #69707a;
      border-bottom-width: 0.125rem;
      border-bottom-style: solid;
      border-bottom-color: transparent;
      padding-top: 0.5rem;
      padding-bottom: 0.5rem;
      padding-left: 0;
      padding-right: 0;
      margin-left: 1rem;
      margin-right: 1rem;
  }
</style>
