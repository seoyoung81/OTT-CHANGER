<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleForm',
  data() {
    return {
      title: null,
      content: null,
      user: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const user = this.$store.state.user.id
      // console.log('넌 어디서 찍히는 아이니??', user)

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: { title, content, user},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then(() => {
        // console.log(response)
        this.$router.push({name: 'CommunityView'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>