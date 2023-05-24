<template>
  <div>
    <h1>영화 정보</h1>
    <img :src="backdrop_path_src" style="width:100vw; opacity: 60%;">
    
    <iframe :src="videoSrc" allowfullscreen></iframe>
    <p>영화 제목: {{ movie.title }}</p>
    <p>영화 포스터: <img :src="poster_path_src" style="width:500px;"></p>
    <button v-if="!isLiked" @click="movieLike">좋아요!</button>
    <button v-if="isLiked" @click="movieLike">좋아요 취소</button>
        <p>{{ likes_count }}명이 이 영화를 좋아합니다.</p>

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
            videoSrc: "https://www.youtube.com/embed/",
            autoplay: "?autoplay=1&mute=1",
            backdrop_path_src: 'https://image.tmdb.org/t/p/original/',
            poster_path_src: 'https://image.tmdb.org/t/p/original/',
            likes_count: 0,
            isLiked: false,
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
            url: `https://api.themoviedb.org/3/movie/${movie.id}/videos`,
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
    },
    methods: {
        movieLike() {
            const like_movie = this.movie
            const user_pk = this.$store.state.user.id
            console.log('좋아요 누른 영화 정보', like_movie)
            console.log('좋아요 누른 유저 id', user_pk)
            // console.log(this.$store.state.token)
            axios({
                method: 'post',
                url: 'http://127.0.0.1:8000/api/v1/movie_like/',
                data: { like_movie, user_pk }
            })
            .then((response) => {
                // console.log(response)
                this.likes_count = response.data.like_users_count
                const like_users = response.data.like_users
                console.log('전', this.isLiked)
                for (let element of like_users) {
                    // console.log(element)
                    // console.log(this.$store.state.user.id)
                    if ( this.$store.state.user.id === element.id) {
                        this.isLiked = !this.isLiked
                        console.log('후', this.isLiked)
                    }
                }
                this.$router.go(0)
            })
        }
    }

}
</script>

<style>
.main-container {
  text-align: center;

}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
.backdrop-image {
  width: 100%;
  height: 100%;
  opacity: 60%;
  z-index: 1;
  object-fit: cover;
}

</style>