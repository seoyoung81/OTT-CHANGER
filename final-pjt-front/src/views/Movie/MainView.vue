<template>
  <div>
    <h1>Main Page</h1>
      <div>
      <img :src="backdrop_path_src" style="width:100vw; opacity: 60%;">
      <img :src="poster_path_src" style="width:500px; height:100p">
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import _ from "lodash"

export default {
  name: 'MainView',
  data() {
    return {
      backdrop_path_lst: [],
      backdrop_path_src: 'https://image.tmdb.org/t/p/original/',
      poster_path_lst: [],
      poster_path_src: 'https://image.tmdb.org/t/p/original/'
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
      // console.log(response)
      // console.log(response.data.results)
      const movies = response.data.results
      movies.forEach(movie => {
        this.backdrop_path_lst.push(movie.backdrop_path)
        this.poster_path_lst.push(movie.poster_path)
        
      })
      const idx = _.random(20)
      this.backdrop_path_src = this.backdrop_path_src + `${this.backdrop_path_lst[idx]}`
      this.poster_path_src = this.poster_path_src + `${this.poster_path_lst[idx]}`
    console.log(this.backdrop_path_src)
      // console.log(this.backdrop_path_lst)
    })
    .catch((error) =>{
      console.log(error)
    })
  }
}
</script>

<style>

</style>