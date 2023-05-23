<template>
  <div>
    <div class="comments-align">
      <span><span>{{ idx + 1 }}&nbsp;&nbsp; &nbsp;</span>{{ comment.content }}</span>&nbsp;&nbsp;&nbsp;&nbsp;
      <div class="hover-effect-delete">
        <img src="@/assets/delete.png" @click="deleteComment" style="width: 30px;">
      </div>
    </div>
    <hr style="width: 80vw; margin-left: 10%;">
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
  created() {
    console.log('created',this.article_id)
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
.hover-effect-delete img {
  width: 30px;
  transition: filter 0.3s ease-in-out; /* Adding a smooth transition effect */
}

.hover-effect-delete img:hover {
  filter: brightness(70%); /* Adjust the brightness value to change the color effect */
}

.comments-align {
  display: flex;
    justify-content: center;
    align-items: center;
  
}

</style>