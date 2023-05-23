<template>
  <div>
    <!-- <h5>{{ article.id }}</h5> -->
    <br><br>

    
    <!-- 게시글 번호 -->
    <span class="article-number">
      {{ article.id }}
    </span>
    
    <!-- 작성자 -->
    <router-link :to="{
      name: 'MyPageView',
      params: {id: user }}"
      class="article-link">
      <p class="article-user">
        {{ article.username }}
      </p>  
    </router-link>

    <!-- 게시글 -->
    <router-link :to="{
      name: 'ArticleDetailView',
      params: {id: article.id }}"
      class="article-link">
      <span class="article-title">{{ article.title }}</span>
    </router-link>



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
.article-number {
    display: inline-block;
    width: 40px;
    text-align: left;
    float: left;
    margin-left: 50px;
  }

.article-title {
    display: inline-block;
  
  }

.article-user {
    display: inline-block;
    float: right;
    margin-right: 90px;
  
      
  }

.article-link {
    color: #e0e0e0; /* 변경할 링크 색상 설정 */
    transition: font-size 0.2s;
    text-align: left;
    display: block;
    margin-left: 100px;
    
  }
  
  .article-link:hover {
    color: #61DAFB;
    
  }


  



</style>