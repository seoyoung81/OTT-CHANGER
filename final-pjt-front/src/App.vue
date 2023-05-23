<template>
  <div id="app">
    <nav >
      <router-link v-if="isLogin" to="/main">Main</router-link>
      <router-link v-if="!isLogin" to="/signup">Sign Up | </router-link>
      <router-link v-if="!isLogin" to="/login" >Log In</router-link>
      <router-link to="/community">Community</router-link>
      <router-link v-if="isLogin" to="/ott">OTT Changer</router-link>
      <router-link v-if="isLogin" :to="{name: 'MyPageView', params: { id: loggedin_user_id}}">MyPage</router-link>
      <button v-if="isLogin" @click="logOut">Log Out</button>
      <br><br>
    </nav>
    <router-view/>
   
  </div>
</template>

<script>
export default {
    name: 'AppView',
    components: {
    },
    data() {
      return {
        searchMovie: null,
        loggedin_user_id : null,
      }
    },
    computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
      }
    },
    created() {
      // console.log(this.isLogin)
      // console.log(this.$store.state.token)
      this.loggedin_user_id = this.$store.state.user.id
      // console.log(this.loggedin_user_id)

      // const path = '/main'
      // if (this.$route.path != path) {
      //   this.$router.push({name:'MainView'})
      // }
    },
    methods: {
      logOut(){
        this.$store.dispatch('logOut')
      },
    }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #e0e0e0;
}

nav a.router-link-exact-active {
  color: #61dafb;
}

body {
  margin: 0;
  padding: 0;
  background-color: #282c34;
}



</style>
