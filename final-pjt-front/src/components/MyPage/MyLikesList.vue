<template>
  <div>
    <br>
    <div class="text-align">
        <h5>내가 
            <img src="@/assets/heart.png" style="width: 50px;">
            한 영화
        </h5>
    </div>
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
    props: {
        user_id: Number,
    },
    data() {
        return {
            my_likes: []
        }
    },
    created() {
        console.log('MyArticleList',this.user_id)
        this.$route.params.user_id = this.user_id
        console.log(this.user_id)
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