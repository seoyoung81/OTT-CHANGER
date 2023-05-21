<template>
    <div class="dis-flex mx-auto" style="width: 80%; height: 450px;" >
        <NowPlayingItem
        v-for="(movie, idx) in nowplaying_lst"
        :key="idx"
        :movie="movie"
        class="NowPlayingItem"
        />
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import NowPlayingItem from '@/components/Movie/NowPlayingItem'

  export default {
      name: 'NowPlayingList',
      components: {
        NowPlayingItem
      },
      data() {
        return {
            nowplaying_lst : [],

        }
      },
      created() {
        axios({
            method: 'get',
            url: 'https://api.themoviedb.org/3/movie/now_playing',
            params: {
                api_key: process.env.VUE_APP_TMDB_API_KEY,
                language: 'ko-KR',
                page: 1
                }
        })
        .then((response) => {
            const movies = response.data.results
            movies.forEach(movie => {
                this.nowplaying_lst.push(movie)
            
        
      })
            // console.log(this.nowplaying_lst)
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
  
  .NowPlayingItem {
    flex-shrink: 0;
    width: 100px;
    height: 200px;
    margin-right: 10px;
  }
  
  </style>