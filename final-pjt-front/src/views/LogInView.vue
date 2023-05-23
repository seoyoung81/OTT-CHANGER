<template>
  <div>
    <h1>LogIn Page</h1><br>
    <form @submit.prevent="login" class="form-container">
    <div class="align">
      <label for="username">Username</label>
      <input type="text" id="username" v-model="username"><br>
    </div>

    <div class="align">
      <label for="password">Password</label>
      <input type="password" id="password" v-model="password"><br>
    </div>
    <input type="submit" value="logIn">
  </form>
    
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('logIn', payload)

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

.align input[type="text"]{
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
