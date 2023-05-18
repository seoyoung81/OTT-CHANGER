<template>
  <div>
    
    <p><span>{{ idx + 1 }}    </span>{{ comment.content }}</p>
    <button @click="deleteComment">삭제하기</button>
    
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'CommentItem',
  props: {
    comment: Object,
    idx: Number,
    article_id: Number,
  },
  methods: {
    deleteComment() {
      console.log('일단 들어와')
      const user = this.$store.state.user.id
      this.$route.params.id = this.comment.id
      console.log(user)
      console.log(this.$route.params.id)
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/comments/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        params: {},
        data: { user },
      })
      .then((response) => {
        console.log('삭제 응답 ::::::', response)
        // this.$router.push({name: 'ArticleDetailView', params: {id: this.article_id}})
        this.$emit('reload-comment')
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