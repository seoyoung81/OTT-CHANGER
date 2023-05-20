<template>
    <div>
        <img 
        :src="poster_src"
        style="width:100px; height:200px;"
        @click="getMovieDetail"
        >
    </div>
  </template>
  
  <script>
  export default {
      name: 'PopularItem',
      props: {
        movie: Object
    },
    data() {
        return {
            poster_src: 'https://image.tmdb.org/t/p/original/'
        }
    },
    created() {
        // console.log('포스터 주소는 !!!', this.poster_src)
        this.poster_src = this.poster_src + `${this.movie.poster_path}`
    },
    methods: {
        getMovieDetail(){
            this.$router.push({
                path: '/movie_detail',
                query: {
                    data: JSON.stringify(this.movie)
                }
            })
        }
    }
  }
  </script>
  
  <style>
  
  </style>