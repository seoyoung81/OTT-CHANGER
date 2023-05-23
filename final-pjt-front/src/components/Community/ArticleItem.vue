<template>
  <div>
    <!-- <h5>{{ article.id }}</h5> -->
    <br><br>
    
    <!-- 작성자 -->
    <router-link :to="{
      name: 'MyPageView',
      params: { id: user_id }}"
      class="article-link">
      <p class="article-user">
        {{ article.username }}
      </p>  
    </router-link>

    <!-- 게시글 -->
    <router-link :to="{
      name: 'ArticleDetailView',
      params: { articleId: article_id }}"
      class="article-link">
      <span class="article-title">{{ article.title }}</span>
    </router-link>



  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  data() {
    return {
      article_id : null,
      user_id : null,
    }
  },
  props: {
    article: Object,
  },
  created() {
    this.article_id = this.article.id
    this.user_id = this.article.user
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