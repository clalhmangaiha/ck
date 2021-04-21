<template>
  <div class="container mx-auto px-4">
<h1>Username:{{username}}</h1>
      <div class="" v-for="post ,index in posts" :key="index">

          <div class="  ">
              <router-link :to="'/detail/'+post.slug">
              <Cards :title='post.title' :coverimage='post.coverimage'></Cards>
              </router-link>
          </div>

          
      
      </div>
     
  </div>
</template>

<script>
import axios from 'axios'
import Cards from './small_components/Cards'
export default {
    data(){
        return{
            posts:{},
            username:this.$store.state.username
        }
    },
    components:{Cards, },
    created(){
        axios.get(`http://127.0.0.1:8000/api/v2`)
        .then(response =>{
            this.posts = response.data;
            console.log("STATE",this.$store.state.username);
        })
        .catch(error=>{
            console.log(error)
        })
    }


}
</script>

<style>

</style>