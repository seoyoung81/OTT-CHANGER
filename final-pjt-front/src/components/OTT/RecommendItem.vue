<template>
  <div>
    <img :src="poster_src"
    style="height:300px;"
    >
  </div>
  
</template>

<script>
export default {
    name: 'RecommendItem',
    props: {
        movie: Object,
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
}
</script>

<style>

</style>