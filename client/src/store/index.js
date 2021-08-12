import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
//
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    user: [],
  },
  mutations: {
    createData: function(state, userData) {
      state.user.push(userData)
    },
  },
  actions: {
    createUserData: function({ commit }, userData) {
      commit('createData', userData)
    }
  },
  modules: {
  }
})