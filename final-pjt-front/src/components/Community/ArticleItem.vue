<template>
  <div>
    <!-- <h5>{{ article.id }}</h5> -->
    <br>
    <p>{{ article.title }}</p>
    <router-link :to="{
      name: 'ArticleDetailView',
      params: {id: article.id }}">
      <button type="button" class="btn btn-outline-info">DETAIL</button>
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>