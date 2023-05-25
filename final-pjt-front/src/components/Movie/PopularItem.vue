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
  .card-image {
    width: 200px;
    height: auto;
    border-radius: 30px;
    transition: transform 0.3s ease;
    }

    .card-image:hover {
        transform: scale(1.1);
    }

  </style>