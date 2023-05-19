<template>
  <div id="app">
    <nav>
      <router-link to="/main">Main</router-link> | 
      <router-link to="/signup">Sign Up</router-link> | 
      <router-link to="/login" >|  Log In</router-link> |
      <!-- v-if="!`${this.$store.getters.isLogin}`" -->
      <router-link to="/community">Community</router-link>
      <!-- <button v-if="$store.state.isLogin" @click="logOut">로그아웃</button> -->
    </nav>
    <router-view/>
   
  </div>
</template>

<script>
export default {
    name: 'IntroView',
    components: {
      
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
  color: #000000;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}


</style>
