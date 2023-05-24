<template>
  <div>
    <h1>{{ ott }} 구독중이시군요! 다음 영화를 추천 드릴게요</h1>
    <br>
    <button @click="goMain" class="ott-btn">구독 유지</button>
    <button @click="goMovieSelect" class="ott-changer-btn">OTT CHANGER</button>
    
    <RecommendList
    :ott_pk="ott_pk"
    />
    <br>
  </div>
</template>

<script>
import RecommendList from '@/components/OTT/RecommendList'
export default {
    name: 'RecommendFromCurrentOttView',
    data() {
      return {
        ott: null,
        ott_pk: null,
        ott_k: null,
      }
    },
    components: {
      RecommendList
    },
    created() {
      const ottData = this.$route.query.data
      console.log(ottData)
      this.ott = ottData
      console.log(this.ott) 
      if (this.ott === 'netflix') {
        this.ott_pk = 8
        this.ott = '넷플릭스를'
      }
      else if (this.ott === 'tving') {
        this.ott_pk = 33
        this.ott = '티빙을'
      } 
      else if (this.ott === 'watcha') {
        this.ott_pk = 97
        this.ott = '왓챠를'
      } 
      else if (this.ott === 'dplus') {
        this.ott_pk = 337
        this.ott = '디즈니 플러스를'
      } 
      else if (this.ott === 'wavve') {
        this.ott_pk = 356
        this.ott = '웨이브를'
      } 
    },
    methods: {
      goMain(){
        this.$router.push({name: 'MainView'})
      },
      goMovieSelect(){
        this.$router.push({name: 'MovieSelectView'})
      }

    }
    
}
</script>

<style>
.ott-changer-btn {
  padding: 10px 15px;
  background-color: #ff4081;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-left: 5px;
  margin-bottom: 20px;
  font-weight: bolder;

}

.ott-changer-btn:hover {
  background-color: #ff4080b7;
  
 
}

.ott-btn {
  padding: 10px 15px;
  background-color: #61DAFB;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 20px;
  font-weight: bolder;

}

.ott-btn:hover {
  background-color: #007997;
 
}


</style>