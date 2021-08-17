import axios from 'axios';

export default {
  namespaced: true,
  state: {
    items: [],
    selectSizeCnt: 0,
  },
  mutations: {
    addItem(state, item) {
      const cartItems = state.items.filter(cartItem => cartItem.product_id === item.product_id); // 중복체크

      const manTopSize = ['XS (KR 90)', 'S (KR 95)', 'M (KR 95-100)', 'L (KR 100-105)', 'XL (KR 105-110)']; // 사이즈별 데이터
      const womanTopSize = ['XS (KR 44)', 'S (KR 55)', 'M (KR 66)', 'L (KR 77)', 'XL (KR 88)'];
      const manBottomSize = ['XS (KR 28)', 'S (KR 30)', 'M (KR 31)', 'L (KR 32)', 'XL (KR 34)'];
      const womanBottomSize = ['XS (KR 24)', 'S (KR 26)', 'M (KR 28)', 'L (KR 30)', 'XL (KR 32)'];
      const manShoesSize = ['KR 250', 'KR 260', 'KR 270', 'KR 280','KR 290'];
      const womanShoesSize = ['KR 230', 'KR 240', 'KR 250', 'KR 260','KR 270'];

      const localURL = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const stockURL = localURL + item.product_id + '/' + 'stocks' +'/'; // 재고 URL
      axios.get(stockURL) // 재고 데이터 받아오기
      .then((res) => {
        const options = [{ value: null, text: '사이즈 선택' },];
        item.stock = res.data.stock;
        item.selectedSize = null;
        if (item.product_type === 1 && item.gender === 'M') { // 남자상의
          for (let i=0; i < item.stock.length; i++){
            // options.push({manTopSize[i]:item.stock[i]});
            if (item.stock[i] == 0) {
              options.push({ value: manTopSize[i], text: manTopSize[i]+'-sold out', disabled: true })
            } else {
              options.push({value:manTopSize[i], text:manTopSize[i]});
            }
          }
        } else if (item.product_type === 2 && item.gender === 'M'){ // 남자하의
          for (let i=0; i < item.stock.length; i++){
            if (item.stock[i] == 0) {
              options.push({ value: manBottomSize[i], text: manBottomSize[i]+'-sold out', disabled: true })
            } else {
              options.push({value:manBottomSize[i], text:manBottomSize[i]});
            }
          }
        } else if (item.product_type === 1 && item.gender === 'F'){ // 여자상의
          for (let i=0; i < item.stock.length; i++){
            if (item.stock[i] == 0) {
              options.push({ value: womanTopSize[i], text: womanTopSize[i]+'-sold out', disabled: true })
            } else {
              options.push({value:womanTopSize[i], text:womanTopSize[i]});
            }
          }
        } else if (item.product_type === 2 && item.gender === 'F'){ // 여자하의
          for (let i=0; i < item.stock.length; i++){
            if (item.stock[i] == 0) {
              options.push({ value: womanBottomSize[i], text: womanBottomSize[i]+'-sold out', disabled: true })
            } else {
              options.push({value:womanBottomSize[i], text:womanBottomSize[i]});
            }
          }
        } else if (item.product_type === 3 && item.gender === 'M'){ // 남자신발
          for (let i=0; i < item.stock.length; i++){
            if (item.stock[i] == 0) {
              options.push({ value: manShoesSize[i], text: manShoesSize[i]+'-sold out', disabled: true })
            } else {
              options.push({value:manShoesSize[i], text:manShoesSize[i]});
            }
          }
        } else if (item.product_type === 3 && item.gender === 'F'){ // 여자신발
          for (let i=0; i < item.stock.length; i++){
            if (item.stock[i] == 0) {
              options.push({ value: womanShoesSize[i], text: womanShoesSize[i]+'-sold out', disabled: true })
            } else {
              options.push({value:womanShoesSize[i], text:womanShoesSize[i]});
            }
          }
        } else { // 악세사리
          if (item.stock[0] == 0) {
            options.push({ value: null, text: 'sold out', disabled: true })
          } else {
            options.push({ value:'freesize', text:'freesize'});
          }
        }
        item.options = options;
      })
      .catch((err) => {
        console.log(err)
      })
      .finally(()=>{ // 장바구니에 넣기
        if (cartItems.length === 0) {
          state.items.push(item);
        }
      })
    },
    delItem(state, product_id) { // 장바구니에서 특정 상품 삭제하기
      state.items = state.items.filter(item => item.product_id !== product_id);
    },
    clearCart(state) { // 장바구니 비우기
      state.items = [];
    },
    plusCounter(state) { // 장바구니에 담은 상품 삭제 시 해당 사이즈 재고 +1
      return state.selectSizeCnt++;
    },
    minusCounter(state) { // 장바구니에 상품 담을 시 해당 사이즈 재고 -1
      return state.selectSizeCnt--;
    },
    cartReload(state, reloadItems) {
      state.items = reloadItems
    },
  },
  actions: {
    addItem({ commit }, item) { // 장바구니에 상품 추가 함수 설정
      commit('addItem', item);
    },
    delItem({ commit }, product_id) {  // 장바구니에 상품 삭제 함수 설정
      commit('delItem', product_id);
    },
    clearCart({ commit }) { // 장바구니 비우는 함수 설정
      commit('clearCart');
    },
    cartReload({ commit }, reloadItems) {  // 장바구니 불러오는 함수 설정
      commit('cartReload', reloadItems)
    },
  },
  getters: {
    totalPrice(state) { // 장바구니 상품 가격 계산
      return state.items.reduce((sum, item) => sum + Number(item.price), 0);
    },
  }
}