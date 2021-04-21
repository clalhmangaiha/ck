<template>
<div>
    <p>Username</p>
  <input type="text" v-model="username"/>
  <input type="password" v-model="password"/>
  <p>Password</p>
  <button @click.prevent="logging">Login</button>
  </div>
</template>

<script>
// import axios from "axios";
import store from '../../store';

export default {
    data(){
        return{
            
            username:'admin',
            password:'admin'
            
        }
    },
    methods:{
        logging(){
            store.dispatch('obtainToken',{username:this.username,password:this.password})
            .then(() =>{
                // this.$router.push({path:'/'});
                // console.log(response)
                // console.log("In dispatch username",this.username,"password",this.password)
            })
            .catch(error=>{
                console.log(error);
            })
        }
    }

}
</script>

<style>

</style>