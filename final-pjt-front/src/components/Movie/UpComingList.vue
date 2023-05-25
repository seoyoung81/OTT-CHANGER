<template>
  <div class="dis-flex mx-auto">
    <UpComingItem
        v-for="(movie, idx) in upcoming_lst"
        :key="idx"
        :movie="movie"
        class="UpComingItem"
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
  .dis-flex {
    display: flex;
    overflow-x: scroll;
    scroll-behavior: smooth;
  }
  
  .UpComingItem {
    flex-shrink: 0;
    width: 100px;
    height: 200px;
    margin-right: 10px;
  }
  
  </style>