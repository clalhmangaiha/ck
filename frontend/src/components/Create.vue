<template>
  <div>
      <form @submit.prevent="CreatePost">
      <input  type="text" v-model="title" /> 
      <input style="display:none" type="file" @change="onFileSelected" ref="fileinputting">

      <button @click="$refs.fileinputting.click()">Pick File </button>


    <!-- <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor> -->
    <button type="submit">Post</button>
        </form>
  </div>
</template>

<script>
// import CKEditor from '@ckeditor/ckeditor5-vue2';
// import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import axios from 'axios'

    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export default {
  components: {
            // Use the <ckeditor> component in this view.
            // ckeditor: CKEditor.component
        },
        data() {
            return {
                title:null,
                newtitle:"",
                coverimage:null,
               
                // editor: ClassicEditor,
                // editorData: {},
                // editorConfig: {
                //     // The configuration of the editor.
                // }

                // ...
            };
        },
        methods:{
          
            CreatePost(){
                const fd = new FormData();
                fd.append('coverimage',this.coverimage,this.coverimage.name);
                fd.append('title',this.title);

                axios.post(`http://127.0.0.1:8000/api/v2/create/`,
                // {
                //         data:fd,
                //         title:this.title,
                       
                    
                // }
                fd,{ headers: { 'Content-Type': 'multipart/form-data' },},
                
                )
                    .then(() =>{
                       
                  
                    })
                .catch(error=>{
                    console.log(error)
                });
            },
            onFileSelected(event){
                this.coverimage=event.target.files[0]
            },
            
        }

}
</script>

<style>

</style>