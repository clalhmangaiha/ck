import Vue from 'vue'
import App from './App.vue'
import router from './routes'
import axios from 'axios'
import VueAxios from 'vue-axios'

import VueRouter from 'vue-router'
import CKEditor from '@ckeditor/ckeditor5-vue2';


Vue.use(VueRouter)
Vue.config.productionTip = false
Vue.use(VueAxios,axios)
Vue.use( CKEditor );

new Vue({
  render: h => h(App),
  router,
  
}).$mount('#app')

// const app =new Vue({
//   App,
//   router
// }).$mount('#app')