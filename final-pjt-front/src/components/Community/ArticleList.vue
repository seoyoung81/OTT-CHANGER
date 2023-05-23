<template>
  <div>
    <!-- <h1>Article List</h1> -->
    <br>
    <span class="number-align">번호</span>
    <span class="title-align">게시글</span>
    <span class="user-align">작성자</span>
    <br><br>
    <hr class="horizontal-line">
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
.number-align {
  float: left;
  margin-left: 37px;
}

.title-align {
  float: left;
  margin-left: 33px;
  
}

.user-align {
  float: right;
  margin-right: 100px;
}

.horizontal-line {
    width: 90vw;
    height: 2px;
    margin: 0 auto;
    margin-left: calc((100vw - 95vw) / 2); /* 반응형으로 가운데 정렬 */
  }

  @media (max-width: 90vw) {
    .horizontal-line {
      margin-left: 0; /* 너비가 화면 너비보다 작을 경우 왼쪽 정렬 */
    }
  }


</style>