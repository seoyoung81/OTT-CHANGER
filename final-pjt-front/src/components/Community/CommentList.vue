<template>
  <div>
    <br><br><br>
    <h1>Comment List</h1>
    <CommentItem
      v-for="(comment, idx) in comment_set"
      :key="comment?.id"
      :comment="comment"
      :idx="idx"
      :article_id="article_id"
      :comment_id="comment.id"
      @reload-comment="reloadComment"
    />
  </div>
</template>

<script>
import CommentItem from '@/components/Community/CommentItem.vue'
export default {
  name: 'CommentList',
  components: {
    CommentItem
  },
  props: {
    comment_set: [],
    article_id: Number,
  },
  computed: {
    
},
  methods: {
    reloadComment() {
      this.$router.go(0)
    }
  }
}
</script>

<style>

</style>



