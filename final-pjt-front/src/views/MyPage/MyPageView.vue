<template>
  <div>
    <h1>{{ username }}'s My Page</h1>
    <MyLikesList/>
    <MyArticlesList/>
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

</style>