<template>
  <div>
    <h1>내가 작성한 게시글</h1>
    <MyArticlesItem
    v-for="(article, idx) in my_articles"
    :key="idx"
    :article="article"/>
  </div>
</template>

<script>
import axios from 'axios'
import MyArticlesItem from '@/components/MyPage/MyArticlesItem'

export default {
    name: 'MyArticlesList',
    components: {
        MyArticlesItem
    },
    data() {
        return {
            my_articles: []
        }
    },
    mounted() {
        console.log('MyArticleList',this.$route.params.user_id)
        console.log('MyArticleList',this.$store.state.user.id)
        this.$route.params.user_id = this.$store.state.user.id
        axios({
            method: 'get',
            url: `http://127.0.0.1:8000/api/v1/articles/my_articles/${this.$route.params.user_id}/`,
            params : {}
        })
        .then((response) => {
            console.log(response)
            this.my_articles = response.data
            console.log(this.my_articles)
        })
        .catch((error) => {
            console.log(error)
        })
    }
}
</script>

<style>

</style>