<template>
<div>
    <div class="form-gorup">
    <button v-on:click="deletePost" >Delete</button>

    </div>
    <p>{{post}}</p>
</div>
  
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            post:{}
        }

    },
    methods:{
        deletePost(){
            axios.delete(`http://127.0.0.1:8000/api/v2/delete/`+this.post.id)
            .then(() =>{
                this.$router.push({path:'/'})
            })
            .catch(error=>
            {
                console.log(error)
            })
        }
    },
    created(){
        axios.get(`http://127.0.0.1:8000/api/v2/`+ this.$route.params.slug)
        .then(response =>{
            this.post = response.data

        })
        .catch(error =>
        console.log(error))
    }


}
</script>

<style>

</style>