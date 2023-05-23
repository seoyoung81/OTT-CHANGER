<template>
  <div class="align">
    <router-link :to="{
        name: 'ArticleDetailView',
        params: {articleId: article.id }}"
        class="link"
        >
        {{ article.title }}
        <hr style="width: 100%; color: #ffffff;">
        <br>
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
.link {
    color: #e0e0e0; /* 변경할 링크 색상 설정 */
    transition: font-size 0.2s;
    text-align: center;
    display: block;
    text-decoration: none;

    
  }
  
  .link:hover {
    color: #61DAFB;
    
  }

</style>