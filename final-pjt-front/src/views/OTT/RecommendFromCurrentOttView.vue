<template>
  <div>
    <h1>{{ ott }}를 구독중이시군요! 다음 영화를 추천 드릴게요</h1>
    <RecommendList
    :ott_pk="ott_pk"
    />
    <br>
    <button @click="goMain">구독 유지해야지!</button>
    <button @click="goMovieSelect">OTT CHANGER</button>
  </div>
</template>

<script>
import RecommendList from '@/components/OTT/RecommendList'
export default {
    name: 'RecommendFromCurrentOttView',
    data() {
      return {
        
        ott: null,
        ott_pk: null
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
      }
      else if (this.ott === 'tving') {
        this.ott_pk = 33
      } 
      else if (this.ott === 'watcha') {
        this.ott_pk = 97
      } 
      else if (this.ott === 'dplus') {
        this.ott_pk = 337
      } 
      else if (this.ott === 'wavve') {
        this.ott_pk = 356
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

</style>