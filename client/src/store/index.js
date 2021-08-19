import Vue from 'vue'
import Vuex from 'vuex'
import cart from './cart/index';
Vue.use(Vuex)

export default new Vuex.Store({
  state: { // 기본 데이터 설정
    selectedProductID: '301',
    productRecommend_1: 'https://static.zara.net/photos///2021/I/0/1/p/8612/743/020/2/w/563/8612743020_6_1_1.jpg?ts=1627914450425',
    productRecommend_2: 'https://static.zara.net/photos///2021/I/1/1/p/6314/810/100/2/w/563/6314810100_6_1_1.jpg?ts=1626859235465',
    productRecommend_3: 'https://static.zara.net/photos///2021/I/0/1/p/0653/226/800/2/w/563/0653226800_6_2_1.jpg?ts=1623851340774',
    productId_1: 302,
    productId_2: 303,
    productId_3: 304,
    productDetail: {},
    productLocation: 'E',
    stock: [],
    user: {
      age: String,
      gen: String,
    },
  },
  mutations: { // vuex에 데이터 저장
    selectedProductID: function (state, payload) {
      state.selectedProductID = payload;
    },
    productRecommend_1: function (state, payload) {
      state.productRecommend_1 = payload;
    },
    productRecommend_2: function (state, payload) {
      state.productRecommend_2 = payload;
    },
    productRecommend_3: function (state, payload) {
      state.productRecommend_3 = payload;
    },
    productId_1: function (state, payload) {
      state.productId_1 = payload;
    },
    productId_2: function (state, payload) {
      state.productId_2 = payload;
    },
    productId_3: function (state, payload) {
      state.productId_3 = payload;
    },
    productDetail: function (state, payload) {
      state.productDetail = payload;
    },
    productLocation: function (state, payload) {
      state.productLocation = payload;
    },
    stock: function (state, payload) {
      state.stock = payload;
    },
    createData: function(state, userData) {
      console.log(userData)
      state.user.age = userData.age
      state.user.gen = userData.gen
    },
  },
  actions: { // 유저 데이터 저장
    createUserData: function({ commit }, userData) {
      commit('createData', userData)
    }
  },
  modules: {
    cart,
  }
})