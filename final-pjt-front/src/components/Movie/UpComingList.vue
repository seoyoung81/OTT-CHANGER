<template>
    <div class="d-flex">
        <UpComingItem
        v-for="(movie, idx) in upcoming_lst"
        :key="idx"
        :movie="movie"
        />
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import UpComingItem from '@/components/Movie/UpComingItem'
  export default {
      name: 'UpComingList',
      components: {
        UpComingItem
      },
      data() {
        return {
          upcoming_lst : [],
        }
      },
      created() {
        axios({
            method: 'get',
            url: 'https://api.themoviedb.org/3/movie/upcoming',
            params: {
                api_key: process.env.VUE_APP_TMDB_API_KEY,
                language: 'ko-KR',
                page: 1
                }
      })
      .then((response) => {
        const movies = response.data.results
        movies.forEach(movie => {
          this.upcoming_lst.push(movie)
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