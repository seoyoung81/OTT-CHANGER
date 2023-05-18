<template>
  <div>
    <h1>Article List</h1>
    <ArticleItem
    v-for="article in articles" :key="article.id" :article="article"/>
  </div>
</template>

<script>
import ArticleItem from '@/components/Community/ArticleItem.vue'
export default {
  name: 'ArticleList',
  components: {
    ArticleItem
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>

</style>