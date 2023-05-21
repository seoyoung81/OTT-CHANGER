<template>
  <div>
    <img :src="poster_src"
    :style="{ height: '300px', filter: grayscale ? 'grayscale(100%)' : 'none' }"
    @click="selectMovie"
    >    
  </div>
</template>

<script>
export default {
    name: 'MovieSelectList',
    props: {
        movie: Object,
        idx: Number,
    },
    data() {
        return {
            poster_src: 'https://image.tmdb.org/t/p/original/',
            grayscale: false,
        }
    },
    created(){
        // console.log(this.movie)
        this.poster_src = this.poster_src + `${this.movie.poster_path}`
    },  
    methods: {
        selectMovie(){
            const payload = {
                idx: this.idx,
                providers: this.movie.providers
            }
            // console.log(payload)
            this.$store.dispatch('selectMovie', payload)
            this.grayscale = !this.grayscale
        },
        
    }  
}
</script>

<style>

</style>