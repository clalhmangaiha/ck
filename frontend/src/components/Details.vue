<template>
<div>
    <div class="form-gorup">
    <button v-on:click="deletePost" >Delete</button>
<Bookmark :post="post.id"></Bookmark>
    </div>
    <p>{{post.title}}</p>
    <p>{{post.Author}}</p>

    <p>{{post.intro}}</p>
    <div v-html="content"></div>
    <p>{{post.category}}</p>
    <p>{{post.tags}}</p>

</div>
  
</template>

<script>
import Bookmark from './small_components/Bookmark'
import axios from 'axios'
export default {
    components: {Bookmark},
    data(){
        return{
            post:{},
            content:''
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
            this.content = response.data.content

        })
        .catch(error =>
        console.log(error))
    }


}
</script>

<style>

</style>