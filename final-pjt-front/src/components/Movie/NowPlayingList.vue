<template>
  <div>
    <div class="dis-flex mx-auto">
        <NowPlayingItem
        v-for="(movie, idx) in nowplaying_lst"
        :key="idx"
        :movie="movie"
        class="NowPlayingItem"
        />
    </div>
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
    width: 80%; 
    height: 270px; 
    padding-top: 15px;
  }

  
  .dis-flex::-webkit-scrollbar {
  width: 5px; /* Width of the vertical scrollbar */
  background-color: transparent; /* Hide the scrollbar background */
  }

.dis-flex::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.2); /* Scrollbar thumb color */
  }

.dis-flex::-webkit-scrollbar-track {
  background-color: transparent; /* Hide the scrollbar track background */
  }

  .NowPlayingItem {
    flex-shrink: 0;
    width: 100px;
    height: 200px;
    margin-right: 10px;
  }
  
  </style>