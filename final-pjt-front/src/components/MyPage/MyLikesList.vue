<template>
  <div>
    <h1>내가 좋아요한 영화</h1>
    <MyLikesItem
    v-for="(movie, idx) in my_likes"
    :key="idx"
    :movie="movie"
    />
  </div>
</template>

<script>
import axios from 'axios'
import MyLikesItem from '@/components/MyPage/MyLikesItem.vue'

export default {
    name: 'MyPageView',
    components: {
        MyLikesItem
    },
    data() {
        return {
            my_likes: []
        }
    },
    created() {
        this.$route.params.user_id = this.$store.state.user.id
        axios({
            method: 'get',
            url: `http://127.0.0.1:8000/api/v1/movies/likes/${this.$route.params.user_id}/`,
            params: {}
        })
        .then((response) => {
            console.log(response.data)
            this.my_likes = response.data
        })
    }
}
</script>

<style>

</style>