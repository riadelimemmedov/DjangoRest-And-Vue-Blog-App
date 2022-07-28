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

          <form @submit.prevent="submitRegisterForm" method="POST">
            <div class="form-row">
              <div class="col form-group">
                <label>First name</label>
                <input @blur="$v.username.$touch()" v-model="username" :class="{'is-invalid':$v.username.$error}" type="text"  class="form-control" placeholder="First Name" required/>
              </div>
              <!-- form-group end.// -->
            </div>
            <!-- form-row end.// -->
            <div class="form-row">
              <div class="form-group col-md-6">
                <label>Create password</label>
                <input class="form-control" v-model="password" type="password" placeholder="Password" required/>
              </div>
              <!-- form-group end.// -->
              <div class="form-group col-md-6">
                <label>Repeat password</label>
                <input class="form-control" v-model="repassword" type="password" placeholder="Repassword" required/>
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
      <br /><br />
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
        username: '',
        password: '',
        repassword: '',
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
        }
      }
    },
    validations:{
        username:{
          required,
          minLength:minLength(5),
          maxLength:maxLength(10)
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
          sameAs:sameAs(this.password)
        },
    },
    mounted() {
      window.document.title = 'Sign Up'
    },
  };
</script>

<style></style>
