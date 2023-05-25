<template>
  <div>
    <div style="position: relative;" class="detail-movie-bg">
        <img :src="backdrop_path_src" class="detail-movie-backdrop">
        <iframe :src="videoSrc" allowfullscreen class="detail-movie-ytb"></iframe>
    </div>


    <!-- <img :src="backdrop_path_src" style="width:100vw; opacity: 60%;"> -->
    
    <!-- <iframe :src="videoSrc" allowfullscreen></iframe>
    <p>영화 제목: {{ movie.title }}</p>
    <p>영화 포스터: <img :src="poster_path_src" style="width:500px;"></p>
    <button v-if="!isLiked" @click="movieLike">좋아요!</button>
    <button v-else @click="movieLike">좋아요 취소</button>
        <p>{{ likes_count }}명이 이 영화를 좋아합니다.</p>

    <p>영화 내용: {{ movie.overview}}</p> -->
    <br><br><br>
    <div class="info-container">
        <img :src="poster_path_src" style="width:700px; float: left; margin-left: 80px;">
        <div class="movie-detail-info">
            <br>
            <div style="display:flex; justify-content: space-between; align-items: center;">
                <h1 style="margin-left: 95px;">{{ movie.title }}</h1>
                <!-- 하트 -->
                <div style="margin-right: 10%;">
                    <img src="@/assets/heart_empty.png" v-if="!isLiked" @click="movieLike" class="heart-img">
                    <img src="@/assets/heart_full.png" v-else @click="movieLike" class="heart-img">
                    <p>{{ likes_count }}명이 이 영화를 좋아합니다.</p>
                </div>
            </div>
            <!-- 수평선 -->
            <hr style="width: 80%; margin: auto; height: 3px; background-color: white;"><br>

            <div style="text-align: left; margin-left: 10%;">
                <p>누적 관객수 &nbsp; {{ movie.popularity * 10000 }} 명</p>
                <p>평점 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ movie.vote_average }}</p>
                <p>개봉일 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {{ movie.release_date }}</p>
            </div>

            <!-- overview -->
            <div style="margin-top: 10%; margin-left: 10%; margin-right: 10%;">
                <span class="overview-text">{{ movie.overview }}</span>
            </div>

            

        </div>
    </div>
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
        // console.log(movie)
        this.movie = movie
        this.movie = { ...this.movie, m_id: 9999999 } // Add m_id field to like_movie object
        this.likeUsers()
        console.log(this.movie)
        
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
                    // console.log(this.videoSrc)
                    break;
            }}
            // console.log(this.videoSrc)
            
            // poster img
            
            })
        .catch((error) => {
            console.log(error)
        })
        console.log(this.Liked)
    },
    methods: {
        movieLike() {
            console.log('enter movieLike')
            const like_movie = this.movie 
            // console.log(like_movie.m_id)
            const user_pk = this.$store.state.user.id
            // console.log('좋아요 누른 영화 정보', like_movie)
            // console.log('좋아요 누른 유저 id', user_pk)
            console.log(like_movie.m_id)
            if (this.$store.getters.isLogin === false) {
                alert('로그인 해주세요!')
                return
            }
            axios({
                method: 'post',
                url: `http://127.0.0.1:8000/api/v1/movie_likes/${like_movie.m_id}/${user_pk}/`,
                data: { like_movie, user_pk },
                params: { }
            })
            .then((response) => {
                console.log(response)
                this.likes_count = response.data.like_users_count
                const like_users = response.data.like_users
                console.log(response.data.m_id)
                // console.log('전', this.isLiked)
                const likedUser = like_users.find(user => user.id === this.$store.state.user.id)
                if (likedUser) {
                    this.isLiked = true
                } else {
                    this.isLiked = false
                }
            })
            .catch((error) =>{
                console.log(error)
            })
        },
        likeUsers() {
            const like_movie = this.movie
            console.log(like_movie.m_id)
            // const user_pk = this.$store.state.user.id
            console.log('hihihihihihihihihihihihihih')
            axios({
                method: 'post',
                url: `http://127.0.0.1:8000/api/v1/movie_likes/${like_movie.id}/`,
                data: { like_movie },
                params: {}
            })
            .then((response) => {
                console.log(response.data)
                console.log('잘왔니..?')
                this.likes_count = response.data.likes_count
                this.movie.m_id = response.data.movie.m_id
                const liked_users = response.data.movie.like_users
                console.log(liked_users)
                const likedCheck = liked_users.find(user => user === this.$store.state.user.id)
                if (likedCheck) {
                    this.isLiked = true
                } else {
                    this.isLiked = false
                }
            })
            .catch((error) => {
                console.log(error)
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