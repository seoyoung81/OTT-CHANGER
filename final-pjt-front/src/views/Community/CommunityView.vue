<template>
  <div>
    <h1>Community</h1><br>
    <hr style="width: 80px; height: 2px; margin: auto; background-color: #ffe4ff;"><br>

    <!-- 글쓰기 버튼 -->
    <router-link to="/create">
      <button type="button" class="custom-button">
        글쓰기
      </button>
    </router-link>
    <br><br>
    
    <!-- 글 -->
    <ArticleList/>

    <router-view/>
  </div>
</template>

<script>
import ArticleList from '@/components/Community/ArticleList'

export default {
  name: 'CommunityView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getArticles()
    // console.log(this.$store.state.articles)
  },
  methods: {
    getComments() {
      this.$store.dispatch('getComments')
    },
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
        this.getComments()
      } else {
        alert('로그인이 필요한 페이지입니다')
        this.$router.push({ name: 'LogInView' })
      }
      // 로그인이 되어 있으면 getArticles action 실행
      // 로그인 X라면 login 페이지로 이동
    },
  }
}
</script>

<style>
.custom-button {
    background-color: #FF4081;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    cursor: pointer;
    float: right;
    margin-right: 90px;
  }

  .custom-button .button-text {
      font-size: 18px;
  }

</style>