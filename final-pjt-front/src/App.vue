<template>
  <div id="app">
    <nav>
      <!-- main logo -->
      <router-link to="/main">
        <img src="@/assets/main_log2.png" style="width: 100px; float: left; margin-left: 5px;">
      </router-link>
      <!-- community -->
      <router-link to="/community" style="float: left; margin: 25px;">
        Community
      </router-link>

      <!-- ott changer -->
      <router-link v-if="isLogin" to="/ott" style="float: left; margin: 25px 0px"> OTT Changer</router-link>

      
      <!-- log in -->
      <router-link v-if="!isLogin" to="/login" style="float: right; margin: 25px;">Log In</router-link>
      
      <!-- log out -->
      <button v-else @click="logOut" class="logout-btn">Log Out</button>

      <!-- mypage -->
      <router-link v-if="isLogin" :to="{name: 'MyPageView', params: { id: $store.state.user.id }, query: { username: $store.state.user.username }}"><img src="@/assets/MyPage_logo02.png"
        style="width: 120px; float: right; margin: 25px 25px 10px 25px;" class="mypage-img">
      </router-link>

      <!-- sign up -->
      <router-link v-if="!isLogin" to="/signup" style="float: right; margin: 25px;"> Sign Up</router-link>



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
      // this.$store.dispatch('clearToken')
      // console.log(this.$store.state.token)

      // const path = '/main'
      // if (this.$route.path != path) {
      //   this.$router.push({name:'MainView'})
      // }
    },
    methods: {
      logOut(){
        this.$store.dispatch('logOut')
        console.log(this.$store.state.token)
        // const path = '/main'
        // if (this.$route.path !== path) {
        //   this.$router.push(path)
        // }
      }
    }
      // beforeRouteLeave(to, from, next) {
      //   if (to.name === 'MainView' && from.name === 'MainView') {
      //     // Prevent navigation duplication when leaving and returning to MainView
      //     next(false)
      //   } else {
      //     next()
      //   }
      // }
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
  text-decoration: none;
}

nav a {
  font-weight: bold;
  color: #e0e0e0;
  text-decoration: none;
  font-size: 24px;
}

nav a.router-link-exact-active {
  color: #ff4081;
}

body {
  margin: 0;
  padding: 0;
  background-color: #282c34;
}

.logout-btn {
  background-color: #50555E;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  float: right;
  margin: 15px;
  

}

.logout-btn .button-text {
    font-size: 18px;
}

.mypage-img:hover {
  filter: brightness(70%);
}



</style>
