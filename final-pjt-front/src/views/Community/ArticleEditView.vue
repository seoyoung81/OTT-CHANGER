<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle" class="article-form-container">
      
      <div class="align-edit">
        <label for="title">제목</label>
        <input type="text" id="title" v-model.trim="title"><br>
      </div>
      
      <div class="align-edit">
        <label for="content">내용</label>
        <textarea id="content" cols="66" rows="10" v-model="content"></textarea><br>
      </div>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleEditView',
  // props: {
  //   article: Object
  // },
  data() {
    return {
      title: null,
      content: null,
      user: null,
      articleId: null,
    }
  },
  created(){
    this.articleId = this.$route.params.articleId
    this.getArticleDetail()
    // console.log(articleId)
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.articleId}/`,
        params: {},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((response) => {
        // console.log('Axios request Successful')
        // console.log(response)
        // console.log(response.data.comment_set)
        // this.article = response.data
        console.log(response.data)
        this.title = response.data.title
        this.content = response.data.content
        this.user = response.data.user
        // console.log(this.title)
        // console.log(this.content)
        // console.log(this.user)
        // this.title = 
        // console.log(this.article)
      })
    },
    updateArticle() {
      const title = this.title
      const content = this.content
      const user = this.user
      console.log('업데이트 시작합니다', user)

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/${this.articleId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        params: {},
        data: { title, content, user},
      })
      .then(() => {
        // console.log(response)
        this.$router.push({name: 'ArticleDetailView', params: { articleId: this.articleId } })
        console.log(this.content)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
.form-edit-container {
  padding-top: 20px;
}

</style>