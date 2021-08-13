export default {
  namespaced: true,
  state: {
    items: []
  },
  mutations: {
    addItem(state, item) {
      const cartItems = state.items.filter(cartItem => cartItem.product_id === item.product_id);
      if (cartItems.length === 0) {
        state.items.push(item);
        console.log(state.items)
      }
    },
    delItem(state, product_id) {
      state.items = state.items.filter(item => item.product_id !== product_id);
    },
    clearCart(state) {
      state.items = [];
    }
  },
  actions: {
    addItem({ commit }, item) {
      commit('addItem', item);
    },
    delItem({ commit }, product_id) {
      commit('delItem', product_id);
    },
    clearCart({ commit }) {
      commit('clearCart');
    }
  },
  getters: {
    totalPrice(state) {
      return state.items.reduce((sum, item) => sum + Number(item.price), 0);
    },
  }
}