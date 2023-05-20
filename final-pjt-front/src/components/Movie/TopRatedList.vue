<template>
    <div class="d-flex">
        <TopRatedItem
        v-for="(movie, idx) in toprated_lst"
        :key="idx"
        :movie="movie"
        />
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import TopRatedItem from '@/components/Movie/TopRatedItem'
  export default {
      name: 'TopRatedList',
      components: {
        TopRatedItem
      },
      data() {
        return {
          toprated_lst : [],
        }
      },
      created() {
        axios({
          method: 'get',
            url: 'https://api.themoviedb.org/3/movie/top_rated',
            params: {
              api_key: process.env.VUE_APP_TMDB_API_KEY,
              language: 'ko-KR',
              page: 1
              }
        })
        .then((response) => {
          const movies = response.data.results
            movies.forEach(movie => {
                this.toprated_lst.push(movie)
        })
      })
        

        .catch((error) => {
          console.log(error)

        })
      } 
  }
  </script>
  
  <style>
  
  </style>