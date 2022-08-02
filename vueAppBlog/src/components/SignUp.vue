<template>
  <div class="page-sign-up">
    <section class="section-content padding-y">
      <!-- ============================ COMPONENT REGISTER   ================================= -->
      <div class="card mx-auto" style="max-width:520px; margin-top:40px;">
        <article class="card-body">
          <header class="mb-4"><h4 class="card-title">Sign up</h4></header>

        <div class="alert alert-danger" v-if="errors.length">
          <strong v-for="error in errors" :key="error">{{error}}</strong>
        </div>

          <form @submit.prevent="submitRegisterForm" method="POST" autocomplete="off">
            <div class="form-row">
              <div class="col form-group">
                <label>First name</label>
                <input @blur="$v.username.$touch()" v-model="username" :class="{'is-invalid':$v.username.$error}" type="text"  class="form-control" placeholder="First Name" required/>
                <small v-if="!$v.username.required" class="form-text text-danger font-weight-bold">This field required input data</small>
                <small v-if="!$v.username.maxLength" class="form-text text-danger font-weight-bold">Limited input 15 character</small>
                <small v-if="!$v.username.minLength" class="form-text text-danger font-weight-bold">Minimum input 3 character</small>
              </div>
              <!-- form-group end.// -->
            </div>
            <!-- form-row end.// -->
            <div class="form-row">
              <div class="form-group col-md-6">
                <label>Create password</label>
                <input @input="$v.password.touch()" v-model="password" class="form-control" type="password" placeholder="Password" required/>
                <small v-if="!$v.password.required" class="form-text text-danger font-weight-bold">This field required input data</small>
                <small v-if="!$v.password.maxLength" class="form-text text-danger font-weight-bold">Limited input 12 character</small>
                <small v-if="!$v.password.minLength" class="form-text text-danger font-weight-bold">Minimum input 8 character</small>


              </div>
              <!-- form-group end.// -->
              <div class="form-group col-md-6">
                <label>Repeat password</label>
                <input @input="$v.repassword.touch()" v-model="repassword" class="form-control" type="password" placeholder="Repassword" required/>
                <small v-if="!$v.repassword.required" class="form-text text-danger font-weight-bold">This field required input data</small>
                <small v-if="!$v.repassword.maxLength" class="form-text text-danger font-weight-bold">Limited input 12 character</small>
                <small v-if="!$v.repassword.minLength" class="form-text text-danger font-weight-bold">Minimum input 8 character</small>
                <small v-if="!$v.repassword.sameAsPassword" class="form-text text-danger font-weight-bold">Password not match</small>
              </div>
              <!-- form-group end.// -->
            </div>
            <div class="form-group">
              <button type="submit" class="btn btn-primary btn-block">
                Sign Up
              </button>
            </div>
            <!-- form-group// -->
          </form>
        </article>
        <!-- card-body.// -->
      </div>
      <!-- card .// -->
      <p class="text-center mt-4">Have an account?
        <router-link :to="{name:'login'}">Login</router-link>
      </p>
      <br/><br />
      <!-- ============================ COMPONENT REGISTER  END.// ================================= -->
    </section>
  </div>
</template>

<script>
  import axios from 'axios'
  import {toast} from 'bulma-toast'
  import {required,email,numeric,minLength,maxLength,sameAs,between} from 'vuelidate/lib/validators'


  export default {
    data() {
      return {
        username: null,
        password: null,
        repassword: null,
        errors: []
      }
    },
    methods:{
      submitRegisterForm(){
        if(this.username !=null && this.password !=null && this.repassword !=null){//if entered all form data
          const formData = {
            username:this.username,
            password:this.password
          }
          //Axios post request back to the server
          axios.post('api/v1/users/',formData)
            .then((response)=>{
              toast({
                message:"Account created successfully,please login",
                type:'is-success',
                dismissible:true,
                pauseOnHover:true,
                duration:2000,
                position:'bottom-right',
              })
              this.$router.push({name:'login'})
            })
            .catch((err)=>{
              if(err.response){
                for(const error in err.response.data){
                  this.errors.push(`${error} : ${err.response.data[error]}`)
                }
                console.log(JSON.stringify(err.response.data))
              }
              else{
                this.errors.push('Something went wrong.Please try again')
                this.$router.push({name:'sign-up'})
                console.log(JSON.stringify(err))
              }
            })
        }
      }
    },
    validations:{
        username:{
          required,
          minLength:minLength(3),
          maxLength:maxLength(15)
        },
        password:{
          required,
          minLength:minLength(6),
          maxLength:maxLength(12)
        },
        repassword:{
          required,
          minLength:minLength(6),
          maxLength:maxLength(12),
          sameAsPassword:sameAs('password')
        },
    },
    mounted() {
      window.document.title = 'Sign Up'
    },
  };
</script>

<style></style>
