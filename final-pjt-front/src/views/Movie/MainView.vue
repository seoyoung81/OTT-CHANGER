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
      <button 
        @click="goSearch" 
        class="search-button">
      검색
      </button>
    </div>
    <!-- 백드롭&포스터 -->
    <div style="position: relative;" class="container">
      <img :src="backdrop_path_src" class="backdrop-image">
      <img :src="poster_path_src" style="width:450px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 2;">
    </div>

    <!-- 영화 정보 제공 -->
    <h1>최신영화</h1>
    <NowPlayingList/>
    <h1>인기영화</h1>
    <PopularList/>
    <h1>개봉예정</h1>
    <UpComingList/>
    <h1>Top 20</h1>
    <TopRatedList/>
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
      const idx = _.random(20)
      this.backdrop_path_src = this.backdrop_path_src + `${this.backdrop_path_lst[idx]}`
      this.poster_path_src = this.poster_path_src + `${this.poster_path_lst[idx]}`
      // console.log(this.backdrop_path_src)
      // console.log(this.backdrop_path_lst)
    })
    .catch((error) =>{
      console.log(error)
    })
  },
  methods: {
    goSearch() {
        this.$router.push({name: 'SearchMovieView', params: { keyword: this.keyword}})
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
  padding: 0 0 0 5px !important;
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
}





.search-button {
  display: inline-block;
  flex-shrink: 0;
  background-color: #5b8dc22f;
  color: #fff;
  border: none;
  outline: none;
  height: 40px;
  border-radius: 0 20px 20px 0; /* 추가: 버튼 모서리 둥글게 조정 */
  /* padding: 8px 12px; */
  cursor: pointer;
}

.search-button:hover {
  background-color: #265f9c;
}
</style>