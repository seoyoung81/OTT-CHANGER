<template>
  <div>
    <h1>보고 싶은 영화를 선택해주세요</h1>
    <MovieSelectList
    v-for="(movie, idx) in random_movie_lst"
    :key="idx"
    :idx="idx"
    :movie="movie"/>
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
    }
}
</script>

<style>

</style>