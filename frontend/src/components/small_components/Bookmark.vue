<template>
  <div>
      <div v-if="bookmarkstate != null">
          bookmarked!!
          <v-else>
              Not bookmarked!!
          </v-else>
          </div>
          
      <button @click.prevent="bookmark">bookmark</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    props:['post'],
    data(){
        return {
            bookmarkstate:null
        }
    },
    created(){

    },
    methods: {

        bookmark(){
            const fd = new FormData();
            fd.append('username',this.$store.state.username);
            fd.append('id',this.post);

            axios.post(`http://127.0.0.1:8000/api/v2/bookmark/`,fd)
            .then(response=>{
                this.bookmarkstate = response.data;
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