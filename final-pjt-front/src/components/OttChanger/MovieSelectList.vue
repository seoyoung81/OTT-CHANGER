<template>
  <div class="movie-select-img">
    <img :src="poster_src"
    :style="{ width: '200px', filter: grayscale ? 'grayscale(100%)' : 'none'}"
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
            if (this.$store.state.selected_lst_length <= 15) {
                this.grayscale = !this.grayscale
            }
        },
        
    }  
}
</script>

<style>
.movie-select-img img {
    border-radius: 10px;
    margin: 5px;
    cursor: pointer;
}

</style>