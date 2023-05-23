<template>
  <div class="card-container">
    <img :src="poster_src"
    class="card-image"
    @click="getMovieDetail"
    >
    <p class="card-title">
        {{ movie.title }}
    </p>
  </div>
</template>

<script>
export default {
    name: 'MyLikesItem',
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
        console.log(this.movie)
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
.card-container {
  position: relative;
  display: inline-block;
}

.card-image {
    width: 150px;
    height: auto;
    border-radius: 20px;
    transition: transform 0.3s ease;
}

.card-image:hover {
    transform: scale(1.1);
    opacity: 80%;
}

.card-title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #fff;
  padding: 10px;
  border-radius: 5px;
  font-weight: bold;
  font-size: 14px;
  text-align: center;
  z-index: 1;
  opacity: 0;
  transition: opacity 0.3s ease;
  white-space: nowrap;
  width: 90vw;
}

.card-image:hover + .card-title {
  opacity: 1;
}

</style>