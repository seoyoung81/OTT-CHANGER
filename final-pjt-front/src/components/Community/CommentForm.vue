<template>
  <div>
    <br>
    <h1>댓글 작성</h1>
    <form @submit.prevent="createComment">
      <label for="content"></label>
      <textarea id="content" cols="30" v-model="content"></textarea><br>
      <button type="submit" id="submit" class="btn btn-outline-primary">댓글 쓰기</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: null,
      user: null,
    }
  },
  props: {
    id: Number,
  },
  methods: {
    createComment() {
      const content = this.content
      const user = this.$store.state.user.id
      const comment = {
        content: content,
        article: this.id
      }
      if (!comment.content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.id}/comments/`,
        data: { content, user },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((response) => {
        console.log(response)
        this.$emit('receive-new-comment', comment)
        this.content = ''
        this.$router.go(0)
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