<template>
  <div id="app">
    <nav style="margin-left: 10%;">
      <router-link v-if="isLogin" to="/main">Main |</router-link>
      <router-link to="/community">
        <img src="@/assets/community.png" style="width: 110px;">
        <!-- 커뮤니티 다시 -->
      </router-link>
      <router-link v-if="isLogin" to="/ott"> OTT Changer |</router-link>
      <router-link v-if="isLogin" :to="{name: 'MyPageView', params: { id: loggedin_user_id}}"><img src="@/assets/MyPage_logo02.png"
        style="width: 110px; margin: 10px; position: sticky; right: 10px; z-index: 999;" class="mypage-img"></router-link>

      <router-link to="/signup"> Sign Up | </router-link>
      <router-link to="/login" >Log In</router-link>


      <button v-if="isLogin" @click="logOut" class="logout-btn">Log Out</button>
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
      console.log(this.isLogin)
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

.logout-btn {
  background-color: #50555E;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  float: right;
  

}

.logout-btn .button-text {
    font-size: 18px;
}

.mypage-img:hover {
  filter: brightness(70%);
}



</style>
