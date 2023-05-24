<template>
  <div class="d-flex flex-wrap">
    <br>
    <RecommendItem
    v-for="(movie, idx) in movie_lst"
    :key="idx"
    :movie="movie"/>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import RecommendItem from '@/components/OTT/RecommendItem'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'RecommendList',
    components: {
      RecommendItem
    },
    data() {
      return {
        movie_lst: [],
        pk: null
      }
    },
    props: {
      ott_pk: Number
    },
    created() {
      const pk = this.ott_pk
      console.log(pk)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/`,
        data: { pk }
      })
      .then((response) => {
        console.log(response.data)
        this.movie_lst = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    
}
</script>

<style>

</style>