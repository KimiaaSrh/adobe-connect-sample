<template>
  <div class="login">
    <body>
      <h2>Login Page</h2><br>   
        <b-nav-form @submit.prevent="login" v-if="token==null">
          <label><b>User Name     
        </b>  
        </label>
        <hr>   
        <b-form-input id="Uname" size="sm" class="mr-sm-2" v-model="username" placeholder="username" name="username"></b-form-input>
        <br><br>    
        <label><b>Password     
        </b>    
        </label> 
        <hr>   
        <b-form-input id="Pass" size="sm" class="mr-sm-2" placeholder="password" type="password" v-model="password" name="password"></b-form-input>
        <!-- <hr><hr> -->
        <!-- <br> -->
        <b-button size="sm" class="my-2 my-sm-0" type="submit" id="log">Login</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="logout" v-if="token !== null">
          <b-button type="submit" size="sm" class="my-2 ml-2"> Logout</b-button>
        </b-nav-form>
        <br><br>    
        <input type="checkbox" id="check">    
        <span>Remember me</span>    
        <br><br>    
        Forgot <a href="#">Password</a>  
    </body>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'login',
  components: {

  },
  data() {
    return {
      username: '',
      password: '',
      token: localStorage.getItem('user-token') || null,
    }
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:8000/auth/', {
        username: this.username,
        password: this.password,
      })
      .then(resp => {

      this.token = resp.data.token;
      console.log(this.token)
    //   console.log("kar kard");
      localStorage.setItem('user-token', resp.data.token)
      })
      .catch(err => {
        localStorage.removeItem('user-token')
      })
    },
    logout() {
      localStorage.removeItem('user-token');
      this.token = null;
    },
    }
  }
</script>
<style  scoped>
span{  
    color: white;  
    font-size: 17px;  
}  
a{  
    float: right;  
    background-color: grey;  
} 
#log{  
    width: 100px;  
    height: 30px;  
    border: none; 
    /* margin-top: 17px;  */
    border-radius: 17px;  
    padding-left: 7px;  
    color: rgb(54, 4, 39);  
  
  
} 
h2{  
    text-align: center;  
    color: #277582;  
    padding: 20px;  
} 
body  
{  
    margin: 0;  
    padding: 0;  
    background-color:rgb(189, 147, 147);  
    font-family: 'Arial';  
}
#Uname{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
}  
#Pass{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
      
} 
.login{  
        width: 482px;  
        overflow: hidden;  
        margin: auto;  
        margin: 20 0 0 450px;  
        padding: 40px;  
        background: rgb(189, 147, 147);  
        border-radius: 15px ;  
          
} 
label{  
    color: #42135e;  
    font-size: 17px;  
}  
</style>