<template>
    <div style="width: 150px" class="my-auto">
        <img 
        :src="poster_src"
        @click="getMovieDetail"
        class="card-image"
        >
  </div>

</template>

<script>
export default {
    name: 'NowPlayingItem',
    props: {
        movie: Object
    },
    data() {
        return {
            poster_src: 'https://image.tmdb.org/t/p/original/'
        }
    },
    created(){
        // console.log('where')
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