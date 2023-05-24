<template>
  <div class="mypage-container">
    <form class="mypage">
      <img src="@/assets/MyPage_logo02.png"
        style="width: 250px;">
  
      <MyLikesList/><br>
      <MyArticlesList/>
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
            username: this.$store.state.user.username
        }
    },
    created() {

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
  
}

.mypage {
  display: flex;
  flex-direction: column; 
  align-items: center;
}



</style>