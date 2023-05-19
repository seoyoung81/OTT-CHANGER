<template>
  <div>
    <h1>영화 정보</h1>
    <embed :src="videoSrc">
    <p>영화 제목: {{ movie.title }}</p>
    <p>영화 포스터: <img src="" alt=""></p>
    <p>영화 내용: {{ movie.overview}}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MovieDetailView',
    data() {
        return {
            movie: null,
            videoId: null,
            videoSrc: "https://www.youtube.com/watch?v="
        }
    },
    created() {
        const movieData = this.$route.query.data
        const movie = JSON.parse(movieData)
        this.movie = movie
        console.log(this.movie)
        axios({
            method: 'get',
            url: `https://api.themoviedb.org/3/movie/${movie.id}/videos`,
            params: {
                api_key: process.env.VUE_APP_TMDB_API_KEY,
            }   
        })
        .then((response) => {
            console.log(response.data.results)
            for (const element of response.data.results) {
                if (element.type === 'Trailer') {
                    console.log(element.type)
                    this.videoId = element.id
                    this.videoSrc = this.videoSrc + `${this.videoId}`
                    console.log()

                    break;
            }}
            console.log(this.videoSrc)
                
                    
                
                
                
                // console.log(this.videoSrc)
            })
        
        

        

    }

}
</script>

<style>

</style>