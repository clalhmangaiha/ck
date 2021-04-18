<template>
  <div class="container">
      <div class="row" v-for="post ,index in posts" :key="index">

          <div class="col">
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
            posts:{}
        }
    },
    components:{Cards, },
    created(){
        axios.get(`http://127.0.0.1:8000/api/v2`)
        .then(response =>{
            this.posts = response.data;
        })
        .catch(error=>{
            console.log(error)
        })
    }


}
</script>

<style>

</style>