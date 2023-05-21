<template>
  <div>
    <h1> {{  }} 님에게 어울리는 OTT는 {{ resultOTT }} !!</h1>
    <button @click="goSelect">다시 고르기</button>
  </div>
</template>

<script>
export default {
    name: 'OttResultView',
    data() {
        return {
            resultOTT: null
        }
    },

    created() {
        this.$store.dispatch('calculateResult')
        this.resultOTT = this.$store.state.resultOTT
    },
    methods: {
        goSelect() {
            this.$router.push({name: 'MovieSelectView'})
        }
    }
}
</script>

<style>

</style>