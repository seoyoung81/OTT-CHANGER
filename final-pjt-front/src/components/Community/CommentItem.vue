<template>
  <div>
    
    <p><span>{{ idx + 1 }}    </span>{{ comment?.content }}</p>
    <button v-if="isCommentAuthor" @click="deleteComment" class="btn btn-outline-success">삭제하기</button>
    
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
  data() {
    return {
      isCommentAuthor : false,
    }
  },
  created() {
    console.log('created',this.article_id)
    console.log(this.comment.user)
    if (this.$store.state.user.id === this.comment.user) {
      this.isCommentAuthor = true
    }
    console.log(this.isCommentAuthor)
  },
  methods: {
    deleteComment() {
      
      console.log('일단 들어와')
      console.log(this.comment.id)
      const user = this.$store.state.user.id
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/comments/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        params: {},
        data: { user },
      })
      .then(() => {
        this.$emit('reload-comment')
        console.log(this.article_id)
        this.$router.push({name: 'ArticleDetailView', params: { articleId: this.article_id }})
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