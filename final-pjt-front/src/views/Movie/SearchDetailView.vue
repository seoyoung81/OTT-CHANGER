<template>
  <div>
    <h1>영화 정보</h1>
    <img :src="backdrop_path_src" style="width:100vw; opacity: 60%;">
    
    <iframe :src="videoSrc" allowfullscreen ></iframe>
    <p>영화 제목: {{ movie.title }}</p>
    <p>영화 포스터: <img :src="poster_path_src" style="width:500px;;"></p>
    <p>영화 내용: {{ movie.overview}}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SearchDetailView',
    data() {
        return {
            movie: null,
            videoId: null,
            videoSrc: "https://www.youtube.com/embed/",
            autoplay: "?autoplay=1&mute=1",
            backdrop_path_src: 'https://image.tmdb.org/t/p/original/',
            poster_path_src: 'https://image.tmdb.org/t/p/original/'
        }
    },
    created() {
        const movieData = this.$route.query.data
        const movie = JSON.parse(movieData)
        this.movie = movie
        // console.log(this.movie)

        // poster
        this.backdrop_path_src = this.backdrop_path_src + `${this.movie.backdrop_path}`
        this.poster_path_src = this.poster_path_src + `${this.movie.poster_path}`


        axios({
            method: 'get',
            url: `https://api.themoviedb.org/3/movie/${movie.movie_id}/videos`,
            params: {
                api_key: process.env.VUE_APP_TMDB_API_KEY,
            }   
        })
        .then((response) => {
            // console.log(response.data.results)
            for (const element of response.data.results) {
                if (element.type === 'Trailer') {
                    // console.log(element.type)
                    this.videoId = element.key
                    this.videoSrc = this.videoSrc + `${this.videoId}` + `${this.autoplay}`
                    console.log(this.videoSrc)
                    break;
            }}
            // console.log(this.videoSrc)
            
            // poster img
            
            })
            .catch((error) => {
                console.log(error)
            })
        

        

    }

}
</script>

<style>



</style>