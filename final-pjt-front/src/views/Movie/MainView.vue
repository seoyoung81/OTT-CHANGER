<template>
  <div class="main-container">
    <!-- 검색창 -->
    <div class="search-container">
      <input type="text" 
        v-model="keyword" 
        @keyup.enter="goSearch" 
        class="search-input" 
        placeholder="검색어를 입력하세요"
        >
      <img src="@/assets/search.png" 
        @click="goSearch"
        class="search-img"
        style="width: 60px; margin-left: 30px;">
      </div>
      <br>
      
      <!-- 백드롭&포스터 -->
      <div style="position: relative;" class="container">
        <img :src="backdrop_path_src" class="backdrop-image">
        <img :src="poster_path_src"
        class="main-poster-img"
        @click="getMovieDetail">
      </div>
      <br>
      
    <!-- 영화 정보 제공 -->
    <div>
      <br>
      <h1>최신영화</h1><br>
      <NowPlayingList/>
      <h1>Top 20</h1><br>
      <TopRatedList/>
      <h1>인기영화</h1><br>
      <PopularList/>
      <h1>개봉예정</h1><br>
      <UpComingList/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from "lodash"
import NowPlayingList from '@/components/Movie/NowPlayingList'
import PopularList from '@/components/Movie/PopularList'
import UpComingList from '@/components/Movie/UpComingList'
import TopRatedList from '@/components/Movie/TopRatedList'

export default {
  name: 'MainView',
  components: {
    NowPlayingList,
    PopularList,
    UpComingList,
    TopRatedList
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
      }
    },
  data() {
    return {
      backdrop_path_lst: [],
      backdrop_path_src: 'https://image.tmdb.org/t/p/original/',
      poster_path_lst: [],
      poster_path_src: 'https://image.tmdb.org/t/p/original/',
      keyword: null,
      movie_info: null,
    }
  },
  created() {
    if (this.isLogin){
      this.$store.dispatch('getUserInfo')
    }
    axios({
      method: 'get',
      url: 'https://api.themoviedb.org/3/movie/now_playing',
      params: {
        api_key: process.env.VUE_APP_TMDB_API_KEY,
        language: 'ko-KR',
        page: 1
      }
    })
    .then((response) => {
      // console.log(response)
      // console.log(response.data.results)
      const movies = response.data.results
      movies.forEach(movie => {
        this.backdrop_path_lst.push(movie.backdrop_path)
        this.poster_path_lst.push(movie.poster_path)
        
      })
      const idx = _.random(19)
      this.backdrop_path_src = this.backdrop_path_src + `${this.backdrop_path_lst[idx]}`
      this.poster_path_src = this.poster_path_src + `${this.poster_path_lst[idx]}`
      // console.log(this.backdrop_path_src)
      // console.log(this.backdrop_path_lst)

      this.movie_info = movies[idx]
      // console.log(idx)
      // console.log(this.movie_info)
    })
    .catch((error) =>{
      console.log(error)
    })
  },
  methods: {
    goSearch() {
        this.$router.push({name: 'SearchMovieView', params: { keyword: this.keyword}})
      },
    getMovieDetail(){
          this.$router.push({
              path: '/movie_detail',
              query: {
                  data: JSON.stringify(this.movie_info)
              }
          })
      }
  
  }
}
</script>

<style>
.search-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 300px;
  height: 40px;
  border: 1px solid #ccc;
  /* 둥근 테두리 */
  border-radius: 20px;
  margin: 0 auto;
}

.search-input {
  display: inline;
  border: none !important;;
  outline: none;
  padding: 0 0 0 50px !important;
  margin: 0 !important;
  font-size: 16px;
  color: white;
  background-color: transparent; /* 추가: 배경색 투명하게 설정 */

}

.main-container {
  text-align: center;

}
.backdrop-image {
  width: 180%;
  height: auto;
  opacity: 60%;
  z-index: 1;
  object-fit: cover;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  position: relative;
}


.search-img {
  cursor: pointer;
  width: 30px;
  transition: filter 0.3s ease-in-out;
}

.search-img:hover {
  filter: brightness(70%); 
}


.main-poster-img {
  width: 30%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
  border-radius: 10px;
  transition: transform 0.3s ease;
  }

.main-poster-img:hover {
  filter: brightness(110%);
}


</style>