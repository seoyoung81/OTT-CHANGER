<template>
  <div>
    {{ article.title }}
    <router-link :to="{
        name: 'ArticleDetailView',
        params: {id: article.id }}">
        <button type="button" class="btn btn-outline-info">DETAIL</button>
      </router-link>
  </div>
</template>

<script>
export default {
    name: 'MyArticlesItem',
    props: {
        article: Object
    }
}
</script>

<style>

</style>