<template>
  <div>
    <h1>Comment List</h1>
    <CommentItem
      v-for="(comment, idx) in comment_set"
      :key="comment.id"
      :comment="comment"
      :idx="idx"
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
  },
  computed: {
    
}}
</script>

<style>

</style>



