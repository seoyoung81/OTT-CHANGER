<template>
  <div class="fade-in">
    <div>
        <h1> {{ username }} 님에게 어울리는 OTT는</h1>
        <img :src="require(`@/assets/${resultOTT}_logo.png`)" style="width: 300px; margin-top: 30px; margin-bottom: 20px; border-radius: 15px;">
    </div>
    <button @click="goSelect" class="custom-button-list">다시 고르기</button>
  </div>
</template>

<script>
export default {
    name: 'OttResultView',
    data() {
        return {
            resultOTT: null,
            username: null,
            ott: null,
        }
    },

    created() {
        this.$store.dispatch('calculateResult')
        this.resultOTT = this.$store.state.resultOTT
        this.username = this.$store.state.user.username
        
    },
    methods: {
        goSelect() {
            this.$router.push({name: 'MovieSelectView'})
        }
    }
}
</script>

<style>
.fade-in {
    opacity: 0; /* 초기 투명도를 0으로 설정 */
    animation: fade-in-animation 3s forwards; /* 애니메이션 적용 */
  }
  
  @keyframes fade-in-animation {
    from { opacity: 0; } /* 시작 시 투명도 0 */
    to { opacity: 1; } /* 끝나는 시점에 투명도 1 */
  }

</style>