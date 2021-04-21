import Vue from 'vue'
import jwt_decode from  'jwt-decode'

import Vuex from 'vuex';
import axios from 'axios';
Vue.use(Vuex)

const store = new Vuex.Store({
    state:{
      jwt:localStorage.getItem('t'),
      username:'',
      endpoints:{
        obtainJWT:'http://127.0.0.1:8000/api/token/',
        refreshJWT:'http://127.0.0.1:8000/api/token/refresh'
      }
    },
  
    mutations:{
      updateToken(state,newToken){
        localStorage.setItem('t',newToken.token);
        state.jwt=newToken.token;
        state.username =newToken.username
        localStorage.setItem('username',newToken.username);
      },
      removeToken(state){
        localStorage.removeItem('t');
        state.jwt=null;
      }
    },
  
    actions:{
  
      obtainToken(context,credentials){
        const payload = {
          username:credentials.username,
          password:credentials.password
        }
        console.log("HELLO username",payload.username,"HELLO 2",payload.password);
        axios.post(this.state.endpoints.obtainJWT,payload)
        .then(response =>{
          this.commit('updateToken',{token:response.data.access,username:payload.username});
        //   console.log("this went through")
        })
        .catch(error =>{
          console.log(error);
        })
      },
  
      refreshToken(){
        const payload = {
          token:this.state.jwt
        }
  
        axios.post(this.state.endpoints.refreshJWT,payload)
        .then(response =>{
          this.commit('updateToken',response.data.token)
        })
        .catch(error =>{
          console.log(error)
        })
      },
      inspectToken(){
        const token = this.state.jwt;
        if(token){
          const decoded = jwt_decode(token);
          const exp = decoded.exp
          const orig_iat = decoded.orig_iat
          if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200){
            this.dispatch('refreshToken')
          } else if (exp -(Date.now()/1000) < 1800){
            // DO NOTHING, DO NOT REFRESH          
          } else {
            // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
          }
        }
      }
  
    }
  })

  export default store;