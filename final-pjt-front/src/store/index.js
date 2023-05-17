import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createPersistedState from 'vuex-persistedstate'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
      console.log(state.articles)
    },
    SAVE_TOKEN_SIGNUP(state, token) {
      console.log(token)
      state.token = token
      router.push({name: 'LogInView'})
    },
    SAVE_TOKEN_LOGIN(state, token) {
      console.log(token)
      state.token = token
      router.push({name: 'HomeView'})
      // 일단 홈으로 -> 메인페이지로 보낼 것
    }
  },
  actions: {
    getArticles(context) {
      console.log('엑시오스 전 !@')
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
        .then((response) => {
        console.log(response, context)
          context.commit('GET_ARTICLES', response.data)
        })
        .catch((error) => {
        console.log(error)
      })
    },
    signUp(context, payload) {
      const email = payload.email
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      console.log(email)
      console.log(username)
      console.log(password1)
      console.log(password2)

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, email, password1, password2
        }
      })
      .then((response) => {
        console.log(response)
        console.log(response.data)
        console.log(response.data.key)
        context.commit('SAVE_TOKEN_SIGNUP', response.data.key)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      console.log(username)
      console.log(password)

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((response) => {
        context.commit('SAVE_TOKEN_LOGIN', response.data.key)
        })
      .catch((error) => 
        console.log(error))
    },
  },
  
  modules: {
  }
})
