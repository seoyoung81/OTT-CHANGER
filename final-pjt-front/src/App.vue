<template>
  <div id="app" class="bg-dark bg-gradient">
    <nav>
      <router-link to="/signup">Sign Up</router-link> |
      <router-link to="/login" >Log In</router-link> |
      <!-- v-if="!`${this.$store.getters.isLogin}`" -->
      <router-link to="/community">Community</router-link>
    </nav>
    <router-view/>
    <MainView/>
  </div>
</template>

<script>
import MainView from '@/components/Movie/MainView'
export default {
    name: 'IntroView',
    components: {
      MainView
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
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
