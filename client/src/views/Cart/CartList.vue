<template>
  <!-- 장바구니 페이지에 표시할 상품 리스트 -->
  <div>
    <b-card v-for="item in cartItems" :key="item.product_id" :img-src="item.product_image" img-alt="Card image" img-left class="mb-3">
      <b-card-text>
        <div class="container">
          <div class="product-name">{{ item.product_name }}</div>
          <div >
            <b-form-select class="product-size" v-model="item.selectedSize" :options="item.options" @change="changeSelectSizeCnt(item.selectedSize)"></b-form-select>
          </div>
          <div class="product-price">{{ item.price }}</div>
          <div class="products-delete"><b-icon icon="trash" variant="danger" @click="delItem(item.product_id)"></b-icon></div>
        </div>
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
import {mapState} from 'vuex';


export default {
  computed: {
    ...mapState('cart', { // cartItems : 장바구니 아이템 목록
      cartItems: state => state.items,
    })
  },
  methods: {
    delItem(product_id) { // 단일아이템 제거 함수
      this.$store.dispatch('cart/delItem', product_id);
    },
    changeSelectSizeCnt(selectedSize) { // 사이즈 선택 시 재고 변동
      if (selectedSize === null){
        this.$store.commit('cart/minusCounter');
      } else {
        this.$store.commit('cart/plusCounter');
      }
    }
  }
}
</script>

<style scoped>

.mb-3 {
  width: 90%;
  margin: auto;
  border: 2.5px solid rgba(0, 0, 0, 0.3);
  border-radius: 5rem;
  font-size: 3rem;
  align-items: center;
}

.card-img-left {
  border-radius: 5rem 0 0 5rem;
  height: 5em;
}

.card-body {
  padding: 0px;
}

.container {
  padding: 0px;
  display: flex;
  height: 3rem;
  align-items: center;
}

.product-name {
  flex: 3.5;
  font-size: 0.5em;
}

.product-size {
  flex: 3;
  font-size: 0.4em;
  margin-right: 0.3em;
}

.product-price {
  flex: 3;
  font-size: 0.5em;
  margin-right: 0.1em;
}

.products-delete {
  flex: 3;
  font-size: 0.75em;
  margin-right: 0.3em;
}

</style>