<template>
  <div class="ott-img-select">
    <h1>현재 구독 중인 OTT 서비스를 선택해주세요</h1><br>

    <img alt="netflix" 
    :src="require(`@/assets/${netflix}_logo.png`)"
    @click="goRecommend(netflix)"
    >
    <img alt="wavve" 
    :src="require(`@/assets/${wavve}_logo.png`)"
    @click="goRecommend(wavve)"
    >
    <img alt="tving" 
    :src="require(`@/assets/${tving}_logo.png`)"
    @click="goRecommend(tving)"
    >
    <img alt="dplus" 
    :src="require(`@/assets/${dplus}_logo.png`)"
    @click="goRecommend(dplus)"
    >
    <img alt="watcha" 
    :src="require(`@/assets/${watcha}_logo.png`)"
    @click="goRecommend(watcha)"
    >
  </div>
</template>

<script>
export default {
    name: 'OttSelect',
    data(){
        return {
            netflix: "netflix",
            wavve: "wavve",
            watcha: "watcha",
            dplus: "dplus",
            tving: "tving",
        }
    },
    methods: {
        goRecommend(service) {
            console.log(service)
            this.$router.push({
                path: 'ott/recommend',
                query: {
                    data: service
                }
            
            })
        },
        
    }
}
</script>

<style>
.ott-img-select img {
    width: 250px; 
    border-radius: 5px; 
    margin-left: 5px; 
    margin-right: 5px; 
    cursor: pointer;
}

</style>