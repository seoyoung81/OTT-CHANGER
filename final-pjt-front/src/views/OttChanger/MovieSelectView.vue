<template>
  <div>
    <h1>보고 싶은 영화를 선택해주세요</h1>
    <h5 style="margin-top: 20px;">{{ this.$store.state.selected_lst.length }}</h5>
    <br>
    <div class="d-flex flex-wrap">
      <MovieSelectList
      v-for="(movie, idx) in random_movie_lst"
      :key="idx"
      :idx="idx"
      :movie="movie"/>
    </div>
    <button @click="goResult" class="ott-changer-btn" style="margin-top: 30px;">결과 보기</button>
  </div>
</template>

<script>
import MovieSelectList from '@/components/OttChanger/MovieSelectList'
const API_URL = 'http://127.0.0.1:8000/api/v1/movie_select/'
import axios from 'axios'

export default {
    name: 'MovieSelectView',
    components: {
      MovieSelectList
    },
    data() {
      return {
        random_movie_lst : [],
      }
    },
    created() {
      axios({
        method: 'get',
        url: API_URL
      })
      .then((response) => {
        // console.log(response.data)
        this.random_movie_lst = response.data
      })
      .catch((error) => {
        console.log(error)
      })
      this.$store.dispatch('resetLst')

    },
    methods: {
      goResult() {
        if (this.$store.state.selected_lst.length < 10) {
          alert('10개 이상 선택해주세요')
        } else (
          this.$router.push({name: 'OttResultView'})
        )
      }
    }
}
</script>

<style>

</style>