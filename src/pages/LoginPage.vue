<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <div align="center">
        <q-toolbar>
          <q-toolbar-title> Welcome! </q-toolbar-title>
        </q-toolbar>
      </div>
    </q-header>

    <q-page-container>
      <q-card class="my-card">
        <q-card-actions vertical align="center">
         
          <q-input outlined v-model="email" type="email" label="Enter email" />
          <q-separator/>
          <q-input outlined v-model="password" type="password" label="Enter password" />
          <q-separator/>
        
          <q-btn type="submit" color="secondary" @click="onClick()" label="login"/>
          
        </q-card-actions>
      </q-card>
    </q-page-container>
  </q-layout>
</template>

<script>
import {useRouter} from 'vue-router';
import {ref} from 'vue';
  export default{
    setup(){
      return{
        email: ref(''),
        password: ref(''),
        router:useRouter(),
      }
    },
  
    methods:{
      reset(){
        this.email = '';
        this.password = '';
      },

      onClick(){
        if(this.email == "abc" && this.password=="pass" ){
          this.router.push('/')
        }
        else{
          alert("Enter Valid Mail and Password !!")
          this.reset();
        }
      }
    }
  }
</script>
