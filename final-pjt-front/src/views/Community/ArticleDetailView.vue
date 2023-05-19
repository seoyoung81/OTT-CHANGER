<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>작성자 : {{ article?.username }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <router-link :to="{ name: 'ArticleEditView', query: { articleId: article.id } }">
      <button class="btn btn-outline-primary">수정하기</button>
    </router-link>
    <router-view/>
    <button @click="deleteArticle" class="btn btn-outline-primary">삭제하기</button><br><br>
    <button @click="backArticle" class="btn btn-outline-primary">목록보기</button>
    <CommentForm :id="article.id" @receive-new-comment="newComment"/>
    <CommentList :comment_set="comment_set" :article_id="article_id" />
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/Community/CommentList.vue'
import CommentForm from '@/components/Community/CommentForm.vue'
// import ArticleEditView from '@/components/Community/ArticleEditView.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  components: {
    CommentList,
    CommentForm,
    // ArticleEditView,
  },
  data() {
    return {
      article: null,
      comment_set : [],
      article_id: null,
      user: null,
    }
  },
  created() {
    // console.log('Article Detail View Created')
    this.getArticleDetail()
    // console.log('아티클 디테일 정보랑 토큰 ::::::::', this.$store.state.token)
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        params: {},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((response) => {
        // console.log('Axios request Successful')
        // console.log(response)
        // console.log(response.data.comment_set)
        this.article = response.data
        // console.log(this.article)
        console.log(response.data)
        this.comment_set = response.data.comment_set
        this.article_id = response.data.id

      })
    },
    backArticle() {
      this.$router.push({name: 'CommunityView'})
    },
    newComment(newcomment) {
      this.comment_set.push(newcomment)
    },
    deleteArticle() {
      const user = this.$store.state.user.id
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        params: {},
        data: { user },
      })
      .then((response) => {
        console.log('삭제 응답 ::::::', response)
        this.$router.push({name: 'CommunityView'})
      })
      .catch((error) => {
        console.log(error)
      })
    },
  }
}
</script>

<style>

</style>