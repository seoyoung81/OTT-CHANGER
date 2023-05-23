<template>
  <div>
    <button @click="backArticle" class="btn btn-outline-primary" style="float: left; margin-left: 10%;">목록보기</button>
    <h1 style="margin-right: 25%;">Detail</h1><br>
    
    <div class="detail-form">
      <br><br>
      
      <!-- 게시글 -->
      <div class="detail-container">
        <p style="font-weight: bolder;">{{ article?.title }}</p><hr>
        <p>{{ article?.content }}</p>
      </div>
      

      <router-link :to="{
        name: 'MyPageView',
        params: {id: user }}"
          class="article-link">
          <p class="article-detail-user">
            {{ article?.username }}
          </p>  
        </router-link>
        <p style="margin-top: 100px;">수정시간 {{ article?.updated_at }}</p>
      </div>




    <div>
      <button @click="deleteArticle" class="custom-button">삭제하기</button><br><br>

      <router-link :to="{ name: 'ArticleEditView', query: { articleId: article?.id } }">
        <button type="button" class="custom-button">
          수정하기
        </button>
      </router-link>
  
    </div>

    
    <router-view/>
    <CommentForm :id="article?.id" @receive-new-comment="newComment"/>   
    <CommentList :comment_set="comment_set" :article_id="article_id" />
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/Community/CommentList.vue'
import CommentForm from '@/components/Community/CommentForm.vue'
// import ArticleEditView from '@/components/Community/ArticleEditView.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  components: {
    CommentList,
    CommentForm,
    // ArticleEditView,
  },
  data() {
    return {
      article: null,
      comment_set : [],
      article_id: null,
      user: null,
    }
  },
  created() {
    // console.log('Article Detail View Created')
    // console.log(this.$route.params.articleId)
    this.getArticleDetail()
    // const articleId = this.
    // console.log('아티클 디테일 정보랑 토큰 ::::::::', this.$store.state.token)
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.articleId}/`,
        params: {},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((response) => {
        // console.log('Axios request Successful')
        // console.log(response)
        // console.log(response.data.comment_set)
        this.article = response.data
        // console.log(this.article)
        console.log('afvasjfalsjflasjflasj',response.data)
        this.comment_set = response.data.comment_set
        this.article_id = response.data.id

      })
    },
    backArticle() {
      this.$router.push({name: 'CommunityView'})
    },
    newComment(newcomment) {
      this.comment_set.push(newcomment)
    },
    deleteArticle() {
      const user = this.$store.state.user.id
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/articles/${this.$route.params.articleId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        params: {},
        data: { user },
      })
      .then(() => {
        // console.log('삭제 응답 ::::::', response)
        this.$router.push({name: 'CommunityView'})
      })
      .catch((error) => {
        console.log(error)
      })
    },
  }
}
</script>

<style>
.custom-button {
  padding: 10px 15px;
  background-color: #FF4081;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
 
}

.custom-button:hover {
  background-color: #ff4080bd;
 
}

.detail-form {
  width: 80vw;
  display: block;
  height: 100%;
  outline: 2px solid #e0e0e0;
  padding: 10px 40px 10px;
  border-radius: 30px;
  justify-content: center;
  align-items: center;
  margin: auto;

}

.article-detail-user {
    display: inline-block;
    float: right;
    margin-top: 85px;
  }


</style>