<template>
  <div>
    
    <p><span>{{ idx + 1 }}    </span>{{ comment.content }}</p>
    
    <hr>
  </div>
</template>

<script>
export default {
  name: 'CommentItem',
  props: {
    comment: Object,
    idx: Number,
  }
}
</script>

<style>

</style>