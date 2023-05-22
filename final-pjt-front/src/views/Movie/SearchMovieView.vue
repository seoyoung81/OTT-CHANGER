<template>
  <div>
    <p>{{ movie.title }}</p>
    <img
    :src="poster_src"
    style="height: 300px"
    @click="getMovieDetail"
    ><br>
    <!-- ott img -->
    <img alt="netflix" 
    v-if="netflix"
    :src="require(`@/assets/netflix_logo.png`)"
    >
    <img 
    v-if="tving"
    :src="require(`@/assets/tving_logo.png`)"
    >
    <img 
    v-if="wavve"
    :src="require(`@/assets/wavve_logo.png`)"
    >
    <img 
    v-if="dplus"
    :src="require(`@/assets/dplus_logo.png`)"
    >
    <img 
    v-if="watcha"
    :src="require(`@/assets/watcha_logo.png`)"
    >

  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'SearchMovieView',
    data() {
        return {
            movie: null,
            poster_src: 'https://image.tmdb.org/t/p/original/',
            netflix: false,
            wavve: false,
            dplus: false,
            tving: false,
            watcha: false,
        }
    },
    created() {
        console.log(this.$route.params.keyword)
        const keyword = this.$route.params.keyword
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/v1/movie_search/',
            data: { keyword }
        })
        .then((response) => {
            console.log(response.data)
            this.movie = response.data
            this.poster_src = this.poster_src + `${this.movie.poster_path}`
            console.log(this.movie.providers)
            // ott 화면에 띄우기
            if (this.movie.providers.includes(8)) {
                this.netflix = true
            } 
            if (this.movie.providers.includes(33)) {
                this.tving = true
            } 
            if (this.movie.providers.includes(97)) {
                this.watcha = true
            } 
            if (this.movie.providers.includes(337)) {
                this.dplus = true
            } 
            if (this.movie.providers.includes(356)) {
                this.wavve = true
            }
        })
        .catch((error) => {
            console.log(error)
        })

    },
    methods: {
        getMovieDetail(){
            this.$router.push({
                path: '/search_detail',
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