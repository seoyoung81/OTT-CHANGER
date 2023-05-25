<template>
  <div>
    <h1>Sign Up</h1><br>
    <form @submit.prevent="signUp" class="form-container">
      <div class="align">
        <label for="email">Email</label>&nbsp;&nbsp;
        <input type="text" id="email" v-model="email"><br>
      </div>
      
      <div class="align">
        <label for="username">Username</label>&nbsp;&nbsp;
        <input type="text" id="username" v-model="username"><br>
      </div>

      <div class="align">
        <label for="password1"> Password</label>&nbsp;&nbsp;
        <input type="password" id="password1" v-model="password1"><br>
      </div>

      <div class="align">
        <label for="password2"> Password Confirmation</label>&nbsp;&nbsp;
        <input type="password" id="password2" v-model="password2">
      </div>
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      email: null,
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const email = this.email
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, email, password1, password2
      }
      console.log(payload)
      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>
.form-container {
  width: 400px;
  margin: 0 auto;
  
}

.align {
  display: flex;
  align-items: center;
}

.align label {
  width: 120px;
  text-align: right;
  margin-right: 10px;
}

.align input[type="text"],
.align input[type="password"] {
  flex: 1;
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 10px;
}

input[type="submit"] {
  float: right;
  padding: 10px 15px;
  background-color: #FF4081;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
 
}

input[type="submit"]:hover {
  background-color: #ff4080bd;
 
}

label {
  display: inline-block;
  width: 120px;
  text-align: right;
  margin-right: 10px;
}




</style>