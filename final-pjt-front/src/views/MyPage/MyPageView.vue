<template>
  <div class="mypage-container">
    <form class="mypage">
      <h3>{{ username }}'s Page</h3>
      <!-- <img src="@/assets/MyPage_logo02.png"
        style="width: 250px;"> -->

      <MyLikesList :user_id="user_id"/><br>
      <MyArticlesList :user_id="user_id"/>
    </form>
  </div>
</template>

<script>
import MyLikesList from '@/components/MyPage/MyLikesList'
import MyArticlesList from '@/components/MyPage/MyArticlesList'

export default {
    name: 'MyPageView',
    components: {
        MyLikesList,
        MyArticlesList
    },
    data() {
        return {
            user_id: this.$route.params.id,
            username: null
        }
    },
    mounted() {
      this.username = this.$route.query.username
    }
    
}
</script>

<style>
.mypage-container {
  display: flex;
  height: 100%;
  outline: 2px solid #e0e0e0;
  padding: 40px;
  border-radius: 50px;
  justify-content: center;
  align-items: center;
  width: 90%;
  margin-left: 5%;
  
}

.mypage {
  display: flex;
  flex-direction: column; 
  align-items: center;
}



</style>