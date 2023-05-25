<template>
  <div class="dis-flex mx-auto">
    <PopularItem
      v-for="(movie, idx) in popular_lst"
      :key="idx"
      :movie="movie"
      class="PopularItem"
      />
  </div>
</template>

<script>
import axios from 'axios'
import PopularItem from '@/components/Movie/PopularItem'

export default {
    name: 'PopularList',
    components: {
      PopularItem
    }, 
    data() {
      return {
        popular_lst: [],
      }
    },
    created() {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/popular',
    
        params: {
          api_key: process.env.VUE_APP_TMDB_API_KEY,
          language: 'ko-KR',
          page: 1
          }
      })
      .then((response) => {
        const movies = response.data.results
        movies.forEach(movie => {
          this.popular_lst.push(movie)
        })
        // console.log(this.popular_lst)
      })
      .catch((error) => {
        console.log(error)
      })
    }
}
</script>

<style>
.dis-flex {
  display: flex;
  overflow-x: scroll;
  scroll-behavior: smooth;
}

.PopularItem {
  flex-shrink: 0;
  width: 100px;
  height: 200px;
  margin-right: 10px;
}

</style>