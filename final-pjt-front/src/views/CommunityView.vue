<template>
  <div>
    <h1>Community Page</h1>
    <ArticleForm/>
    <ArticleList/>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm'
import ArticleList from '@/components/ArticleList'

export default {
  name: 'CommunityView',
  components: {
    ArticleForm,
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
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
        console.log('들어간다~~')
      } else {
        alert('로그인이 필요한 페이지입니다')
        this.$router.push({ name: 'LogInView' })
      }


      // 로그인이 되어 있으면 getArticles action 실행
      // 로그인 X라면 login 페이지로 이동

    }
  }
}
</script>

<style>

</style>