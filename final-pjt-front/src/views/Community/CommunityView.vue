<template>
  <div>
    <h1>Community</h1>
    <router-link to="/create"><button type="button" class="btn btn-outline-primary">글쓰기</button></router-link>
    <ArticleList/>
    <span class="bottom-0 end-0">
    </span>
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
  },
  methods: {
    getComments() {
      this.$store.dispatch('getComments')
    },
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
        this.$store.dispatch('getUserInfo')
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

</style>