<template>
  <div id="app">
    <nav>
      <router-link to="/main">Main</router-link> | 
      <router-link to="/signup">Sign Up</router-link> | 
      <router-link to="/login" >Log In</router-link> |
      <!-- v-if="!`${this.$store.getters.isLogin}`" -->
      <router-link to="/community">Community</router-link> |
      <!-- <button v-if="$store.state.isLogin" @click="logOut">로그아웃</button> -->
      <router-link to="/ott">OTT Changer</router-link>
      <br><br>
    </nav>
    <router-view/>
   
  </div>
</template>

<script>
export default {
    name: 'IntroView',
    components: {
      
    },
    data() {
      return {
        searchMovie: null
      }
    },
    methods: {
      logOut(){
        console.log('일단')
        this.$store.state.isLogin = false
        this.$router.go(0)
       
      },
      toMain(){
        this.$router.push({name:'MainView'})
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
  color: #ffffff;
}

nav a.router-link-exact-active {
  color: #2a73ac;
}

body {
  margin: 0;
  padding: 0;
  background-color: rgb(51, 51, 51);
}



</style>
