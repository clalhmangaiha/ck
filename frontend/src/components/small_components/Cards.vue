<template>
  <div class="card" style="width: 18rem;">
  <img v-bind:src="'http://127.0.0.1:8000'+coverimage" class="card-img-top" alt="...">
  <div class="card-body">
     
    <h5 class="card-title">{{title}}</h5>
    <p class="card-text"></p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
</template>

<script>
export default {
props :[
    'title','coverimage'
],
}
</script>

<style>

</style>