<template>
    <div style="width: 150px" class="card-container">
      <img 
      :src="poster_src"
      @click="getMovieDetail"
      class="card-image"
      >
      <p class="card-title">
        {{ movie.title }}
      </p>
    </div>
  </template>
  
  <script>
  export default {
      name: 'TopRatedItem',
      props: {
        movie: Object
      },
      data() {
        return {
            poster_src: 'https://image.tmdb.org/t/p/original/'
        }
      },
      created(){
        // console.log(this.movie)
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