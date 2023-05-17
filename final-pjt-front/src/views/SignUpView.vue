<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="email">Email : </label>
      <input type="text" id="email" v-model="email"><br>

      <label for="username">Username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> Password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> Password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="signUp">
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